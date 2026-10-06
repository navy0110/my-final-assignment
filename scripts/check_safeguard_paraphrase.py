"""Self-authored security paraphrase over the public corpus."""

import json
from pathlib import Path

from agent import YourAgent


def main():
    question = "Which safeguards reduce risks from hostile OpenAPI descriptions?"
    result = YourAgent().run(question)
    answer = result.answer
    concepts = ("**Mark boundaries**", "**Constrain output**", "**Test it**")
    passed = (
        answer.citations == ("prompt-injection",)
        and not answer.needs_human_review
        and all(concept in answer.answer for concept in concepts)
    )
    destination = Path(__file__).resolve().parents[1] / "docs" / "PUBLIC_SAFEGUARD_PARAPHRASE.json"
    destination.write_text(
        json.dumps(
            dict(
                scope="Public self-authored question; phrase checks do not prove entailment.",
                question=question,
                passed=passed,
                answer=answer.answer,
                citations=list(answer.citations),
                confidence=answer.confidence,
                needs_human_review=answer.needs_human_review,
                trace=[dict(kind=e.kind, detail=e.detail) for e in result.trace],
            ),
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"Safeguard paraphrase: {'PASS' if passed else 'FAIL'}", flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
