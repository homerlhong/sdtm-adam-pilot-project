# Phase 2: SAS Code Lab (first 3 exercises)

Status: **LOCAL PASS / NOT DEPLOYED**. Code Lab is served from the same Pages site, which is still disabled.

| ID | Level | Skill | Bug | Output check |
|---|---|---|---|---|
| CL-001 | L2 | MERGE / IN= | No BY statement, so records match by position | Missing EXTRT after fix = 1 |
| CL-002 | L3 | ADSL TRTDURD | Missing +1 | TRTDURD = 73 |
| CL-003 | L4 | PROC COMPARE QC | QC not sorted by the ID variable | Subjects with differences = 2 |

Design
- Grading is deterministic: the exact choice index plus an exact numeric value. There is no keyword or LLM grading.
- Every answer key is recomputed from the embedded input data by `tests/codelab_check.py` (Part A), so the data and the key cannot drift apart.
- Results are stored under `stat-interview-codelab-v1`, separate from the forest score. Merging them into the score is Phase 3 work.
- SAS is not executed in the browser. The output questions ask the learner to predict the result. Running the programs in real SAS remains a manual verification item.

Tests: `python3 tests/codelab_check.py` gives 28 PASS. Without Playwright the script now exits 1 unless `--allow-skip-browser` is passed. It covers sticky solves (correct then wrong), attempt counting, reset with cancel and confirm, and persistence. CI: `.github/workflows/stat-interview-tests.yml`. Scope: grading checks a predicted output, not the semantics of SAS code the learner writes. The `phase0_smoke.py` regression gives 22 PASS.

## Update: T1 Onboarding W1-W2 (Toronto Intelligent College)
- Added 6 exercises: OB-W1-01..03 (AE verbatim vs coded term, DM key uniqueness, partial ISO 8601 dates) and OB-W2-01..03 (SAFFL by exposure, AGEGR1 boundaries, baseline selection).
- Week gate: W2 unlocks only when at least 80% of W1 is solved. The earlier 3 exercises are now the "Practice set".
- Export (TXT and JSON) now also opens a copy panel, because the hosted page blocks downloads.
- Data: invented teaching slices in CDISC Pilot style. No NAMTSO research data.
- Tests: codelab_check.py 45 PASS; phase0_smoke.py 22 PASS.

## Update: Interview training cloud
- Exam mode: full level, hints and code disabled. Records time per answer and paste share. Answers that are 50% or more pasted are flagged in the report, the JSON export and the instructor panel. The flag is deterministic: pasted characters divided by answer length.
- cloud.js: after explicit consent, syncs history and Code Lab results to `attempts/<viewer id>`. The page falls back to "Local only" when the cloud isn't available.
- instructor.html: owner/editors only. Shows KPIs, self-review by level, exam attempts, integrity flags, Code Lab progress by week, and a copyable evaluation packet.
- Access rules: `attempts` read=admin, write=owner. `attempts/{self}` read/write=interact. Learners need Contributor access and see only their own record.
- Tests: cloud_exam_check.py 24 PASS, run against an in-memory mock of the db and user capabilities. The real cloud is checked manually after publishing.
