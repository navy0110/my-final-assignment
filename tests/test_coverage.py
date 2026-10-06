"""Coverage checks using synthetic sources and the public security document."""

import json

from bootcamp_agent.documents import Document
from bootcamp_agent.llm import FakeLLM

from agent import YourAgent


def model_reply(citation):
    return FakeLLM(
        default=json.dumps(
            dict(
                answer="A brief summary.",
                citations=[citation],
                confidence=0.9,
                needs_human_review=False,
            )
        )
    )


def test_three_requested_mechanisms_are_not_cut_to_two_paragraphs():
    sections = (
        "Read limits permit three reads before the task must stop safely.",
        "Write limits permit zero writes so that stored data remains unchanged.",
        "Retry rules permit one retry after a recoverable failure, then stop.",
    )
    agent = YourAgent(client=model_reply("limits"))
    agent.documents = [
        Document(
            "limits",
            "Limits",
            "\n\n".join(sections),
            "synthetic.md",
            (),
        )
    ]
    answer = agent("Explain read limits, write limits and retry rules.")
    assert not answer.needs_human_review
    assert all(section in answer.answer for section in sections)


def test_public_security_answer_covers_entry_defenses_and_mindset():
    agent = YourAgent(client=model_reply("prompt-injection"))
    answer = agent(
        "Describe prompt injection entry points, layered defenses and the untrusted-input mindset."
    )
    assert not answer.needs_human_review
    for concept in ("OpenAPI", "**Mark boundaries**", "**Test it**", "untrusted input"):
        assert concept in answer.answer


def test_conjoined_public_topics_both_reach_model_context():
    from bootcamp_agent.retrieval import retrieve

    from agent import EvidenceClient

    agent = YourAgent(client=model_reply("prompt-injection"))
    question = "Explain prompt injection defenses and JSON parsing failure handling."
    ids = {item.chunk.doc_id for item in retrieve(question, agent.documents, top_k=3)}
    sources = [doc for doc in agent.documents if doc.doc_id in ids]
    context = EvidenceClient(agent.client, question, sources)
    assert {"prompt-injection", "structured-outputs"} <= context.source_ids


def test_conjoined_synthetic_topics_remain_unflagged_with_both_citations():
    paragraphs = (
        "Storage limits permit three reads and no writes before the task stops.",
        "Audit validation verifies recorded events before reporting them as trusted.",
    )
    model = FakeLLM(
        default=json.dumps(
            dict(
                answer="Both mechanisms apply.",
                citations=["limits", "audit"],
                confidence=0.9,
                needs_human_review=False,
            )
        )
    )
    agent = YourAgent(client=model)
    agent.documents = [
        Document("limits", "Storage Limits", paragraphs[0], "a.md", ()),
        Document("audit", "Audit Validation", paragraphs[1], "b.md", ()),
    ]
    answer = agent("Explain storage limits and audit validation.")
    assert not answer.needs_human_review
    assert set(answer.citations) == {"limits", "audit"}
    assert all(paragraph in answer.answer for paragraph in paragraphs)


def test_exact_quantity_absent_from_cited_source_is_refused():
    agent = YourAgent(client=model_reply("agent-loops"))
    answer = agent("What exact number of tool calls is mandatory for every production agent?")
    assert answer.needs_human_review and answer.confidence == 0.0
    assert answer.citations == ()


def test_documented_exact_quantity_is_not_rejected():
    agent = YourAgent(client=model_reply("limits"))
    source = "Storage limits permit three reads before the task must stop safely."
    agent.documents = [Document("limits", "Storage Limits", source, "a.md", ())]
    answer = agent("What exact number of reads is allowed?")
    assert not answer.needs_human_review and answer.citations == ("limits",)
    assert source in answer.answer
