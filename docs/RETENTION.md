# Retention policy

STORED: No conversation history, preferences, or user episodes. The agent holds the six read-only documents and its model adapter in memory. A question, its selected evidence and a model reply exist transiently during a run.

WHY: Corpus documents support retrieval; transient inputs support one answer. No previous question is used as evidence for another.

CORRECTED BY: Start a new agent instance to reset runtime state. There is no persistent conversation store to edit or clear.

EXPIRES: Conversation-history cap: 0 episodes. Normal-run objects become eligible for cleanup when the run returns. A timed-out provider thread may retain transient inputs until the underlying request terminates; the caller's deadline does not guarantee immediate deletion.

WE REFUSE TO REMEMBER: API keys, credentials, personal profiles, private final questions, and user conversation history in any persistent application store. Provider configuration stays in the ignored local .env; the agent never opens that file as a document source.

## How the code enforces it

`YourAgent.run` constructs evidence and deadline adapters for each question. Only the current question and the versioned corpus feed retrieval. There is no database or history collection.

`test_memory_is_capped_reset_and_kept_per_user` verifies that a marker from an earlier question does not enter a subsequent prompt, that an unsupported question spends no model call after a supported one, and that separate agent instances do not share mutable document lists. The offline FakeLLM intentionally records prompts for test assertions; this is test instrumentation, not application conversation memory.

## Operational boundary

Returned traces and CLI output can be saved explicitly by the operator. Ollama has its own process and lifecycle; this policy describes the application, not a claim about all retention inside that service.

## Development artifacts

The PUBLIC_VARIANTS reports intentionally retain self-authored public-corpus questions, answers and traces for before/after review. They contain no private final questions or user conversation history. They are versioned development evidence, separate from runtime memory.
