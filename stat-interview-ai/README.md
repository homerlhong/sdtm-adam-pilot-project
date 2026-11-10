# STAT Interview AI — Seven-Level Question Bank

**DRAFT — NOT AUDITED — NO GO.** Seven independent Markdown banks with 35 initial seed questions. This is not yet the proposed 800-question corpus.

- [Level 1: L1-Foundation](question-bank/L1-Foundation.md)
- [Level 2: L2-Junior](question-bank/L2-Junior.md)
- [Level 3: L3-Programmer](question-bank/L3-Programmer.md)
- [Level 4: L4-Senior](question-bank/L4-Senior.md)
- [Level 5: L5-Lead](question-bank/L5-Lead.md)
- [Level 6: L6-Associate-Principal](question-bank/L6-Associate-Principal.md)
- [Level 7: L7-Principal](question-bank/L7-Principal.md)

Each question includes an English prompt, concise reference answer, Chinese evaluation focus and follow-up. Answers are editorial starting points, not yet quality-reviewed model answers. See [Quality Gate 90](evaluation-rubrics/Quality-Gate-90.md). Do not use confidential sponsor data or patient records.

## Browser practice platform (Beta)

The self-contained [index.html](index.html) is a working static practice interface. It embeds the 35 seed questions from the seven Markdown banks and supports level selection, typed responses, progress tracking, draft-answer comparison, manual self-review and a local text-report export. It does **not** provide AI grading, accounts, persistence or a certified 90-point quality score.

### Run locally

Download `index.html` and open it in a modern browser; no build tools or API keys are required.

### Publish with GitHub Pages

This repository's Pages configuration has **not** been checked or changed. For a site at the repository root, configure GitHub Pages to publish the default branch root, then open `/stat-interview-ai/` under the resulting Pages site. If Pages is already configured for another source or site, avoid overwriting it without reviewing existing deployment settings.

The current embedded question snapshot must be regenerated when Markdown questions change. Answers remain in the browser session unless the user explicitly exports the report.

### Guided practice features

- Two progressive, answer-neutral hints per question (concept and approach).
- Contextual **View code** panel for selected programming questions, with illustrative SAS examples; non-code questions clearly mark code as not applicable.
- Random-order option and tracking of hints/code viewed in the review and exported report.
- Hints are learning aids, **not** solutions; code samples are illustrative and require review against applicable study specifications.
- These features do not imply automated answer grading or passing the bank's 90/100 editorial quality gate.

### Day / Dark themes following sunrise and sunset

The interface now offers **Auto (sunrise/sunset)**, **Day**, and **Dark**. In Auto mode, an explicit **Use location** click requests browser geolocation and computes approximate astronomical sunrise and sunset locally. No coordinates are transmitted or stored by this app. Without location permission, Auto uses an explicitly labeled **07:00–19:00 local-clock approximation**, not actual sunrise/sunset. Theme updates approximately once per minute; the manually selected mode is stored in localStorage when available. Location access generally requires HTTPS or localhost, and the calculation is an approximation (not an official astronomical timetable).

### Personalized backgrounds

Choose **Aurora**, **Sunrise**, **Forest**, or **Minimal** and adjust background intensity from 0–100%. The scene palette adapts to the existing Day/Dark theme (including automatic sunrise/sunset switching). Settings are saved locally when browser storage is available; Reset restores Aurora at 72%. Backgrounds are CSS-only and require no image downloads or accounts. Reduced-motion preferences are respected.

### Seven-section learning forest and practice scores

The home page displays seven forest cards (L1–L7). Each completed practice session yields a **self-assessed percentage**: (answers marked Met / all answered questions) × 100. Every 10 percentage points grows approximately one tree in a ten-tree forest. **80% is a provisional practice target, not a certified pass**. A score appears only after every answer in the session has been manually rated; an incomplete review displays no score. The latest completed session per level is saved in browser localStorage, with an explicit Reset learning forest action. The score and tree progress do **not** imply AI grading, independent validation, or passage of the question-bank's separate editorial 90/100 gate.
