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
# Onboarding W1-W2
a = ex["OB-W1-01"]["data"]["ae"]
check("OB-W1-01 key", len({r["USUBJID"] for r in a if r["AEDECOD"] == "Headache"}) == ex["OB-W1-01"]["outputAnswer"])
check("OB-W1-02 key", len({r["USUBJID"] for r in ex["OB-W1-02"]["data"]["dm"]}) == ex["OB-W1-02"]["outputAnswer"])
import re as _re
check("OB-W1-03 key", sum(not _re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["AESTDTC"]) for r in ex["OB-W1-03"]["data"]["ae"]) == ex["OB-W1-03"]["outputAnswer"])
check("OB-W2-01 key", sum(r["DOSES"] >= 1 for r in ex["OB-W2-01"]["data"]["adsl"]) == ex["OB-W2-01"]["outputAnswer"])
check("OB-W2-02 key", sum(65 <= r["AGE"] <= 80 for r in ex["OB-W2-02"]["data"]["adsl"]) == ex["OB-W2-02"]["outputAnswer"])
t = ex["OB-W2-03"]["data"]["adsl"][0]["TRTSDT"]
pre = [r for r in sorted(ex["OB-W2-03"]["data"]["lb"], key=lambda r: r["ADT"]) if r["ADT"] <= t and r["AVAL"] != ""]
check("OB-W2-03 key", pre[-1]["AVAL"] == ex["OB-W2-03"]["outputAnswer"])
check("every exercise has a key check", len(ex) == 9)

check("bugAnswer in range", all(0 <= e["bugAnswer"] < len(e["choices"]) for e in ex.values()))

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    if "--allow-skip-browser" in sys.argv:
        print("SKIP browser tests (playwright not installed; --allow-skip-browser given)")
    else:
        check("playwright installed (browser tests are required; pass --allow-skip-browser to run key checks only)", False)
else:
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto((ROOT/"index.html").as_uri())
        check("index links to Code Lab", pg.locator("#codelabLink").count() == 1)
        pg.goto((ROOT/"codelab.html").as_uri())
        check("W2 locked at start", pg.locator("#ex-OB-W2-01").count() == 0 and "locked" in pg.locator("#week-2").inner_text())
        check("W1 + practice render (6)", pg.locator("section.card").count() == 6)
        def attempt(eid, choice, val):
            s = pg.locator(f"#ex-{eid}")
            s.locator(f"input[type=radio][value='{choice}']").check()
            s.locator("input.out").fill(str(val)); s.locator("button.check").click()
            return pg.locator(f"#ex-{eid} .result").get_attribute("class")
        check("wrong number rejected", "bad" in attempt("CL-002", 1, 72))
        check("wrong choice rejected", "bad" in attempt("CL-002", 0, 73))
        check("non-numeric rejected", "bad" in attempt("CL-001", 1, ""))
        for eid in ["OB-W1-01", "OB-W1-02"]:
            e = ex[eid]; check(f"{eid} correct accepted", "ok" in attempt(eid, e["bugAnswer"], e["outputAnswer"]))
        check("W2 still locked at 67%", pg.locator("#ex-OB-W2-01").count() == 0)
        e = ex["OB-W1-03"]; check("OB-W1-03 correct accepted", "ok" in attempt("OB-W1-03", e["bugAnswer"], e["outputAnswer"]))
        check("W2 unlocks at 100%", pg.locator("#ex-OB-W2-01").count() == 1)
        for eid, e in ex.items():
            if eid.startswith("OB-W1"): continue
            check(f"{eid} correct accepted", "ok" in attempt(eid, e["bugAnswer"], e["outputAnswer"]))
        check("score 9/9", "9 / 9" in pg.locator("#labScore").inner_text())
        before = pg.evaluate("JSON.parse(localStorage.getItem('stat-interview-codelab-v1'))['CL-001'].attempts")
        check("correct-then-wrong shows fail", "bad" in attempt("CL-001", 0, 99))
        after = pg.evaluate("JSON.parse(localStorage.getItem('stat-interview-codelab-v1'))['CL-001']")
        check("solve is sticky after later wrong", after["solved"] is True)
        check("attempt counted", after["attempts"] == before + 1)
        pg.reload()
        check("score persists", "9 / 9" in pg.locator("#labScore").inner_text())
        check("W2 open after reload", pg.locator("#ex-OB-W2-01").count() == 1)
        forest = pg.evaluate("localStorage.getItem('stat-interview-learning-forest-v1')")
        check("forest untouched", forest is None)
        pg.once("dialog", lambda d: d.dismiss())
        pg.click("#labReset")
        check("reset cancel keeps results", "9 / 9" in pg.locator("#labScore").inner_text())
        pg.once("dialog", lambda d: d.accept())
        pg.click("#labReset")
        check("reset confirm clears score", "0 / 9" in pg.locator("#labScore").inner_text())
        check("reset relocks W2", pg.locator("#ex-OB-W2-01").count() == 0)
        check("reset clears storage", pg.evaluate("localStorage.getItem('stat-interview-codelab-v1')") == "{}")
        pg.reload()
        check("reset survives reload", "0 / 9" in pg.locator("#labScore").inner_text())
        for w in (320, 375):
            pg.set_viewport_size({"width": w, "height": 800})
            check(f"no overflow {w}", pg.evaluate("document.documentElement.scrollWidth<=innerWidth"))
        check("no JS errors", not errs)
        b.close()
print(f"\n{'ALL PASS' if not fails else str(len(fails))+' FAIL'}"); sys.exit(1 if fails else 0)
