"""Synthetic robustness checks, independent of the course's final questions."""

import json

from bootcamp_agent.agent import REFUSAL_TEXT
from bootcamp_agent.documents import Document
from bootcamp_agent.llm import FakeLLM

from agent import EvidenceClient, YourAgent


def reply(text, citations, review=False, confidence=0.9):
    return json.dumps(
        dict(answer=text, citations=citations, confidence=confidence, needs_human_review=review)
    )


def test_comparison_keeps_secondary_source_even_with_explicit_primary_title():
    documents = [
        Document("limits", "Storage Limits", "Storage limits permit three reads.", "limits.md", ()),
        Document(
            "audit", "Audit Checks", "Audit validation verifies recorded events.", "audit.md", ()
        ),
    ]
    model = FakeLLM(default=reply("A comparison.", ["limits", "audit"]))
    EvidenceClient(model, "Compare Storage Limits with audit validation.", documents).complete(
        "", ""
    )
    assert "Audit validation verifies recorded events." in model.calls[0][1]


def test_actual_refusal_cannot_keep_a_valid_source_citation():
    model = FakeLLM(default=reply(REFUSAL_TEXT, ["rag-basics"], review=True, confidence=0.0))
    answer = YourAgent(client=model)("How does chunking work in RAG?")
    assert answer.citations == ()
    assert answer.needs_human_review and answer.confidence == 0.0


def test_appended_evidence_cannot_exceed_submission_character_limit():
    source = "Storage limits protect the application. " * 250
    model = FakeLLM(default=reply("Storage has limits.", ["limits"]))
    agent = YourAgent(client=model)
    agent.documents = [Document("limits", "Storage Limits", source, "limits.md", ())]
    answer = agent("Explain the storage limits.")
    assert len(answer.answer) <= 8000
    assert answer.needs_human_review and not answer.citations


def test_overlong_model_answer_is_flagged_without_truncating():
    model = FakeLLM(default=reply("Long unsupported prose. " * 400, ["rag-basics"]))
    answer = YourAgent(client=model)("How does chunking work in RAG?")
    assert answer.answer == REFUSAL_TEXT
    assert answer.needs_human_review and answer.citations == ()


def test_unique_adjacent_terms_focus_single_topic_on_matching_source():
    documents = [
        Document("search", "Search Guide", "Retrieved documents are untrusted data.", "a.md", ()),
        Document(
            "result", "Result Guide", "Treat the model's output as untrusted input.", "b.md", ()
        ),
    ]
    model = FakeLLM(default=reply("Validate the result.", ["result"]))
    EvidenceClient(model, "How should model output be checked?", documents).complete("", "")
    prompt = model.calls[0][1]
    assert '"doc_id": "result"' in prompt
    assert "Retrieved documents are untrusted data." not in prompt


def test_conflicting_model_prose_is_not_presented_as_grounded_fact():
    source = "Storage limits permit three reads and zero writes; exceeding them stops the task."
    model = FakeLLM(default=reply("Storage allows unlimited writes.", ["limits"]))
    agent = YourAgent(client=model)
    agent.documents = [Document("limits", "Storage Limits", source, "limits.md", ())]
    answer = agent("Explain the storage limits.")
    assert "unlimited writes" not in answer.answer
    assert source in answer.answer
    assert answer.citations == ("limits",) and not answer.needs_human_review


def test_exact_model_quote_is_preserved_as_cited_evidence():
    source = "Storage limits permit three reads and zero writes; exceeding them stops the task."
    model = FakeLLM(default=reply(source, ["limits"]))
    agent = YourAgent(client=model)
    agent.documents = [Document("limits", "Storage Limits", source, "limits.md", ())]
    answer = agent("Explain the storage limits.")
    assert source in answer.answer and not answer.needs_human_review


def test_stronger_phrase_match_focuses_source_even_when_another_matches_one_phrase():
    documents = [
        Document(
            "eval",
            "Evaluation Guide",
            "Evaluation checks a model's output with examples.",
            "a.md",
            (),
        ),
        Document(
            "check", "Check Guide", "Validate the model's output as data before use.", "b.md", ()
        ),
    ]
    model = FakeLLM(default=reply("Check the data.", ["check"]))
    EvidenceClient(model, "How should model output as data be checked?", documents).complete("", "")
    prompt = model.calls[0][1]
    assert "Validate the model" in prompt
    assert "Evaluation checks" not in prompt


def test_citation_must_have_reached_model_not_merely_retrieval():
    model = FakeLLM(default=reply("Storage permits three reads.", ["limits", "audit"]))
    agent = YourAgent(client=model)
    agent.documents = [
        Document(
            "limits",
            "Storage Limits",
            "Storage limits permit three reads and no writes.",
            "a.md",
            (),
        ),
        Document(
            "audit", "Audit Checks", "Storage risks require audit validation of events.", "b.md", ()
        ),
    ]
    answer = agent("Explain storage limits.")
    assert "Storage risks require audit validation" not in model.calls[0][1]
    assert answer.citations == ("limits",)
    assert answer.needs_human_review and answer.confidence <= 0.2


def test_review_flag_cannot_bypass_grounded_output_validation():
    source = "Storage limits permit three reads and zero writes; exceeding them stops the task."
    model = FakeLLM(default=reply("Storage allows unlimited writes.", ["limits"], review=True))
    agent = YourAgent(client=model)
    agent.documents = [Document("limits", "Storage Limits", source, "limits.md", ())]
    answer = agent("Explain the storage limits.")
    assert "unlimited writes" not in answer.answer
    assert source in answer.answer
    assert answer.needs_human_review and answer.citations == ("limits",)


def test_reviewed_answer_without_relevant_passage_is_canonical_refusal():
    source = "Storage limits permit three reads and zero writes; exceeding them stops the task."
    model = FakeLLM(default=reply("The founder lives in Paris.", ["limits"], review=True))
    agent = YourAgent(client=model)
    agent.documents = [Document("limits", "Storage Limits", source, "limits.md", ())]
    answer = agent("Where does the founder live?")
    assert answer.answer == REFUSAL_TEXT
    assert answer.citations == () and answer.confidence == 0.0
    assert answer.needs_human_review
