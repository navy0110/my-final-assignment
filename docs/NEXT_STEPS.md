# Current checkpoint

2026-10-05: public practice evaluation PASSED with Ollama / qwen2.5:3b-instruct.

- Project: C:\Users\USUARIO\my-final-assignment.
- Full public evaluation: 7/10 (70%); all five critical cases passed. fa-01, fa-02 and fa-03 failed claim_support.
- Contract tests: 13 passed; lint passed.
- Generation: JSON mode, temperature=0, seed=0, one initial call and one parsing retry sharing a 110-second deadline.
- Cited relevant lists are completed with exact source excerpts when labels are omitted. Zero-confidence uncited flagged refusals use the standard course text.
- The evaluation used explicit process environment variables for 3B. Persistent .env was not changed; never read or print it. Use BOOTCAMP_PROVIDER=ollama and BOOTCAMP_MODEL=qwen2.5:3b-instruct for the official submission.
- GitHub CLI is installed at C:\Program Files\GitHub CLI\gh.exe, authenticated as navy0110.
- Public origin: https://github.com/navy0110/my-final-assignment. The approved code is published. Official submission and private grading remain pending.

Next steps:
1. Confirm gh auth status shows navy0110.
2. Review the learner-authored cap01-e5 issue list against docs/ISSUES.md; course checks previously passed 5/5 but the issue text is stale.
3. Publish the project as its own public navy0110/my-final-assignment repository and push the clean committed tree.
4. Use the 3B provider configuration and DEV3PACK_API_BASE=https://app.geckovision.tech for bootcamp final submit --github navy0110.
5. Read the official result in finals/navy0110/result.json; never inspect or tune on private final questions.

Course root: C:\Users\USUARIO\dev3pack-cohort-2026-09. Submission fork: C:\Users\USUARIO\submissions. Preserve completed notebooks; never open solutions/ or secrets.

## Official delivery result

The bundle was delivered through https://github.com/Gecko-Academy/dev3pack-submissions/pull/711, whose submission check passed and which merged automatically on 2026-10-05. The course result evaluated commit 5bfad336c497a87803dab2c7f9f1d479454e3fdb: 10/15 (67%), overall_threshold=true, critical_safety=false, passed=false, certificate_eligible=false. The automatic CLI hand-in failed on an unsupported gh repo fork flag; the already-generated bundle was copied unchanged into an isolated branch of the existing submissions fork. No private questions were inspected to improve the code. Subsequent development must use public practice and general contract tests. The learner's cap01-e5 issue-list review remains pending.
