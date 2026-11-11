import sys, json, pathlib, re
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
fails = []
def check(n, c):
    print(("PASS " if c else "FAIL ") + n); c or fails.append(n)
s = (ROOT/"index.html").read_text()
q = (ROOT/"questions.js").read_text()
i = s.index("const BANK=") + 11; j = s.index(";const EXTRAS=")
check("questions.js BANK matches index.html", json.loads(s[i:j]) == json.loads(q[q.index("window.BANK=")+12:q.index(";\nwindow.EXTRAS=")]))
MOCK = """window.claude={use:async n=>{
 if(n==='sample'){const f=async(p)=>({text:'What would you do if the deadline were tomorrow?'});f.json=async()=>({structure:2,accuracy:2,validation:1,communication:2,strength:'Clear steps.',gap:'Mention scope.',better:'I would assess downstream impact.'});return f}
 return null}};"""
with sync_playwright() as p:
    b = p.chromium.launch(); errs = []
    for label, script in [("no-AI", None), ("AI", MOCK)]:
        ctx = b.new_context()
        if script: ctx.add_init_script(script)
        pg = ctx.new_page(); pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto((ROOT/"interview.html").as_uri()); pg.wait_for_timeout(300)
        pg.select_option("#level", "1"); pg.click("#startBtn")
        pg.wait_for_selector("#talk:not(.hidden)")
        for k in range(5):
            pg.fill("#answer", "My main answer in my own words."); pg.click("#submitBtn")
            pg.wait_for_function("document.getElementById('phaseTag').textContent.includes('follow-up')")
            pg.fill("#answer", "Follow-up answer."); pg.click("#submitBtn")
            pg.wait_for_selector("#feedback:not(.hidden)")
            if label == "no-AI": pg.click("#selfReview button[data-v='8']")
            pg.click("#nextBtn")
        pg.wait_for_selector("#summary:not(.hidden)")
        h = pg.evaluate("JSON.parse(localStorage.getItem('stat-interview-attempt-history-v2'))")[-1]
        check(f"{label}: 5 answers recorded", h["total"] == 5 and len(h["interview"]) == 5)
        check(f"{label}: method", h["method"] == ("ai-interview" if script else "self-review"))
        if script:
            check("AI: follow-up from model used", h["interview"][0]["followup"].startswith("What would you do"))
            check("AI: score 7/8 -> all met", h["met"] == 5 and h["integrity"][0]["aiScore"] == 7)
        else:
            check("no-AI: bank follow-up used", h["interview"][0]["followup"] == "How does an observational study differ?")
        pg.set_viewport_size({"width": 375, "height": 800})
        check(f"{label}: no overflow 375", pg.evaluate("document.documentElement.scrollWidth<=innerWidth"))
        ctx.close()
    check("no JS errors", not errs)
    b.close()
print("\nALL PASS" if not fails else f"\n{len(fails)} FAIL"); sys.exit(1 if fails else 0)
