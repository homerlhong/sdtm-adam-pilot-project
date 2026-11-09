# RCT Statistical Programmer — Mock Interview Q&A

> Practical interview script for Senior Statistical Programmer / Clinical Statistical Programming roles.
>
> Use the answers as speaking frameworks rather than memorizing them word for word.

## 1. Tell me about yourself.

Thank you for taking the time to speak with me today.

I have more than six years of experience in clinical statistical programming, with a strong focus on oncology and end-to-end clinical data delivery. My experience covers SDTM and ADaM development, TFL programming and validation, database-lock activities, and support for regulatory and CSR deliverables.

In addition to hands-on programming, I have taken ownership of delivery coordination—working closely with statisticians, prioritizing critical-path outputs, resolving programming issues under tight timelines, and making sure final deliverables are reproducible and independently QC'd.

One example was a lymphoma study where a specification discrepancy potentially affected 385 outputs close to a reporting milestone. I helped quantify the impact, align the correction with statistics, organize a controlled rerun and independent QC, and complete the remediation within about three days without delaying the CSR.

I am now looking for a role where I can combine strong technical statistical programming with study-level ownership, quality, and cross-functional collaboration.

---

## 2. Walk me through your experience on randomized clinical trials.

My role typically starts with understanding the protocol, SAP, CRF, data standards, randomization and treatment structure, analysis populations, endpoints, and reporting requirements.

From there, I support or develop SDTM and ADaM datasets, implement analysis derivations, program and validate TFLs, and participate in data review and database-lock preparation.

Near final analysis, I focus heavily on controlled inputs, specification freeze, reproducibility, independent QC, and consistency across datasets and outputs. I also work closely with statisticians to resolve analysis questions and make sure the implementation matches the SAP.

The important point for me is that RCT programming is not just producing tables. It is maintaining a traceable chain from collected data through analysis datasets to the final statistical result.

---

## 3. What is the difference between SDTM and ADaM?

SDTM is primarily a standardized representation of collected clinical trial data for regulatory review and downstream use.

ADaM is designed for statistical analysis. It contains analysis-ready variables and derivations that implement the SAP and support traceability to SDTM.

For example, SDTM might contain the collected tumor assessments and dates, while an ADaM time-to-event dataset could contain the derived PFS event indicator, censoring status, analysis date, and time-to-event value.

The key principle is traceability: I should be able to explain how an analysis result was derived from ADaM and how the relevant ADaM variables trace back to standardized or source data.

---

## 4. What is ADSL?

ADSL is the subject-level analysis dataset, normally with one record per subject.

It commonly contains treatment variables, population flags, demographic or baseline characteristics, randomization or stratification information, key dates, and other subject-level variables needed across analyses.

Because many downstream datasets and outputs depend on ADSL, I treat it as a foundational analysis dataset and pay particular attention to treatment definitions, population flags, and consistency of key dates.

---

## 5. Explain ADTTE.

ADTTE is an ADaM time-to-event structure.

Each analysis parameter represents a time-to-event endpoint or related analysis. Typical variables include the parameter, start date, event or censoring date, analysis value, and censoring indicator.

For an endpoint such as PFS, the difficult part is usually not calculating the number of days. The critical programming work is implementing the SAP-defined event and censoring rules correctly—for example, how progression, death, missing assessments, new anticancer therapy, or analysis cutoff are handled.

I therefore make the event/censoring logic explicit and test boundary cases carefully.

---

## 6. How would you program PFS?

I start with the exact SAP definition rather than assuming a generic PFS algorithm.

I identify the time origin, qualifying progression assessments, death rules, censoring rules, analysis cutoff, handling of missing assessments, and any rules around subsequent therapy.

Then I build a subject-level event timeline, identify the earliest qualifying event according to the SAP, derive the censoring date when there is no event, and calculate the analysis time.

I validate both the derived date and the reason for event or censoring. For important endpoints, I also review representative edge cases manually because a plausible-looking PFS number can still be derived under the wrong rule.

---

## 7. What is the difference between OS and PFS?

OS is generally time from the defined origin, often randomization, to death from any cause.

PFS is time to disease progression or death, based on protocol-defined assessment and censoring rules.

OS is usually simpler from an event-definition perspective, while PFS can be considerably more complex because assessment schedules, missing tumor assessments, progression criteria, new therapy, and censoring rules can affect the derivation.

---

## 8. What oncology endpoints have you worked with or can you discuss?

I am comfortable discussing endpoints such as PFS, OS, ORR and DOR.

For time-to-event endpoints I can work with Kaplan–Meier estimates, medians and confidence intervals, Cox proportional hazards models, hazard ratios, stratified analyses, and sensitivity analyses.

For response endpoints, the programming focus includes the response criteria, analysis population, confirmation requirements where applicable, best overall response logic, and denominator definition.

In oncology, I pay particular attention to dates and assessment sequences because small differences in event logic can materially change the endpoint.

