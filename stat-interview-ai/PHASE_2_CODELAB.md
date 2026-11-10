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

Tests: `python3 tests/codelab_check.py` gives 19 PASS. The `phase0_smoke.py` regression gives 22 PASS.
