# RCT Statistical Programming — Interview Pack

> Interview preparation notes for Senior Statistical Programmer / Clinical Statistical Programming roles.

## 1. 60–90 Second Introduction

Thank you for taking the time to speak with me today.

My background is in clinical statistical programming, with more than six years of experience supporting end-to-end clinical data delivery, particularly in oncology. I have worked across the programming lifecycle, including SDTM and ADaM development, TFL programming and validation, database-lock activities, and regulatory submission deliverables.

Beyond hands-on programming, a significant part of my experience has been delivery ownership. I have coordinated programming activities with statisticians and cross-functional teams, managed issues on the critical path, and helped teams move from database lock through final outputs and CSR delivery while maintaining traceability and independent QC.

One example was a lymphoma study where we identified a specification discrepancy late in the reporting cycle. After impact assessment, we determined that 385 outputs were potentially affected. I helped assess the impact, aligned with the statistician on the corrected specification, and we ran a controlled rerun and independent QC in parallel; remediation was completed in approximately three days and the CSR remained on schedule.

What I am looking for now is a role where I can combine strong hands-on statistical programming with delivery ownership, quality, and cross-functional collaboration.

## 2. RCT Programming Workflow

A practical end-to-end workflow:

1. Review protocol, SAP, CRF, data standards and reporting requirements.
2. Understand randomization, treatment arms, analysis populations, estimands/endpoints and key study milestones.
3. Build or validate SDTM domains and define traceability from source data.
4. Develop ADaM datasets according to the SAP and analysis requirements.
5. Program and independently validate TFLs.
6. Perform ongoing data review and issue reconciliation before database lock.
7. Freeze specifications and inputs at the appropriate milestone.
8. Run final production and independent QC.
9. Support CSR, define.xml, reviewer guides and submission packages where applicable.
10. Maintain reproducibility and source-to-output traceability throughout.

## 3. SDTM

### What is the purpose of SDTM?

SDTM standardizes collected clinical trial data into a consistent structure for regulatory review and downstream analysis.

### Domains I can discuss

- DM — Demographics
- AE — Adverse Events
- CM — Concomitant Medications
- EX — Exposure
- LB — Laboratory Tests
- VS — Vital Signs
- MH — Medical History
- DS — Disposition
- oncology-specific response or disease assessment domains where applicable

### Interview point

I distinguish clearly between **collected data**, **SDTM tabulation**, and **analysis-ready derivations**. Analysis decisions should normally live in ADaM rather than being hidden inside reporting programs.

## 4. ADaM

### Core datasets

**ADSL** — one record per subject; treatment assignments, populations, stratification/baseline variables and key subject-level attributes.

**BDS datasets** — parameter-based analysis structures such as laboratory, efficacy or questionnaire analyses.

**ADTTE** — time-to-event analyses such as PFS or OS, with event/censoring logic and analysis dates explicitly derived.

### Key principle

A reviewer should be able to trace an analysis result from a TFL back to ADaM and ultimately to the standardized/source data.

## 5. TFL Programming and Validation

My approach is to separate production from validation whenever possible.

For a final output I verify:

- correct analysis population;
- treatment assignment and ordering;
- denominators;
- parameter and visit definitions;
- missing-data handling;
- statistical methods;
- titles, footnotes and formatting;
- consistency with SAP and shells;
- traceability to ADaM;
- reproducibility from frozen inputs.

For high-risk outputs, I prioritize independent derivation or independent programming rather than relying only on visual review.

## 6. Oncology Endpoints

### Overall Survival (OS)

Time from the protocol-defined origin, commonly randomization, to death from any cause. Subjects without an event are censored according to the SAP.

### Progression-Free Survival (PFS)

Time from the defined origin to progression or death, according to the protocol/SAP-defined assessment and censoring rules.

### ORR

Typically based on subjects achieving a qualifying confirmed or unconfirmed response according to the protocol-defined response criteria.

### DOR

Duration from the first qualifying response to progression or death, according to the SAP.

### Methods

For time-to-event endpoints I am comfortable discussing Kaplan–Meier estimation, median survival and confidence intervals, Cox proportional hazards models, hazard ratios, stratified analyses, and sensitivity analyses.

