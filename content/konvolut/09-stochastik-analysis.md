# Aufgabe 9 — Stochastik & Analysis

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Stochastik**, **Teil 2 (Gespräch) aus der Analysis**. Alles lässt sich
**ohne großen Rechenaufwand** lösen — Terme angeben, am Tafelwerk ablesen, aus einem Graphen
herauslesen. Arbeitet die Aufgabe wie eine echte Simulation durch — eine Person trägt vor, die andere
prüft mit dem Lösungsweg und dem [Prüfer-Leitfaden](#prüfer-leitfaden-für-die-abfragende-person) am
Ende mit.

> **Lesehilfe für die Detailkästen.** Jeder Lösungsschritt hat darunter einen klappbaren Kasten
> **„Haltung dahinter"**. Der erklärt den Schritt **von Grund auf** — so, als hätte man den Stoff
> lange nicht mehr gesehen. Jeder Fachbegriff wird beim ersten Auftauchen in einfachen Worten erklärt.
> Wer nur das Ergebnis braucht, lässt die Kästen zu; wer *verstehen* will, klappt sie auf.

<details><summary><b>Kurzanleitung für die abfragende Person</b> (zuerst lesen)</summary>

Du musst den Stoff **nicht** selbst beherrschen, um diese Aufgabe abzunehmen. So gehst du vor:

- Lass die andere Person nur die **grauen Aufgabenkästen** sehen und **laut erklären**.
- Du hast den **ausgeklappten Lösungsweg** vor dir. Vergleiche nicht Wort für Wort — achte auf die
  **fett markierten Kernschritte** und die **Ergebnisse**.
- Die **„Haltung dahinter"-Kästen** erklären dir jeden Schritt in Alltagssprache. Lies sie ruhig
  selbst mit — danach kannst du die Erklärung der anderen Person einordnen, auch ohne Vorwissen.
- Am Ende findest du den **Prüfer-Leitfaden**: dort steht je Teilaufgabe in einem Satz, *was eine
  gute Antwort enthält* und *welche Rückfrage* du stellen kannst.
- Grüne Markierung = Grundwissen (sollte sicher sitzen), gelbe = anspruchsvoller (Nachfragen ok).

</details>

> **Werkzeug zum Nachschlagen:** Die wiederkehrenden Stochastik-Werkzeuge (Bernoulli-Kette,
> Binomialverteilung, Erwartungswert, kumulierte Wahrscheinlichkeiten) stehen kompakt im
> [Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html). Die Analysis-Werkzeuge findest
> du in den Kapiteln [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Funktionsuntersuchung](kap-funktionsuntersuchung.html),
> [Integral-Grundlagen](kap-integral-grundlagen.html) und
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).

---

## Teil 1 — Vortrag (Stochastik): Kugeln aus der Urne

<div class="aufgabenkasten">

**In einer Urne befinden sich sechs blaue und vier weiße Kugeln.** Betrachtet wird das
Zufallsexperiment, bei dem aus der Urne mehrmals nacheinander eine Kugel **mit Zurücklegen** gezogen
wird.

**a)** Das Zufallsexperiment wird **dreimal** nacheinander durchgeführt. Gib für die
Wahrscheinlichkeiten der folgenden Ereignisse jeweils einen **Term** an:
\( A \): „Alle Kugeln sind blau." — \( B \): „Genau zwei der gezogenen Kugeln sind blau."

Das Zufallsexperiment wird nun **15 Mal** nacheinander durchgeführt. Die Zufallsgröße \( Y \) gibt die
Anzahl der dabei gezogenen blauen Kugeln an.

**b)** Begründe, dass \( Y \) binomialverteilt ist. Bestimme den **Erwartungswert** von \( Y \) und
erläutere dessen Bedeutung für das durchgeführte Zufallsexperiment. Berechne die Wahrscheinlichkeit
dafür, dass **mindestens 5 und höchstens 10** blaue Kugeln gezogen werden.

**c)** Die drei Histogramme **(1)**, **(2)**, **(3)** stellen Binomialverteilungen von Zufallsgrößen
bei 15-maliger Durchführung des entsprechenden Bernoulli-Experiments dar. Untersuche, welches Diagramm
die Verteilung von \( Y \) darstellt. Untersuche für die beiden anderen Diagramme, welche Aussagen
jeweils über die zugehörige **Trefferwahrscheinlichkeit** möglich sind.

</div>

So ist die Urne besetzt — die „Trefferwahrscheinlichkeit" für blau ist
\( p = \tfrac{6}{10} = 0{,}6 \).

<figure>
<svg viewBox="0 0 300 220" role="img" aria-label="Urne mit sechs blauen und vier weißen Kugeln" style="width:100%;max-width:300px;height:auto;background:#fbf7ef;border-radius:8px">
  <path d="M72 38 L228 38 L208 178 Q150 200 92 178 Z" fill="#ffffff" fill-opacity="0.45" stroke="#7a7163" stroke-width="2"/>
  <circle cx="108" cy="78"  r="13" fill="#3a5a9c"/>
  <circle cx="146" cy="74"  r="13" fill="#3a5a9c"/>
  <circle cx="184" cy="78"  r="13" fill="#3a5a9c"/>
  <circle cx="112" cy="116" r="13" fill="#3a5a9c"/>
  <circle cx="150" cy="120" r="13" fill="#3a5a9c"/>
  <circle cx="132" cy="154" r="13" fill="#3a5a9c"/>
  <circle cx="200" cy="116" r="13" fill="#ffffff" stroke="#3a5a9c" stroke-width="2"/>
  <circle cx="188" cy="150" r="13" fill="#ffffff" stroke="#3a5a9c" stroke-width="2"/>
  <circle cx="170" cy="114" r="13" fill="#ffffff" stroke="#3a5a9c" stroke-width="2"/>
  <circle cx="152" cy="156" r="13" fill="#ffffff" stroke="#3a5a9c" stroke-width="2"/>
  <text x="150" y="214" font-size="13" fill="#26324a" text-anchor="middle">6 blau · 4 weiß → P(blau) = 0,6</text>
</svg>
<figcaption>Schematische Urne. Beim Ziehen <b>mit Zurücklegen</b> bleibt \( p=0{,}6 \) bei jedem Zug gleich.</figcaption>
</figure>

Und das sind die drei Histogramme aus der Aufgabe — jedes zeigt eine Binomialverteilung bei
\( n=15 \) Versuchen, aber mit **unterschiedlicher** Trefferwahrscheinlichkeit \( p \). Schau sie dir
an und überlege selbst, welches zu \( Y \) gehört, bevor du die Lösung aufklappst.