---

## 9. How do you validate a TFL?

I first verify that the output matches the approved shell and SAP.

Then I validate the analysis population, treatment groups, denominators, parameters, visits or time points, statistical method, missing-data handling, titles and footnotes.

I also verify traceability to the analysis dataset.

For critical outputs, I prefer independent programming or independent derivation rather than simply reviewing production code. I want QC to provide independent evidence that the result is correct.

---

## 10. What is independent QC?

Independent QC means the validation is sufficiently independent from the production implementation to detect errors rather than reproduce them.

For a critical analysis, that may involve a separate programmer, independently written code, an alternative derivation, or targeted independent calculations.

The appropriate level depends on risk. A primary efficacy endpoint deserves stronger independent validation than a low-risk formatting change.

---

## 11. Tell me about a major issue you found near database lock.

In a lymphoma study, we identified a discrepancy between the intended specification and its implementation near a critical reporting milestone.

The first thing I did was quantify the impact. We determined that 385 outputs were potentially affected, but we also identified what remained unaffected and which outputs were on the CSR critical path.

I aligned the corrected specification with the statistician and divided the remediation into parallel workstreams: specification alignment, controlled production reruns, and independent QC beginning as soon as corrected outputs became available.

We maintained a controlled list of impacted deliverables and did not release outputs until the required QC evidence was complete.

The remediation was completed within approximately three days and the CSR remained on schedule.

The main lesson was that under pressure, the fastest approach is not uncontrolled rerunning. It is rapid impact assessment followed by controlled parallel execution.

---

## 12. How did you determine the rerun scope for the 385 potentially affected outputs?

I would distinguish between potentially impacted and confirmed impacted outputs.

The impact assessment traced the specification discrepancy to the datasets, derivations, programs, or shared components that depended on it. From that dependency analysis we identified the population of outputs that required remediation or verification.

I would never claim that every output changed numerically simply because it was in the rerun scope. The controlled rerun scope is intentionally conservative when an upstream dependency could affect an output.

---

## 13. How did you prevent the rerun from introducing new errors?

We treated the rerun as a controlled change.

The corrected specification was aligned first, the affected scope was documented, production and QC responsibilities were separated, and independent QC started on completed outputs rather than waiting until the entire batch was finished.

We also tracked completion status so that only outputs with the required evidence could be released.

That is important because a large emergency rerun can itself become a quality risk if change control is weak.

---

## 14. When would you tell the sponsor about a programming issue?

Early, but with enough information to make the communication useful.

My approach is to establish the initial scope quickly and communicate three things: what we found, what is and is not affected, and the remediation plan with its expected timeline.

I do not want the sponsor to hear only that "there is a problem" with no assessment behind it. At the same time, I would not wait until everything is fixed if a significant milestone could be affected.

---

## 15. What if the CSR date really cannot be met?

I would escalate early with options rather than allow the deadline to fail silently.

For example, depending on the study, we might prioritize primary efficacy and key safety outputs first, use a phased delivery, or adjust lower-priority deliverables.

The statistician, programming lead and relevant stakeholders need a transparent view of the critical path, risks and trade-offs.

My role is to provide an evidence-based assessment of what can realistically be delivered and what controls are required.

---

## 16. How do you handle an ambiguous SAP or specification?

I do not silently make a statistical decision in the program.

I identify the ambiguity, reproduce or illustrate the issue if necessary, determine which datasets or outputs it could affect, and discuss it with the statistician.

Once the decision is agreed, it should be reflected in the controlled specification or documented decision trail before implementation.

This keeps the boundary clear between statistical decision-making and programming implementation.

---

## 17. What would you do if you disagree with the statistician?

I would focus on evidence and the analysis requirement rather than framing it as a personal disagreement.

I would explain what I see in the protocol, SAP, data, or existing specification; show the downstream consequence of each interpretation; and ask for clarification or a documented decision.

If the issue has regulatory, scientific, or timeline implications, I would escalate through the appropriate study process.

Once the statistical decision is made and documented, my responsibility is to implement it correctly.

---

## 18. How do you prioritize when everything is urgent?

I prioritize based on the critical path and risk.

Primary efficacy, key safety, database-lock dependencies and CSR-critical outputs generally come before lower-priority exploratory or cosmetic work.

I identify dependencies so that one blocked task does not stop independent work, and I split the team into parallel streams where possible.

During a high-pressure period I also use short checkpoints so blockers and changes in priority become visible quickly.

---

## 19. How do you ensure reproducibility?

I use controlled versions of programs and specifications, clearly defined input datasets, documented dependencies, deterministic derivations, and retained logs and QC evidence.

At important milestones, analysis inputs should be frozen or otherwise controlled.

Another programmer should be able to understand which code and inputs produced the final output and reproduce it without relying on undocumented manual steps.

---

## 20. What does traceability mean to you?

Traceability means being able to follow a reported result backward through the analysis dataset and derivations to the standardized or source data and the analysis requirement.

