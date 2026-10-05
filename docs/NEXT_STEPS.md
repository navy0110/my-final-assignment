# Resume here

Paused at the learner's request on 2026-10-05.

## Current state

- Local repository: C:\Users\USUARIO\my-final-assignment.
- Ollama: qwen2.5:7b-instruct, local endpoint, configured in ignored .env. Do not read or print .env.
- Nine tests passed after replacing the memory and regression placeholders. No skip or xfail markers remain.
- Full-source evidence expansion fixes the reproduced missing-security-paragraph failure. The live security trace cited prompt-injection and described the documented defenses.
- The waiting deadline is 110 seconds. A timed-out worker can continue until its underlying provider request terminates.
- The last completed full practice score was 5/10 (50%), NOT YET, before complete-source expansion. Do not attribute that score to the latest code.
- The full grading run on the expanded-context version was interrupted to honor the pause. It produced no completed score. An Ollama request may take a short time to wind down.
- docs/ISSUES.md, RETENTION.md, SKILL.md, and adr/0001-run-shape.md contain factual drafts. EVAL_REPORT.md records the measured history and limits.
- README still needs its final project description and demos. The final EVAL_REPORT After section also needs a completed score for the latest implementation.
- No GitHub origin or publication has been configured for this repository. Nothing has been submitted.

## Next steps

1. Run `uv run bootcamp final grade` once and record its actual score and failing gates. Avoid concurrent model evaluations.
2. Diagnose remaining retrieval/generation failures using traces. Do not inspect or tune on private final questions.
3. Finish README and EVAL_REPORT with real command output, preserving honest limitations and source/AI-assistance credits.
4. Copy the three ranked issues to cap01-e5 in the course notebook; let the learner author assessment cells in accordance with the course instructions. Check and submit from the course folder.
5. Publish the final project to its own public navy0110 repository and push the lockfile and code. GitHub CLI was not found on PATH earlier.
6. Only from a clean, pushed repository and with a real provider: prepare the final dry run, then submit to Gecko-Academy/dev3pack-submissions using the navy0110 fork.

Relevant roots: C:\Users\USUARIO\dev3pack-cohort-2026-09 and C:\Users\USUARIO\submissions. Preserve completed student notebooks and never open solutions/ or secrets.
