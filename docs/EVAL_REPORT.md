# Evaluation report

**Filled by:** session 7 (the baseline, and the evaluator's weakness), session 9
(failures named from traces), session 14 (one fix, measured after).

Every number below has the command that produced it, the commit it ran on, and
the model. A number without its command is an impression, and this file holds
none. CI has no keys, so any number CI printed is the offline fake model's.

## Before

- model: Ollama / qwen2.5:7b-instruct (CPU)
- commit: f1fa10d
- command: `uv run bootcamp final grade`
- result: 4/10 (40%), NOT YET; critical safety gate failed.

### The evaluator's weakness (session 7)

<!-- write this: what the pass condition does not check. The cite-everything
fake's pass rate is the evidence (`pass_rate` and `weakness` in ch07-e3). -->

### Failures, named from traces (session 9)

| Case | Bucket | The trace line that decided it |
|---|---|---|
| <!-- write this --> | <!-- e.g. retrieval_miss, instruction_following --> | <!-- paste this: the line --> |

## After

The fix for rank 1 of [ISSUES.md](ISSUES.md) (session 14).

- model: <!-- write this: the SAME model as Before, or the comparison means nothing -->
- commit: <!-- write this -->
- command: <!-- write this: the same command as Before -->
- result: <!-- paste this -->
- regression test: <!-- write this: its name in tests/ -->

### What got better (session 7's `improvement`)

<!-- write this: one sentence naming what improved, and by how much. -->

### What got worse, or could (session 7's `regression_or_risk`)

<!-- write this: one sentence. "None" is almost never true. -->


## Additional measured runs — 2026-10-05

All scores below are public practice results, not certificate evidence. Runs after the initial baseline used an uncommitted working tree; the baseline commit listed above is not their code revision.

| Configuration | Exact command | Observed result |
|---|---|---|
| Ollama / qwen2.5:7b-instruct, hardened agent, 30-second deadline, Spanish failure messages | `uv run bootcamp final grade` | 2/10 (20%), NOT YET; critical safety gate failed |
| Same model, 110-second deadline, standard corpus refusal phrase | `uv run bootcamp final grade` | 5/10 (50%), NOT YET; critical safety gate failed |
| Complete retrieved-source context and heading regression test | `uv run pytest` | 8 passed, 1 skipped |

The 5/10 score predates the complete-source context fix. No complete grading score has yet been measured for that fix.

### Diagnosed retrieval failure

For the public security question, the top three chunks contained the heading `Defenses that actually help` but not the paragraph describing the defenses. The regression test confirmed that `Bound capabilities` was absent from the model prompt before the fix and present after it.

### Evaluator limitation

The practice grader checks required concepts through normalized phrase matches. A paraphrase can fail `claim_support`; passing that dimension is not an independent semantic proof that every claim is supported.
