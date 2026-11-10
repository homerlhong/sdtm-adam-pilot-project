# Phase 0B — Browser Runtime QA

Date: 2026-11-10
Status: **RUNTIME QA PASS (local) / DEPLOYMENT NOT TESTED** — Phase 0 is not GO until the Pages check passes.
Method: Playwright + headless Chrome against `index.html` (file://). Script: `tests/phase0_smoke.py`. Screenshots: `tests/screenshots/`.

## Critical defect found and fixed
| ID | Severity | Finding | Fix |
|---|---|---|---|
| D-001 | **Critical** | On page load: `ReferenceError: Cannot access '$' before initialization`. `$("hint1").onclick=...` ran before `const $` was declared, so the script stopped. Nothing was interactive and the forest dashboard rendered 0 cards. | Moved `const $=id=>document.getElementById(id);` to the first line of the script. Rerunning the test suite on the unfixed file reproduces the FAIL, which shows the test detects this defect. |

Implication: the earlier source audit marked these features as present, but at runtime none of them worked. This confirms decision 6: source presence ≠ runtime PASS.

## Results (after fix): 22 PASS / 0 FAIL
| # | Area | Check | Result |
|---|---|---|---|
| T1 | Load | No JS errors, 7 forest cards | PASS |
| T2 | Bank | 35 unique IDs, 5 per level, required fields non-empty, ID prefix = level, EXTRAS keys valid | PASS |
| T3 | Interaction | All 35 questions render; Hint 1 / Hint 2 on every question; View Code opens on all 9 questions with code, disabled on the 26 without | PASS |
| T4 | Validation | Blank answer does not advance | PASS |
| T5 | Scoring | Full L4, 4/5 Met → 80%, "practice target reached" | PASS |
| T6 | Export | TXT filename and content (level, coverage, score, IDs, marks) | PASS |
| T7 | Persistence | L4 80% survives reload | PASS |
| T8 | Scoring | Quick test saved as `coverage:"quick"`, does not overwrite full score | PASS |
| T9 | Export | JSON `schemaVersion:2`, every attempt has id/level/met/total/questionIds/method/coverage/updated | PASS |
| T10 | Reset | Reset clears forest | PASS |
| T11 | Responsive | No horizontal overflow at 320/375/768/1280 (setup + exam with code panel) | PASS |
| T12 | Keyboard | Tab reaches level, mode, Start; no JS errors across full run | PASS |
| T13 | Theme | Manual Day/Dark applies and persists after reload | PASS |

## NOT TESTED
- **GitHub Pages deployment**: the sandbox network blocks github.io (HTTP 403 from proxy), so this needs a manual check.
- **Branch note**: the default branch is `master` (contains `stat-interview-ai/`). A separate `main` branch (181be24) does **not** contain `stat-interview-ai/`. Links to `.../blob/main/stat-interview-ai/...` return 404. Confirm which branch Pages serves.
- Auto theme by sunrise/sunset (needs geolocation permission), real-device mobile (only viewport emulation was tested), screen-reader behaviour.

## Re-run
```
pip install playwright && python -m playwright install chromium
python3 stat-interview-ai/tests/phase0_smoke.py            # bundled Chromium
python3 stat-interview-ai/tests/phase0_smoke.py index.html /path/to/chrome
```