The programming responsibility is not merely to call a statistical procedure. The critical work is implementing the endpoint, event and censoring rules exactly as specified and making those derivations auditable.

## 7. Specification Discrepancy / 385 Potentially Affected Outputs Case

### Situation

During a lymphoma study near a critical reporting milestone, we identified a discrepancy between the intended specification and its implementation. The issue potentially affected 385 outputs.

### Task

My responsibility was to establish the true impact quickly, align the correction with statistics, protect the CSR timeline, and ensure that remediation did not introduce additional quality risk.

### Action

First, I quantified before communicating. We performed a rapid impact assessment to identify the root cause, affected outputs, unaffected outputs and items on the CSR critical path.

Second, I communicated the issue early with a defined scope and remediation plan rather than reporting an undefined problem.

Third, I split the work into parallel streams: specification alignment with the statisticians, controlled production reruns, and independent QC beginning as soon as the first corrected outputs became available.

We maintained a controlled list of impacted deliverables and required evidence of successful QC before an output was released.

### Result

The affected outputs were corrected and independently QC'd within approximately three days, and the CSR delivery remained on schedule.

### What this demonstrates

- impact assessment;
- delivery ownership;
- communication under pressure;
- statistician/programmer alignment;
- controlled reruns;
- risk-based prioritization;
- independent QC;
- protection of regulatory traceability.

## 8. Sponsor Communication

When a significant programming issue occurs, I communicate three things:

1. **What happened and why.**
2. **What is and is not affected.**
3. **What we are doing next, with timing and controls.**

I avoid escalating an undefined problem. I first establish enough scope to give stakeholders actionable information, while still communicating early enough that there are no surprises.

If a deadline is genuinely at risk, I present options—for example phased delivery of critical efficacy and safety outputs—rather than waiting until the deadline has already been missed.

## 9. Prioritization Under Tight Timelines

I prioritize by:

- regulatory/CSR critical path;
- primary and key secondary endpoints;
- safety-critical outputs;
- dependencies between datasets and outputs;
- size and severity of the identified issue;
- opportunities for parallel production and QC.

I also use short checkpoints during high-pressure periods so that blockers are identified quickly.

## 10. Quality Philosophy

Quality is not a final-stage inspection activity.

Good statistical programming quality starts with:

- clear specifications;
- controlled inputs;
- reproducible code;
- explicit derivations;
- traceability;
- independent validation;
- documented issue resolution.

The goal is not simply to produce the correct number once. It is to make the result reproducible and defensible.

## 11. Common Interview Questions

### Tell me about a difficult programming issue.

Use the **specification discrepancy / 385 potentially affected outputs case**.

### How do you work with statisticians?

Emphasize early alignment on analysis definitions, documenting decisions, resolving ambiguous specifications before large-scale production, and maintaining a clear boundary between statistical decisions and programming implementation.

### How do you handle conflicting priorities?

Rank by critical path and risk, identify dependencies, agree priorities with the lead/statistician, parallelize independent workstreams, and communicate trade-offs early.

### What do you do when you disagree with a specification?

Do not silently reinterpret it. Reproduce the issue, document the ambiguity or inconsistency, quantify downstream impact, discuss it with the statistician, obtain an agreed decision, update the controlled specification, and then implement.

### How do you ensure reproducibility?

Controlled versions of programs/specifications, frozen analysis inputs at milestones, deterministic derivations, logs/QC evidence, documented dependencies and source-to-output traceability.

### What is the difference between production and QC?

Production implements the approved analysis. QC provides independent evidence that the implementation and result are correct. For critical derivations, independent programming or derivation is stronger than simply reviewing the production code.

## 12. Questions to Ask the Interviewer

Good questions include:

- How is programming ownership divided between study programmers, leads and statisticians?
- How independent is QC for key efficacy and safety deliverables?
- What does the team's workflow look like from database lock through CSR?
- How much direct sponsor interaction do programmers typically have?
- Which CDISC and submission activities would this role own?
- What would success look like in the first six months?

## 13. Final Interview Positioning

The strongest positioning is not simply:

> "I know SAS and CDISC."

It is:

> **I can take ownership of clinical statistical programming from specifications and analysis datasets through validated outputs and critical delivery milestones, while maintaining quality, traceability and clear communication with statisticians and stakeholders.**

That is the message to reinforce throughout the interview.
