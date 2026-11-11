/* Training cloud sync (Toronto Intelligent College).
   Uploads this viewer's practice history and Code Lab results to attempts/<their id>.
   Works only inside the hosted page with db + user capabilities; otherwise stays "Local only".
   Students see only their own record; the instructor (owner/editors) sees all. */
(function () {
  const HISTORY_KEY = "stat-interview-attempt-history-v2";
  const LAB_KEY = "stat-interview-codelab-v1";
  const CONSENT_KEY = "tic-cloud-consent-v1";
  const chip = document.createElement("div");
  chip.id = "cloudStatus";
  chip.setAttribute("aria-live", "polite");
  chip.style.cssText = "position:fixed;right:10px;bottom:10px;z-index:98;font:12px system-ui;background:#16263d;color:#e6edf6;border:1px solid #3c516f;border-radius:999px;padding:5px 10px;max-width:90vw";
  chip.textContent = "Local only";
  document.body.append(chip);
  const set = (t) => { chip.textContent = t; };

  function read(key, fallback) { try { return JSON.parse(localStorage.getItem(key) || "null") ?? fallback; } catch (e) { return fallback; } }
  function consented() { try { return !!localStorage.getItem(CONSENT_KEY); } catch (e) { return false; } }

  function askConsent(onYes) {
    const bar = document.createElement("div");
    bar.id = "cloudConsent";
    bar.style.cssText = "position:fixed;left:10px;right:10px;bottom:46px;z-index:99;background:#16263d;color:#e6edf6;border:1px solid #60a5fa;border-radius:12px;padding:12px;font:14px system-ui";
    const p = document.createElement("p");
    p.style.margin = "0 0 8px";
    p.textContent = "Toronto Intelligent College training cloud: your answers, scores, time per question and paste share will be visible to the instructor for evaluation. Nothing is shared with other students.";
    const yes = document.createElement("button"); yes.id = "cloudAgree"; yes.textContent = "I agree, sync my results";
    const no = document.createElement("button"); no.textContent = "Not now (stay local)"; no.style.marginLeft = "8px";
    yes.onclick = () => { try { localStorage.setItem(CONSENT_KEY, new Date().toISOString()); } catch (e) {} bar.remove(); onYes(); };
    no.onclick = () => { bar.remove(); set("Local only (not synced)"); };
    bar.append(p, yes, no); document.body.append(bar);
  }

  async function start() {
    if (!window.claude || typeof window.claude.use !== "function") return;
    const [db, user] = await Promise.all([claude.use("db"), claude.use("user")]);
    if (!db || !user) return;
    let uid = null; try { uid = await user.id(); } catch (e) {}
    if (!uid) return;
    const ref = db.doc("attempts/" + uid);
    let last = null, busy = false, readOnly = false;

    async function sync() {
      if (busy || readOnly || !consented()) return;
      const history = read(HISTORY_KEY, []).slice(-100);
      const codelab = read(LAB_KEY, {});
      const body = JSON.stringify({ history, codelab });
      if (body === last) return;
      busy = true; set("Syncing…");
      try {
        await ref.set({ schemaVersion: 1, history, codelab, consentAt: localStorage.getItem(CONSENT_KEY), updated: new Date().toISOString() });
        last = body;
        set("Training cloud · synced " + new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }));
      } catch (e) {
        if (e && (e.code === "invalid_argument" || e.code === "revoked")) { readOnly = true; set("Local only (no permission to sync)"); }
        else set("Sync paused · will retry");
      } finally { busy = false; }
    }
    window.tcSyncNow = sync;
    if (consented()) sync(); else askConsent(sync);
    // Poll local storage for changes; writes only happen when the data actually changed.
    setInterval(sync, 5000);
  }
  start().catch(() => set("Local only"));
})();
