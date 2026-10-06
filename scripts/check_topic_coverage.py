"""Self-authored conjunction case from the public corpus; mechanical checks only."""

import json
from pathlib import Path

from agent import YourAgent


def main():
    question = "Explain prompt injection defenses and JSON parsing failure handling."
    result = YourAgent().run(question)
    answer = result.answer
    concepts = ("**Mark boundaries**", "**Test it**", "retry once", "typed refusal")
    passed = (
        set(answer.citations) == {"prompt-injection", "structured-outputs"}
        and not answer.needs_human_review
        and all(concept in answer.answer for concept in concepts)
    )
    report = dict(
        scope="Self-authored public-corpus question; phrase checks do not prove entailment.",
        question=question,
        expected_concepts=list(concepts),
        passed=passed,
        answer=answer.answer,
        citations=list(answer.citations),
        confidence=answer.confidence,
        needs_human_review=answer.needs_human_review,
        trace=[dict(kind=event.kind, detail=event.detail) for event in result.trace],
    )
    destination = Path(__file__).resolve().parents[1] / "docs" / "PUBLIC_TOPIC_COVERAGE.json"
    destination.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Public topic coverage: {'PASS' if passed else 'FAIL'}; {destination}", flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
