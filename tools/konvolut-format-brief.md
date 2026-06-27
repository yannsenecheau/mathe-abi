# Format-Brief — Konvolut-Aufgaben (verbindlich für Writer-Agenten)

Du schreibst **eine** vollständige Konvolut-Aufgabenseite als Markdown-Datei für ein HTML-Lernbuch
(Baden-Württemberg, Basisfach, mündliche Mathe-Abiturprüfung). Die Datei wird mit pandoc + KaTeX +
JSXGraph gebaut. **Gold-Vorlage ist `content/konvolut/01-analysis-geometrie.md`** — lies sie zuerst
vollständig und ahme Aufbau, Tonfall, Tiefe und Konventionen exakt nach. Quelle der Aufgabe ist das
offizielle PDF (du bekommst die genauen Seiten genannt) — lies es und übernimm die Aufgabenstellung
inhaltlich korrekt.

## Oberstes Ziel: Erklärtiefe für geringen Mathe-Reifegrad

Die Seite dient einer **Prüfungssimulation zu zweit**: Eine Person trägt vor, eine zweite (ohne tiefes
Mathe-Wissen) prüft mit. Deshalb sind die **„Haltung dahinter"-Kästen das Wichtigste**. Sie erklären
jeden Schritt **von Grund auf**, als hätte man den Stoff lange nicht gesehen:

- **Jeden Fachbegriff beim ersten Auftauchen in einfachen Worten erklären** (Nullstelle, Ableitung,
  Stammfunktion, Vektor, Normalenvektor, Erwartungswert, …).
