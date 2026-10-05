# Ranked issues

| rank | issue | impact |
|---:|---|---|
| 1 | Lexical retrieval, source focusing and excerpt ranking can miss paraphrases, implicit multi-topic questions and other languages. | Relevant evidence can be omitted or incidental passages selected. |
| 2 | Exact quotations and valid citations do not prove question coverage; confidence remains model-reported. | Extractive answers can be incomplete, less fluent or overconfident. Flagged answers can retain prose requiring review. |
| 3 | Direct-command detection covers a small set of English line-start patterns, including list items. | Rephrased attacks can bypass the heuristic; ambiguous examples can cause false positives. |

## Fixed regressions

Complete-source expansion restored paragraphs omitted by chunk retrieval. Public synthetic regressions now also cover comparison-source loss, cited refusals, oversized output, incorrect phrase focusing, unshown citations and generated claims conflicting with source text. Current checks: 27 offline tests, three self-authored citation/refusal contracts and 10/10 public practice cases passed.

## Operational limitation

The 110-second waiting deadline does not cancel an in-flight provider request. Avoid concurrent CPU grading. The latest official revision scored 10/15 (67%) with the critical gate failed. This new revision has only public evidence; private questions were not inspected or used for changes.
