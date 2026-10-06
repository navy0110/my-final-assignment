# Current checkpoint

2026-10-05, branch codex/generalization-checks, project C:\Users\USUARIO\my-final-assignment.

- Current revision: 27 offline tests and lint passed; 3/3 self-authored citation/refusal variants passed; complete public practice evaluation 10/10, all gates passed, on Ollama / qwen2.5:3b-instruct.
- Responses without a review flag now contain exact source passages; comparison sources, actual-context citation validation, canonical refusals and the 8,000-character budget have regression coverage.
- This revision has not been officially resubmitted. Latest official result: PR #716, evaluated commit 297381ca657a0b2ee40ac2c5ed3d2d2d907ce1d9, 10/15 (67%), critical_safety=false, certificate_eligible=false.
- No private questions or private per-case results informed these changes.
- The unused Ollama 7B model was removed to free disk space. The 3B model and project remain. Explicitly select BOOTCAMP_PROVIDER=ollama and BOOTCAMP_MODEL=qwen2.5:3b-instruct in PowerShell. Do not read or print the ignored .env.

Next steps:
1. Review the generalization proposal and its extractive-answer tradeoff.
2. Update the learner-authored cap01-e5 issue list using docs/ISSUES.md. Course checks previously passed 5/5; the issue text remains stale.
3. Merge the chosen revision and authorize a new official submission.
4. Use DEV3PACK_API_BASE=https://app.geckovision.tech for `uv run bootcamp final submit --github navy0110`.
5. If the known GitHub CLI fork flag incompatibility recurs after generation, deliver the completed bundle unchanged through the existing submissions fork. Verify matching file hashes and evaluated commit.
6. Check only aggregate official results; never inspect or tune on private final questions.

Public project: https://github.com/navy0110/my-final-assignment.
Course root: C:\Users\USUARIO\dev3pack-cohort-2026-09.
Submission fork: C:\Users\USUARIO\submissions.
Preserve completed notebooks and the read-only corpus.


## Official generalization revision, 2026-10-06

Delivery PR #754 (https://github.com/Gecko-Academy/dev3pack-submissions/pull/754) was accepted and merged. Evaluated commit: 5c4661bda7f347a458d46d9d7ecafecf282a2f7f. Practice during submission: 10/10. Official aggregate: 12/15 (80%), overall_threshold=true, critical_safety=false, passed=false, certificate_eligible=false. This improves the previous official aggregate of 10/15 but does not earn certification. The known CLI fork incompatibility was bypassed by copying the completed bundle unchanged, with matching hashes. No private questions or per-case results were inspected. No agent changes followed this result.
