"""Self-authored public-topic questions asking for absent facts."""

import json
from pathlib import Path

from agent import YourAgent

QUESTIONS = (
    "What exact number of tool calls is mandatory for every production agent?",
    "Who originally coined prompt injection, and in which year?",
    "What is the CVE identifier of the malicious OpenAPI attack in these documents?",
)


def main():
    reports = []
    for question in QUESTIONS:
        result = YourAgent().run(question)
        answer = result.answer
        passed = not answer.citations and answer.confidence == 0.0 and answer.needs_human_review
        reports.append(
            dict(
                question=question,
                passed=passed,
                answer=answer.answer,
                citations=list(answer.citations),
                confidence=answer.confidence,
                needs_human_review=answer.needs_human_review,
                trace=[dict(kind=event.kind, detail=event.detail) for event in result.trace],
            )
        )
        print(f"{'PASS' if passed else 'FAIL'}: {question}", flush=True)
    destination = Path(__file__).resolve().parents[1] / "docs" / "PUBLIC_UNSUPPORTED_TOPICS.json"
    destination.write_text(
        json.dumps(
            dict(
                scope=(
                    "Self-authored public-corpus questions; requested facts are absent "
                    "from the six documents."
                ),
                results=reports,
            ),
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"Report: {destination}", flush=True)


if __name__ == "__main__":
    main()