<div class="graph-row">
<figure>
<div class="jxgbox" id="jxg-k9-hist1" style="width:100%;max-width:320px;aspect-ratio:1/1"></div>
<figcaption>Histogramm (1)</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k9-hist2" style="width:100%;max-width:320px;aspect-ratio:1/1"></div>
<figcaption>Histogramm (2)</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k9-hist3" style="width:100%;max-width:320px;aspect-ratio:1/1"></div>
<figcaption>Histogramm (3)</figcaption>
</figure>
</div>

<script>(function(){var d=[0,0.0005,0.0032,0.0139,0.0417,0.0916,0.1527,0.1964,0.1964,0.1527,0.0916,0.0417,0.0139,0.0032,0.0005,0];var b=JXG.JSXGraph.initBoard('jxg-k9-hist1',{boundingbox:[-1.2,0.31,16,-0.035],axis:true,showCopyright:false,showNavigation:false});for(var k=0;k<16;k++){var h=d[k];b.create('polygon',[[k-0.42,0],[k+0.42,0],[k+0.42,h],[k-0.42,h]],{fillColor:'#3a5a9c',fillOpacity:0.55,borders:{strokeColor:'#3a5a9c',strokeWidth:1},vertices:{visible:false},fixed:true,highlight:false});}})();</script>
<script>(function(){var d=[0,0,0.0003,0.0016,0.0074,0.0245,0.0612,0.1181,0.1771,0.2066,0.1859,0.1268,0.0634,0.0219,0.0047,0.0005];var b=JXG.JSXGraph.initBoard('jxg-k9-hist2',{boundingbox:[-1.2,0.31,16,-0.035],axis:true,showCopyright:false,showNavigation:false});for(var k=0;k<16;k++){var h=d[k];b.create('polygon',[[k-0.42,0],[k+0.42,0],[k+0.42,h],[k-0.42,h]],{fillColor:(k===9?'#d98324':'#3a5a9c'),fillOpacity:0.6,borders:{strokeColor:'#3a5a9c',strokeWidth:1},vertices:{visible:false},fixed:true,highlight:false});}})();</script>
<script>(function(){var d=[0,0,0,0.0001,0.0006,0.003,0.0116,0.0348,0.0811,0.1472,0.2061,0.2186,0.17,0.0916,0.0305,0.0047];var b=JXG.JSXGraph.initBoard('jxg-k9-hist3',{boundingbox:[-1.2,0.31,16,-0.035],axis:true,showCopyright:false,showNavigation:false});for(var k=0;k<16;k++){var h=d[k];b.create('polygon',[[k-0.42,0],[k+0.42,0],[k+0.42,h],[k-0.42,h]],{fillColor:'#3a5a9c',fillOpacity:0.55,borders:{strokeColor:'#3a5a9c',strokeWidth:1},vertices:{visible:false},fixed:true,highlight:false});}})();</script>

### Teilaufgabe a) — Terme für \( A \) und \( B \)

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Trefferwahrscheinlichkeit für blau: \( p = \tfrac{6}{10} = 0{,}6 \); für weiß \( 1-p = 0{,}4 \). Weil
**mit Zurücklegen** gezogen wird, ist jeder der drei Züge gleich und unabhängig.

**Ereignis \( A \) — „Alle drei blau".** Drei Mal blau hintereinander, jedes Mal mit
Wahrscheinlichkeit \( 0{,}6 \). Die Einzelwahrscheinlichkeiten werden multipliziert:

\[ P(A) = 0{,}6 \cdot 0{,}6 \cdot 0{,}6 = 0{,}6^3. \]

**Ereignis \( B \) — „Genau zwei blau".** Hier sind zwei Kugeln blau und eine weiß — aber in
**verschiedenen Reihenfolgen** (blau-blau-weiß, blau-weiß-blau, weiß-blau-blau). Jede einzelne
Reihenfolge hat die Wahrscheinlichkeit \( 0{,}6^2 \cdot 0{,}4 \); die Anzahl der Reihenfolgen ist der
**Binomialkoeffizient** \( \binom{3}{2} = 3 \):

\[ P(B) = \binom{3}{2}\cdot 0{,}6^2 \cdot 0{,}4. \]

<details><summary>Haltung dahinter: „mit Zurücklegen", „mal" statt „plus", und der Binomialkoeffizient (ganz von vorn)</summary>

Drei Bausteine, der Reihe nach.

**Was heißt „mit Zurücklegen"?** Nach jedem Zug legt man die Kugel zurück und mischt. Dadurch ist die
Urne vor jedem Zug **wieder genau gleich** voll: immer 6 blau, 4 weiß. Die Wahrscheinlichkeit für blau
bleibt deshalb bei **jedem** Zug \( 0{,}6 \) — sie ändert sich nicht. (Ohne Zurücklegen würde sich die
Urne leeren und die Wahrscheinlichkeit von Zug zu Zug verändern; das ist hier ausdrücklich nicht der
Fall.)

**Warum multipliziert man?** Eine feste Reihenfolge von Ergebnissen ist ein **„und"**: erst blau *und*
dann blau *und* dann blau. Bei unabhängigen Zufallsschritten gilt die **Pfadregel**: Entlang eines
Pfades (einer festen Reihenfolge) werden die Einzelwahrscheinlichkeiten **multipliziert**. Anschaulich:
Jeder weitere Zug macht den gemeinsamen Treffer *seltener*, also kleiner — und Multiplizieren mit einer
Zahl unter 1 macht kleiner.

**Was ist der Binomialkoeffizient \( \binom{3}{2} \)?** Er zählt, **auf wie viele Arten** man aus 3
Zügen die 2 „blauen" auswählen kann — also wie viele verschiedene Reihenfolgen es für „genau zwei blau"
gibt. Man liest ihn „3 über 2". Hier sind es 3 Möglichkeiten. Genau diese 3 gleich
wahrscheinlichen Pfade addieren sich, deshalb steht der Faktor 3 (= \( \binom{3}{2} \)) vor dem Term.

<details><summary>… ganz langsam (mit Zahlen)</summary>

- \( P(A) = 0{,}6^3 = 0{,}6 \cdot 0{,}6 \cdot 0{,}6 \). Erst \( 0{,}6 \cdot 0{,}6 = 0{,}36 \), dann
  \( 0{,}36 \cdot 0{,}6 = 0{,}216 \). Also \( P(A) = 0{,}216 \).
- Für \( B \): ein einzelner Pfad ist \( 0{,}6^2 \cdot 0{,}4 = 0{,}36 \cdot 0{,}4 = 0{,}144 \). Es gibt
  \( \binom{3}{2} = 3 \) solche Pfade. Zusammen: \( 3 \cdot 0{,}144 = 0{,}432 \). Also
  \( P(B) = 0{,}432 \).

In der mündlichen Prüfung ist nur der **Term** verlangt — die ausgerechnete Zahl ist eine schöne
Zugabe, kein Muss.

