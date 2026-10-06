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

A public conjoined-topic query reproduced dropping a retrieved secondary source. Distinct clause winners now prevent single-source focusing. Lexical ambiguity and multilingual phrasing remain limitations. Current offline suite: 47 tests passed.

A real-model public probe returned generic budget paragraphs for an absent universal exact tool-call count. Explicit exact-count requests now require a matching quantity and topic in a cited sentence. This narrow English heuristic does not establish general entailment; numeric paraphrases and coincident quantities remain risks. Offline suite: 49 passed.

Documented retry-once evidence now survives plural exact-count requests. Simple query inflection expansion repairs a reproduced public retrieval miss without adding documents or changing top_k=3. False lexical matches and other languages remain limitations. Current offline suite: 52 passed.

A public safeguard paraphrase omitted the cited defenses paragraph under query-only filtering. Draft term-pair hints restore source quotations without exposing generated prose. Relevance and incidental matches remain risks; current offline suite: 54 passed.

Consistent plural normalization in adjacent-term scoring fixes a reproduced incidental citation on the public OpenAPI safeguard question. Current offline suite: 55 passed; heuristic scoring and draft-hint relevance remain imperfect.

Reviewed-answer validation gap: a valid citation plus human-review flag previously exposed generated claims without passage validation. A synthetic unlimited-writes claim reproduced this bypass. Both reviewed and unreviewed answers now use the same evidence checks and exact excerpts; review remains enabled when requested. Lexical relevance remains a limitation.
