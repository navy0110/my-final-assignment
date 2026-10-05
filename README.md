# Source-grounded developer research assistant

A developer research assistant that answers from six versioned course documents, checks source citations, and refuses unsupported questions and detected instruction attacks.

## The problem

Developers need answers they can check against source material. A plausible answer without a valid citation can mislead them, while instructions embedded in retrieved documents can redirect a model away from the task.

## Demo

These are actual CLI outputs captured during development on Ollama / qwen2.5:7b-instruct. No private final questions are included.

### One supported answer

Command: `uv run bootcamp final trace "Which layered defenses help against prompt injection?"`

```text
[retrieve] top_k=3 -> [('prompt-injection', 1), ('prompt-injection', 0), ('structured-outputs', 2)]
[llm_call] attempt 1: 921 chars
[decision] answered with citations ['prompt-injection']

answer: Prompt injection can be defended against by layering multiple approaches. Specifically, **mark boundaries**, **constrain output**, **bound capabilities**, and **keep credentials out of the model's reach**. These methods collectively reduce the risk. For example, marking boundaries involves wrapping retrieved content in delimiters and instructing the model that it is data to be quoted, not instructions. Constraining output ensures that injected 'instructions' must pass through a strict schema validation to have any effect. Bound capabilities limit the actions an agent can perform, such as restricting it to read-only operations and setting a tool-call budget to limit the blast radius. Keeping credentials out of the model's reach prevents injection into a system that cannot act on them, ensuring they are not leaked.
citations: ['prompt-injection']
confidence: 1.0
needs_human_review: False
```

This is the model's verbatim answer, not an endorsement that its self-reported confidence is calibrated. The credential sentence is imprecise; the source's claim is that credentials kept outside the model's input cannot be exposed through that input.

### One refusal

Command: `uv run bootcamp final trace "What is the capital city of Mongolia?"`

```text
[retrieve] top_k=3 -> []
[decision] no relevant chunks; refusing without an LLM call

answer: I don't know based on the provided corpus.
citations: []
confidence: 0.0
needs_human_review: True
```

## Architecture

A bounded chain retrieves top_k=3 chunks, expands only their selected source documents, prioritizes sources whose complete title is explicitly named in the question, and asks one model through LLMClient for strict ResearchAnswer JSON. The course parser permits one corrective retry; both calls share a 110-second waiting budget. The application checks citation IDs and rejects answers when the expanded evidence matches its direct-instruction detector. When a cited list section matches the question and the answer omits its bold item labels, the application adds the source paragraph as a labeled excerpt without another model call. Empty retrieval spends zero model calls; provider failures and timeouts return typed refusals.

The chain has no persistent conversation memory, database, network search or writing tools. Ollama is the local model endpoint. See [the architecture decision](docs/adr/0001-run-shape.md), [retention](docs/RETENTION.md), and [workflow](docs/SKILL.md).

## Measured results

| Version | Command | Model | Observed result |
|---|---|---|---|
| Initial starter, f1fa10d | `uv run bootcamp final grade` | Ollama / qwen2.5:7b-instruct | 4/10 (40%), critical gate failed |
| Hardened agent before complete-source expansion | `uv run bootcamp final grade` | Same Ollama model | 5/10 (50%), critical gate failed |
| Complete-source expansion and stateless-memory test, 5b4df0d | `uv run pytest` | Offline scripted models | 9 passed |
| Complete-source version, 5b4df0d | `uv run bootcamp final grade` | Same Ollama model | 6/10 (60%), critical gate failed |
| Current coverage and refusal normalization | `uv run bootcamp final grade` | Ollama / qwen2.5:3b-instruct | 7/10 (70%), all critical cases passed |
| Current contract checks | `uv run pytest` | Offline scripted models | 13 passed |

Practice results do not establish certificate eligibility. Only the course's private grading result does. Detailed measurements and evaluator limitations are in [EVAL_REPORT.md](docs/EVAL_REPORT.md).

## The honest limitation

A lexical query selected a heading while omitting its supporting paragraph. Complete-source expansion fixes that reproduced failure, but cannot repair selection of the wrong document and increases context size. A subsequent full-source evaluation reached 6/10 but still failed the critical coverage question. The current 3B evaluation passed 7/10 and every critical case. Three noncritical questions still failed claim_support: chunking, application-owned validation and production stopping conditions. Passing practice does not guarantee the private certificate result.

The injection detector recognizes only a few English paragraph-start patterns. The caller timeout bounds waiting but does not cancel an in-flight provider request. See [ranked issues](docs/ISSUES.md).

## How to run it

From the local project folder: `uv sync && uv run pytest`.

For the current evaluated configuration, install Ollama, pull `qwen2.5:3b-instruct`, and set BOOTCAMP_PROVIDER=ollama and BOOTCAMP_MODEL=qwen2.5:3b-instruct in your terminal or ignored local configuration. No API key is needed. Then run `uv run bootcamp final trace "How does chunking work in RAG?"`.

Without a provider, the offline fake model is the default. It is appropriate for tests, not for certificate submission. Do not run concurrent evaluations on the CPU model.

Public repository: https://github.com/navy0110/my-final-assignment. Clone and verify with `git clone https://github.com/navy0110/my-final-assignment && cd my-final-assignment && uv sync && uv run pytest`.

## Sources

Answer sources are only the six unchanged files in data/corpus. The pinned course package at 81a918144aeae97db58c871c1f4e2be68cdd1bc5 supplies parsing, retrieval, citation checks, adapters, CLI and the public grader.

## Credits

The generated starter and contract tests come from [Gecko Academy's Dev3Pack course](https://github.com/Gecko-Academy/dev3pack-cohort-2026-09). Development used Codex explanations, review, debugging and implementation assistance for timeout handling, evidence expansion, safety checks, tests and documentation. The learner must review and understand this work before submission.

## Smoke check and rollback

Run `uv run pytest` and the unsupported trace above; its citations must be empty, needs_human_review true, and the trace must show no model call. For provider health, also run one supported trace; a refusal-only smoke check does not prove the model is reachable.

Rollback target: 10 minutes (an operational target, not a measured duration). Revert the faulty commit with git revert, run all thirteen contract tests, and push the revert before submitting again. Never use the fake model as an undisclosed production fallback.

## Deliverables

- agent.py: YourAgent and bounded provider/evidence adapters.
- tests/test_contract.py: thirteen executable contract, memory, regression, coverage, refusal and provider-adapter checks.
- data/corpus/: six read-only source documents.
- docs/EVAL_REPORT.md, ISSUES.md, RETENTION.md, SKILL.md, adr/0001-run-shape.md: measurements, limits and operating decisions.