</details>

<details><summary>Typische Falle</summary>

Bei \( B \) den Faktor \( \binom{3}{2}=3 \) **vergessen** und nur \( 0{,}6^2\cdot 0{,}4 = 0{,}144 \)
hinschreiben. Das ist die Wahrscheinlichkeit für **eine bestimmte** Reihenfolge (z. B.
blau-blau-weiß), aber „genau zwei blau" lässt drei Reihenfolgen zu. Ohne den Zählfaktor ist die Lösung
zu klein und unvollständig.

</details>
</details>
</details>

### Teilaufgabe b) — Binomialverteilung, Erwartungswert, \( P(5 \le Y \le 10) \)

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Begründung, dass \( Y \) binomialverteilt ist.** Das Experiment ist eine **Bernoulli-Kette der
Länge \( n=15 \)**:

- Jeder Zug hat **nur zwei** interessierende Ausgänge — „blau" (Treffer) oder „nicht blau" (Niete).
- Wegen des **Zurücklegens** sind die 15 Züge **unabhängig** voneinander, und die Trefferwahrscheinlichkeit
  bleibt **konstant** bei \( p=0{,}6 \).

\( Y \) zählt die Treffer (blaue Kugeln) in diesen 15 Versuchen. Die Trefferzahl einer Bernoulli-Kette
ist **binomialverteilt**: \( Y \sim B(15;\,0{,}6) \), mit

\[ P(Y=k) = \binom{15}{k}\, 0{,}6^{\,k}\, 0{,}4^{\,15-k}. \]

**Erwartungswert.** Für die Binomialverteilung gilt \( E(Y) = n\cdot p \):

\[ E(Y) = 15 \cdot 0{,}6 = 9. \]

**Bedeutung.** Führt man die ganze 15er-Kette **sehr oft** durch, sind im Mittel (auf lange Sicht)
**9 von 15** gezogenen Kugeln blau.

**Wahrscheinlichkeit \( P(5 \le Y \le 10) \)** („mindestens 5 und höchstens 10"). Man rechnet sie über
**kumulierte** (aufsummierte) Wahrscheinlichkeiten aus dem Tafelwerk / GTR:

\[ P(5 \le Y \le 10) = P(Y \le 10) - P(Y \le 4) \approx 0{,}783 - 0{,}009 \approx 0{,}773. \]

<details><summary>Haltung dahinter: Bernoulli-Kette, Binomialverteilung, Erwartungswert und der „minus"-Trick (ganz von vorn)</summary>

Vier Begriffe, einer nach dem anderen.

**Bernoulli-Experiment.** Ein Zufallsversuch mit **genau zwei** Ausgängen, die man „Treffer" und
„Niete" nennt. Hier: Eine Kugel ziehen — „blau" = Treffer, „weiß" = Niete. (Münzwurf, „Lampe defekt
ja/nein", „Tor ja/nein" sind weitere Beispiele.)

**Bernoulli-Kette.** Denselben Bernoulli-Versuch **\( n \)-mal** wiederholen, **unabhängig** und mit
**gleichbleibender** Trefferwahrscheinlichkeit \( p \). Das „mit Zurücklegen" ist genau das, was die
Unabhängigkeit und das konstante \( p \) sichert — ohne Zurücklegen wäre es **keine** Bernoulli-Kette.

**Binomialverteilung.** Die Zufallsgröße „Anzahl der Treffer in einer Bernoulli-Kette" heißt
**binomialverteilt**. Ihre Formel \( P(Y=k)=\binom{n}{k}p^k(1-p)^{n-k} \) ist genau das, was wir in
Teil a) für \( n=3 \) per Hand gebaut haben — \( \binom{n}{k} \) zählt die Reihenfolgen, \( p^k \) sind
die Treffer, \( (1-p)^{n-k} \) die Nieten.

**Erwartungswert \( E(Y) \).** Der „Mittelwert auf lange Sicht". Anschaulich: Wenn jeder einzelne Zug
mit Wahrscheinlichkeit \( 0{,}6 \) blau ist, erwartet man bei 15 Zügen ungefähr
\( 15 \cdot 0{,}6 = 9 \) blaue — wie „60 % von 15". Daher die einfache Formel \( E(Y)=n\cdot p \).

<details><summary>Der „minus"-Trick bei \( P(5 \le Y \le 10) \) — warum \( P(Y\le4) \) und nicht \( P(Y\le5) \)?</summary>

Im Tafelwerk stehen nur **kumulierte** Werte \( P(Y \le k) \), also „k oder weniger Treffer". Ein
Bereich „von 5 bis 10" baut man daraus als Differenz: „alles bis 10" **minus** „alles, was unterhalb
von 5 liegt".

Der heikle Punkt ist die untere Grenze. „Mindestens 5" heißt: die **5 gehört dazu**. Abziehen darf man
deshalb nur, was **echt kleiner** als 5 ist, also \( Y \le 4 \):

\[ P(5 \le Y \le 10) = \underbrace{P(Y \le 10)}_{\text{alles bis 10}} - \underbrace{P(Y \le 4)}_{\text{alles unter 5}}. \]

Würde man \( P(Y \le 5) \) abziehen, hätte man die 5 mit weggeschnitten — der Wert wäre falsch
(zu klein). Merksatz: **untere Grenze einschließen heißt „eins darunter" abziehen.**

</details>

<details><summary>… ganz langsam (mit Zahlen)</summary>

\( E(Y) = 15 \cdot 0{,}6 \): das ist \( 15 \cdot 0{,}6 = 9{,}0 = 9 \). Aus dem Tafelwerk für
\( B(15;0{,}6) \): \( P(Y \le 10) \approx 0{,}783 \) und \( P(Y \le 4) \approx 0{,}009 \). Differenz:
\( 0{,}783 - 0{,}009 = 0{,}774 \approx 0{,}773 \). Es ist also mit knapp **77 %**
Wahrscheinlichkeit so, dass zwischen 5 und 10 blaue Kugeln gezogen werden — die wahrscheinlichsten
Fälle liegen rund um den Erwartungswert 9.

</details>
</details>
</details>

### Teilaufgabe c) — Histogramme zuordnen

<span class="tag tag-warn">AB II / AB III</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Welches Diagramm gehört zu \( Y \)?** Für \( Y \sim B(15;0{,}6) \) ist \( E(Y) = 9 \) — eine **ganze
Zahl**. Bei einer Binomialverteilung liegt der **höchste Balken** (der wahrscheinlichste Wert) bei
einer ganzzahligen Erwartung **genau am Erwartungswert**, hier also bei \( k=9 \).

\[ \Rightarrow \text{Diagramm } \mathbf{(2)} \text{ zeigt die Verteilung von } Y. \]

