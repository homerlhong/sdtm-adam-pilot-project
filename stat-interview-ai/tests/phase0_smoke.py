"""Phase 0 runtime acceptance tests for stat-interview-ai/index.html.
Run: python3 tests/phase0_smoke.py [path/to/index.html] [chrome_path]
Each check prints PASS / FAIL; exit code 1 if any FAIL."""
import sys, json, os
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__))
PAGE=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else os.path.join(HERE,"..","index.html"))
CHROME=sys.argv[2] if len(sys.argv)>2 else os.environ.get("CHROME_PATH")
URL="file://"+PAGE
results=[]
def check(name,ok,detail=""):
    results.append((name,bool(ok),detail)); print(("PASS" if ok else "FAIL"),"|",name,("| "+str(detail)) if detail else "")

def run_session(pg,level,mode,met_count):
    pg.select_option("#level",str(level)); pg.select_option("#mode",mode); pg.click("#start")
    n=pg.evaluate("questions.length")
    for i in range(n):
        pg.fill("#answer",f"answer {i}"); pg.click("#next")
    btns=pg.locator("#reviews .item")
    for i in range(n):
        pg.locator("#reviews .item").nth(i).get_by_role("button",name="Met" if i<met_count else "Needs work",exact=True).click()
    return n

with sync_playwright() as p:
    kw={"args":["--no-sandbox"]}
    if CHROME: kw["executable_path"]=CHROME
    b=p.chromium.launch(**kw)
    ctx=b.new_context(accept_downloads=True); pg=ctx.new_page(); errs=[]
    pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.on("dialog",lambda d:d.accept())
    pg.goto(URL); pg.wait_for_timeout(300)

    # T1 load
    check("T1 page loads without JS errors",not errs,errs)
    check("T1 forest dashboard renders 7 cards",pg.locator(".forest-card").count()==7)
    # T2 bank integrity
    bank=pg.evaluate("BANK.map(q=>({id:q.id,level:q.level,ok:!!(q.question&&q.answer&&q.focus&&q.followup)}))")
    ids=[q["id"] for q in bank]
    per={l:sum(q["level"]==l for q in bank) for l in range(1,8)}
    check("T2 35 questions, unique IDs",len(bank)==35 and len(set(ids))==35,len(bank))
    check("T2 5 questions per level",all(v==5 for v in per.values()),per)
    check("T2 all required fields non-empty",all(q["ok"] for q in bank))
    check("T2 ID prefix matches level",all(q["id"].startswith(f"L{q['level']}-") for q in bank))
    extras=pg.evaluate("Object.keys(EXTRAS)")
    check("T2 every EXTRAS key maps to a question",set(extras)<=set(ids),set(extras)-set(ids))

    # T3 every question renders; hints & code work
    bad=[]
    for level in range(1,8):
        pg.select_option("#level",str(level)); pg.select_option("#mode","all"); pg.click("#start")
        for i in range(5):
            qid=pg.evaluate("questions[pos].id"); q=pg.inner_text("#question")
            if not q.strip(): bad.append((qid,"empty question"))
            pg.click("#hint1")
            if not pg.is_visible("#hintpanel") or "Hint 1" not in pg.inner_text("#hintpanel"): bad.append((qid,"hint1"))
            pg.click("#hint2")
            if "Hint 2" not in pg.inner_text("#hintpanel"): bad.append((qid,"hint2"))
            has_code=qid in extras and pg.evaluate(f"!!EXTRAS['{qid}'].code")
            if has_code:
                pg.click("#codebtn")
                if not pg.is_visible("#codepanel") or not pg.inner_text("#codesample").strip(): bad.append((qid,"code"))
            elif not pg.is_disabled("#codebtn"): bad.append((qid,"code button should be disabled"))
            pg.fill("#answer","x"); pg.click("#next")
        pg.click("#restart")
    check("T3 all 35 questions render with working Hint1/Hint2/View Code",not bad,bad)

    # T4 empty answer blocked
    pg.select_option("#level","1"); pg.click("#start"); pg.fill("#answer","  "); pg.click("#next")
    check("T4 empty answer does not advance",pg.evaluate("pos")==0)
    pg.click("#quit")

    # T5 full session scoring 4/5 = 80%
    pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(200)
    run_session(pg,4,"all",4)
    check("T5 full session score 80%",pg.inner_text("#sectionScore").strip()=="80%",pg.inner_text("#sectionScore"))
    check("T5 practice target message",'practice target reached' in pg.inner_text("#forestMessage"))
    # T6 TXT export
    with pg.expect_download() as d: pg.click("#export")
    txt=open(d.value.path(),encoding="utf-8").read()
    check("T6 TXT export filename",d.value.suggested_filename=="stat-interview-practice.txt")
    check("T6 TXT export content",all(s in txt for s in ["Level 4","Coverage: full","Section self-assessed score: 80%","L4-Q001","Self-review: met"]))
    pg.click("#restart")
    # T7 reload persistence
    pg.reload(); pg.wait_for_timeout(200)
    card4=pg.locator(".forest-card").nth(3).inner_text()
    check("T7 L4 forest persists after reload",'80%' in card4 and "Practice target reached" in card4,card4.replace("\n"," "))
    # T8 quick test does not replace full score
    run_session(pg,4,"3",0); pg.click("#restart")
    card4=pg.locator(".forest-card").nth(3).inner_text()
    hist=pg.evaluate("JSON.parse(localStorage.getItem('stat-interview-attempt-history-v2'))")
    check("T8 quick test saved to history",len(hist)==2 and hist[-1]["coverage"]=="quick")
    check("T8 quick test does not replace full-level forest",'80%' in card4,card4.replace("\n"," "))
    # T9 JSON export schema
    with pg.expect_download() as d: pg.click("#exportHistory")
    js=json.load(open(d.value.path()))
    keys={"id","level","met","total","questionIds","method","coverage","updated"}
    check("T9 JSON export schemaVersion 2 and attempt fields",js.get("schemaVersion")==2 and all(keys<=set(a) for a in js["attempts"]),list(js.keys()))
    # T10 reset
    pg.click("#clearForest")
    check("T10 reset clears forest",pg.locator(".forest-card").nth(3).inner_text().count("—")==1)

    # T11 responsive: no horizontal overflow
    over={}
    for w in [320,375,768,1280]:
        pg.set_viewport_size({"width":w,"height":800})
        for view in ["setup","exam"]:
            if view=="exam": pg.select_option("#level","2"); pg.select_option("#mode","all"); pg.click("#start"); pg.click("#codebtn")
            sw=pg.evaluate("document.documentElement.scrollWidth")
            if sw>w: over[f"{w}/{view}"]=sw
            pg.screenshot(path=os.path.join(HERE,"screenshots",f"{view}_{w}.png"),full_page=False) if os.path.isdir(os.path.join(HERE,"screenshots")) else None
            if view=="exam": pg.click("#quit")
    check("T11 no horizontal overflow at 320/375/768/1280",not over,over)

    # T12 keyboard: Tab reaches Start button
    pg.set_viewport_size({"width":1280,"height":800}); pg.reload(); pg.wait_for_timeout(200)
    seen=set()
    for _ in range(40):
        pg.keyboard.press("Tab"); seen.add(pg.evaluate("document.activeElement.id"))
    check("T12 keyboard Tab reaches level, mode and Start",{"level","mode","start"}<=seen)
    # T13 theme
    th={}
    for m in ["day","dark"]:
        pg.select_option("#themeMode",m); th[m]=pg.evaluate("document.documentElement.dataset.theme")
    pg.reload(); pg.wait_for_timeout(200)
    check("T13 Day/Dark manual theme applies and persists",th=={"day":"day","dark":"dark"} and pg.evaluate("document.documentElement.dataset.theme")=="dark",th)
    check("T12 no JS errors during whole run",not errs,errs)
    b.close()
fails=[r for r in results if not r[1]]
print(f"\nSUMMARY: {len(results)-len(fails)} PASS / {len(fails)} FAIL")
sys.exit(1 if fails else 0)
