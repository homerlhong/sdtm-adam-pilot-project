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