**Was lässt sich über die beiden anderen sagen?**

- **Diagramm (1)** ist **achsensymmetrisch** (spiegelgleich um die Mitte \( k = 7{,}5 \)). Eine
  Binomialverteilung ist nur dann symmetrisch, wenn Treffer und Niete gleich wahrscheinlich sind:
  \[ \Rightarrow p = 0{,}5. \]
- **Diagramm (3)** hat seinen Schwerpunkt **weiter rechts**; der höchste Balken liegt etwa bei
  \( 10 \) bis \( 11 \), der Erwartungswert \( \mu = 15p \) also zwischen 10 und 12:
  \[ 10 < 15p < 12 \quad\Longleftrightarrow\quad \tfrac{2}{3} < p < \tfrac{4}{5}. \]

<details><summary>Haltung dahinter: Was verrät die Form eines Histogramms über \( p \)? (ganz von vorn)</summary>

Ein **Histogramm** zeichnet für jede mögliche Trefferzahl \( k \) einen Balken, dessen Höhe die
Wahrscheinlichkeit \( P(Y=k) \) ist. Die Form trägt zwei Informationen, die man direkt ablesen kann:

**1. Die Lage des höchsten Balkens verrät den Erwartungswert.** Der höchste Balken (der
*wahrscheinlichste* Wert, „Modalwert") liegt immer dicht beim Erwartungswert \( \mu = n\cdot p \). Steht
er bei \( k=9 \), ist \( \mu \approx 9 \), also \( p \approx \tfrac{9}{15} = 0{,}6 \). Steht er weiter
rechts, ist \( p \) größer; weiter links, kleiner. So ordnet man (2) dem \( Y \) zu — der Gipfel sitzt
auf der 9.

**2. Symmetrie tritt nur bei \( p=0{,}5 \) auf.** Bei \( p=0{,}5 \) sind Treffer und Niete gleich
wahrscheinlich, deshalb ist die Verteilung **spiegelgleich** um die Mitte \( n/2 = 7{,}5 \). Sobald
\( p \neq 0{,}5 \), kippt die Verteilung zur einen Seite (Schiefe). Ein perfekt symmetrisches Bild ⇒
\( p=0{,}5 \).

<details><summary>… ganz langsam: woher \( \tfrac{2}{3} \) und \( \tfrac{4}{5} \) bei Diagramm (3)?</summary>

Man liest aus (3) ab, dass der Erwartungswert zwischen 10 und 12 liegen muss (höchster Balken um
10–11). Der Erwartungswert ist \( \mu = 15p \). Aus \( 10 < 15p < 12 \) löst man nach \( p \) auf,
indem man **alle drei Teile durch 15 teilt**:

\[ \frac{10}{15} < p < \frac{12}{15} \quad\Longrightarrow\quad \frac{2}{3} < p < \frac{4}{5}, \]

denn \( \tfrac{10}{15} = \tfrac{2}{3} \approx 0{,}667 \) und \( \tfrac{12}{15} = \tfrac{4}{5} = 0{,}8 \).
Man kann also nur einen **Bereich** für \( p \) angeben, keinen einzelnen Wert — das Histogramm legt
\( p \) nicht eindeutig fest, sondern grenzt es ein.

</details>

<details><summary>Typische Falle</summary>

Diagramm (1) mit der Verteilung von \( Y \) verwechseln, weil beide einen Gipfel „in der Mitte" haben.
Der Unterschied steckt in der genauen Lage: der Gipfel von \( Y \) sitzt auf **9**, der Gipfel bei
\( p=0{,}5 \) auf **7/8** (Mitte). Und: Aus einem schiefen Histogramm lässt sich \( p \) nur als
**Bereich** angeben — wer dort einen exakten Wert behauptet, überinterpretiert das Bild.

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- a) \( P(A)=0{,}6^3\ (=0{,}216) \); \( P(B)=\binom{3}{2}\cdot 0{,}6^2\cdot 0{,}4\ (=0{,}432) \)
- b) \( Y\sim B(15;0{,}6) \) (Bernoulli-Kette, unabhängig wegen Zurücklegen); \( E(Y)=15\cdot0{,}6=9 \)
  („im Mittel 9 von 15 blau"); \( P(5\le Y\le 10)=P(Y\le10)-P(Y\le4)\approx 0{,}773 \)
- c) \( Y \to \) Diagramm **(2)** (Gipfel bei \( k=9 \), weil \( E(Y)=9 \) ganzzahlig); (1) \( p=0{,}5 \)
  (symmetrisch); (3) \( \tfrac{2}{3}<p<\tfrac{4}{5} \)

</details>

---

## Teil 2 — Gespräch (Analysis): Vom Graphen der Ableitung auf \( f \) schließen

<div class="aufgabenkasten">

