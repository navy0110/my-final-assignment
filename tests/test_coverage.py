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
