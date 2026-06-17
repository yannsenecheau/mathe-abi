#!/usr/bin/env python3
"""Baut die Spec-Site (Landing + klappbare Specs) aus Markdown nach docs/.

Nutzt pandoc (--section-divs) für die Markdown->HTML-Wandlung und ein eigenes Design-System
(tools/assets/site.css + site.js). Klappbare Level-2-Abschnitte, Sidebar-TOC, responsiv, kein
Passwortschutz. Aufruf:  python3 tools/build_site.py
"""
import datetime
import html as _html
import os
import re
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
ASSETS_SRC = os.path.join(ROOT, "tools", "assets")
DOMAIN = "mathe.senecheau.com"

# Reihenfolge = Navigation
PAGES = [
    {"slug": "index",       "nav": "Start",          "title": None},
    {"slug": "bau-charter", "nav": "Bau-Charter",    "src": "specs/00-bau-charter.md"},
    {"slug": "design-spec", "nav": "Design-Spec",    "src": "specs/10-repo-design-spec.md"},
]


def sh(args):
    return subprocess.run(args, capture_output=True, text=True)


def git_sha():
    r = sh(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"])
    return r.stdout.strip() or "uncommitted"


def md_to_html(src_path):
    with open(src_path, encoding="utf-8") as fh:
        md = fh.read()
    title = None
    lines = md.splitlines()
    out = []
    for ln in lines:
        if title is None and ln.startswith("# "):
            title = ln[2:].strip()
            continue
        out.append(ln)
    md_body = "\n".join(out)
    r = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", "--section-divs"],
        input=md_body, capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise RuntimeError("pandoc failed: " + r.stderr)
    body = r.stdout
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return title or "Mathe-Abi", body


def build_toc(body):
    items = []
    for m in re.finditer(r'<section id="([^"]+)"[^>]*class="[^"]*level2[^"]*">\s*<h2[^>]*>(.*?)</h2>', body, re.S):
        sec_id, raw = m.group(1), m.group(2)
        label = re.sub(r"<[^>]+>", "", raw).strip()
        items.append((sec_id, label))
    if not items:
        return ""
    lis = "\n".join('<li><a href="#%s">%s</a></li>' % (i, _html.escape(l)) for i, l in items)
    return '<h3>Auf dieser Seite</h3><ul class="toc">%s</ul>' % lis


def topbar(active_slug):
    links = "".join(
        '<a class="navlink%s" href="%s.html">%s</a>' % (
            " active" if p["slug"] == active_slug else "",
            "index" if p["slug"] == "index" else p["slug"],
            p["nav"],
        )
        for p in PAGES
    )
    return (
        '<header class="topbar">'
        '<button class="menu-toggle" aria-label="Menü">&#9776;</button>'
        '<span class="brand">Mathe&#8209;Abi · <b>Léona</b></span>'
        '<span class="spacer"></span>'
        + links +
        '<button id="collapse-all" title="Alles zuklappen">– alle</button>'
        '<button id="expand-all" title="Alles aufklappen">+ alle</button>'
        '</header>'
    )


def shell(active_slug, toc_html, main_html):
    return (
        '<aside class="sidebar">%s</aside>'
        '<main><div class="content">%s</div></main>'
        '<div class="backdrop"></div>'
    ) % (toc_html, main_html)


def page(active_slug, title, toc_html, main_html):
    return (
        "<!doctype html><html lang=de><head><meta charset=utf-8>"
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<meta name="color-scheme" content="light">'
        "<title>%s — Mathe-Abi</title>"
        '<link rel="icon" href="assets/favicon.svg">'
        '<link rel="stylesheet" href="assets/site.css">'
        "</head><body>%s<div class=\"shell\">%s</div>"
        '<script src="assets/site.js" defer></script>'
        "</body></html>"
    ) % (_html.escape(title), topbar(active_slug), shell(active_slug, toc_html, main_html))


def landing(sha, stamp):
    body = """
<h1>Léonas Mathe-Abi-Lernbuch</h1>
<p class="lede">Vorbereitung auf die mündliche Abiturprüfung Mathematik — Baden-Württemberg, Basisfach,
Schwerpunkt Analysis. Diese Startseite hält die Spezifikationen; das eigentliche Lernbuch wird hier
laufend ergänzt.</p>
<div class="meta-row">
  <span>Status: Spezifikation · Aufbau läuft</span>
  <span>Datenklasse: öffentlich</span>
  <span>kein Passwortschutz</span>
  <span>Web &amp; Mobil</span>
</div>
<div class="cards">
  <a class="card" href="bau-charter.html"><h3>Bau-Charter <span class="arrow">→</span></h3>
    <p>Wie wir das Lernbuch bauen und weiterentwickeln: Leitprinzipien, Abläufe, Design- und
    Tech-Entscheidungen mit Begründung.</p></a>
  <a class="card" href="design-spec.html"><h3>Design-Spec <span class="arrow">→</span></h3>
    <p>Was wir bauen: Architektur, Inhalts-Scope (Analysis), Beispielaufgaben, Lernstand, Audio,
    Deployment, Tests, Provenance.</p></a>
</div>
<h2 style="border:none">Worum es geht</h2>
<p>Das Lernbuch erklärt jeden Schritt mitsamt der Haltung dahinter, in klappbaren Detailkästen, die
kaskadiert in die Tiefe gehen. Aufgaben sind realitätsnah zum mündlichen Prüfungsformat; Diagramme sind
interaktiv. Inhalte gibt es genau einmal — an Schnitten wird verwiesen statt wiederholt.</p>
""".strip()
    return body


def main():
    os.makedirs(DOCS, exist_ok=True)
    # Assets
    dst_assets = os.path.join(DOCS, "assets")
    os.makedirs(dst_assets, exist_ok=True)
    for f in os.listdir(ASSETS_SRC):
        shutil.copy2(os.path.join(ASSETS_SRC, f), os.path.join(dst_assets, f))

    sha = git_sha()
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    for p in PAGES:
        if p["slug"] == "index":
            html_doc = page("index", "Start", "", landing(sha, stamp))
        else:
            title, body = md_to_html(os.path.join(ROOT, p["src"]))
            toc = build_toc(body)
            footer = ('<footer class="site">Build %s · %s · Provenance: DLG-2026-06-17-B61, '
                      'DLG-2026-06-18-B62/B63, DLG-2026-06-18-Z01 · Strang <code>mathe-abi</code></footer>'
                      ) % (sha, stamp)
            html_doc = page(p["slug"], title, toc, body + footer)
        with open(os.path.join(DOCS, p["slug"] + ".html"), "w", encoding="utf-8") as out:
            out.write(html_doc)

    # GitHub-Pages-Helfer
    with open(os.path.join(DOCS, ".nojekyll"), "w") as fh:
        fh.write("")
    with open(os.path.join(DOCS, "CNAME"), "w") as fh:
        fh.write(DOMAIN + "\n")
    with open(os.path.join(DOCS, "version.json"), "w", encoding="utf-8") as fh:
        fh.write('{\n  "sha": "%s",\n  "built": "%s",\n  "site": "spec",\n  "strang": "mathe-abi"\n}\n' % (sha, stamp))

    print("Build ok:", sha, stamp)
    print("Seiten:", ", ".join(p["slug"] + ".html" for p in PAGES))


if __name__ == "__main__":
    main()
