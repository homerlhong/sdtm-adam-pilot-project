# Phase 0 — Source Audit and Acceptance Checklist

Date: 2026-11-10
Status: SOURCE AUDIT COMPLETE / BROWSER QA NOT TESTED
Scope: stat-interview-ai/index.html and current GitHub source

## Evidence
- GitHub connector fetched EXECUTION_PLAN_v1.0.md (8,046 characters) and SPRINT_01_STATUS.md (2,001 characters).
- GitHub connector fetched index.html (39,126 characters), blob SHA 81977a9fc88bc5733b8bbbe8bf7602e9d2046140.
- This verifies files exist on the repository default branch; it does **not** independently verify historical commit a142bb89 or any public Pages deployment.

## Source-level checklist
- [x] Source contains 35 question IDs in seven levels (static inspection; not browser-loaded).
- [x] Two hint controls and contextual View Code control exist.
- [x] Forest dashboard, local attempt history, and reset control exist.
- [x] Day/Dark auto mode and solar-time calculation exist.
- [x] Practice report TXT and history JSON export code exist.
- [x] Forest default background selector exists.
- [ ] 35 questions successfully load and render in browser: NOT TESTED.
- [ ] All hints and code panels function on every eligible question: NOT TESTED.
- [ ] Full/quick session scoring and reload persistence: NOT TESTED.
- [ ] Exported TXT/JSON file contents and schema: NOT TESTED.
- [ ] Mobile layout at 320px/375px/768px and desktop: NOT TESTED.
- [ ] Keyboard navigation and accessible controls: NOT TESTED.
- [ ] Live GitHub Pages URL and HTTPS deployment: NOT TESTED.

## Decisions to lock before Phase 2
1. Code Lab MVP uses precomputed, reviewed expected SAS outputs, never arbitrary SAS execution in browser.
2. Versioned JSON question schema fields: id, level, skill_tag, type, stem, answer_key, rubric, hints, references (with version), reviewer, status. Optional fields for code, expected_log, expected_dataset, and test cases.
3. Scores stay in browser localStorage for MVP. No backend or cross-device sync; JSON export is the backup path.
4. Source checking and technical self-review are required; a second reviewer is optional, not a mandatory gate. Retain existing editorial quality gate of 90/100 with zero critical errors.
5. Practice target 80% is provisional and self-review is not a certified assessment.
6. Acceptance evidence must distinguish source presence from actual runtime PASS.

## Important follow-up
Run browser smoke tests and capture screenshots/console errors before marking Phase 0 GO. No runtime or Pages success is asserted by this report.
