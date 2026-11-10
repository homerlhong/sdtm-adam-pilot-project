# L2-Junior — Interview Questions

**Status: DRAFT / SELF-REVIEW PENDING / NO GO**

## Level competency and review guidance

**Expected evidence:** Explain SAS processing behavior and basic SDTM record granularity.

**Common failure modes:** Treating NODUPKEY as a safe fix; overlooking BY-key cardinality.

**Scoring per question (0–10):** technical correctness 0–4; level-appropriate reasoning 0–2; clarity 0–2; edge cases or limitations 0–2. A score is not assigned until a documented review is performed.

**Important:** The concise reference answer is a starting point, not an exhaustive or universally applicable response. Check study-specific definitions against the applicable protocol, SAP, and standard version.


## Q001 — How do SET and MERGE differ in SAS?

**Reference answer (EN):** SET reads observations from input datasets; MERGE combines observations, often by BY groups.

**考察要点：** 数据拼接与合并

**Follow-up:** What happens with duplicate BY keys?

**Review status:** SELF-REVIEW PENDING

**Candidate scoring guide:** 0–4 accuracy; 0–2 reasoning; 0–2 clarity; 0–2 limitations. **Score:** NOT ASSESSED

---

## Q002 — How do WHERE and subsetting IF differ?

**Reference answer (EN):** WHERE filters input observations before DATA-step execution; subsetting IF filters during execution.

**考察要点：** 执行时机

**Follow-up:** Can WHERE use a variable newly created in the step?

**Review status:** SELF-REVIEW PENDING

**Candidate scoring guide:** 0–4 accuracy; 0–2 reasoning; 0–2 clarity; 0–2 limitations. **Score:** NOT ASSESSED

---

## Q003 — What is USUBJID?

**Reference answer (EN):** A sponsor-defined identifier uniquely identifying a subject across relevant study datasets.

**考察要点：** 受试者唯一标识

**Follow-up:** How does it differ from SUBJID?

**Review status:** SELF-REVIEW PENDING

**Candidate scoring guide:** 0–4 accuracy; 0–2 reasoning; 0–2 clarity; 0–2 limitations. **Score:** NOT ASSESSED

---

## Q004 — What is the DM domain?

**Reference answer (EN):** The SDTM Demographics domain contains one record per subject.

**考察要点：** DM 粒度

**Follow-up:** How do you verify uniqueness?

**Review status:** SELF-REVIEW PENDING

**Candidate scoring guide:** 0–4 accuracy; 0–2 reasoning; 0–2 clarity; 0–2 limitations. **Score:** NOT ASSESSED

---

## Q005 — What is independent QC?

**Reference answer (EN):** A verification process sufficiently independent of production to detect errors.

**考察要点：** 独立验证

**Follow-up:** Why not copy production logic?

**Review status:** SELF-REVIEW PENDING

**Candidate scoring guide:** 0–4 accuracy; 0–2 reasoning; 0–2 clarity; 0–2 limitations. **Score:** NOT ASSESSED
