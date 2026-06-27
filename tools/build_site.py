#!/usr/bin/env python3
"""Baut die Mathe-Abi-Site aus Markdown nach docs/.

Zwei Seitenfamilien teilen sich dieselbe Shell (Topbar + Sidebar + klappbare Level-2-Abschnitte):
  - Spec-Seiten:    index (Startseite), bau-charter, design-spec.
  - Inhaltsseiten:  content/{kapitel,aufgaben,simulationen,reflexion}/*.md.

Markdown -> HTML via pandoc (-f gfm -t html5 --section-divs --mathjax). Mathe wird clientseitig von
KaTeX gerendert (\\(..\\) inline, \\[..\\] display), Funktionsgraphen von JSXGraph. KaTeX und JSXGraph
sind lokal vendored (tools/assets/vendor/, KEIN CDN zur Laufzeit) und werden nach docs/assets/vendor/
kopiert. Kein Passwortschutz.

Aufruf:  python3 tools/build_site.py
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
VENDOR_SRC = os.path.join(ASSETS_SRC, "vendor")
CONTENT = os.path.join(ROOT, "content")
DOMAIN = "mathe.senecheau.com"

PROVENANCE = ("DLG-2026-06-17-B61, DLG-2026-06-18-B62/B63, DLG-2026-06-18-Z01")

# Spec-Seiten (feste Topbar-Navigation, Reihenfolge = Navigation)
SPEC_PAGES = [
    {"slug": "index",       "nav": "Start",       "title": None},
    {"slug": "bau-charter", "nav": "Bau-Charter", "src": "specs/00-bau-charter.md"},
    {"slug": "design-spec", "nav": "Design-Spec", "src": "specs/10-repo-design-spec.md"},
]

# Inhalts-Verzeichnisse: (Ordner unter content/, Überschrift im Kapitelbaum, Slug-Präfix)
CONTENT_DIRS = [
    {"dir": "kapitel",       "label": "Kapitel",         "prefix": "kap-"},
    {"dir": "aufgaben",      "label": "Aufgaben",        "prefix": "auf-"},
    {"dir": "simulationen",  "label": "Prüfungssimulationen", "prefix": "sim-"},
    {"dir": "konvolut",      "label": "Konvolut (Abitur-Aufgaben 2023)", "prefix": "konv-"},
    {"dir": "reflexion",     "label": "Reflexion",       "prefix": "refl-"},
]


def sh(args):
    return subprocess.run(args, capture_output=True, text=True)


def git_sha():
    r = sh(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"])
    return r.stdout.strip() or "uncommitted"


# Math-Delimiter \(..\) und \[..\] sind die Autoren-Konvention; KaTeX rendert sie clientseitig.
# Problem: pandoc -f gfm behandelt '\(' / '\[' als CommonMark-Escapes und frisst den Backslash
# (-> '(' bzw. '['), wodurch die Delimiter verloren gehen. Lösung: Math- und Code-Regionen VOR
# pandoc durch eindeutige Platzhalter schützen und DANACH die Original-LaTeX-Delimiter wieder
# einsetzen. So sieht pandoc die Mathe nie, escaped nichts, und KaTeX bekommt exakt \(..\) / \[..\].
_FENCE_RE = re.compile(r"(^```.*?^```)", re.S | re.M)          # ```-Codeblöcke
_DISPLAY_RE = re.compile(r"\\\[.*?\\\]", re.S)                  # \[ ... \]
_INLINE_RE = re.compile(r"\\\(.*?\\\)", re.S)                   # \( ... \)
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")                      # `inline code`


def _protect_math(md):
    """Ersetzt Code-Fences/Inline-Code und Math-Spans durch Platzhalter; gibt (text, mapping) zurück."""
    store = {}
    counter = [0]

    def stash(s, is_math=False):
        # Rein alphanumerischer Token (kein Sonderzeichen) -> pandoc lässt ihn als Wort unangetastet.
        key = "zZmathphZz%dzZendZz" % counter[0]
        store[key] = (is_math, s)
        counter[0] += 1
        return key

    # Reihenfolge: zuerst Code (damit Mathe-aussehender Text in Code unangetastet bleibt),
    # dann Display-Mathe (greedy-sicher non-greedy), dann Inline-Mathe.
    md = _FENCE_RE.sub(lambda m: stash(m.group(0), False), md)
    md = _INLINE_CODE_RE.sub(lambda m: stash(m.group(0), False), md)
    md = _DISPLAY_RE.sub(lambda m: stash(m.group(0), True), md)
    md = _INLINE_RE.sub(lambda m: stash(m.group(0), True), md)
    return md, store


def _restore_math(html, store):
    # In Math-Spans rohe '<'/'>' zu \lt/\gt wandeln: sonst parst der Browser z. B. '\( a<b \)'
    # als Start-Tag '<b' und die Formel zerbricht (unrendiertes \( bleibt sichtbar). \lt/\gt
    # rendern in KaTeX identisch zu < / >. Code-Spans bleiben unangetastet (is_math=False).
    for key, (is_math, original) in store.items():
        if is_math:
            original = original.replace("<", r" \lt ").replace(">", r" \gt ")
        html = html.replace(key, original)
    return html


def pandoc(md_body):
    shielded, store = _protect_math(md_body)
    r = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", "--section-divs", "--mathjax"],
        input=shielded, capture_output=True, text=True,
    )
    if r.returncode != 0:
        raise RuntimeError("pandoc failed: " + r.stderr)
    body = r.stdout
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    body = _restore_math(body, store)
    body = wrap_jsxgraph_scripts(body)
    return body


def split_title(md):
    """Erste '# '-Zeile = Titel; Rest = Body. Titel wird nicht erneut als <h1> gerendert."""
    title = None
    out = []
    for ln in md.splitlines():
        if title is None and ln.startswith("# "):
            title = ln[2:].strip()
            continue
        out.append(ln)
    return (title or "Mathe-Abi"), "\n".join(out)


def md_file_to_html(src_path):
    with open(src_path, encoding="utf-8") as fh:
        md = fh.read()
    title, body_md = split_title(md)
    return title, pandoc(body_md)


def build_toc(body):
    """TOC der klappbaren Level-2-Abschnitte (für die Sidebar 'Auf dieser Seite')."""
    items = []
    for m in re.finditer(r'<section id="([^"]+)"[^>]*class="[^"]*level2[^"]*">\s*<h2[^>]*>(.*?)</h2>', body, re.S):
        sec_id, raw = m.group(1), m.group(2)
        label = re.sub(r"<[^>]+>", "", raw).strip()
        items.append((sec_id, label))
    if not items:
        return ""
    lis = "\n".join('<li><a href="#%s">%s</a></li>' % (i, _html.escape(l)) for i, l in items)
    return '<h3>Auf dieser Seite</h3><ul class="toc">%s</ul>' % lis


def discover_content():
    """Liest content/{...}/*.md (außer Dateien, deren Name mit '.' beginnt) ein.

    Liefert: dict ordner -> Liste von {slug, title, src, html, toc, label}, alphabetisch nach Dateiname.
    Dateien mit führendem '_' (z. B. _beispiel.md) werden gebaut, aber im Kapitelbaum als (Test) markiert.
    """
    groups = {}
    for spec in CONTENT_DIRS:
        d = os.path.join(CONTENT, spec["dir"])
        entries = []
        if os.path.isdir(d):
            for fn in sorted(os.listdir(d)):
                if not fn.endswith(".md") or fn.startswith("."):
                    continue
                src = os.path.join(d, fn)
                stem = fn[:-3]
                slug = spec["prefix"] + stem.lstrip("_")
                title, html = md_file_to_html(src)
                entries.append({
                    "slug": slug,
                    "title": title,
                    "src": src,
                    "html": html,
                    "toc": build_toc(html),
                    "is_test": fn.startswith("_"),
                })
        groups[spec["dir"]] = entries
    return groups


def chapter_tree(groups, active_slug):
    """Kapitelbaum für die Sidebar der Inhaltsseiten: Gruppen mit Links auf alle Inhaltsseiten."""
    parts = ['<a class="tree-home" href="index.html">&#8962; Startseite</a>']
    for spec in CONTENT_DIRS:
        entries = groups.get(spec["dir"], [])
        if not entries:
            continue
        parts.append('<h3>%s</h3><ul class="tree">' % _html.escape(spec["label"]))
        for e in entries:
            cls = " active" if e["slug"] == active_slug else ""
            suffix = ' <span class="tree-test">Test</span>' if e["is_test"] else ""
            parts.append('<li><a class="tree-link%s" href="%s.html">%s%s</a></li>' % (
                cls, e["slug"], _html.escape(e["title"]), suffix))
        parts.append("</ul>")
    return "".join(parts)


def topbar(active_slug, is_content):
    links = "".join(
        '<a class="navlink%s" href="%s.html">%s</a>' % (
            " active" if p["slug"] == active_slug else "",
            p["slug"],
            p["nav"],
        )
        for p in SPEC_PAGES
    )
    # Auf Inhaltsseiten ist kein Spec-Slug aktiv; Startseite bleibt der Anker.
    return (
        '<header class="topbar">'
        '<button class="menu-toggle" aria-label="Menü">&#9776;</button>'
        '<a class="brand" href="index.html"><b>Mathe&#8209;Abi</b></a>'
        '<span class="spacer"></span>'
        + links +
        '<button class="readaloud" type="button" title="Abschnitt vorlesen lassen">&#9658; Vorlesen</button>'
        '<button id="collapse-all" title="Alles zuklappen">– alle</button>'
        '<button id="expand-all" title="Alles aufklappen">+ alle</button>'
        '</header>'
    )


def shell(sidebar_html, main_html):
    return (
        '<aside class="sidebar">%s</aside>'
        '<main><div class="content">%s</div></main>'
        '<div class="backdrop"></div>'
    ) % (sidebar_html, main_html)


# Bootstrap (synchron, im <head>): eine globale Warteschlange für JSXGraph-Zeichenfunktionen.
# Inline-<script> ohne src ignorieren 'defer' und laufen beim Parsen — also BEVOR die deferte
# jsxgraphcore.js ausgeführt ist. Autoren-Snippets (JXG.JSXGraph.initBoard) werden im Build so
# umgeschrieben, dass sie ihre Funktion in __JXGQ einreihen; ein deferter Runner leert die Queue,
# sobald JXG geladen ist. So bleibt die große Lib non-blocking deferred und das Snippet im Quelltext
# unverändert (Autoren schreiben weiter <script>(function(){var b=JXG.JSXGraph.initBoard(...)...})()</script>).
HEAD_BOOTSTRAP = (
    '<script>window.__JXGQ=window.__JXGQ||[];'
    'window.__jxg=function(fn){if(window.JXG){try{fn();}catch(e){console.error(e);}}'
    'else{window.__JXGQ.push(fn);}};</script>'
)

HEAD_ASSETS = (
    '<link rel="icon" href="assets/favicon.svg">'
    '<link rel="stylesheet" href="assets/vendor/katex.min.css">'
    '<link rel="stylesheet" href="assets/vendor/jsxgraph.css">'
    '<link rel="stylesheet" href="assets/site.css">'
)

# KaTeX + JSXGraph + auto-render. defer hält die Reihenfolge ein; renderMathInElement nach DOMContentLoaded.
BODY_SCRIPTS = (
    '<script src="assets/vendor/katex.min.js" defer></script>'
    '<script src="assets/vendor/auto-render.min.js" defer></script>'
    '<script src="assets/vendor/jsxgraphcore.js" defer></script>'
    '<script src="assets/site.js" defer></script>'
    # Nach DOMContentLoaded: Mathe rendern, dann die eingereihten JSXGraph-Funktionen abarbeiten.
    '<script defer>document.addEventListener("DOMContentLoaded",function(){'
    'if(window.renderMathInElement){renderMathInElement(document.body,{delimiters:['
    '{left:"\\\\[",right:"\\\\]",display:true},'
    '{left:"\\\\(",right:"\\\\)",display:false}'
    '],throwOnError:false});}'
    'if(window.JXG&&window.__JXGQ){var q=window.__JXGQ;window.__JXGQ=[];'
    'q.forEach(function(fn){try{fn();}catch(e){console.error(e);}});}'
    '});</script>'
)

# Inline-Content-<script>, die JSXGraph zeichnen, in die Warteschlange umschreiben (s. HEAD_BOOTSTRAP).
_JXG_SCRIPT_RE = re.compile(
    r'<script(?![^>]*\bsrc=)([^>]*)>(.*?JXG\.JSXGraph.*?)</script>', re.S | re.I)


def wrap_jsxgraph_scripts(html):
    def repl(m):
        attrs, code = m.group(1), m.group(2)
        return '<script%s>window.__jxg(function(){%s});</script>' % (attrs, code)
    return _JXG_SCRIPT_RE.sub(repl, html)


def page(title, sidebar_html, main_html, active_slug, is_content):
    return (
        "<!doctype html><html lang=de><head><meta charset=utf-8>"
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<meta name="color-scheme" content="light">'
        "<title>%s — Mathe-Abi</title>"
        + HEAD_BOOTSTRAP + HEAD_ASSETS +
        "</head><body>%s<div class=\"shell\">%s</div>"
        + BODY_SCRIPTS +
        "</body></html>"
    ) % (_html.escape(title), topbar(active_slug, is_content), shell(sidebar_html, main_html))


def footer(sha, stamp):
    return ('<footer class="site">Build %s · %s · Provenance: %s · Strang <code>mathe-abi</code></footer>'
            ) % (sha, stamp, PROVENANCE)


def landing(groups):
    """Startseite: Lede, zwei Lernpfade, Feedback-Hinweis, Kapitelbaum, Specs."""
    # Kapitel-Karten für den Kapitelbaum-Block auf der Startseite
    tree_cards = []
    for spec in CONTENT_DIRS:
        entries = groups.get(spec["dir"], [])
        if not entries:
            continue
        lis = "".join(
            '<li><a href="%s.html">%s</a>%s</li>' % (
                e["slug"], _html.escape(e["title"]),
                ' <span class="tree-test">Test</span>' if e["is_test"] else "")
            for e in entries
        )
        tree_cards.append('<div class="tree-group"><h3>%s</h3><ul>%s</ul></div>' % (
            _html.escape(spec["label"]), lis))
    tree_html = "".join(tree_cards) or (
        '<p class="muted">Die Kapitel werden hier in Kürze ergänzt. Schau bald wieder vorbei.</p>')

    return """
<h1>Mathe-Abi &mdash; Analysis fürs mündliche Abi</h1>
<p class="lede">Lernbuch für die mündliche Mathe-Abiturprüfung (Baden-Württemberg, Basisfach,
Schwerpunkt Analysis). Alles wird von Hand gerechnet &mdash; hilfsmittelfrei, genau wie in der Prüfung.
Das Buch wächst mit deinem Lernstand mit.</p>

<div class="cards"><a class="card path-verstehen" href="kap-grenzwerte-randverhalten.html">
  <h3>Vertiefung: Grenzwerte (Limes) &amp; Randverhalten <span class="arrow">→</span></h3>
  <p>Wie der Grenzwertbegriff und das „Verhalten an den Rändern" zusammenhängen — ausführlich erklärt mit
  Beispielen, einseitigen Grenzwerten, Asymptoten und der Dominanz der e-Funktion. Eine Ebene tiefer als
  die übrigen Kapitel.</p></a></div>

<p class="podcast-link">&#127911; <b>Zum Anhören unterwegs:</b> <a href="audio/podcast-grenzwerte-ln.mp3">Podcast – Grenzwerte &amp; natürlicher Logarithmus (MP3)</a></p>

<div class="meta-row">
  <span>Mündlich · hilfsmittelfrei</span>
  <span>Schwerpunkt Analysis</span>
  <span>Web &amp; Smartphone</span>
  <span>wächst mit deinem Lernstand</span>
</div>

<h2 style="border:none">So nutzt du das Lernbuch</h2>
<ul>
  <li><b>Lies aktiv.</b> Rechne jeden Beispielschritt selbst mit, bevor du die Lösung aufklappst.</li>
  <li><b>Geh in die Tiefe, wenn du willst.</b> Aufklappbare Kästen (Dreieck &#9658;) zeigen die Haltung hinter jedem Schritt &mdash; warum, welches Prinzip, welche Falle.</li>
  <li><b>Nutze die Graphen.</b> Die Diagramme sind interaktiv &mdash; bewege Punkte, schau, was passiert.</li>
  <li><b>Wiederhole laut.</b> Erkläre dir einen Schritt so, als würdest du ihn im Prüfungsgespräch vortragen.</li>
</ul>

<h2>Feedback</h2>
<p>Beantworte die <a href="refl-reflexion.html">Reflexionsfragen</a> laut als Sprachnachricht &mdash;
daraus passen wir die Inhalte für dich an: Wo es sicher sitzt, geht es schneller; wo noch nicht,
entstehen passgenaue Kapitel und Extra-Übungen für deine Lücken.</p>
<p><a class="btn-primary" href="refl-reflexion.html">&#127908; Zu den Reflexionsfragen</a></p>

<h2>Zwei Wege durch den Stoff</h2>
<div class="cards">
  <a class="card path-pruefung" href="#kapitelbaum"><h3>Prüfungspfad <span class="arrow">→</span></h3>
    <p>Die kürzeste Strecke zur Prüfungsreife. Direkt zu den prüfungsrelevanten Kapiteln, Beispielaufgaben
    im echten mündlichen Format und den Simulationen. Für den Endspurt.</p></a>
  <a class="card path-verstehen" href="#kapitelbaum"><h3>Verstehenspfad <span class="arrow">→</span></h3>
    <p>Von Grund auf. Mehr Tiefe in den Detailkästen, jede Herleitung Schritt für Schritt. Wenn du ein
    Thema wirklich durchdringen willst, statt es nur zu können.</p></a>
</div>
<p class="muted">Beide Wege führen durch dieselben Kapitel &mdash; du entscheidest, wie tief du gehst.
Die genaue Kapitel-Reihenfolge je Pfad wird ergänzt, sobald die ersten Kapitel stehen.</p>

<h2 id="kapitelbaum">Alle Kapitel, Aufgaben und Simulationen</h2>
<div class="tree-overview">%s</div>

<h2>Hintergrund &amp; Spezifikationen</h2>
<p>Wie dieses Lernbuch gebaut und weiterentwickelt wird, steht in den beiden Spezifikationen:</p>
<div class="cards">
  <a class="card" href="bau-charter.html"><h3>Bau-Charter <span class="arrow">→</span></h3>
    <p>Leitprinzipien, Abläufe, Design- und Tech-Entscheidungen mit Begründung.</p></a>
  <a class="card" href="design-spec.html"><h3>Design-Spec <span class="arrow">→</span></h3>
    <p>Architektur, Inhalts-Scope, Beispielaufgaben, Lernstand, Audio, Deployment, Tests.</p></a>
</div>
""".strip() % tree_html


def main():
    os.makedirs(DOCS, exist_ok=True)

    # Assets (CSS/JS/Favicon) flach kopieren, vendor/ separat als Unterordner.
    dst_assets = os.path.join(DOCS, "assets")
    os.makedirs(dst_assets, exist_ok=True)
    for f in os.listdir(ASSETS_SRC):
        s = os.path.join(ASSETS_SRC, f)
        if os.path.isfile(s):
            shutil.copy2(s, os.path.join(dst_assets, f))
    # vendor/ vollständig spiegeln (KaTeX + Fonts + JSXGraph), KEIN CDN zur Laufzeit.
    dst_vendor = os.path.join(dst_assets, "vendor")
    if os.path.isdir(dst_vendor):
        shutil.rmtree(dst_vendor)
    shutil.copytree(VENDOR_SRC, dst_vendor)

    sha = git_sha()
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    groups = discover_content()

    # --- Spec-Seiten ---
    for p in SPEC_PAGES:
        if p["slug"] == "index":
            html_doc = page("Start", "", landing(groups), "index", is_content=False)
        else:
            title, body = md_file_to_html(os.path.join(ROOT, p["src"]))
            toc = build_toc(body)
            html_doc = page(p["slug"], toc, body + footer(sha, stamp), p["slug"], is_content=False)
        with open(os.path.join(DOCS, p["slug"] + ".html"), "w", encoding="utf-8") as out:
            out.write(html_doc)

    # --- Inhaltsseiten ---
    content_count = 0
    for spec in CONTENT_DIRS:
        for e in groups.get(spec["dir"], []):
            sidebar = chapter_tree(groups, e["slug"])
            main_html = e["html"] + footer(sha, stamp)
            html_doc = page(e["title"], sidebar, main_html, e["slug"], is_content=True)
            with open(os.path.join(DOCS, e["slug"] + ".html"), "w", encoding="utf-8") as out:
                out.write(html_doc)
            content_count += 1

    # GitHub-Pages-Helfer
    with open(os.path.join(DOCS, ".nojekyll"), "w") as fh:
        fh.write("")
    with open(os.path.join(DOCS, "CNAME"), "w") as fh:
        fh.write(DOMAIN + "\n")
    with open(os.path.join(DOCS, "version.json"), "w", encoding="utf-8") as fh:
        fh.write('{\n  "sha": "%s",\n  "built": "%s",\n  "site": "lernbuch",\n  "strang": "mathe-abi"\n}\n'
                 % (sha, stamp))

    print("Build ok:", sha, stamp)
    print("Spec-Seiten:", ", ".join(p["slug"] + ".html" for p in SPEC_PAGES))
    print("Inhaltsseiten:", content_count, "(" + ", ".join(
        "%s: %d" % (s["dir"], len(groups.get(s["dir"], []))) for s in CONTENT_DIRS) + ")")


if __name__ == "__main__":
    main()
