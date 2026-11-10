"""Phase 2 Code Lab check.
Part A: recompute every answer key from the embedded data (no SAS needed).
Part B: browser test of grading and persistence (skipped if Playwright is missing)."""
import json, sys, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT/"codelab/exercises.js").read_text()
lab = json.loads(src[src.index("{"):src.rstrip().rstrip(";").rindex("}")+1])
ex = {e["id"]: e for e in lab["exercises"]}
fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name); cond or fails.append(name)

# CL-001: merge BY USUBJID, IF a -> count missing EXTRT
d = ex["CL-001"]["data"]; exmap = {r["USUBJID"]: r["EXTRT"] for r in d["ex"]}
check("CL-001 key", sum(r["USUBJID"] not in exmap for r in d["dm"]) == ex["CL-001"]["outputAnswer"])
# CL-002: TRTEDT - TRTSDT + 1
r = ex["CL-002"]["data"]["adsl"][0]; f = datetime.date.fromisoformat
check("CL-002 key", (f(r["TRTEDT"]) - f(r["TRTSDT"])).days + 1 == ex["CL-002"]["outputAnswer"])
# CL-003: subjects with any differing value
qc = {r["USUBJID"]: r for r in ex["CL-003"]["data"]["qc"]}
diff = sum(any(p[k] != qc[p["USUBJID"]][k] for k in p) for p in ex["CL-003"]["data"]["prod"])
check("CL-003 key", diff == ex["CL-003"]["outputAnswer"])
check("unique ids", len(ex) == len(lab["exercises"]))
check("bugAnswer in range", all(0 <= e["bugAnswer"] < len(e["choices"]) for e in ex.values()))

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("SKIP browser tests (playwright not installed)")
else:
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto((ROOT/"index.html").as_uri())
        check("index links to Code Lab", pg.locator("#codelabLink").count() == 1)
        pg.goto((ROOT/"codelab.html").as_uri())
        check("3 exercises render", pg.locator("section.card").count() == 3)
        def attempt(eid, choice, val):
            s = pg.locator(f"#ex-{eid}")
            s.locator(f"input[type=radio][value='{choice}']").check()
            s.locator("input.out").fill(str(val)); s.locator("button.check").click()
            return s.locator(".result").get_attribute("class")
        check("wrong number rejected", "bad" in attempt("CL-002", 1, 72))
        check("wrong choice rejected", "bad" in attempt("CL-002", 0, 73))
        check("non-numeric rejected", "bad" in attempt("CL-001", 1, "") )
        for eid, e in ex.items():
            check(f"{eid} correct accepted", "ok" in attempt(eid, e["bugAnswer"], e["outputAnswer"]))
        check("score 3/3", "3 / 3" in pg.locator("#labScore").inner_text())
        pg.reload()
        check("score persists", "3 / 3" in pg.locator("#labScore").inner_text())
        forest = pg.evaluate("localStorage.getItem('stat-interview-learning-forest-v1')")
        check("forest untouched", forest is None)
        for w in (320, 375):
            pg.set_viewport_size({"width": w, "height": 800})
            check(f"no overflow {w}", pg.evaluate("document.documentElement.scrollWidth<=innerWidth"))
        check("no JS errors", not errs)
        b.close()
print(f"\n{'ALL PASS' if not fails else str(len(fails))+' FAIL'}"); sys.exit(1 if fails else 0)
