# Ranked issues

| rank | issue | impact |
|---:|---|---|
| 1 | Lexical retrieval and excerpt ranking can miss paraphrases or favor incidental overlap. | Relevant evidence can still be omitted; complete-source expansion cannot recover an unretrieved document. |
| 2 | Valid source IDs and appended excerpts do not establish that every generated claim is faithful; confidence remains model-reported. | Unsupported original prose or overconfidence can coexist with accurate quotations. |
| 3 | Direct-command detection covers a small set of English line-start patterns, including list items. | Rephrased attacks can bypass the heuristic; ambiguous examples can cause false positives. |

## Fixed regression

A retrieved security heading omitted its supporting paragraph. Complete-source expansion fixed the reproduced regression. A subsequent check covered only bold lists, omitting ordinary prose. The current paragraph ranking covers both forms and reached 10/10 public practice cases. The list-command guard was extended afterwards and passed the final 18 offline tests, including the unchanged real-corpus check.

## Operational limitation

The 110-second waiting deadline does not cancel an in-flight provider request. Avoid concurrent grading runs on CPU. The previous official score remains 10/15 (67%) with the critical gate failed; this revision has not been resubmitted.
