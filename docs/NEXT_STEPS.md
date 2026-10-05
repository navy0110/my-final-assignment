# Current checkpoint

Work resumed on 2026-10-05. The project has not been published or submitted.

- Local repository: C:\Users\USUARIO\my-final-assignment.
- Eleven contract tests pass; lint passes. GitHub CLI is installed but has no authenticated account.
- Ollama models available locally: qwen2.5:7b-instruct and qwen2.5:3b-instruct.
- The current evaluation explicitly selects the 3B model through process environment variables. Persistent local configuration was not changed. Never read or print .env.
- Latest completed full practice run: 79da180, 7B, 6/10, critical gate failed.
- Latest complete 3B evaluation: 4/10; fa-07 citation failure fixed, critical gate still false.
- The title-selected evidence version is undergoing full 7B public evaluation; result pending.
- Provider requests use JSON mode, temperature=0, seed=0 and a shared 110-second waiting deadline. Deadline expiry does not cancel an in-flight request.

Next: record the full result, fix remaining critical failures if any, align final documentation, commit, publish the public repository and run the official submission from a clean pushed tree. Only public practice cases may guide development.

The cap01 notebook passed 5/5 checks but its issue-list cell still needs learner review against docs/ISSUES.md. Course root: C:\Users\USUARIO\dev3pack-cohort-2026-09. Submission fork: C:\Users\USUARIO\submissions. Preserve completed notebooks and never open solutions/ or secrets.