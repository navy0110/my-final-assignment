# Ranked issues

| rank | issue | impact |
|---:|---|---|
| 1 | Lexical retrieval selected the security section heading while omitting its explanatory paragraph. | The model could not enumerate the documented defenses, causing failures on critical safety questions. |
| 2 | The latest complete 3B evaluation passed 7 of 10; chunking, validation and stopping-condition answers failed claim_support. | All critical practice cases passed, but incomplete noncritical answers remain a quality limitation; private certificate eligibility is unverified. |
| 3 | The instruction detector recognizes only a small set of English commands at paragraph starts. | Rephrased or embedded commands can evade detection; this heuristic is not a complete injection defense. |

## Rank 1, fixed and evaluated

- Fix: include the complete text of each document already returned by retrieval. Do not add unreturned source IDs. Inspect the expanded source text for direct instructions.
- Regression test: `test_regression_rank_1_of_the_issue_list`. It failed before the fix and passed after it.
- Tradeoff: complete sources increase prompt size and may include irrelevant passages. A wrongly selected document is still a retrieval failure.
- Before and after: see [EVAL_REPORT.md](EVAL_REPORT.md).

## Operational limitation

The 110-second waiting deadline does not cancel a provider request already running in a daemon thread. Repeated timeouts can leave overlapping requests until the underlying transport returns. Avoid concurrent grading runs on the CPU model.
