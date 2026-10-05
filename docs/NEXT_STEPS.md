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


## Improvement branch checkpoint

Branch codex/improve-public-evidence improves paragraph coverage and rejects uncited answers. Its full public 3B evaluation passed 10/10. A subsequent guard change detects commands hidden in lists or later lines; final offline tests: 18 passed, lint passed, including quoted examples and all real corpus documents. Full model grading was not repeated after the guard-only change. The improved version is prepared for review; no official resubmission has run. Next: review the change, update learner-authored cap01-e5 from the revised docs/ISSUES.md, merge/push the chosen final version, then authorize a new official submission. Do not tune on private cases.


## Latest state after authorized resubmission

The improvement PR #1 merged, and main at 297381ca657a0b2ee40ac2c5ed3d2d2d907ce1d9 was officially resubmitted. Practice passed 10/10. Delivery PR #716 was accepted and merged; official grading again returned 10/15 (67%), critical_safety=false and certificate_eligible=false. The course's incompatible GitHub CLI fork option was bypassed by copying the completed bundle unchanged into the isolated submission branch. No new code changes followed the private result. The learner's cap01-e5 issue-list review remains pending. Further improvements must use public examples and general contract tests, never private-question tuning.
