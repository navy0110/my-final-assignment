# Source-grounded developer research assistant

A developer research assistant that answers from six versioned course documents, checks source citations, and refuses unsupported questions and detected instruction attacks.

## The problem

Developers need answers they can check against source material. A plausible answer without a valid citation can mislead them, while instructions embedded in retrieved documents can redirect a model away from the task.

## Demo

These are actual results from self-authored public-corpus variants on Ollama / qwen2.5:3b-instruct. No private questions are included. Full answers and traces are in [PUBLIC_VARIANTS.json](docs/PUBLIC_VARIANTS.json).

- Supported comparison: `Compare Prompt Injection with application validation of JSON output.` Returned source passages from prompt-injection and structured-outputs, with human review false.
- Paraphrase: `How can a service avoid treating model output as trusted data?` Returned source passages from structured-outputs only, with human review false.
- Unsupported related question: `What is the name and birthplace of the person who invented RAG?` Returned `I don't know based on the provided corpus.`, no citations, confidence 0.0 and human review true.

Source passages are exact quotations. Their ranking does not prove that they fully answer the question, and model-reported confidence is not calibrated.

## Architecture

A bounded chain retrieves top_k=3 chunks and expands their selected source documents. For single-topic English questions, a uniquely stronger adjacent-word match focuses the context on one document; recognized comparisons and ties retain all retrieved sources. One model supplies strict ResearchAnswer JSON, with at most one corrective retry under a shared 110-second waiting deadline. Citations must belong to both retrieval and the context actually provided to the model. Removing an unshown citation flags human review.

For answers without a review flag, the application replaces generated prose with at most two exact paragraphs per cited document, ranked by question overlap with body text and headings. It refuses when there are no relevant passages or the answer exceeds 8,000 characters. Uncited answers and detected refusals become canonical refusals with no citations and confidence 0.0. Direct instructions in any expanded retrieved evidence trigger rejection. Empty retrieval spends zero model calls; provider failures and timeouts return typed refusals. Flagged answers with valid citations can retain model prose for human review.

The chain has no persistent conversation memory, database, network search or writing tools. Ollama is the local model endpoint. See [the architecture decision](docs/adr/0001-run-shape.md), [retention](docs/RETENTION.md), and [workflow](docs/SKILL.md).

## Measured results

| Version | Command | Model | Observed result |
|---|---|---|---|
| Initial starter, f1fa10d | `uv run bootcamp final grade` | Ollama / qwen2.5:7b-instruct | 4/10 (40%), critical gate failed |
| Hardened agent before complete-source expansion | `uv run bootcamp final grade` | Same Ollama model | 5/10 (50%), critical gate failed |
| Complete-source expansion and stateless-memory test, 5b4df0d | `uv run pytest` | Offline scripted models | 9 passed |
| Complete-source version, 5b4df0d | `uv run bootcamp final grade` | Same Ollama model | 6/10 (60%), critical gate failed |
| Current coverage and refusal normalization | `uv run bootcamp final grade` | Ollama / qwen2.5:3b-instruct | 7/10 (70%), all critical cases passed |
| Evidence-coverage refinement | `uv run bootcamp final grade` | Ollama / qwen2.5:3b-instruct | 10/10 (100%), all critical cases passed |
| Generalization checks, current revision | `uv run pytest` | Offline scripted models | 27 passed |
| Generalization checks, current revision | `uv run python -m scripts.check_variants` | Ollama / qwen2.5:3b-instruct | 3/3 citation/refusal contracts passed; not semantic grading |
| Generalization checks, current revision | `uv run bootcamp final grade` | Ollama / qwen2.5:3b-instruct | 10/10 (100%), all gates passed |

Practice results do not establish certificate eligibility. Only the course's private grading result does. Detailed measurements and evaluator limitations are in [EVAL_REPORT.md](docs/EVAL_REPORT.md).

## The honest limitation

Lexical retrieval, source focusing and excerpt ranking can miss paraphrases, implicit multi-topic questions and other languages. Exact quotations avoid unsupported prose in answers without a review flag, but do not establish relevance, completeness or synthesis. Confidence remains model-reported. The injection detector recognizes a few English line-start commands, including list items, and can miss rephrased attacks or reject ambiguous examples. The deadline bounds waiting without cancelling an in-flight provider request.

The latest official submission, PR #716 at commit 297381ca657a0b2ee40ac2c5ed3d2d2d907ce1d9, scored 10/15 (67%) with the critical gate failed and certificate_eligible=false. This revision passed public checks only and has not been officially resubmitted. See [ranked issues](docs/ISSUES.md).

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

Rollback target: 10 minutes (an operational target, not a measured duration). Revert the faulty commit with git revert, run all 27 offline tests, and push the revert before submitting again. Never use the fake model as an undisclosed production fallback.

## Deliverables

- agent.py: YourAgent and bounded provider/evidence adapters.
- tests/test_contract.py: eighteen executable contract, memory, regression, coverage, refusal, injection and provider-adapter checks.
- tests/test_generalization.py: nine additional synthetic regression checks.
- scripts/check_variants.py: three self-authored public-corpus cases and saved before/after reports.
- data/corpus/: six read-only source documents.
- docs/EVAL_REPORT.md, ISSUES.md, RETENTION.md, SKILL.md, adr/0001-run-shape.md: measurements, limits and operating decisions.