- **Alltagsanalogien** verwenden (Bankkonto fürs orientierte Integral, Zeltmast für „senkrechte
  Pyramide", Kreismittelpunkt für gleiche Abstände …).
- Eine **zusätzliche tiefste Drilldown-Ebene „… ganz langsam (mit Zahlen)"**, in der eine Rechnung
  Ziffer für Ziffer vorgeführt wird (inkl. „minus mal minus ist plus" u. Ä.).
- Wo sinnvoll ein nested Kasten **„Typische Falle"**.
- Lieber **zu ausführlich als zu knapp**. Keine ungeklärten Voraussetzungen.

## Dateigerüst (Reihenfolge wie in der Gold-Vorlage)

1. `# Aufgabe N — <Teil1-Gebiet> & <Teil2-Gebiet>` (Titel; erste Zeile).
2. Einleitungsabsatz (vollständige mündliche Beispielprüfung; Teil 1 Vortrag, Teil 2 Gespräch;
   rechnerfrei; Hinweis auf Simulation + Link auf den Prüfer-Leitfaden am Ende).
3. Blockzitat **„Lesehilfe für die Detailkästen"** (wie Gold-Vorlage).
4. `<details><summary><b>Kurzanleitung für die abfragende Person</b> (zuerst lesen)</summary>` … (wie Gold-Vorlage, rollenneutral).
5. Blockzitat **„Werkzeug zum Nachschlagen"** mit passenden Links (siehe unten).
6. `---`
7. `## Teil 1 — Vortrag (<Gebiet>): <kurzer Titel>` mit grauem Aufgabenkasten + Teilaufgaben.
8. `---`
9. `## Teil 2 — Gespräch (<Gebiet>): <kurzer Titel>` mit grauem Aufgabenkasten + gelösten Aspekten.
10. `---`
11. `## Prüfer-Leitfaden (für die abfragende Person)` mit zwei `<details>` (Teil 1 / Teil 2).
12. `## Selbstcheck: Kannst du es mündlich erklären?` (4–6 Fragen).

## Aufgabenstellung-Kasten

Verwende für die Original-Aufgabenstellung jeweils:

```
<div class="aufgabenkasten">

**Fettgesetzter Aufgabentext / Input.** … Teilaufgaben **a)** **b)** … wörtlich sinngemäß aus dem PDF.

</div>
```

Bei Teil 2 zusätzlich die „denkbaren Aspekte (AB I/II/III)" aus dem PDF kurz im Kasten nennen.

## Lösungen

- **Teil 1:** Das PDF enthält einen **offiziellen Erwartungshorizont** — deine Lösung muss damit
  übereinstimmen (Ergebnisse identisch). Rechne den Weg sauber und rechnerfrei vor.
- **Teil 2:** Das PDF gibt **nur Aspekte, keine Lösung** — du **löst sie selbst** vollständig und
  korrekt, mit der gleichen Drilldown-Tiefe. Rechne alles nach. (Ein Prüf-Agent kontrolliert dich.)
- Jede Teilaufgabe als eigener `### Teilaufgabe x) — <Titel>`-Abschnitt mit AB-Tag und
  `<details><summary>Lösung Schritt für Schritt anzeigen</summary>` … darin die fett markierten
  Kernschritte, KaTeX-Formeln und die „Haltung dahinter"-Kaskade.
- Am Ende von Teil 1 ein `<details>`-**Kurz-Spickzettel** mit allen Ergebnissen.
- Wo das Aufgabenbeispiel nur „Verfahren beschreiben" verlangt (häufig AB III, Teil-2-Aspekte), gib das
  **Verfahren** + Begründung an (keine erfundenen Zahlen, wenn keine gegeben sind — das transparent sagen).

## AB-Tags (Anforderungsbereich)

`<span class="tag tag-ok">AB I — Grundkompetenz</span>` (grün, einfach),
`<span class="tag tag-warn">AB II — Standardanforderung</span>` bzw. `AB III — vertiefte Vernetzung`
(gelb). Setze pro Teilaufgabe/Abschnitt einen passenden Tag wie in der Gold-Vorlage.

## Mathe-Notation (KaTeX)

- Inline-Mathe in `\( … \)`, abgesetzte Formeln in `\[ … \]`. **Niemals** `$…$`.
- Brüche `\tfrac{}{}` (inline) / `\frac{}{}` (abgesetzt), Vektoren `\begin{pmatrix}…\end{pmatrix}`,
  Wurzeln `\sqrt{}`, Grenzwerte `\lim_{x \to \infty}`, Integrale `\int_a^b f(x)\,dx`, Kreuz `\times`,
  Skalarprodukt mit `\cdot`. Dezimaltrennzeichen **Komma** im Fließtext-Sinn als `1{,}5` schreiben.

## Figuren

- **Funktionsgraphen** (2D) als JSXGraph, exakt im Muster der Gold-Vorlage:
  `<div class="jxgbox" id="jxg-kN-…" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>`
  gefolgt von `<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-kN-…',{boundingbox:[xmin,ymax,xmax,ymin],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return …;},xmin,xmax],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>`.
  Eindeutige `id` je Board (Präfix `jxg-kN-` mit N = Aufgabennummer). Graphfarbe `#3a5a9c`, Akzent
  `#d98324`, Extra `#3a8a5a`. Mehrere kleine Graphen in `<div class="graph-row"><figure>…<figcaption>…</figcaption></figure>…</div>`.
- **Histogramme / Glockenkurven** (Stochastik): JSXGraph (Balken über `b.create('line'/'polygon')` oder
  Funktionsgraph der Glocke). Halte es einfach und korrekt.
- **3D-Geometrie / Schemata:** sauberes, statisches **inline-SVG** (wie das Pyramiden-Schrägbild der
  Gold-Vorlage), Hintergrund `#fbf7ef`, Achsen `#7a7163`, Objekt `#3a5a9c`, Akzent `#d98324`. **Keine
  Textüberschneidungen**, Labels versetzt. Nur einsetzen, wenn ein Bild wirklich hilft.
- Wo das Original einen Graphen zum **Ablesen** zeigt (z. B. Steigung, Kästchenzählen): den Graphen per
  JSXGraph reproduzieren (Funktionsterm aus dem Erwartungshorizont) und im Text erklären, *wie* man
  abliest.
- **Niemals** Bilder/Scans aus dem PDF einbetten.

## Sprache (verbindlich)

- **Deutsch**, menschlich-nüchtern, kein Marketing-/KI-Sprech, **keine kontrastive Rhetorik**
  („nicht X, sondern Y" vermeiden — positiv formulieren).
- **Rollenneutral**: „die abfragende/prüfende Person", **kein** „Papa", **kein** Vorname, neutrales „du".
- Du-Ansprache an die lernende Person wie in der Gold-Vorlage.

## Werkzeugkasten-Links (im „Werkzeug"-Blockzitat oben + an passenden Stellen)

- Geometrie: `[Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html)` (Anker u. a.
  `#kreuzprodukt`, `#skalarprodukt`).
- Stochastik: `[Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html)` (Anker u. a.
  `#binomialverteilung`, `#normalverteilung`, `#erwartungswert`, `#vierfeldertafel`, `#bernoulli-kette`).
- Analysis-Kapitel: `[Ableit-Handwerk](kap-ableiten-handwerk.html)`,
  `[Integral-Grundlagen](kap-integral-grundlagen.html)`,
  `[Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html)`,
  `[Grundfunktionen](kap-grundfunktionen.html)`,
  `[Funktionsuntersuchung](kap-funktionsuntersuchung.html)`,
  `[Grenzwerte & Randverhalten](kap-grenzwerte-randverhalten.html)`.

## Prüfer-Leitfaden (Pflicht, rollenneutral)

Zwei `<details>` (Teil 1, Teil 2). Je Teilaufgabe ein Stichpunkt: **was eine gute Antwort enthält**,
**eine Rückfrage**, ggf. **rote Flagge**. Alltagssprachlich, so dass eine fachfremde Person die Antwort
einordnen kann.

## Qualität

Lieber gründlich als schnell. Rechne jede Zahl selbst nach. Halte dich strikt an die Struktur der
Gold-Vorlage, damit alle elf Aufgaben einheitlich wirken.
