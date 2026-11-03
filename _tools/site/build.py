"""Builds kaluach.com's app sections: /mac, /iKaluach, /win, /android, each with
an about page, a privacy statement and a support page (with the contact form),
in English and Hebrew (he/). Usage: python build.py <site folder>"""
import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import APPS, COMMON_PRIVACY, ACCESS_KEY

SITE = sys.argv[1]
UPDATED = {"en": "Last updated: October 2026", "he": "עודכן לאחרונה: אוקטובר 2026"}
L = {
    "en": dict(home="← Kaluach home", about="About", privacy="Privacy", support="Support", other="עברית",
               features="What it does", req="Requirements", help="Help", more="Privacy and support",
               privacy_title="Privacy Policy", support_title="Support", contact="Contact",
               contact_text="Questions, problems or suggestions? Send a message and you’ll get an answer by email. When reporting a problem with times, please include the date, the location and the zmanim shita selected.",
               name="Your name", email="Your email", version="App version and device (optional)", message="Message", send="Send",
               empty="Leave this empty", privacy_link="Privacy policy", support_card="Questions, problems or suggestions",
               privacy_card="What the app does with your data", footer="Kaluach™ · iKaluach™ · © Abu Mami",
               support_lead="Help and contact for {name}."),
    "he": dict(home="→ דף הבית של קלוח", about="אודות", privacy="פרטיות", support="תמיכה", other="English",
               features="מה האפליקציה עושה", req="דרישות", help="עזרה", more="פרטיות ותמיכה",
               privacy_title="מדיניות פרטיות", support_title="תמיכה", contact="יצירת קשר",
               contact_text="שאלות, בעיות או הצעות? שלחו הודעה, והתשובה תגיע בדוא״ל. בדיווח על בעיה בזמנים, נא לציין את התאריך, את המיקום ואת שיטת הזמנים שנבחרה.",
               name="שם", email="דוא״ל", version="גרסת האפליקציה והמכשיר (לא חובה)", message="הודעה", send="שליחה",
               empty="יש להשאיר ריק", privacy_link="מדיניות פרטיות", support_card="שאלות, בעיות או הצעות",
               privacy_card="מה האפליקציה עושה במידע שלך", footer="קלוח™ · איי־קלוח™ · © Abu Mami",
               support_lead="עזרה ויצירת קשר עבור {name}."),
}


def write(rel, text):
    path = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def root_of(rel):
    """'../' repeated for the page's depth (rel like 'win/privacy/he/index.html')."""
    return "../" * (rel.count("/"))


def page(rel, lang, title, body, app, kind):
    root = root_of(rel)
    he = lang == "he"
    t = L[lang]
    base = f"{root}{app}/"                       # the app's English pages
    def link(k):                                 # this language's page of kind k
        sub = {"about": "", "privacy": "privacy/", "support": "support/"}[k]
        return f"{base}{sub}{'he/' if he else ''}index.html"
    other = f"{base}{ {'about': '', 'privacy': 'privacy/', 'support': 'support/'}[kind] }{'' if he else 'he/'}index.html"
    tabs = " ".join(
        f'<a href="{link(k)}"{" aria-current=\"page\" class=\"current\"" if k == kind else ""}>{t[k]}</a>'
        for k in ("about", "privacy", "support"))
    home = f'<a class="homelink"{" dir=\"rtl\"" if he else ""} href="{root}index.html">{t["home"]}</a>'
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if he else 'ltr'}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <link rel="icon" href="{root}favicon.svg" />
  <link rel="stylesheet" href="{root}assets/site.css" />
</head>
<body><main>
<nav class="booknav">{home}<span class="apptabs">{tabs}</span><span class="langswitch"><a href="{other}">{t['other']}</a></span></nav>
{body}
<footer>{t['footer']}</footer>
</main></body></html>
"""


def app_header(app, d, root, h1, badge=False):
    icon = APPS[app]["icon"]
    mark = (f'<img src="{root}assets/{icon}" width="84" height="84" alt="" />' if icon
            else '<span class="appmark" aria-hidden="true">ק</span>')
    store = APPS[app].get("store")
    if store and store["live"]:
        # About: the store's badge in place of the status line (as the site's commit "Microsoft Store badge").
        # Privacy and Support: "Available in the …Store" instead of "Coming soon".
        # alt_en/alt_he and width default to the Microsoft Store badge's.
        if badge:
            alt = (store.get("alt_he", "הורדה מ־Microsoft Store") if d is APPS[app]["he"]
                   else store.get("alt_en", "Get it from Microsoft"))
            status = (f'<a class="store-badge" href="{store["url"]}"><img src="{store["badge"]}" '
                      f'width="{store.get("width", 200)}" alt="{alt}" /></a>')
        else:
            status = store["he" if d is APPS[app]["he"] else "en"]
        return f'<header class="apphead">{mark}<div><h1>{h1}</h1><p class="status">{status}</p></div></header>'
    return f'<header class="apphead">{mark}<div><h1>{h1}</h1><p class="status">{d["status"]}</p></div></header>'


def help_cards(d, root):
    if not d["help"]:
        return f'<p>{d["helpnote"]}</p>'
    cards = "\n".join(
        f'<a class="card" href="{root}{href.lstrip("./")}"{' dir="rtl" lang="he"' if lang == "עברית" else ' dir="ltr" lang="en"'}><strong>{name}</strong>{lang}</a>'
        for href, name, lang in d["help"])
    return f'<div class="grid">\n{cards}\n</div>\n<p>{d["helpnote"]}</p>'


def build_app(app):
    for lang in ("en", "he"):
        d = APPS[app][lang]
        t = L[lang]
        he = "he/" if lang == "he" else ""

        # About
        rel = f"{app}/{he}index.html"
        root = root_of(rel)
        feats = "\n".join(f"<li>{f}</li>" for f in d["features"])
        extra = f'<h2>{d["extra"][0]}</h2>\n<p>{d["extra"][1]}</p>' if d.get("extra") else ""
        body = f"""{app_header(app, d, root, d['name'], badge=True)}
