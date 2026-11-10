# STAT Interview AI — Forest Learning Platform Execution Plan v1.0

Date: 2026-11-10
Status: PROPOSED / IMPLEMENTATION PLAN
Repository: homerlhong/sdtm-adam-pilot-project
Scope: stat-interview-ai/

## 1. Mission and boundaries
Build a reliable interview preparation platform for clinical statistical programmers, covering L1–L7, with progressive hints, SAS code reading, objective exercises, honest feedback and a forest-growth learning dashboard. This is a practice platform, not a certification body.

Existing baseline: static HTML/CSS/JS beta, 35 draft seed questions, seven levels, manual self-review, progressive hints, selected SAS examples, local-only reports, sunrise/sunset theme switching, Forest default and per-level forest visualization. Target bank: 800 (80/100/120/140/120/120/120). No claim of published Pages deployment or browser QA.

## 2. Product principles
1. Forest is a visualization of evidence-based practice progress, not a substitute for assessment.
2. Distinguish user performance scores from the separate editorial question quality gate (90/100).
3. Keep draft questions marked DRAFT until self-review and source/technical checks pass; independent technical review is not a mandatory gate.
4. Code examples are illustrative; no untrusted SAS is executed in the browser.
5. Never present keyword heuristics as validated AI grading.
6. Accessible contrast, keyboard navigation, reduced motion and privacy-first storage are release requirements.

## 3. Workstreams and milestones

### Phase 0 — Baseline audit and test harness (1–2 working days)
- Inspect HTML/JS, document existing flows and failure modes; confirm GitHub Pages deployment status.
- Add automated static checks and browser smoke tests: start, level selection, hint disclosure, code display, review, export, theme switching, forest persistence.
- Verify accessibility and responsive behavior at mobile/desktop widths.
Deliverable: baseline test report, issue list, reproducible checks.
Exit: critical existing flows pass; blockers documented.

### Phase 1 — Forest dashboard and score semantics (2–3 days)
- Separate per-session results from per-level aggregates; store attempt IDs, timestamps, level, question IDs, assessment method and score provenance.
- Define provisional session score = Met / total × 100, only when all answers are self-rated.
- Display coverage and latest attempt alongside score; avoid treating a 3-question attempt as equivalent to a full assessment.
- Provisional 80% practice target, explicitly NOT certified passing; 10-tree growth visualization, accessible text equivalents.
- Add reset/export/import local history; schema versioning and migration from v1 localStorage.
Deliverable: tested seven-forest dashboard with truthful labels.
Exit: no unreviewed answers counted, partial sessions clearly distinguished, persistence tested.

### Phase 2 — Question content architecture and Code Lab MVP (4–6 days)
- Move questions from embedded JS snapshot to structured, versioned JSON with IDs, level, topic, question type, difficulty, learning objective, hints, answer/rubric, source and review status.
- Build question types: multiple-choice, predict-output, find-bug, code-reading and open-ended interview.
- Use safe, deterministic checks for objective exercises; show expected output and rationale after submission.
- Provide SAS syntax highlighting, accessible code copy, and side-by-side explanation. Do not run arbitrary code.
- Add 5–10 carefully checked Code Lab exercises across levels, keeping seed bank counts transparent.
Deliverable: working Code Lab and documented question schema.
Exit: every new exercise has a reproducible expected result or clear review rubric; no false auto-grading claims.

### Phase 3 — Assessment and feedback (4–6 days)
- Implement objective question scoring with test cases and per-question audit trail.
- Open-ended responses remain self-assessed or rubric-assisted; avoid fabricated model scores.
- Add optional hints-used indicators, retry, targeted remediation and follow-up questions.
- Separate diagnostic practice from assessment mode; define how hints affect eligibility for a future benchmark.
Deliverable: score provenance and transparent review screen.
Exit: scoring regression tests pass and the UI identifies grading method for every result.

### Phase 4 — Bank expansion and editorial QA (ongoing, 2–4 weeks for initial tranche)
- Expand in reviewable batches, prioritizing L3–L5 SDTM/ADaM/TFL and SAS cases.
- Each item: technical source check, ambiguity check, correct answer and alternatives, difficulty, rubric, code reproducibility if relevant.
- Apply existing 90/100 editorial quality gate with technical accuracy >=27/30 and zero critical errors, without mandatory independent technical validation.
- Release reviewed batches incrementally; keep unreviewed content labeled draft.
Deliverable: first 100 reviewed items, then successive batches toward 800.
Exit: per-item status and editorial score traceable; counts distinguish draft from approved.

### Phase 5 — Release hardening and launch (2–3 days)
- Verify Pages configuration, deployed URL, HTTPS and asset loading.
- Test desktop/mobile, accessibility, localStorage restrictions, no-data-loss migration and export.
- Add privacy statement, limitation notices, version/changelog, bug-report route and rollback plan.
Deliverable: release candidate and deployment evidence.
Exit: zero known critical defects, smoke tests pass on actual published URL.

## 4. Score model
- Self-review score: 100 × Met / total, shown only when every question is rated.
- Objective score: 100 × correctly answered eligible objective questions / eligible objective questions, separately labeled.
- Never combine methods into one authoritative 'pass' without a published weighting and validated standard.
- Provisional practice target: 80%; editorial item quality gate: 90/100; keep separate.
- Tree growth: floor/round to nearest ten percent for ten visual trees; always show numeric percentage and denominator.
- History: latest, best, number of attempts, question coverage, method, timestamp. For first iteration, latest score only is acceptable if explicitly labeled.

## 5. Architecture
- Static frontend, modular JS, JSON question content, localStorage versioned persistence.
- Optional future server/backend for accounts, secure sync, AI feedback or SAS execution only after separate security and cost design.
- No private clinical data, secrets, or credentials in repository or client-side scripts.

## 6. Acceptance tests
- L1–L7 selection and practice completion work.
- Hints and code examples cannot silently alter objective scoring.
- 0%, 50%, 80%, 100% produce correct tree/percentage views.
- Partial reviews never appear as completed scores.
- Local history survives reload, reset requires confirmation, export is readable.
- Auto Day/Dark changes with local solar times when permission granted; fallback clearly identified.
- Forest theme stays legible at all background intensities.
- Keyboard-only use, semantic labels and reduced-motion behavior verified.
- Published deployment, if claimed, verified with a live smoke test.

## 7. Risks and mitigations
- Small 35-question seed set: show coverage and avoid overinterpreting scores.
- Subjective self-rating: label honestly; add objective tasks incrementally.
- SAS code correctness: validate examples and state assumptions.
- Browser-only storage loss: export/import, warn about clearing browser data.
- Geolocation privacy: opt-in, local computation, no location persistence.
- Scope creep: release vertical slices and stop at acceptance criteria.

## 8. Priority order and first sprint
P0: baseline audit, tests, reliable score model and Forest dashboard.
P1: structured question data and Code Lab MVP.
P2: objective assessment and feedback.
P3: content expansion and live release verification.

First sprint deliverables: QA report, score schema, dashboard refinements, first three Code Lab exercises, and a demo walkthrough. Do not declare GO until tested.
