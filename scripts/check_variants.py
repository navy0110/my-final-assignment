"""Manual public variants: contract checks, not semantic or certificate grading."""

from __future__ import annotations

import json
from pathlib import Path

from agent import YourAgent

CASES = (
    (
        "comparison",
        "Compare Prompt Injection with application validation of JSON output.",
        {"prompt-injection", "structured-outputs"},
    ),
    (
        "paraphrase",
        "How can a service avoid treating model output as trusted data?",
        {"structured-outputs"},
    ),
    (
        "unsupported-related",
        "What is the name and birthplace of the person who invented RAG?",
        set(),
    ),
)


def main() -> None:
    records = []
    for name, question, expected in CASES:
        result = YourAgent().run(question)
        answer = result.answer
        if expected:
            contract_passed = set(answer.citations) == expected and not answer.needs_human_review
        else:
            contract_passed = (
                not answer.citations and answer.needs_human_review and answer.confidence == 0.0
            )
        records.append(
            dict(
                name=name,
                question=question,
                expected_citations=sorted(expected),
                contract_passed=contract_passed,
                answer=answer.answer,
                citations=list(answer.citations),
                confidence=answer.confidence,
                needs_human_review=answer.needs_human_review,
                trace=[dict(kind=item.kind, detail=item.detail) for item in result.trace],
            )
        )
        print(
            f"{name}: contract {'PASS' if contract_passed else 'FAIL'}; "
            f"citations={list(answer.citations)}; review={answer.needs_human_review}",
            flush=True,
        )
    destination = Path(__file__).resolve().parents[1] / "docs" / "PUBLIC_VARIANTS.json"
    destination.write_text(
        json.dumps(
            dict(
                scope="Self-authored cases based on public corpus; checks do not prove entailment.",
                results=records,
            ),
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"Report: {destination}", flush=True)


if __name__ == "__main__":
    main()
