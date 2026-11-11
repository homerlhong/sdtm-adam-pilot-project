"""Exam mode, paste/time logging, training-cloud sync and instructor panel.
Cloud tests run against an in-memory mock of claude.use('db'/'user')."""
import sys, json, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
fails = []
def check(n, c):
    print(("PASS " if c else "FAIL ") + n); c or fails.append(n)

MOCK = """
(() => {
  const store = JSON.parse(sessionStorage.getItem('mockdb') || '{}');
  const save = () => sessionStorage.setItem('mockdb', JSON.stringify(store));
  const snapDoc = (p) => ({id: p.split('/').pop(), exists: p in store, data: () => store[p], metadata: {fromCache: false, hasPendingWrites: false}});
  const db = {
    doc: (p) => ({path: p, get: async () => snapDoc(p), set: async (d) => { store[p] = JSON.parse(JSON.stringify(d)); save(); }}),
    collection: (c) => ({onSnapshot: (next) => { const ds = Object.keys(store).filter(k => k.startsWith(c + '/')).map(snapDoc);
      setTimeout(() => next({docs: ds, size: ds.length, empty: !ds.length, metadata: {fromCache: false}}), 50); return () => {}; }})
  };
  const role = sessionStorage.getItem('mockrole') || 'student';
  const user = {id: async () => role === 'student' ? 'stu1' : 'own1', canEdit: () => role === 'owner',
    profiles: async (ids) => Object.fromEntries(ids.map(i => [i, {name: i === 'stu1' ? 'Test Learner' : ''}]))};
  window.claude = {use: async (n) => n === 'db' ? db : n === 'user' ? user : null};
})();
"""

with sync_playwright() as p:
    b = p.chromium.launch(); errs = []
    # ---- Local mode (no claude) ----
    pg = b.new_page(); pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto((ROOT/"index.html").as_uri())
    check("local: status chip says Local only", "Local only" in pg.locator("#cloudStatus").inner_text())
    check("instructor link present", pg.locator("#instructorLink").count() == 1)
    pg.select_option("#level", "4"); pg.select_option("#mode", "exam"); pg.click("#start")
    check("exam: hints disabled", pg.is_disabled("#hint1") and pg.is_disabled("#hint2"))
    check("exam: code disabled", pg.is_disabled("#codebtn"))
    # Q1 pasted, Q2-5 typed
    pg.evaluate("""() => { const dt = new DataTransfer(); dt.setData('text/plain', 'x'.repeat(200));
      document.getElementById('answer').dispatchEvent(new ClipboardEvent('paste', {clipboardData: dt, bubbles: true})); }""")
    pg.fill("#answer", "x" * 200); pg.click("#next")
    for _ in range(4):
        pg.type("#answer", "own words answer"); pg.click("#next")
    rep = pg.locator("#reviews").inner_text()
    check("report shows pasted flag", "flagged: mostly pasted" in rep)
    check("report shows time", "Time (s)" in rep)
    for btn in pg.locator("#reviews .row button:text('Met')").all(): btn.click()
    hist = pg.evaluate("JSON.parse(localStorage.getItem('stat-interview-attempt-history-v2'))")
    last = hist[-1]
    check("record mode=exam", last.get("mode") == "exam")
    check("integrity has 5 items", len(last.get("integrity", [])) == 5)
    check("Q1 pastedPct 100", last["integrity"][0]["pastedPct"] == 100)
    check("Q2 pastedPct 0", last["integrity"][1]["pastedPct"] == 0)
    check("seconds recorded", all(isinstance(x["seconds"], int) for x in last["integrity"]))
    pg.goto((ROOT/"instructor.html").as_uri())
    check("instructor local preview message", "Local preview" in pg.locator("#state").inner_text())
    pg.close()

    # ---- Cloud mode as student ----
    ctx = b.new_context(); ctx.add_init_script(MOCK)
    pg = ctx.new_page(); pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto((ROOT/"index.html").as_uri())
    pg.wait_for_selector("#cloudAgree", timeout=5000)
    check("consent banner shown", pg.locator("#cloudConsent").count() == 1)
    pg.evaluate("localStorage.setItem('stat-interview-attempt-history-v2', JSON.stringify([{id:'s1',level:2,met:4,total:5,coverage:'full',mode:'exam',integrity:[{id:'L2-Q001',seconds:90,pastedPct:80}],updated:'2026-11-10T10:00:00Z'}]))")
    pg.click("#cloudAgree")
    pg.wait_for_function("document.getElementById('cloudStatus').textContent.includes('synced')", timeout=5000)
    stored = pg.evaluate("JSON.parse(sessionStorage.getItem('mockdb'))")
    check("student doc written at attempts/stu1", "attempts/stu1" in stored)
    check("history synced", stored["attempts/stu1"]["history"][0]["id"] == "s1")
    check("consent time stored", bool(stored["attempts/stu1"]["consentAt"]))
    pg.goto((ROOT/"instructor.html").as_uri())
    check("student blocked from instructor panel", "Instructor only" in pg.locator("#state").inner_text(timeout=5000) if pg.wait_for_function("!document.getElementById('state').textContent.includes('Connecting')", timeout=5000) else False)
    # ---- same session as owner ----
    pg.evaluate("sessionStorage.setItem('mockrole','owner')")
    pg.reload(); pg.wait_for_selector("#panel:not([hidden])", timeout=5000)
    rows = pg.locator("#rows").inner_text()
    check("owner sees learner name", "Test Learner" in rows)
    check("owner sees L2 80%", "L2 80%" in rows)
    check("owner sees pasted flag", "1 pasted" in rows)
    check("kpi learners = 1", pg.locator("#kLearners").inner_text() == "1")
    check("kpi exam = 1", pg.locator("#kExam").inner_text() == "1")
    pg.set_viewport_size({"width": 375, "height": 800})
    check("instructor no page overflow 375", pg.evaluate("document.documentElement.scrollWidth<=innerWidth"))
    check("no JS errors", not errs)
    b.close()
print(f"\n{'ALL PASS' if not fails else str(len(fails))+' FAIL'}"); sys.exit(1 if fails else 0)
