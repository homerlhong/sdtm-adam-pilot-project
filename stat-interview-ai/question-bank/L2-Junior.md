# L2-Junior — Interview Questions

**Status: DRAFT / UNREVIEWED / NO GO**

## Q001 — How do SET and MERGE differ in SAS?

**Reference answer (EN):** SET reads observations from input datasets; MERGE combines observations, often by BY groups.

**考察要点：** 数据拼接与合并

**Follow-up:** What happens with duplicate BY keys?

**Review status:** UNREVIEWED

---

## Q002 — How do WHERE and subsetting IF differ?

**Reference answer (EN):** WHERE filters input observations before DATA-step execution; subsetting IF filters during execution.

**考察要点：** 执行时机

**Follow-up:** Can WHERE use a variable newly created in the step?

**Review status:** UNREVIEWED

---

## Q003 — What is USUBJID?

**Reference answer (EN):** A sponsor-defined identifier uniquely identifying a subject across relevant study datasets.

**考察要点：** 受试者唯一标识

**Follow-up:** How does it differ from SUBJID?

**Review status:** UNREVIEWED

---

## Q004 — What is the DM domain?

**Reference answer (EN):** The SDTM Demographics domain contains one record per subject.

**考察要点：** DM 粒度

**Follow-up:** How do you verify uniqueness?

**Review status:** UNREVIEWED

---

## Q005 — What is independent QC?

**Reference answer (EN):** A verification process sufficiently independent of production to detect errors.

**考察要点：** 独立验证

**Follow-up:** Why not copy production logic?

**Review status:** UNREVIEWED