There are different levels of traceability, but the practical question is simple: if a reviewer challenges a number in a table, can we explain where it came from and reproduce it?

Good traceability makes both QC and regulatory review much stronger.

---

## 21. What do you check before database lock?

I focus on unresolved data issues, key endpoint data, analysis population inputs, treatment and randomization information, important dates, protocol deviations, coding status where relevant, and any open programming or specification issues.

From the programming side, I also want critical derivations tested before lock. Database lock should not be the first time we discover that the final endpoint algorithm has an unresolved interpretation.

---

## 22. What is your approach after database lock?

After lock, change control becomes especially important.

I verify the correct locked input, execute the approved production workflow, review logs and unexpected changes, complete independent QC, and reconcile final outputs.

Any post-lock data or specification change needs to be controlled and its downstream impact assessed.

The objective is a reproducible final analysis package rather than a collection of manually corrected outputs.

---

## 23. How do you handle log warnings?

I do not use a blanket rule that every warning is an error or that warnings can simply be ignored.

I classify them.

Some messages are expected and documented; others may indicate missing values, conversion problems, uninitialized variables, merge issues, truncation, invalid operations, or other programming defects.

For production deliverables, unexpected warnings need investigation and resolution or documented justification.

---

## 24. How do you validate a derived variable?

I start with the specification and identify the inputs, algorithm and edge cases.

Then I validate representative subjects, including normal cases and boundary conditions, and compare against an independent implementation or derivation where appropriate.

For a complex variable, I also inspect intermediate components rather than validating only the final value.

This is particularly important for dates, baseline selection, population flags and time-to-event variables.

---

## 25. How do you approach a new study?

I first understand the study rather than immediately start coding.

I review the protocol, SAP, CRF, standards, treatment design, populations, endpoints, shells, timelines and existing reusable standards.

Then I identify high-risk or complex areas early—often efficacy endpoints, time-to-event logic, special safety analyses, or unusual data structures.

Early clarification is much cheaper than discovering an interpretation problem during final production.

---

## 26. How do you work with junior programmers?

I try to give them both a clear deliverable and the context behind it.

For technical review, I focus first on whether the analysis logic and traceability are correct, then on code quality and efficiency.

I also encourage them to escalate ambiguity early rather than make silent assumptions.

During critical milestones, I assign work according to experience and risk so that complex endpoints receive the appropriate level of oversight.

---

## 27. What makes a strong Senior Statistical Programmer?

Technical SAS or R skills are necessary, but they are not sufficient.

A strong senior programmer understands the study, anticipates downstream impact, recognizes ambiguity, protects quality under timeline pressure, communicates clearly with statisticians and stakeholders, and takes ownership of delivery.

At senior level, I think the question changes from "Can you program this table?" to "Can we trust you to help deliver this analysis correctly?"

---

## 28. Why should we hire you?

I bring a combination of hands-on statistical programming and delivery ownership.

I understand SDTM, ADaM, TFL production and validation, but I have also worked through the operational realities of clinical reporting—database locks, specification issues, large-scale reruns, independent QC, tight CSR timelines, and cross-functional communication.

My strength is that I do not treat programming as an isolated coding task. I focus on the complete evidence chain: the analysis requirement, implementation, validation, traceability and final delivery.

---

## 29. Why are you looking for a new opportunity?

I am looking for a role where statistical programming is a core capability and where I can continue developing both technically and as a study-level contributor.

I particularly value environments where programmers work closely with statisticians, have meaningful ownership of deliverables, and are involved in solving analysis and delivery problems rather than only receiving isolated programming tasks.

---

## 30. Do you have any questions for us?

Yes. I would like to understand how programming ownership works on your studies.

How are responsibilities divided between the study programmer, programming lead and statistician, particularly around database lock and final analysis?

I would also be interested in how independent QC is organized for key efficacy and safety deliverables, and what you would expect someone in this role to take ownership of during the first six months.

---

# Rapid-Fire Technical Review

Before an interview, be ready to explain these without memorized textbook definitions:

- SDTM vs ADaM
- ADSL
- BDS
- ADTTE
- treatment-emergent adverse events
- baseline definition
- analysis population flags
- randomization vs actual treatment
- Kaplan–Meier analysis
- hazard ratio and Cox model
- censoring
- PFS vs OS
- ORR and DOR
- independent QC
- double programming
- define.xml
- reviewer guides
- database lock
- source-to-output traceability
- controlled rerun
- impact assessment

# Interview Rule

For technical questions:

**Definition → how I implement it → what can go wrong → how I validate it.**

For behavioral questions:

**Situation → scope/impact → action → control/QC → measurable result → lesson.**

For the lymphoma database-lock case, keep the factual anchors consistent:

**specification discrepancy → 385 potentially affected outputs → statistician alignment → controlled rerun + independent QC in parallel → approximately three days → CSR remained on schedule.**
