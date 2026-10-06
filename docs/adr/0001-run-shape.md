# ADR 0001: bounded chain with complete retrieved sources

- Status: accepted
- Date: 2026-10-05

## Context

The corpus has six small documents. A lexical query selected a security heading but omitted the paragraph below it. The regression test failed before complete-source expansion and passed after it. An unsupported demo used zero model calls; supported demos used one. The parser permits one corrective retry, so the maximum is two calls, sharing a 110-second waiting budget.

## Decision (`decision`)

Keep the course's bounded answer chain, expand only the documents already selected by retrieval, and validate the returned answer before exposing it. Use one LLMClient interface for offline fakes and Ollama. Preserve citation validation, strict parsing, a single corrective retry, typed failure refusals, and an application check for direct instructions in the actual evidence.

## Options considered (`options_considered`)

1. Bounded chain with complete retrieved sources: adopted and measured through tests and demos.
2. Autonomous tool-selection loop: not implemented or benchmarked; no additional capability is required for six fixed documents.
3. Orchestration graph: not implemented or benchmarked; the current branches remain explicit in a small chain.

## Why not the other option (`why_not`)

A loop or graph adds control flow without repairing the observed missing-evidence failure. We do not claim that either was slower: no comparative benchmark was run.

## What would reverse it (`reverses_it`)

Revisit full-document expansion if context exceeds 4096 tokens in any fixed evaluation case. Revisit orchestration if at least 3 of 10 independently written developer tasks require conditional use of more than one distinct reader tool. Measure both alternatives on the same model and cases before replacing the chain.

## Limitations

A complete wrong document is still wrong evidence. The instruction detector is a heuristic. The caller timeout bounds waiting but does not forcibly cancel an in-flight provider request. Increased context may increase latency.


## Extractive response refinement

For answers without a review flag, return ranked exact source paragraphs rather than generated synthesis. Validate citations against the context actually shown to the model, preserve recognized comparisons and refuse output exceeding 8,000 characters. This prevents exposing conflicting generated prose as an unflagged answer, at the cost of fluent explanation and potentially incomplete coverage. Lexical ranking and source focusing remain heuristics; exact quotation does not prove entailment or completeness. The model-call and tool budgets are unchanged.
