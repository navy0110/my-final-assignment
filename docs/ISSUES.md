# Ranked issues

| rank | issue | impact |
|---:|---|---|
| 1 | Lexical retrieval, source focusing and excerpt ranking can miss paraphrases, implicit multi-topic questions and other languages. | Relevant evidence can be omitted or incidental passages selected. |
| 2 | Exact quotations and valid citations do not prove question coverage; confidence remains model-reported. | Extractive answers can be incomplete, less fluent or overconfident. Flagged answers can retain prose requiring review. |
| 3 | Direct-command detection normalizes Unicode presentation and covers selected English commands, formatting, role prefixes and assignments. | Rephrased attacks can bypass the heuristic; ambiguous examples can cause false positives. |

## Fixed regressions

Complete-source expansion restored paragraphs omitted by chunk retrieval. Public synthetic regressions now also cover comparison-source loss, cited refusals, oversized output, incorrect phrase focusing, unshown citations and generated claims conflicting with source text. Current checks: 43 offline tests; previous revision also passed three self-authored citation/refusal contracts and 10/10 public practice cases passed.

## Operational limitation

The 110-second waiting deadline does not cancel an in-flight provider request. Avoid concurrent CPU grading. The latest official revision scored 10/15 (67%) with the critical gate failed. This new revision has only public evidence; private questions were not inspected or used for changes.

Security command variants reproduced eleven missed detections and now pass. Educational quotations remain allowed; quote-wrapped attacks and indirect or multilingual commands are not comprehensively detected. See EVAL_REPORT.md for measured scope.

The two-paragraph source cap reproduced omissions on a synthetic three-mechanism question and a public multi-part security question. It is now removed; query filtering and the 8,000-character refusal limit remain. Current offline suite: 45 checks passed. Longer or incidentally relevant extracts remain a tradeoff.