**Input.** Gegeben ist **ausschnittsweise der Graph der Ableitungsfunktion \( f' \)** einer
ganzrationalen Funktion \( f \) (siehe Abbildung unten). Im Gespräch denkbare Aspekte:

**(AB I)** Bestimmen von \( f'(1) \); Bedeutung von \( f'(1)=2 \) für den Graphen von \( f \);
Nullstellen von \( f' \).
**(AB II)** Bedeutung der Nullstellen von \( f' \) für \( f \); Monotonieverhalten von \( f \);
Näherungswert für \( f''(1) \) und dessen Bedeutung; Krümmungsverhalten von \( f \); Skizze von \( f \)
mit \( f(0)=0{,}6 \) und \( f(2)=3 \) samt Inhalt der Fläche, die \( f' \) im Intervall \( [0;2] \) mit
der \( x \)-Achse einschließt; Begründung, ob \( f(-1)<f(0) \), \( f(-1)=f(0) \) oder \( f(-1)>f(0) \).
**(AB III)** Minimaler Grad einer Stammfunktion \( F \) von \( f \); ein möglicher Funktionsterm von
\( f' \).

</div>

> **Der eine Gedanke, der alles trägt:** Im Bild ist **\( f' \)** gezeichnet, **nicht** \( f \). Jeder
> Höhenwert der gezeichneten Kurve ist also eine **Steigung** von \( f \). „\( f' \) liegt bei \( x=1 \)
> auf Höhe 2" bedeutet: „\( f \) steigt bei \( x=1 \) mit Steigung 2." Halte diesen Übersetzungs-Schritt
> während der ganzen Aufgabe fest. Werkzeuge dazu im Kapitel
> [Funktionsuntersuchung](kap-funktionsuntersuchung.html).

Hier ist der Graph von \( f' \) reproduziert. Der orange Punkt markiert \( f'(1)=2 \), die roten Punkte
die Nullstellen.

<figure>
<div class="jxgbox" id="jxg-k9-fstrich" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Graph der <b>Ableitung</b> \( f' \) (nicht von \( f \)). Form: von links oben herab, Tief unter der Achse, mittlere Beule mit Scheitel knapp links von \( x=1 \) (der orange Punkt markiert nur den Wert \( f'(1)=2 \), nicht den Scheitel), Berührung der Achse bei \( x=2 \), dann steil hoch.</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k9-fstrich',{boundingbox:[-2.3,5.8,3.3,-2.7],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return x*(x+1)*(x-2)*(x-2);},-1.78,2.83],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[-1,0],{name:'−1',size:2,fixed:true,strokeColor:'#b03a2e',fillColor:'#b03a2e',label:{offset:[-6,-14]}});b.create('point',[0,0],{name:'0',size:2,fixed:true,strokeColor:'#b03a2e',fillColor:'#b03a2e',label:{offset:[6,-14]}});b.create('point',[2,0],{name:'2',size:2,fixed:true,strokeColor:'#b03a2e',fillColor:'#b03a2e',label:{offset:[8,-14]}});b.create('point',[1,2],{name:"f '(1)=2",size:2.5,fixed:true,strokeColor:'#d98324',fillColor:'#d98324',label:{offset:[8,6]}});})();</script>

### AB I — \( f'(1) \), Bedeutung, Nullstellen von \( f' \)

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**\( f'(1) \) ablesen.** Man geht bei \( x=1 \) senkrecht hoch bis zur gezeichneten Kurve und liest die
Höhe ab:

\[ f'(1) = 2. \]

**Bedeutung von \( f'(1)=2 \) für den Graphen von \( f \).** \( f' \) ist die **Steigung** von \( f \).
Also: An der Stelle \( x=1 \) hat der Graph von \( f \) die **Steigung 2** — die Tangente dort steigt
um 2 Höheneinheiten pro 1 Einheit nach rechts; \( f \) ist an dieser Stelle wachsend und ziemlich
steil.

**Nullstellen von \( f' \).** Das sind die Stellen, an denen die gezeichnete \( f' \)-Kurve die
\( x \)-Achse **schneidet oder berührt**:

\[ x = -1, \qquad x = 0, \qquad x = 2. \]

(Bei \( x=2 \) **berührt** die Kurve die Achse nur — dazu mehr im nächsten Abschnitt.)

<details><summary>Haltung dahinter: „Das Bild ist die Ableitung" — was heißt das überhaupt? (ganz von vorn)</summary>

Der wichtigste und am leichtesten zu verwechselnde Punkt der ganzen Aufgabe.

**Ableitung = Steigung.** Die **Ableitung** \( f' \) einer Funktion \( f \) gibt an **jeder** Stelle an,
**wie steil** \( f \) dort ist — wie eine Steigungsanzeige am Berg. Ein **positiver** \( f' \)-Wert
heißt „\( f \) geht bergauf", ein **negativer** „\( f \) geht bergab", **null** heißt „waagrecht".

**Was zeigt das Bild?** Hier ist die **Steigungsanzeige selbst** als Kurve gezeichnet, also \( f' \) —
\( f \) sieht man **nicht**. Wenn die \( f' \)-Kurve bei \( x=1 \) auf Höhe 2 liegt, dann ist das die
**Aussage über die Steigung** von \( f \): „\( f \) steigt dort mit Tempo 2". Höhe der \( f' \)-Kurve =
Steigung von \( f \).

**Warum sind die Nullstellen von \( f' \) wichtig?** Eine Nullstelle von \( f' \) ist eine Stelle, an
der die **Steigung von \( f \) null** ist — wo \( f \) also eine **waagrechte Tangente** hat. Solche
Stellen sind die Kandidaten für Hochpunkte, Tiefpunkte oder Sattelpunkte von \( f \). Deshalb sucht man
sie zuerst.

<details><summary>… ganz langsam (so liest man Höhe und Nullstellen ab)</summary>

- **Höhe ablesen \( f'(1) \):** Finger bei \( x=1 \) auf die Achse, senkrecht hoch bis zur Kurve, dann
  waagrecht nach links zur \( y \)-Achse — dort steht 2. Also \( f'(1)=2 \).
- **Nullstellen:** Augen auf die \( x \)-Achse, schauen, wo die Kurve sie trifft. Links schneidet sie
  bei \( -1 \) (von oben nach unten), dann bei \( 0 \) (von unten nach oben), und bei \( 2 \) **berührt**
  sie die Achse nur (kommt von oben herunter, tippt die Achse an, geht wieder hoch).

</details>

<details><summary>Typische Falle</summary>

\( f \) und \( f' \) verwechseln. \( f'(1)=2 \) ist **kein** Punkt des Graphen von \( f \) (nicht
„\( f \) ist 2 bei \( x=1 \)"), sondern die **Steigung** von \( f \) dort. Und die im Bild sichtbaren
Hoch-/Tiefpunkte gehören zu \( f' \), nicht zu \( f \). Wer das vertauscht, beantwortet die halbe
Aufgabe falsch.

</details>
</details>
</details>

### AB II — Nullstellen-Bedeutung, Monotonie, \( f''(1) \), Krümmung, Skizze + Fläche, Vergleich

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Bedeutung der Nullstellen von \( f' \) für \( f \) (Extrempunkte).** An einer Nullstelle von \( f' \)
hat \( f \) eine waagrechte Tangente. Ob dort ein Hoch-, Tief- oder Sattelpunkt liegt, entscheidet der
**Vorzeichenwechsel** von \( f' \):

- **\( x=-1 \):** \( f' \) wechselt von **\( + \) nach \( - \)** (links der \( -1 \) ist die Kurve oben,
  rechts davon unter der Achse) → \( f \) steigt erst, dann fällt → **Hochpunkt** von \( f \).
- **\( x=0 \):** \( f' \) wechselt von **\( - \) nach \( + \)** → \( f \) fällt erst, dann steigt →
  **Tiefpunkt** von \( f \).
- **\( x=2 \):** \( f' \) **berührt** die Achse nur und bleibt **positiv** (kein Vorzeichenwechsel) →
  **kein** Extrempunkt, sondern ein **Sattelpunkt** (Terrassenpunkt): waagrechte Tangente, aber \( f \)
  steigt davor und danach weiter.

**Monotonieverhalten von \( f \).** \( f \) steigt, wo \( f'>0 \); \( f \) fällt, wo \( f'<0 \). Aus dem
Bild:

- \( f'>0 \) für \( x<-1 \) → \( f \) **streng wachsend** auf \( (-\infty;-1] \).
- \( f'<0 \) für \( -1<x<0 \) → \( f \) **streng fallend** auf \( [-1;0] \).
- \( f'>0 \) für \( 0<x<2 \) und \( x>2 \) → \( f \) **streng wachsend** auf \( [0;\infty) \) (bei
  \( x=2 \) kurz waagrecht, dann weiter steigend).

**Näherungswert für \( f''(1) \) und Bedeutung.** \( f'' \) ist die Ableitung von \( f' \), also die
**Steigung der \( f' \)-Kurve**. In der Aufgabenskizze liegt der **Scheitel** (höchste Stelle) der
mittleren Beule **nahe \( x=1 \)**; dort verläuft die Tangente an \( f' \) **fast waagrecht**. Aus dem
Graphen liest man deshalb ab:

\[ f''(1) \approx 0. \]

(Der orange Punkt \( (1\,|\,2) \) markiert nur den **Wert** \( f'(1)=2 \) — wie hoch die Kurve bei
\( x=1 \) liegt —, nicht den Scheitel. Im hier reproduzierten exakten Term \( f'(x)=x(x+1)(x-2)^2 \)
sitzt der Scheitel ein kleines Stück weiter links, bei \( x\approx0{,}84 \); für die Prüfung zählt der
**abgelesene Näherungswert** \( f''(1)\approx0 \).)

Bedeutung: Ein Scheitel von \( f' \) **nahe \( x=1 \)** bedeutet, dass die **Steigung von \( f \) dort am
größten** ist. \( f \) hat bei \( x\approx 1 \) einen **Wendepunkt** und steigt dort **am
steilsten**.

**Krümmungsverhalten von \( f \).** Die Krümmung von \( f \) hängt am Vorzeichen von \( f'' \), also
daran, ob die \( f' \)-Kurve **steigt** oder **fällt**:

- \( f' \) **fällt** von links oben bis zum Tief der Kurve (etwa \( x\approx -0{,}5 \)) → \( f''<0 \) →
  \( f \) **rechtsgekrümmt**.
- \( f' \) **steigt** vom Tief bis zum Gipfel (etwa \( x\approx 1 \)) → \( f''>0 \) → \( f \)
  **linksgekrümmt**.
- \( f' \) **fällt** vom Gipfel bis zur Berührung bei \( x=2 \) → \( f''<0 \) → \( f \)
  **rechtsgekrümmt**.
- \( f' \) **steigt** ab \( x=2 \) → \( f''>0 \) → \( f \) **linksgekrümmt**.

An den Übergängen (\( x\approx-0{,}5 \), \( x\approx1 \), \( x=2 \)) liegen die **Wendepunkte** von
\( f \) — genau dort, wo \( f' \) seine Hoch-/Tiefpunkte hat.

**Inhalt der Fläche zwischen \( f' \) und der \( x \)-Achse auf \( [0;2] \).** Auf \( [0;2] \) liegt die
\( f' \)-Kurve **ganz über (bzw. auf) der \( x \)-Achse** (\( f'\ge 0 \)). Die Fläche ist deshalb das
Integral von \( f' \) über \( [0;2] \), und nach dem **Hauptsatz** ist das Integral der Ableitung gleich
der **Änderung von \( f \)**:

\[ A = \int_0^2 f'(x)\,dx = f(2) - f(0) = 3 - 0{,}6 = 2{,}4. \]

Die eingeschlossene Fläche misst also **\( 2{,}4 \) Flächeneinheiten** — ohne dass man eine
Stammfunktion von \( f' \) ausrechnen muss.

<figure>
<div class="jxgbox" id="jxg-k9-flaeche" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Die markierte Fläche zwischen \( f' \) und der \( x \)-Achse auf \( [0;2] \) hat den Inhalt \( f(2)-f(0)=2{,}4 \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k9-flaeche',{boundingbox:[-2.3,5.8,3.3,-2.7],axis:true,showCopyright:false,showNavigation:false});var g=b.create('functiongraph',[function(x){return x*(x+1)*(x-2)*(x-2);},-1.78,2.83],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('integral',[[0,2],g],{fillColor:'#d98324',fillOpacity:0.3,curveLeft:{visible:false},curveRight:{visible:false},baseLeft:{visible:false},baseRight:{visible:false},label:{visible:false}});})();</script>

**Skizze des Graphen von \( f \) mit \( f(0)=0{,}6 \) und \( f(2)=3 \).** Aus allem oben ergibt sich die
Form von \( f \):

- **Hochpunkt** bei \( x=-1 \), dann **fallend** bis zum **Tiefpunkt** \( (0\,|\,0{,}6) \),
- danach **steigend** durch den steilsten Punkt (Wendepunkt um \( x\approx1 \)) bis zum **Sattelpunkt**
  \( (2\,|\,3) \) mit waagrechter Tangente,
- ab \( x=2 \) weiter **steigend**.

<figure>
<div class="jxgbox" id="jxg-k9-fskizze" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Skizze von \( f \) selbst (grün): Hochpunkt bei \( x=-1 \), Tiefpunkt \( (0\,|\,0{,}6) \), Sattelpunkt \( (2\,|\,3) \). Diese Kurve ist <b>nicht</b> die Abbildung aus dem Input — die zeigt \( f' \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k9-fskizze',{boundingbox:[-1.8,3.9,2.9,-0.7],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return Math.pow(x,5)/5-3*Math.pow(x,4)/4+2*x*x+0.6;},-1.55,2.55],{strokeColor:'#3a8a5a',strokeWidth:2.5});b.create('point',[-1,1.65],{name:'Hochp.',size:2,fixed:true,strokeColor:'#b03a2e',fillColor:'#b03a2e',label:{offset:[-50,2]}});b.create('point',[0,0.6],{name:'(0|0,6) Tiefp.',size:2.5,fixed:true,strokeColor:'#3a5a9c',fillColor:'#3a5a9c',label:{offset:[8,-12]}});b.create('point',[2,3],{name:'(2|3) Sattel',size:2.5,fixed:true,strokeColor:'#d98324',fillColor:'#d98324',label:{offset:[-30,16]}});})();</script>

**Vergleich \( f(-1) \) und \( f(0) \).** Zwischen \( x=-1 \) und \( x=0 \) ist \( f'<0 \), also ist
\( f \) auf \( [-1;0] \) **streng fallend**. Damit liegt der linke Wert höher:

\[ f(-1) > f(0). \]

<details><summary>Haltung dahinter: Vorzeichen → Monotonie → Extrempunkte (ganz von vorn)</summary>

Eine zusammenhängende Kette, die fast alle Teilfragen oben erklärt.

**Vorzeichen von \( f' \) ⇒ Auf/Ab von \( f \).** Steigung positiv = bergauf, negativ = bergab. Man
liest also nur, **wo die \( f' \)-Kurve über und wo sie unter der Achse** liegt, und übersetzt: über der
Achse → \( f \) steigt; unter der Achse → \( f \) fällt. Das ist das **Monotonieverhalten**.

**Vorzeichen**wechsel** von \( f' \) ⇒ Art des Extrempunkts.** An einer waagrechten Tangente
(\( f'=0 \)) schaut man, **wie** das Vorzeichen wechselt:

- von \( + \) zu \( - \): erst hoch, dann runter → **Hochpunkt** („Bergkuppe").
- von \( - \) zu \( + \): erst runter, dann hoch → **Tiefpunkt** („Tal").
- **kein** Wechsel (z. B. \( + \) bleibt \( + \), die Kurve berührt nur): die Steigung wird kurz null und
  bleibt sonst gleich gerichtet → **Sattelpunkt** (waagrechtes „Treppchen" in einem steigenden Hang).

Genau die Berührung bei \( x=2 \) ist so ein Fall: \( f' \) tippt die Achse an und bleibt positiv —
deshalb Sattelpunkt, kein Extrempunkt.

**Steigt/fällt \( f' \) ⇒ Krümmung von \( f \).** Eine Stufe höher: \( f'' \) ist die Steigung von
\( f' \). Wo die \( f' \)-Kurve **steigt**, ist \( f''>0 \) und \( f \) macht eine **Linkskurve**
(linksgekrümmt, „lächelnde" Schale); wo sie **fällt**, ist \( f''<0 \) und \( f \) macht eine
**Rechtskurve** (rechtsgekrümmt, „traurige" Haube). Die Wendepunkte von \( f \) sitzen dort, wo \( f' \)
am höchsten/tiefsten ist.

<details><summary>… ganz langsam: warum ist die Fläche \( = f(2)-f(0) \)?</summary>

Das ist der **Hauptsatz der Differential- und Integralrechnung**, in einem Satz: „Das Integral der
Ableitung über ein Intervall ist gleich, wie viel sich die Funktion auf dem Intervall **insgesamt
geändert** hat." Bild **Tachometer/Wegstrecke**: \( f' \) ist die Geschwindigkeit, \( f \) der
zurückgelegte Weg. Die Fläche unter der Geschwindigkeitskurve von \( 0 \) bis \( 2 \) ist der in dieser
Zeit zurückgelegte Weg — also \( f(2)-f(0) \).

Hier: \( f(2)=3 \), \( f(0)=0{,}6 \), Änderung \( = 3-0{,}6 = 2{,}4 \). Weil \( f' \) auf \( [0;2] \)
nirgends unter die Achse geht (\( f'\ge0 \)), ist diese Änderung zugleich der echte **Flächeninhalt**:
\( A = 2{,}4 \). Hätte \( f' \) im Intervall einen Teil unter der Achse, müsste man wie bei einer
Flächenaufgabe an den Nullstellen trennen — hier ist das nicht nötig.

</details>

<details><summary>Typische Falle</summary>

Beim Sattelpunkt bei \( x=2 \) trotzdem einen Extrempunkt von \( f \) behaupten. Die Tangente ist zwar
waagrecht (\( f'(2)=0 \)), aber ohne **Vorzeichenwechsel** von \( f' \) ist es **kein** Hoch- oder
Tiefpunkt. Zweite Falle: \( f''(1) \) und \( f'(1) \) verwechseln — \( f'(1)=2 \) (Höhe der Kurve),
\( f''(1)\approx0 \) (Steigung der Kurve am Gipfel).

</details>
</details>

> **Transparenz zu den \( \approx \)-Werten:** \( f''(1)\approx 0 \) und die genaue Lage der
> Wendepunkte (\( x\approx-0{,}5 \), \( x\approx1 \)) sind **aus dem Graphen abgelesen** und damit
> Näherungen — die Aufgabe verlangt für \( f''(1) \) ausdrücklich nur einen **Näherungswert**. Die
> exakten Werte hingen vom genauen Funktionsterm ab; die **gegebenen** Größen \( f(0)=0{,}6 \) und
> \( f(2)=3 \) und damit die Fläche \( 2{,}4 \) sind dagegen exakt.

</details>

### AB III — Minimaler Grad von \( F \), möglicher Term von \( f' \)

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Verfahren anzeigen</summary>

**Minimaler Grad einer Stammfunktion \( F \) von \( f \).** Man zählt von unten nach oben — jede
Integration („Aufleiten") erhöht den Grad um 1:

- Die gezeichnete \( f' \)-Kurve hat **drei** Hoch-/Tiefpunkte (bzw. **vier** Nullstellen mit
  Vielfachheit). Eine ganzrationale Funktion mit drei Extremstellen hat **mindestens Grad 4** →
  \( f' \) hat mindestens **Grad 4**.
- \( f \) ist eine Stammfunktion von \( f' \) → mindestens **Grad 5**.
- \( F \) ist eine Stammfunktion von \( f \) → mindestens **Grad 6**.

\[ \Rightarrow \text{Minimaler Grad von } F \text{ ist } \mathbf{6}. \]

**Ein möglicher Funktionsterm von \( f' \).** Aus den Nullstellen baut man **Linearfaktoren**; die
**Berührung** bei \( x=2 \) liefert einen **doppelten** Faktor:

\[ f'(x) = a\cdot x\,(x+1)\,(x-2)^2. \]

Den Vorfaktor \( a \) bestimmt man mit \( f'(1)=2 \):

\[ f'(1) = a\cdot 1 \cdot 2 \cdot (1-2)^2 = a\cdot 2 = 2 \;\;\Longrightarrow\;\; a=1. \]

Also ein möglicher Term:

\[ f'(x) = x\,(x+1)\,(x-2)^2 = x^4 - 3x^3 + 4x. \]

**Probe:** \( f'(1)=1\cdot2\cdot1=2 \) ✓; Nullstellen \( -1,\ 0,\ 2 \) (doppelt) ✓; beide Ränder laufen
nach oben (Grad 4, positiver Leitkoeffizient) ✓.

<details><summary>Haltung dahinter: Aufleiten erhöht den Grad — und warum die Berührung einen doppelten Faktor gibt</summary>

**Warum erhöht Integrieren den Grad?** Aufleiten ist Ableiten rückwärts. Ableiten **senkt** den Grad um
1 (aus \( x^4 \) wird \( 4x^3 \)). Also **hebt** das Rückwärts-Verfahren den Grad um 1 (aus etwas vom
Grad 4 wird beim Aufleiten Grad 5). Zweimal aufleiten von \( f' \) (Grad 4) → \( f \) (Grad 5) →
\( F \) (Grad 6). Daher die 6.

**Warum „mindestens" Grad 4 für \( f' \)?** Eine ganzrationale Funktion vom Grad \( n \) kann höchstens
\( n-1 \) Extrempunkte und höchstens \( n \) Nullstellen haben. Drei Extrempunkte erzwingen also
\( n-1\ge 3 \), d. h. \( n\ge 4 \). Mehr als das Bild zeigt, darf man nicht annehmen — deshalb
**minimal** 4.

**Warum doppelter Faktor bei der Berührung?** Eine Nullstelle, an der die Kurve die Achse nur
**berührt** (nicht durchschneidet), ist eine Nullstelle **gerader** Vielfachheit — der einfachste Fall
ist die **doppelte** Nullstelle, also \( (x-2)^2 \). Ein einfacher Faktor \( (x-2) \) würde die Achse
**durchschneiden** (Vorzeichenwechsel); das passt nicht zum Bild. Eine einfache Nullstelle (Schnitt)
wie bei \( -1 \) und \( 0 \) liefert dagegen den einfachen Faktor.

<details><summary>Schöne Bestätigung: der Term passt zu allen gegebenen Daten</summary>

Leitet man \( f'(x)=x^4-3x^3+4x \) auf, erhält man mit \( f(0)=0{,}6 \) den Term
\( f(x)=\tfrac{1}{5}x^5-\tfrac{3}{4}x^4+2x^2+0{,}6 \). Daraus:
\( f(2)=\tfrac{32}{5}-12+8+0{,}6=3 \) ✓ (der gegebene Wert), \( f(-1)=1{,}65>0{,}6=f(0) \) ✓ (passt zur
Monotonie), und \( \int_0^2 f'(x)\,dx = f(2)-f(0)=2{,}4 \) ✓. Der gewählte mögliche Term ist also mit
**allen** Angaben der Aufgabe verträglich. Das Bild ist eine **Skizze**; verlangt war nur **ein**
passender Term, der die ablesbaren Merkmale (Nullstellen, \( f'(1)=2 \), Form) trifft.

</details>
</details>
</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Aspekt, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen kannst. Du
musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Stochastik) aufklappen</summary>

- **a) Terme.** Erwartet: \( P(A)=0{,}6^3 \) und \( P(B)=\binom{3}{2}\cdot0{,}6^2\cdot0{,}4 \).
  *Rückfrage:* „Warum steht bei \( B \) der Faktor 3 (bzw. \( \binom{3}{2} \)) davor?" (Antwort:
  drei mögliche Reihenfolgen.) *Rote Flagge:* nur \( 0{,}6^2\cdot0{,}4 \) ohne den Zählfaktor.
- **b) Binomial / Erwartungswert / Bereich.** Erwartet: **Bernoulli-Kette** (zwei Ausgänge, unabhängig
  **wegen Zurücklegen**, konstantes \( p=0{,}6 \)); \( E(Y)=15\cdot0{,}6=9 \) mit Deutung „im Mittel 9
  von 15 blau"; \( P(5\le Y\le10)=P(Y\le10)-P(Y\le4)\approx0{,}773 \). *Rückfrage:* „Warum ziehen Sie
  \( P(Y\le4) \) ab und nicht \( P(Y\le5) \)?" (Antwort: die 5 gehört dazu.) *Rote Flagge:*
  \( -P(Y\le5) \).
- **c) Histogramme.** Erwartet: **(2)** ist \( Y \), weil \( E(Y)=9 \) ganzzahlig → höchster Balken bei
  \( k=9 \); **(1)** \( p=0{,}5 \) (achsensymmetrisch); **(3)** \( \tfrac{2}{3}<p<\tfrac{4}{5} \).
  *Rückfrage:* „Woran sieht man am Histogramm, wie groß \( p \) ist?" (Antwort: an der Lage des höchsten
  Balkens / am Erwartungswert.) *Rote Flagge:* für (3) einen einzelnen \( p \)-Wert behaupten.

</details>

<details><summary>Leitfaden Teil 2 (Analysis) aufklappen</summary>

- **AB I.** Erwartet: \( f'(1)=2 \) abgelesen; Bedeutung = **Steigung** des Graphen von \( f \) bei
  \( x=1 \); Nullstellen \( -1,\ 0,\ 2 \). *Rückfrage:* „Zeigt das Bild \( f \) oder \( f' \)?" *Rote
  Flagge:* \( f \) und \( f' \) verwechseln (z. B. „\( f \) hat bei \( x=1 \) den Wert 2").
- **AB II.** Erwartet: Nullstellen von \( f' \) → **Hochpunkt** bei \( -1 \), **Tiefpunkt** bei \( 0 \),
  **Sattelpunkt** bei \( 2 \) (über den **Vorzeichenwechsel** begründet); Monotonie über das Vorzeichen
  von \( f' \); \( f''(1)\approx0 \) (Gipfel von \( f' \)) → Wendepunkt/steilster Anstieg von \( f \);
  Krümmung über Steigen/Fallen von \( f' \); **Fläche** \( =\int_0^2 f' = f(2)-f(0)=2{,}4 \); Vergleich
  \( f(-1)>f(0) \) (weil \( f \) auf \( [-1;0] \) fällt). *Rückfragen:* „Warum ist \( x=2 \) **kein**
  Extrempunkt?" · „Wie kommen Sie ohne Stammfunktion auf die Fläche 2,4?" *Rote Flagge:* Fläche über
  eine mühsame Stammfunktion von \( f' \) statt über \( f(2)-f(0) \).
- **AB III.** Erwartet: minimaler Grad von \( F \) ist **6** (\( f' \) Grad 4 → \( f \) Grad 5 → \( F \)
  Grad 6); möglicher Term \( f'(x)=x(x+1)(x-2)^2 \). *Rückfrage:* „Warum ist der Faktor \( (x-2) \)
  **quadriert**?" (Antwort: Berührung = doppelte Nullstelle.) *Hinweis für dich:* Andere Terme sind
  erlaubt, solange Nullstellen und \( f'(1)=2 \) stimmen — es ist **ein** möglicher Term gefragt.

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Warum steht bei „genau zwei blau" ein Binomialkoeffizient vor dem Term, bei „alle blau" aber nicht?
- Welche drei Eigenschaften machen aus dem Ziehen mit Zurücklegen eine Bernoulli-Kette, und warum ist
  das Zurücklegen entscheidend?
- Wie liest du aus einem Binomial-Histogramm die Trefferwahrscheinlichkeit \( p \) ab?
- Das Bild zeigt \( f' \): Wie kommst du von den Nullstellen von \( f' \) auf die Hoch-, Tief- und
  Sattelpunkte von \( f \)?
- Warum ist die Fläche zwischen \( f' \) und der \( x \)-Achse auf \( [0;2] \) genau \( f(2)-f(0) \)?
- Warum hat eine Stammfunktion \( F \) von \( f \) mindestens den Grad 6?
</content>
</invoke>