<p class="lead">{d['lead']}</p>
<h2>{t['features']}</h2>
<ul class="features">
{feats}
</ul>
<h2>{t['req']}</h2>
<p>{d['requirements']}</p>
<h2>{t['help']}</h2>
{help_cards(d, root)}
{extra}
<h2>{t['more']}</h2>
<div class="grid">
<a class="card" href="privacy/{he}index.html"><strong>{t['privacy_title']}</strong>{t['privacy_card']}</a>
<a class="card" href="support/{he}index.html"><strong>{t['support_title']}</strong>{t['support_card']}</a>
</div>"""
        if lang == "he":   # links from app/he/index.html
            body = body.replace('href="privacy/he/index.html"', 'href="../privacy/he/index.html"').replace('href="support/he/index.html"', 'href="../support/he/index.html"')
        write(rel, page(rel, lang, d["plain"], body, app, "about"))

        # Privacy
        rel = f"{app}/privacy/{he}index.html"
        root = root_of(rel)
        support = f"{root}{app}/support/{he}index.html"
        lead = d["privacy"][0][1]
        sections = d["privacy"][1:] + [(h, p.format(support=support)) for h, p in COMMON_PRIVACY[lang]]
        secs = "\n".join(f"<h2>{h}</h2>\n<p>{p}</p>" for h, p in sections)
        body = f"""{app_header(app, d, root, t['privacy_title'] + ' · ' + d['name'])}
<p class="lead">{lead}</p>
{secs}
<p class="note">{UPDATED[lang]}</p>"""
        write(rel, page(rel, lang, f"{d['plain']} · {t['privacy_title']}", body, app, "privacy"))

        # Support
        rel = f"{app}/support/{he}index.html"
        root = root_of(rel)
        subject = f"Kaluach support: {APPS[app]['en']['plain']}"
        body = f"""{app_header(app, d, root, t['support_title'] + ' · ' + d['name'])}
<p class="lead">{t['support_lead'].format(name=d['plain'])}</p>
<h2>{t['help']}</h2>
{help_cards(d, root)}
<h2>{t['contact']}</h2>
<p>{t['contact_text']}</p>
<form class="contact" action="https://api.web3forms.com/submit" method="POST">
  <input type="hidden" name="access_key" value="{ACCESS_KEY}" />
  <input type="hidden" name="subject" value="{html.escape(subject)}" />
  <input type="hidden" name="from_name" value="Kaluach support page ({html.escape(APPS[app]['en']['plain'])})" />
  <input type="hidden" name="topic" value="{html.escape(d['topic'])}" />
  <input type="hidden" name="redirect" value="https://kaluach.com/support/thanks/" />
  <div class="hidden-field" aria-hidden="true"><label>{t['empty']} <input type="checkbox" name="botcheck" tabindex="-1" /></label></div>
  <label>{t['name']} <input type="text" name="name" required="required" maxlength="100" /></label>
  <label>{t['email']} <input type="email" name="email" required="required" maxlength="200" /></label>
  <label>{t['version']} <input type="text" name="version" maxlength="200" /></label>
  <label>{t['message']} <textarea name="message" required="required" maxlength="5000"></textarea></label>
  <button type="submit">{t['send']}</button>
</form>
<p><a href="{root}{app}/privacy/{he}index.html">{t['privacy_link']}</a></p>"""
        write(rel, page(rel, lang, f"{d['plain']} · {t['support_title']}", body, app, "support"))


for a in APPS:
    build_app(a)

# A page that doesn't exist: /ikaluach… (any case) goes to /iKaluach…, as do /Mac, /WIN …
# (GitHub Pages paths are case-sensitive; a second folder can't be used, since macOS
# treats iKaluach and ikaluach as the same folder). Otherwise a short not-found page.
write("404.html", """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Page not found · Kaluach</title>
  <link rel="icon" href="/favicon.svg" />
  <link rel="stylesheet" href="/assets/site.css" />
  <script>
    (function () {
      var p = location.pathname, m = p.match(/^\\/(ikaluach|mac|win|android)(\\/.*)?$/i);
      var canonical = { ikaluach: "iKaluach", mac: "mac", win: "win", android: "android" };
      if (m) {
        var target = "/" + canonical[m[1].toLowerCase()] + (m[2] || "/");
        if (target !== p) location.replace(target + location.search + location.hash);
      }
    })();
  </script>
</head>
<body><main>
<nav class="booknav"><a class="homelink" href="/index.html">← Kaluach home</a></nav>
<header><h1>Page not found</h1></header>
<p class="lead">This page doesn’t exist (any more). The Kaluach apps: <a href="/mac/">Kaluach for the Mac</a> · <a href="/iKaluach/">iKaluach</a> · <a href="/win/">Kaluach for Windows</a> · <a href="/android/">Kaluach for Android</a>.</p>
<p dir="rtl" lang="he">הדף לא נמצא. <a href="/index.html">לדף הבית של קלוח</a></p>
<footer>Kaluach™ · iKaluach™ · © Abu Mami</footer>
</main></body></html>
""")
print("built", len(APPS), "apps")
