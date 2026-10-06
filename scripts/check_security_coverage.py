"""Self-authored public coverage case; lexical checks are not semantic grading."""

import json
from pathlib import Path

from agent import YourAgent


def main():
    question = (
        "Describe prompt injection entry points, layered defenses and the untrusted-input mindset."
    )
    result = YourAgent().run(question)
    answer = result.answer
    concepts = ("OpenAPI", "**Mark boundaries**", "**Test it**", "untrusted input")
    passed = (
        set(answer.citations) == {"prompt-injection"}
        and not answer.needs_human_review
        and all(concept in answer.answer for concept in concepts)
    )
    report = dict(
        scope="Self-authored question using public corpus; phrase checks do not prove entailment.",
        question=question,
        expected_concepts=list(concepts),
        passed=passed,
        answer=answer.answer,
        citations=list(answer.citations),
        confidence=answer.confidence,
        needs_human_review=answer.needs_human_review,
        trace=[dict(kind=event.kind, detail=event.detail) for event in result.trace],
    )
    destination = Path(__file__).resolve().parents[1] / "docs" / "PUBLIC_SECURITY_COVERAGE.json"
    destination.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Public security coverage: {'PASS' if passed else 'FAIL'}; {destination}", flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
