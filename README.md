# mathe-abi

Öffentliches HTML-Lernbuch zur Vorbereitung auf die **mündliche Mathe-Abiturprüfung**
(Baden-Württemberg, Basisfach, Schwerpunkt **Analysis**). Datenklasse **public**, kein Passwortschutz.

Live: **https://mathe.senecheau.com** (GitHub Pages, Quelle `main` / `docs`).

## Stand

Aufbauphase. Veröffentlicht sind die **Startseite** (`index.html`) mit Lernpfaden und
Feedback-Hinweis, die beiden **Spezifikationen** sowie die ersten **Inhaltsseiten**:
- `specs/00-bau-charter.md` — wie wir das Lernbuch bauen und weiterentwickeln (Meta-Spec).
- `specs/10-repo-design-spec.md` — was wir bauen (Design-Spec).
- `content/{kapitel,aufgaben,simulationen,reflexion}/*.md` — das eigentliche Lernbuch (laufend ergänzt).

## Bauen

```bash
python3 tools/build_site.py   # rendert specs/ + content/ -> docs/ (benötigt pandoc)
```

Design-System: `tools/assets/site.css` + `tools/assets/site.js` (klappbare Abschnitte, Sidebar-Navigation,
responsiv Web/Mobil, KaTeX-Skalierung, Vorlesen-Stub). KaTeX und JSXGraph sind lokal vendored unter
`tools/assets/vendor/` (kein CDN zur Laufzeit) und werden nach `docs/assets/vendor/` kopiert.

## Inhalte schreiben (Konventionen für Content-Autoren)

**Ablage je Art** (Dateiname bestimmt die alphabetische Reihenfolge im Kapitelbaum):

| Art | Verzeichnis | Slug-Präfix der Seite |
|---|---|---|
| Themenseite/Kapitel | `content/kapitel/` | `kap-` |
| Beispielaufgabe | `content/aufgaben/` | `auf-` |
| Prüfungssimulation | `content/simulationen/` | `sim-` |
| Reflexionsseite | `content/reflexion/` | `refl-` |

Dateinamen mit führendem `_` (z. B. `_beispiel.md`) werden gebaut, aber im Kapitelbaum als **Test**
markiert. Gebaut wird mit `pandoc -f gfm -t html5 --section-divs --mathjax`.

**Seitenaufbau:** Erste Zeile `# <Titel>` (wird Seitentitel, nicht erneut als Überschrift gerendert).
Danach Top-Level-Abschnitte mit `## ` — sie werden klappbar gerendert.

**Mathe:** LaTeX in `\( … \)` (inline) und `\[ … \]` (abgesetzt) — clientseitig von KaTeX gerendert.
**Keine** `$…$`-Delimiter. Displayformeln stehen in einem horizontal scrollbaren Container.

**Detailkästen** als rohes HTML, beliebig verschachtelt (Schritt → Begründung → Annahme → Herleitung):

```html
<details><summary>Haltung dahinter</summary> … <details><summary>tiefer</summary> … </details></details>
```

**Funktionsdiagramme** als rohes HTML (JSXGraph, jede `id` eindeutig):

```html
<div class="jxgbox" id="jxg-XYZ" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-XYZ',{boundingbox:[xmin,ymax,xmax,ymin],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return x*x;}]);})();</script>
```

Solche Inline-Skripte werden beim Build automatisch so umgeschrieben, dass sie erst laufen, wenn
JSXGraph geladen ist — das Snippet selbst bleibt unverändert.

**Relevanz-/Konfidenz-Tags:** `<span class="tag tag-ok">…</span>` (gesichert) bzw.
`<span class="tag tag-warn">…</span>` (unsicher, z. B. „offiziell Leistungsfach, Basisfach unsicher [80 %]
— mit Lehrkraft prüfen").

## Provenance

Planung, Dialoge und Lernstand bleiben privat im mywiki-Harness; dieses Repo trägt nur rückverweisende
IDs: DLG-2026-06-17-B61, DLG-2026-06-18-B62/B63, DLG-2026-06-18-Z01.
