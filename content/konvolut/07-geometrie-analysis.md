# Aufgabe 7 — Geometrie & Analysis

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Geometrie**, **Teil 2 (Gespräch) aus der Analysis**. Alles ist
**rechnerfrei** zu lösen. Arbeitet die Aufgabe wie eine echte Simulation durch — eine Person trägt
vor, die andere prüft mit dem Lösungsweg und dem [Prüfer-Leitfaden](#prufer-leitfaden-fur-die-abfragende-person)
am Ende mit.

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

> **Werkzeug zum Nachschlagen:** Die wiederkehrenden Vektor- und Geometrie-Werkzeuge (Punkte,
> Vektoren, Länge, Skalarprodukt, Kreuzprodukt, Geraden- und Ebenengleichung) stehen kompakt im
> [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html) (Anker u. a.
> [#skalarprodukt](konv-90-werkzeugkasten-geometrie.html#skalarprodukt),
> [#kreuzprodukt](konv-90-werkzeugkasten-geometrie.html#kreuzprodukt)). Die Analysis-Werkzeuge findest
> du in den Kapiteln [Funktionsuntersuchung](kap-funktionsuntersuchung.html),
> [Integral-Grundlagen](kap-integral-grundlagen.html) und
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).

---

## Teil 1 — Vortrag (Geometrie): Punkte und Ebenen einer Geraden

<div class="aufgabenkasten">

**Die Punkte \( A(2\,|\,1\,|\,0) \) und \( B(4\,|\,0\,|\,2) \) liegen auf der Geraden \( g \).**

**a)** Prüfe, ob der Punkt \( C(0\,|\,2\,|\,-2) \) auf der Geraden \( g \) liegt.

**b)** Zeige, dass die Gerade \( g \) in der Ebene \( E:\ x_1 + 2x_2 = 4 \) liegt. Ermittle außerdem die
Gleichung einer weiteren Ebene, die ebenfalls die Gerade \( g \) enthält.

**c)** Bestimme die Koordinaten eines Punktes \( D \), der auf der Geraden \( g \) liegt und vom Punkt
\( A \) den Abstand \( 9 \) hat.

**d)** Beschreibe ein Verfahren, mit dem man die Koordinaten eines Punktes \( P \) bestimmen kann, der
mit den beiden Punkten \( A \) und \( B \) ein gleichseitiges Dreieck bildet.

</div>

> **Vorab, in einem Satz, was ein Koordinatensystem im Raum ist:** Jeder Punkt im Raum braucht **drei**
> Zahlen — \( (x_1 \mid x_2 \mid x_3) \) —, weil es „rechts/links", „vorne/hinten" und „oben/unten"
> gibt. \( B(4\,|\,0\,|\,2) \) heißt: 4 Schritte in \( x_1 \)-Richtung, 0 in \( x_2 \), 2 in \( x_3 \).
> Eine **Gerade** ist eine unendlich lange, schnurgerade Linie durch diesen Raum.

So liegen die Punkte und die Gerade \( g \) im Koordinatensystem (schematisch):

<figure>
<svg viewBox="0 0 460 320" role="img" aria-label="Schrägbild der Geraden g durch die Punkte A, B, C und D mit der Ebene E" style="width:100%;max-width:480px;height:auto;background:#fbf7ef;border-radius:8px">
  <defs>
    <marker id="ah7" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#7a7163"/></marker>
  </defs>
  <polygon points="306,210 138,102 138,186 306,294" fill="#3a5a9c" fill-opacity="0.07" stroke="#3a5a9c" stroke-width="0.8" stroke-opacity="0.4"/>
  <text x="150" y="128" font-size="13" fill="#3a5a9c" font-weight="bold">E</text>
  <line x1="250" y1="210" x2="250" y2="70"  stroke="#7a7163" stroke-width="1.5" marker-end="url(#ah7)"/>
  <line x1="250" y1="210" x2="420" y2="210" stroke="#7a7163" stroke-width="1.5" marker-end="url(#ah7)"/>
  <line x1="250" y1="210" x2="180" y2="260" stroke="#7a7163" stroke-width="1.5" marker-end="url(#ah7)"/>
  <text x="238" y="66"  font-size="13" fill="#7a7163">x₃</text>
  <text x="424" y="214" font-size="13" fill="#7a7163">x₂</text>
  <text x="168" y="276" font-size="13" fill="#7a7163">x₁</text>
  <line x1="306" y1="266" x2="82" y2="122" stroke="#3a5a9c" stroke-width="2"/>
  <text x="330" y="148" font-size="12" fill="#26324a">g</text>
  <circle cx="306" cy="266" r="3.5" fill="#3a8a5a"/><text x="312" y="282" font-size="12" fill="#26324a">C(0|2|−2)</text>
  <circle cx="250" cy="230" r="3.5" fill="#3a5a9c"/><text x="256" y="244" font-size="12" fill="#26324a" font-weight="bold">A(2|1|0)</text>
  <circle cx="194" cy="194" r="3.5" fill="#3a5a9c"/><text x="120" y="186" font-size="12" fill="#26324a" font-weight="bold">B(4|0|2)</text>
  <circle cx="82"  cy="122" r="3.5" fill="#d98324"/><text x="40"  y="112" font-size="12" fill="#26324a">D(8|−2|6)</text>
</svg>
<figcaption>Schematisches Schrägbild — \( A,\ B,\ C,\ D \) liegen alle auf \( g \). Die Ebene \( E \) (blau angedeutet) enthält die ganze Gerade. Es gilt \( |\overline{AB}| = 3 \) und \( |\overline{AD}| = 9 = 3\cdot|\overline{AB}| \).</figcaption>
</figure>

### Teilaufgabe a) — Punktprobe: Liegt \( C \) auf \( g \)?

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Schritt 1 — Richtungsvektor der Geraden.** Die Gerade läuft durch \( A \) und \( B \). Ihr
**Richtungsvektor** (der Pfeil, in den die Gerade zeigt) ist „Ziel minus Start":

\[ \overrightarrow{AB} = B - A = \begin{pmatrix}4\\0\\2\end{pmatrix} - \begin{pmatrix}2\\1\\0\end{pmatrix}
   = \begin{pmatrix}2\\-1\\2\end{pmatrix}. \]

**Schritt 2 — Pfeil von \( C \) nach \( A \).** Wir prüfen, ob man von \( C \) aus genau in dieser
Richtung zu \( A \) (und damit auf die Gerade) kommt:

\[ \overrightarrow{CA} = A - C = \begin{pmatrix}2\\1\\0\end{pmatrix} - \begin{pmatrix}0\\2\\-2\end{pmatrix}
   = \begin{pmatrix}2\\-1\\2\end{pmatrix}. \]

**Schritt 3 — Vergleich.** Es ist \( \overrightarrow{CA} = \overrightarrow{AB} \): der Pfeil von
\( C \) nach \( A \) ist **genau** der Richtungsvektor der Geraden. Damit liegt \( C \) auf derselben
Geraden — eine Schrittlänge „vor" \( A \).

**Ergebnis: \( C \) liegt auf \( g \), denn \( \overrightarrow{CA} = \overrightarrow{AB} = \begin{pmatrix}2\\-1\\2\end{pmatrix} \).**

<details><summary>Haltung dahinter: Was ist eine Gerade, ein Richtungsvektor — und was bedeutet „Punktprobe"? (ganz von vorn)</summary>

Erst die Bausteine, ganz langsam.

**Punkt und Vektor.** Ein **Punkt** ist ein Ort im Raum, festgelegt durch drei Zahlen
\( (x_1\mid x_2\mid x_3) \). Ein **Vektor** ist ein **Pfeil** — eine Bewegung mit Richtung und Länge,
geschrieben als Spalte mit drei Zahlen. Den Pfeil von einem Punkt \( P \) zu einem Punkt \( Q \)
schreibt man \( \overrightarrow{PQ} \) und rechnet ihn als **„Ziel minus Start"**: \( Q - P \).
Man zieht dafür die Koordinaten einzeln voneinander ab.

**Gerade in Parameterform.** Eine **Gerade** beschreibt man durch einen **Startpunkt** (Ortsvektor)
und einen **Richtungsvektor** (in welche Richtung die Linie zeigt):

\[ g:\quad \vec x = \underbrace{\begin{pmatrix}2\\1\\0\end{pmatrix}}_{A,\ \text{Stützpunkt}} \;+\;
   t\cdot \underbrace{\begin{pmatrix}2\\-1\\2\end{pmatrix}}_{\overrightarrow{AB},\ \text{Richtung}}. \]

Das \( t \) ist eine frei wählbare Zahl (der **Parameter**). Für jedes \( t \) bekommt man **einen**
Punkt der Geraden: \( t=0 \) liefert \( A \), \( t=1 \) liefert \( B \). Bild: \( A \) ist der
Bahnhof, der Richtungsvektor ist „eine Fahrt", und \( t \) sagt, wie viele Fahrten man von \( A \) aus
macht (auch rückwärts mit negativem \( t \)).

**Punktprobe.** „Punktprobe" heißt: nachprüfen, ob ein gegebener Punkt **wirklich** auf der Geraden
sitzt. Man fragt: Gibt es ein \( t \), für das die Geradenformel genau diesen Punkt ausspuckt? Hier ist
es besonders bequem: Der Pfeil von \( C \) zu \( A \) ist **identisch** mit dem Richtungsvektor. Das
heißt, von \( C \) aus erreicht man \( A \) mit genau einem „Richtungsschritt" — also ist \( C \) der
Geradenpunkt mit \( t = -1 \) (man geht von \( A \) einen Schritt **zurück**). Probe:
\( A + (-1)\cdot\overrightarrow{AB} = (2,1,0) - (2,-1,2) = (0,2,-2) = C \). ✓

<details><summary>Ganz langsam (mit Zahlen): warum ist „Ziel minus Start" richtig?</summary>

\( \overrightarrow{CA} = A - C \) rechnet man Zeile für Zeile:

- 1. Zeile: \( 2 - 0 = 2 \).
- 2. Zeile: \( 1 - 2 = -1 \).
- 3. Zeile: \( 0 - (-2) = 0 + 2 = 2 \) — **Achtung:** „minus minus zwei" wird „plus zwei".

Ergebnis \( (2,\,-1,\,2) \). Vergleich mit \( \overrightarrow{AB} = (2,-1,2) \): Zeile für Zeile
gleich. Wären auch nur **eine** Zahl verschieden, läge \( C \) nicht auf \( g \). Hier stimmt alles,
also liegt \( C \) auf der Geraden.

</details>

<details><summary>Typische Falle</summary>

Man darf nicht nur **eine** Koordinate vergleichen. \( C \) liegt nur dann auf \( g \), wenn der Pfeil
\( \overrightarrow{CA} \) in **allen drei** Zeilen ein **Vielfaches** des Richtungsvektors ist (hier
sogar das \( 1 \)-fache). Stimmt eine einzige Zeile nicht zum selben Faktor, liegt der Punkt daneben.
In der Prüfung also immer alle drei Zeilen nennen.

</details>
</details>
</details>

### Teilaufgabe b) — Gerade in einer Ebene zeigen und eine weitere Ebene finden

<span class="tag tag-ok">AB I</span> <span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Teil 1 — \( g \) liegt in \( E:\ x_1 + 2x_2 = 4 \).** Eine Gerade liegt vollständig in einer Ebene,
wenn schon **zwei** ihrer Punkte in der Ebene liegen. Wir setzen \( A \) und \( B \) in die
Ebenengleichung ein:

\[ A(2\,|\,1\,|\,0):\quad 2 + 2\cdot 1 = 4 \;\checkmark \qquad
   B(4\,|\,0\,|\,2):\quad 4 + 2\cdot 0 = 4 \;\checkmark \]

Beide Punkte erfüllen die Gleichung. Da \( A \) und \( B \) in \( E \) liegen, liegt die gesamte
Gerade \( g \) (sie geht durch \( A \) und \( B \)) in \( E \).

**Ergebnis: Weil \( A \) und \( B \) die Gleichung \( x_1+2x_2=4 \) erfüllen, liegt \( g \) in \( E \).**

**Teil 2 — eine weitere Ebene durch \( g \).** Durch eine Gerade gibt es **unendlich viele** Ebenen
(wie unendlich viele Buchseiten an einem Buchrücken). Eine bequeme Beschreibung ist die
**Parameterform**: man nimmt die Gerade und spannt mit einem **zweiten** Richtungsvektor eine Ebene
auf. Wir wählen \( \begin{pmatrix}1\\1\\1\end{pmatrix} \):

\[ F:\quad \vec x = \begin{pmatrix}2\\1\\0\end{pmatrix} + t\cdot\begin{pmatrix}2\\-1\\2\end{pmatrix}
   + u\cdot\begin{pmatrix}1\\1\\1\end{pmatrix},\qquad t,u\in\mathbb{R}. \]

Das ist eine **gültige neue** Ebene, weil \( \begin{pmatrix}1\\1\\1\end{pmatrix} \)

- **nicht parallel** zu \( \overrightarrow{AB}=\begin{pmatrix}2\\-1\\2\end{pmatrix} \) ist (sonst würde
  keine Fläche aufgespannt, sondern wieder nur die Gerade), und
- **nicht orthogonal** zum Normalenvektor \( \vec n_E = \begin{pmatrix}1\\2\\0\end{pmatrix} \) von
  \( E \) ist — der Test ist das Skalarprodukt:
  \( \begin{pmatrix}1\\1\\1\end{pmatrix}\cdot\begin{pmatrix}1\\2\\0\end{pmatrix} = 1+2+0 = 3 \neq 0 \).
  Weil das nicht \( 0 \) ist, „sticht" der neue Vektor aus \( E \) heraus, also ist \( F \neq E \).

**Ergebnis: \( F:\ \vec x = \begin{pmatrix}2\\1\\0\end{pmatrix} + t\begin{pmatrix}2\\-1\\2\end{pmatrix} + u\begin{pmatrix}1\\1\\1\end{pmatrix} \) ist eine weitere Ebene durch \( g \).**

<details><summary>Haltung dahinter: Was ist eine Ebene, ein Normalenvektor — und warum reichen zwei Punkte? (ganz von vorn)</summary>

**Ebene.** Eine **Ebene** ist eine vollkommen flache, unendlich ausgedehnte Fläche — wie eine
unendlich große, ideal glatte Tischplatte. Eine **Koordinatengleichung** der Form
\( n_1x_1 + n_2x_2 + n_3x_3 = d \) beschreibt **genau die Punkte, die auf der Ebene liegen**: setzt man
einen Ebenenpunkt ein, kommt die Zahl \( d \) heraus; setzt man einen Punkt daneben ein, kommt etwas
anderes heraus. Bei \( E \) fehlt \( x_3 \) — das heißt nur, dass \( x_3 \) frei ist (die Ebene steht
„senkrecht" und enthält die ganze Höhenrichtung).

**Warum reichen zwei Punkte für „Gerade liegt in Ebene"?** Durch zwei Punkte geht **genau eine**
Gerade. Liegen diese zwei Punkte in der flachen Ebene, dann kann die geradlinige Verbindung zwischen
ihnen nicht aus der Ebene „herausbeulen" — sie bleibt komplett drin. Also genügt es, \( A \) und \( B \)
einzusetzen; alle anderen Geradenpunkte liegen dann automatisch mit drin.

**Normalenvektor.** Der **Normalenvektor** \( \vec n \) ist ein Pfeil, der **senkrecht** auf der Ebene
steht — wie ein Fahnenmast gerade aus dem Boden. Seine drei Zahlen sind genau die Vorfaktoren vor
\( x_1, x_2, x_3 \) in der Ebenengleichung. Bei \( E:\ x_1 + 2x_2 = 4 \) liest man also direkt ab:
\( \vec n_E = (1,\,2,\,0) \).

<details><summary>Skalarprodukt: der „Senkrecht-Test" — wozu, und wie?</summary>

Das **Skalarprodukt** zweier Pfeile ist eine Zahl: man multipliziert die Vektoren zeilenweise und
addiert. Sein wichtigster Nutzen: Es ist **genau dann \( 0 \), wenn die beiden Pfeile senkrecht
(orthogonal) aufeinander stehen**.

Wir brauchen es hier umgekehrt: Damit unsere zweite Ebene \( F \) **wirklich neu** ist (also nicht
zufällig wieder \( E \)), darf der Spannvektor \( (1,1,1) \) **nicht in \( E \) liegen**. „In \( E \)
liegen" würde bedeuten: senkrecht zum Mast \( \vec n_E \). Wir rechnen das Skalarprodukt:

\[ \begin{pmatrix}1\\1\\1\end{pmatrix}\cdot\begin{pmatrix}1\\2\\0\end{pmatrix}
   = 1\cdot 1 + 1\cdot 2 + 1\cdot 0 = 3. \]

Das ist **nicht \( 0 \)**, also steht \( (1,1,1) \) **nicht** senkrecht auf dem Mast, liegt also
**nicht** in \( E \) — es ragt heraus. Damit ist \( F \) eine andere Ebene als \( E \), enthält die
Gerade aber trotzdem (für \( u=0 \) bleibt genau \( g \) übrig). Mehr zum Skalarprodukt im
[Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html#skalarprodukt).

</details>

<details><summary>Alternative: dieselbe „weitere Ebene" als Koordinatengleichung</summary>

Wer lieber eine Gleichung \( n_1x_1+n_2x_2+n_3x_3=d \) nennt, sucht einen Normalenvektor, der
**senkrecht zum Richtungsvektor** \( \overrightarrow{AB}=(2,-1,2) \) steht (damit die Ebene die
Gerade enthält) und **nicht parallel** zu \( \vec n_E=(1,2,0) \) ist (damit es eine andere Ebene ist).
Zum Beispiel \( \vec n = (2,2,-1) \): Test \( (2,2,-1)\cdot(2,-1,2) = 4-2-2 = 0 \) ✓. Einsetzen von
\( A \): \( 2\cdot2 + 2\cdot1 - 0 = 6 \). Also

\[ F:\quad 2x_1 + 2x_2 - x_3 = 6. \]

Probe mit \( B(4|0|2): 8+0-2 = 6 \) ✓. Beide Formen — Parameterform oder diese Gleichung — sind
korrekte Antworten.

</details>
</details>
</details>

### Teilaufgabe c) — Punkt \( D \) auf \( g \) mit Abstand \( 9 \) von \( A \)

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Schritt 1 — Länge des Richtungsvektors.** Wie weit kommt man mit **einem** Richtungsschritt? Das ist
der Betrag (die Länge) von \( \overrightarrow{AB} \):

\[ |\overrightarrow{AB}| = \sqrt{2^2 + (-1)^2 + 2^2} = \sqrt{4+1+4} = \sqrt{9} = 3. \]

Ein Schritt entlang der Geraden ist also \( 3 \) lang.

**Schritt 2 — wie viele Schritte für Abstand \( 9 \)?** Wir wollen Abstand \( 9 \). Da jeder Schritt
\( 3 \) misst, brauchen wir \( \dfrac{9}{3} = 3 \) Schritte. Also \( t = 3 \) (man kann auch
\( t = -3 \) nehmen — das gäbe einen zweiten Punkt auf der anderen Seite von \( A \)).

**Schritt 3 — Punkt ausrechnen.**

\[ \overrightarrow{OD} = \begin{pmatrix}2\\1\\0\end{pmatrix} + 3\cdot\begin{pmatrix}2\\-1\\2\end{pmatrix}
   = \begin{pmatrix}2+6\\1-3\\0+6\end{pmatrix} = \begin{pmatrix}8\\-2\\6\end{pmatrix}. \]

**Ergebnis: \( D(8\,|\,-2\,|\,6) \).** (Der zweite mögliche Punkt wäre \( D'(-4\,|\,4\,|\,-6) \) für
\( t=-3 \).)

<details><summary>Haltung dahinter: Was ist der „Betrag" eines Vektors, und warum löst er die Aufgabe? (ganz von vorn)</summary>

**Abstand und Betrag.** Der **Abstand** zweier Punkte ist die Länge der Strecke dazwischen. Die
**Länge eines Pfeils** \( |\vec v| \) (auch „Betrag" genannt) bekommt man mit dem **Satz des
Pythagoras**, nur in drei Dimensionen: jede der drei Zahlen quadrieren, addieren, Wurzel ziehen:

\[ \left|\begin{pmatrix}a\\b\\c\end{pmatrix}\right| = \sqrt{a^2+b^2+c^2}. \]

Hier wird \( \sqrt{4+1+4}=\sqrt 9 = 3 \) — eine seltene runde Zahl, das macht die Aufgabe angenehm.

**Die Idee der Lösung.** Auf der Geraden bewegt man sich in Vielfachen des Richtungsvektors. Ein
Vielfaches \( t\cdot\overrightarrow{AB} \) ist \( |t| \) mal so lang wie ein Schritt, also
\( |t|\cdot 3 \). Soll der Abstand \( 9 \) sein, muss \( |t|\cdot 3 = 9 \), also \( |t| = 3 \). Mit
\( t=3 \) geht man drei volle Schritte von \( A \) weg und landet bei \( D \).

<details><summary>Ganz langsam (mit Zahlen): die Multiplikation \( 3\cdot\overrightarrow{AB} \)</summary>

„Einen Vektor mit einer Zahl multiplizieren" heißt: **jede Zeile** mit der Zahl multiplizieren.

\[ 3\cdot\begin{pmatrix}2\\-1\\2\end{pmatrix}
   = \begin{pmatrix}3\cdot 2\\ 3\cdot(-1)\\ 3\cdot 2\end{pmatrix}
   = \begin{pmatrix}6\\-3\\6\end{pmatrix}. \]

Dann zu \( A \) addieren — auch das geht zeilenweise: \( 2+6=8 \), \( 1+(-3)=1-3=-2 \), \( 0+6=6 \).
Ergebnis \( (8,-2,6) \).

**Probe:** \( \overrightarrow{AD} = D - A = (6,-3,6) \), Länge
\( \sqrt{36+9+36} = \sqrt{81} = 9 \). ✓ Genau der geforderte Abstand.

</details>

<details><summary>Typische Falle</summary>

Man darf den Faktor nicht „nach Gefühl" wählen. Wer \( D = A + 9\cdot\overrightarrow{AB} \) bildet,
bekommt Abstand \( 9\cdot 3 = 27 \), nicht \( 9 \). Erst die **Länge eines Schritts** bestimmen, dann
die Anzahl der Schritte ausrechnen (\( 9 \div 3 = 3 \)). Hätte \( |\overrightarrow{AB}| \) keine runde
Länge, müsste man durch genau diese Länge teilen.

</details>
</details>
</details>

### Teilaufgabe d) — Verfahren: Punkt \( P \) mit gleichseitigem Dreieck \( ABP \)

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Verfahren anzeigen</summary>

Gefragt ist hier ein **Verfahren** (eine beschriebene Vorgehensweise), kein einzelnes Zahlenergebnis.
Ein **gleichseitiges Dreieck** hat drei gleich lange Seiten: \( |\overline{AB}| = |\overline{AP}| =
|\overline{BP}| \). Wir kennen \( |\overline{AB}| = 3 \) (aus Teil c). Das Verfahren in drei Schritten:

**Schritt 1 — Mittelpunkt von \( \overline{AB} \) bestimmen.** Der Mittelpunkt \( M \) ist der
Durchschnitt der Endpunkte:

\[ M = \tfrac12\,(A + B) = \tfrac12\big((2,1,0)+(4,0,2)\big) = (3\,|\,0{,}5\,|\,1). \]

**Schritt 2 — eine zu \( \overrightarrow{AB} \) senkrechte Richtung \( \vec v \) wählen.** \( \vec v \)
muss \( \overrightarrow{AB}\cdot\vec v = 0 \) erfüllen, z. B. \( \vec v = (1,0,-1) \), denn
\( (2,-1,2)\cdot(1,0,-1) = 2+0-2 = 0 \). Damit steht man im rechten Winkel zur Strecke \( \overline{AB} \).

**Schritt 3 — \( P \) auf der „Mittelsenkrechten" \( g' \) so wählen, dass \( |\overline{AP}| =
|\overline{AB}| \).** Man legt die Hilfsgerade

\[ g':\quad \vec x = \overrightarrow{OM} + t\cdot\vec v \]

durch \( M \) und bestimmt das \( t \), für das der Punkt von \( A \) den Abstand \( 3 \) hat. Weil
jeder Punkt auf \( g' \) von \( A \) **und** \( B \) gleich weit entfernt ist, ist mit
\( |\overline{AP}| = 3 \) automatisch auch \( |\overline{BP}| = 3 \) — also gleichseitig.

**Verfahren als Antwort:** Mittelpunkt \( M \) von \( \overline{AB} \) bestimmen → zu
\( \overrightarrow{AB} \) senkrechten Vektor \( \vec v \) wählen → \( P \) auf \( g':\ \vec x =
\overrightarrow{OM} + t\,\vec v \) so bestimmen, dass \( |\overline{AP}| = |\overline{AB}| \).

So sieht das gesuchte Dreieck aus (Prinzip-Skizze):

<figure>
<svg viewBox="0 0 420 300" role="img" aria-label="Gleichseitiges Dreieck ABP mit Mittelpunkt M und Mittelsenkrechter durch M" style="width:100%;max-width:420px;height:auto;background:#fbf7ef;border-radius:8px">
  <defs>
    <marker id="av7" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#d98324"/></marker>
  </defs>
  <polygon points="90,230 330,230 210,22" fill="#3a5a9c" fill-opacity="0.06" stroke="#3a5a9c" stroke-width="1.8"/>
  <line x1="210" y1="230" x2="210" y2="150" stroke="#d98324" stroke-width="1.6" stroke-dasharray="4 3" marker-end="url(#av7)"/>
  <line x1="210" y1="230" x2="210" y2="22" stroke="#d98324" stroke-width="1" stroke-dasharray="2 3" opacity="0.6"/>
  <rect x="210" y="222" width="8" height="8" fill="none" stroke="#7a7163" stroke-width="1"/>
  <line x1="148" y1="120" x2="160" y2="130" stroke="#26324a" stroke-width="1.4"/>
  <line x1="272" y1="120" x2="260" y2="130" stroke="#26324a" stroke-width="1.4"/>
  <line x1="206" y1="222" x2="214" y2="238" stroke="#26324a" stroke-width="1.4"/>
  <circle cx="90" cy="230" r="3.5" fill="#3a5a9c"/><text x="70" y="250" font-size="13" fill="#26324a" font-weight="bold">A</text>
  <circle cx="330" cy="230" r="3.5" fill="#3a5a9c"/><text x="336" y="250" font-size="13" fill="#26324a" font-weight="bold">B</text>
  <circle cx="210" cy="22"  r="3.5" fill="#3a8a5a"/><text x="200" y="16" font-size="13" fill="#26324a" font-weight="bold">P</text>
  <circle cx="210" cy="230" r="3"   fill="#7a7163"/><text x="190" y="250" font-size="12" fill="#26324a">M</text>
  <text x="224" y="180" font-size="12" fill="#d98324">v ⟂ AB</text>
  <text x="115" y="290" font-size="12" fill="#26324a">|AB| = |AP| = |BP| = 3</text>
</svg>
<figcaption>Prinzip: \( P \) sitzt auf der Mittelsenkrechten von \( \overline{AB} \) (gestrichelt). Dort ist \( P \) von \( A \) und \( B \) gleich weit entfernt; man rückt \( P \) so weit hinaus, bis dieser Abstand \( = |\overline{AB}| \) wird.</figcaption>
</figure>

<details><summary>Haltung dahinter: Warum die Mittelsenkrechte, und warum genügt \( |\overline{AP}| = |\overline{AB}| \)? (ganz von vorn)</summary>

**Gleichseitig vs. gleichschenklig.** „Gleichschenklig" heißt **zwei** gleich lange Seiten,
„gleichseitig" heißt **alle drei** gleich lang. Wir bauen das Dreieck in zwei Etappen: zuerst die
beiden Schenkel \( \overline{AP} \) und \( \overline{BP} \) automatisch gleich machen, dann die Länge
auf \( |\overline{AB}| \) eichen.

**Mittelsenkrechte (Mittelpunkt + senkrechte Richtung).** Die **Mittelsenkrechte** von
\( \overline{AB} \) ist die Linie, die genau durch die Mitte \( M \) geht und im rechten Winkel zur
Strecke steht. Ihr Geheimnis: **Jeder** Punkt auf ihr hat zu \( A \) **denselben** Abstand wie zu
\( B \). Bild: Wenn du genau zwischen zwei Bäumen stehst und seitlich exakt im rechten Winkel
weggehst, bleibst du immer von beiden Bäumen gleich weit entfernt. Setzt man \( P \) also auf diese
Linie, ist \( |\overline{AP}| = |\overline{BP}| \) **geschenkt** — egal wie weit draußen.

**Die letzte Eichung.** Jetzt fehlt nur noch, dass diese gemeinsame Länge gerade \( |\overline{AB}| \)
trifft. Deshalb schiebt man \( P \) auf der Mittelsenkrechten so lange nach außen, bis
\( |\overline{AP}| = |\overline{AB}| = 3 \). Dann sind alle drei Seiten gleich → gleichseitig.

<details><summary>Ganz langsam (mit Zahlen): einen senkrechten Vektor finden und das Dreieck schließen</summary>

**Senkrechte Richtung über das Skalarprodukt.** Gesucht ist \( \vec v \) mit
\( \overrightarrow{AB}\cdot\vec v = 0 \). Mit \( \overrightarrow{AB} = (2,-1,2) \) probiert man eine
einfache Wahl \( \vec v = (1,0,-1) \):

\[ (2,-1,2)\cdot(1,0,-1) = 2\cdot 1 + (-1)\cdot 0 + 2\cdot(-1) = 2 + 0 - 2 = 0. \;\checkmark \]

Das \( 0 \) bestätigt: \( \vec v \) steht senkrecht auf \( \overrightarrow{AB} \).

**Wie weit hinaus?** In einem gleichseitigen Dreieck mit Seitenlänge \( 3 \) ist die **Höhe**
\( h = \tfrac{\sqrt 3}{2}\cdot 3 = \tfrac{3}{2}\sqrt 3 \approx 2{,}6 \). So weit muss \( P \) von \( M \)
entfernt sein. Man wählt \( t \) also so, dass \( |t\cdot\vec v| = \tfrac{3}{2}\sqrt 3 \). Wegen
\( |\vec v| = \sqrt{1^2+0^2+(-1)^2} = \sqrt 2 \) ergibt das \( t = \dfrac{3\sqrt 3}{2\sqrt 2} \approx
1{,}84 \) (oder das negative \( t \) für den gespiegelten Punkt). Einsetzen liefert einen konkreten
Punkt, z. B. \( P \approx (4{,}84\,|\,0{,}5\,|\,-0{,}84) \). **Probe:**
\( |\overline{AP}| \approx 3 \) und \( |\overline{BP}| \approx 3 \). ✓

Dass die Koordinaten **keine** glatten Zahlen sind, ist normal: Die Höhe eines gleichseitigen
Dreiecks enthält immer \( \sqrt 3 \). In der mündlichen Prüfung reicht das **beschriebene Verfahren** —
genau das verlangt der Aufgabentext.

</details>

<details><summary>Feinheit: im Raum gibt es unendlich viele solche \( P \)</summary>

Auf einem Blatt Papier (2D) liegen \( P \) und sein Spiegelbild fest — zwei Lösungen. **Im Raum** (3D)
gibt es **unendlich viele** senkrechte Richtungen \( \vec v \); die passenden \( P \) bilden einen
**ganzen Kreis** um \( \overline{AB} \). Das Verfahren wählt mit einem festen \( \vec v \) eine
Richtung daraus aus — das ist völlig in Ordnung, weil nur **ein** passender Punkt gefragt ist. Wer
mag, nennt das im Gespräch als Zusatz: „Es gibt unendlich viele, ich wähle eine Richtung."

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- a) \( C \) liegt auf \( g \), denn \( \overrightarrow{CA} = \overrightarrow{AB} = (2,-1,2) \) (Parameter \( t=-1 \)).
- b) \( A,B \) erfüllen \( x_1+2x_2=4 \) → \( g \subset E \). Weitere Ebene
  \( F:\ \vec x = (2,1,0) + t(2,-1,2) + u(1,1,1) \) (oder \( 2x_1+2x_2-x_3=6 \)).
- c) \( |\overrightarrow{AB}|=3 \), \( t=3 \): \( D(8\,|\,-2\,|\,6) \).
- d) Mittelpunkt \( M \) → senkrechter Vektor \( \vec v \) → \( P \) auf \( g'=\overrightarrow{OM}+t\vec v \) mit \( |\overline{AP}|=|\overline{AB}| \).

</details>

---

## Teil 2 — Gespräch (Analysis): Zuflussrate und Wasservolumen

<div class="aufgabenkasten">

**Input.** Gegeben ist die Funktion \( f \) mit \( f(t) = -2t^2 + 12t \). In dem Intervall, in welchem
\( f(t) \ge 0 \) ist, beschreibt \( f \) die **momentane Zuflussrate** von Wasser in ein Becken
(\( t \) in Stunden; \( f(t) \) in Liter pro Stunde). Zu Beginn enthält das Becken \( 20 \) Liter Wasser.

**Denkbare Aspekte:**
**(AB I)** Nullstellen und Extrempunkt des Graphen von \( f \) ermitteln; eine Skizze des Graphen
erstellen.
**(AB II)** Das in der ersten Stunde zugeflossene Wasservolumen ermitteln. — *Zusätzlich:* ein
konstanter Abfluss von \( 10 \) Liter pro Stunde seit Beginn. Dann: graphisch die Zeitpunkte des
minimalen und maximalen Wasservolumens bestimmen; rechnerisch das Wasservolumen nach \( 3 \) Stunden
bestimmen; das Wasservolumen in Abhängigkeit von der Zeit beschreiben.
**(AB III)** Ab \( t=4 \) soll die konstante Abflussrate so geändert werden, dass das Becken zum
Zeitpunkt \( t=6 \) leer ist — die Vorgehensweise zur Bestimmung der nötigen Abflussrate erläutern.

</div>

> **Vorab, in einem Satz, was „Zuflussrate" bedeutet:** \( f(t) \) ist **nicht** die Wassermenge,
> sondern das **Tempo** des Zuflusses zu einem Zeitpunkt — wie der Tacho im Auto (Geschwindigkeit),
> nicht der Kilometerzähler (Strecke). Wie viel Wasser tatsächlich **zusammenkommt**, ergibt erst das
> **Aufsummieren** der Rate über die Zeit (das Integral).

So sieht die Zuflussrate \( f \) aus — mit der Linie \( y=10 \), die später (beim Abfluss) wichtig wird:

<figure>
<div class="jxgbox" id="jxg-k7-f" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Zuflussrate \( f(t) = -2t^2+12t \) auf \( [0;6] \). Nullstellen bei \( t=0 \) und \( t=6 \), Hochpunkt \( (3\,|\,18) \). Die grüne Linie ist die spätere Abflussrate \( 10 \); sie schneidet \( f \) bei \( t=1 \) und \( t=5 \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k7-f',{boundingbox:[-1,21,7,-3],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return -2*x*x+12*x;},0,6],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('functiongraph',[function(x){return 10;},0,6],{strokeColor:'#3a8a5a',strokeWidth:1.5,dash:2});b.create('point',[3,18],{name:'HP(3|18)',size:2,fixed:true,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[8,6]}});b.create('point',[6,0],{name:'t=6',size:2,fixed:true,fillColor:'#3a5a9c',strokeColor:'#3a5a9c',label:{offset:[6,-14]}});b.create('point',[1,10],{name:'t=1',size:2,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',label:{offset:[-24,8]}});b.create('point',[5,10],{name:'t=5',size:2,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',label:{offset:[8,8]}});})();</script>

### AB I — Nullstellen, Extrempunkt, Skizze

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Nullstellen.** Wo ist \( f(t) = 0 \)? Man klammert \( t \) aus:

\[ f(t) = -2t^2 + 12t = -2t\,(t - 6). \]

Ein Produkt ist null, wenn ein Faktor null ist: \( -2t = 0 \Rightarrow t=0 \) oder \( t-6=0 \Rightarrow
t=6 \). **Nullstellen: \( t=0 \) und \( t=6 \).** Damit ist \( f(t)\ge 0 \) genau auf dem Intervall
\( [0;6] \) — das ist der Zeitraum, in dem überhaupt Wasser zufließt.

**Extrempunkt.** Der höchste Punkt ist dort, wo die Steigung \( 0 \) ist. Die Steigung liefert die
**Ableitung**:

\[ f'(t) = -4t + 12. \]

Nullsetzen: \( -4t + 12 = 0 \Rightarrow t = 3 \). Der Funktionswert dort:

\[ f(3) = -2\cdot 9 + 12\cdot 3 = -18 + 36 = 18. \]

Weil die Parabel wegen des Vorfaktors \( -2 \) nach unten geöffnet ist, ist das ein **Hochpunkt**.

**Ergebnis: Nullstellen \( t=0 \) und \( t=6 \); Hochpunkt \( H(3\,|\,18) \)** (maximale Zuflussrate
\( 18 \) Liter pro Stunde nach \( 3 \) Stunden).

**Skizze.** Eine nach unten geöffnete Parabel durch \( (0\,|\,0) \) und \( (6\,|\,0) \) mit Scheitel
\( (3\,|\,18) \) — siehe der blaue Graph oben.

<details><summary>Haltung dahinter: Nullstelle, Ableitung, Hochpunkt — was heißt das? (ganz von vorn)</summary>

**Funktion und Graph.** Eine **Funktion** ist eine Rechenvorschrift: man steckt eine Zahl \( t \)
hinein und bekommt eine Zahl \( f(t) \) heraus. Hier steht \( t \) für die Zeit und \( f(t) \) für das
Zufluss-Tempo. Trägt man alle Paare \( (t\mid f(t)) \) ins Koordinatensystem ein, entsteht der
**Graph** — hier eine **Parabel** (die typische „Bogen"-Kurve von \( t^2 \)-Termen).

**Nullstelle.** Eine **Nullstelle** ist eine Stelle, an der der Graph die waagerechte Achse trifft, wo
also \( f(t)=0 \) ist. Inhaltlich: Zufluss-Tempo \( 0 \) — bei \( t=0 \) geht's los, bei \( t=6 \) ist
der Zufluss versiegt.

**Satz vom Nullprodukt.** Wir nutzen: Ein **Produkt ist genau dann null, wenn ein Faktor null ist**.
Deshalb klammert man \( t \) aus und liest die Nullstellen direkt aus den beiden Faktoren ab.

**Ableitung und Hochpunkt.** Die **Ableitung** \( f'(t) \) gibt an jeder Stelle die **Steigung** des
Graphen an — wie stark er gerade steigt (positiv) oder fällt (negativ). Am höchsten Punkt der Parabel
ist der Graph für einen Moment **waagerecht**, die Steigung also \( 0 \). Darum setzt man \( f'(t)=0 \)
und löst nach \( t \) auf. Das Ableiten selbst folgt der Regel „Hochzahl nach vorne, Hochzahl um eins
kleiner": aus \( -2t^2 \) wird \( -4t \), aus \( 12t \) wird \( 12 \) (Details:
[Ableit-Handwerk](kap-ableiten-handwerk.html), Anwendung in
[Funktionsuntersuchung](kap-funktionsuntersuchung.html)).

<details><summary>Schneller Trick: der Scheitel liegt mittig zwischen den Nullstellen</summary>

Eine Parabel ist **symmetrisch**. Ihr Scheitel sitzt genau in der Mitte zwischen den beiden
Nullstellen \( 0 \) und \( 6 \), also bei \( t = \tfrac{0+6}{2} = 3 \). So findet man die Stelle des
Hochpunkts auch ohne Ableitung — und kann das Ergebnis \( t=3 \) gegenprüfen.

</details>
</details>
</details>

### AB II — Zufluss erste Stunde; mit Abfluss: Min/Max, Volumen nach 3 h, Verlauf

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**(1) Zugeflossenes Volumen in der ersten Stunde.** Eine **Rate** über die Zeit aufsummieren heißt
**integrieren**. Das Volumen der ersten Stunde ist

\[ V_{\text{zu}} = \int_0^1 f(t)\,dt = \int_0^1 \big(-2t^2 + 12t\big)\,dt. \]

Eine **Stammfunktion** von \( f \) ist \( F(t) = -\tfrac23 t^3 + 6t^2 \) (Ableiten kehrt das wieder um).
Mit dem Hauptsatz:

\[ \int_0^1 f(t)\,dt = \Big[-\tfrac23 t^3 + 6t^2\Big]_0^1 = \Big(-\tfrac23 + 6\Big) - 0
   = \tfrac{16}{3} \approx 5{,}33. \]

**Ergebnis: In der ersten Stunde fließen \( \tfrac{16}{3} \approx 5{,}33 \) Liter zu.**

<details><summary>Haltung dahinter: Warum berechnet ein Integral aus einer Rate ein Volumen? (ganz von vorn)</summary>

**Integral als Aufsummieren.** Ein **Integral** \( \int_a^b f(t)\,dt \) addiert die Funktionswerte
zwischen \( a \) und \( b \) auf — anschaulich die **Fläche unter dem Graphen**. Wenn \( f(t) \) ein
**Tempo** ist (Liter **pro Stunde**), dann ist „Tempo mal Zeit" eine **Menge** (Liter). Genau das tut
das Integral: Es multipliziert in unendlich vielen hauchdünnen Zeitstreifen „Rate × Zeitdauer" und
summiert alles. Bild: Beim Autofahren ist die Fläche unter der Geschwindigkeits-Kurve die gefahrene
**Strecke** — hier ist die Fläche unter der Zufluss-Kurve das zugeflossene **Wasser**.

**Stammfunktion.** Eine **Stammfunktion** \( F \) ist „Ableiten rückwärts": eine Funktion, deren
Ableitung wieder \( f \) ergibt (\( F' = f \)). Regel fürs Hochintegrieren: Hochzahl um eins
**erhöhen** und durch die neue Hochzahl **teilen**. Aus \( -2t^2 \) wird \( -2\cdot\tfrac{t^3}{3} =
-\tfrac23 t^3 \), aus \( 12t \) wird \( 12\cdot\tfrac{t^2}{2} = 6t^2 \). **Probe durch Ableiten:**
\( \big(-\tfrac23 t^3 + 6t^2\big)' = -2t^2 + 12t = f(t) \) ✓ (mehr:
[Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html)).

<details><summary>Ganz langsam (mit Zahlen): die Grenzen einsetzen</summary>

Der **Hauptsatz** sagt: \( \int_a^b f = F(b) - F(a) \) — oben einsetzen minus unten einsetzen.

- Obere Grenze \( t=1 \): \( -\tfrac23\cdot 1^3 + 6\cdot 1^2 = -\tfrac23 + 6 = \tfrac{16}{3} \).
- Untere Grenze \( t=0 \): \( -\tfrac23\cdot 0 + 6\cdot 0 = 0 \).
- Differenz: \( \tfrac{16}{3} - 0 = \tfrac{16}{3} \approx 5{,}33 \).

Zur Kontrolle: \( 6 = \tfrac{18}{3} \), also \( \tfrac{18}{3} - \tfrac{2}{3} = \tfrac{16}{3} \).

</details>
</details>

---

Ab jetzt gilt **zusätzlich** ein **konstanter Abfluss von \( 10 \) Liter pro Stunde seit Beginn**.
Die entscheidende Größe wird die **Netto-Rate** (Zufluss minus Abfluss):

\[ r(t) = f(t) - 10 = -2t^2 + 12t - 10. \]

Ist \( r(t) > 0 \), **steigt** der Wasserstand; ist \( r(t) < 0 \), **fällt** er.

**(2) Graphisch: Zeitpunkte von minimalem und maximalem Wasservolumen.** Das Volumen wechselt seine
Richtung dort, wo Zufluss = Abfluss, also \( f(t) = 10 \). Im Graphen oben ist das der **Schnitt der
blauen Kurve mit der grünen Linie** \( y=10 \) — abzulesen bei

\[ t = 1 \quad\text{und}\quad t = 5. \]

Vorzeichen der Netto-Rate ablesen:

- \( 0 \le t < 1 \): Kurve **unter** der Linie → Abfluss überwiegt → Volumen **fällt**.
- \( 1 < t < 5 \): Kurve **über** der Linie → Zufluss überwiegt → Volumen **steigt**.
- \( 5 < t \le 6 \): Kurve wieder **unter** der Linie → Volumen **fällt**.

**Ergebnis: minimales Wasservolumen bei \( t=1 \), maximales bei \( t=5 \).**

<details><summary>Haltung dahinter: Warum „Schnittpunkt = Wendepunkt des Wasserstands"?</summary>

Der **Wasserstand** ändert sich mit der **Netto-Rate** \( r(t) = f(t) - 10 \). Solange mehr zufließt
als abfließt (\( f > 10 \)), wird es voller; sobald mehr abfließt als zufließt (\( f < 10 \)), wird es
leerer. Der **Umschlagpunkt** ist genau dort, wo \( f = 10 \). Bild: ein Eimer mit Loch — solange der
Hahn stärker läuft als das Loch leckt, steigt der Pegel; kippt das Verhältnis, sinkt er. Die Stellen
\( t=1 \) und \( t=5 \) sind diese Kippmomente: bei \( t=1 \) der **Tiefststand**, bei \( t=5 \) der
**Höchststand**.

<details><summary>Rechnerische Kontrolle der Ablesung</summary>

\( f(t) = 10 \Rightarrow -2t^2+12t-10 = 0 \). Durch \( -2 \) teilen: \( t^2 - 6t + 5 = 0 \). Faktorisiert
\( (t-1)(t-5)=0 \), also \( t=1 \) und \( t=5 \) — genau die abgelesenen Werte. Damit ist
\( r(t) = -2(t-1)(t-5) \): negativ außerhalb \( [1;5] \), positiv dazwischen.

</details>
</details>

**(3) Rechnerisch: Wasservolumen nach \( 3 \) Stunden.** Das Volumen ist der Startwert \( 20 \) plus
die aufsummierte **Netto-Rate**:

\[ V(t) = 20 + \int_0^t \big(f(s) - 10\big)\,ds
       = 20 + \Big[-\tfrac23 s^3 + 6s^2 - 10s\Big]_0^t
       = 20 - \tfrac23 t^3 + 6t^2 - 10t. \]

Einsetzen von \( t=3 \):

\[ V(3) = 20 - \tfrac23\cdot 27 + 6\cdot 9 - 10\cdot 3 = 20 - 18 + 54 - 30 = 26. \]

**Ergebnis: Nach \( 3 \) Stunden enthält das Becken \( 26 \) Liter.**

<details><summary>Haltung dahinter: Was ist eine „Bestandsfunktion", und warum steht die 20 davor? (ganz von vorn)</summary>

**Rate vs. Bestand.** \( f \) (bzw. \( r \)) ist eine **Rate** (Tempo). Das **Volumen** \( V(t) \) ist
ein **Bestand** (die tatsächlich vorhandene Menge). Man kommt vom Tempo zum Bestand durch
**Aufsummieren über die Zeit** — also Integrieren. Ein Bankkonto-Bild: \( r(t) \) sind die
Ein-/Auszahlungen pro Stunde, \( V(t) \) ist der **Kontostand**.

**Warum der Startwert \( 20 \)?** Ein Integral von \( 0 \) bis \( t \) zählt nur die **Veränderung**
seit Beginn. Das Becken war aber nicht leer, sondern hatte schon \( 20 \) Liter. Deshalb addiert man
diesen **Anfangsbestand** dazu — wie das Startguthaben auf dem Konto, bevor die erste Buchung kommt.

**Warum \( r = f - 10 \)?** Zwei Dinge passieren gleichzeitig: Zufluss \( f(t) \) füllt auf, der feste
Abfluss \( 10 \) zieht ab. Die **echte** Veränderung pro Stunde ist die Differenz. Diese Differenz wird
integriert.

<details><summary>Ganz langsam (mit Zahlen): \( V(3) \) Ziffer für Ziffer</summary>

\[ V(3) = 20 \;\underbrace{-\tfrac23\cdot 27}_{=-18} \;\underbrace{+\,6\cdot 9}_{=+54}
   \;\underbrace{-\,10\cdot 3}_{=-30}. \]

- \( \tfrac23\cdot 27 = \tfrac{54}{3} = 18 \), mit Minus also \( -18 \).
- \( 6\cdot 9 = 54 \).
- \( 10\cdot 3 = 30 \), mit Minus also \( -30 \).
- Zusammen: \( 20 - 18 = 2 \); \( 2 + 54 = 56 \); \( 56 - 30 = 26 \).

Also \( V(3) = 26 \) Liter.

</details>

<details><summary>Typische Falle</summary>

Den Startwert \( 20 \) zu vergessen ist der häufigste Fehler — dann erhielte man \( 6 \) statt \( 26 \).
Ebenso falsch ist, nur den Zufluss \( f \) zu integrieren und den Abfluss zu vergessen. Es muss die
**Netto-Rate** \( f-10 \) sein, plus der **Anfangsbestand** \( 20 \).

</details>
</details>

**(4) Wasservolumen in Abhängigkeit von der Zeit (Beschreibung).** Die Bestandsfunktion ist

\[ V(t) = 20 - \tfrac23 t^3 + 6t^2 - 10t, \qquad t \in [0;6]. \]

Ihr Verlauf (siehe Graph unten): Start bei \( V(0)=20 \), Abfall bis zum **Tiefststand** bei \( t=1 \)
mit \( V(1) = \tfrac{46}{3} \approx 15{,}3 \), dann Anstieg bis zum **Höchststand** bei \( t=5 \) mit
\( V(5) = \tfrac{110}{3} \approx 36{,}7 \), danach wieder Abfall auf \( V(6) = 32 \).

<figure>
<div class="jxgbox" id="jxg-k7-v" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Wasservolumen \( V(t) = 20 - \tfrac23 t^3 + 6t^2 - 10t \) auf \( [0;6] \): Start \( 20 \), Minimum \( \approx 15{,}3 \) bei \( t=1 \), Maximum \( \approx 36{,}7 \) bei \( t=5 \), Endwert \( 32 \) bei \( t=6 \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k7-v',{boundingbox:[-1,42,7,-4],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 20-(2/3)*x*x*x+6*x*x-10*x;},0,6],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[0,20],{name:'Start 20',size:2,fixed:true,fillColor:'#3a5a9c',strokeColor:'#3a5a9c',label:{offset:[8,2]}});b.create('point',[1,46/3],{name:'Min t=1',size:2,fixed:true,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[6,-16]}});b.create('point',[5,110/3],{name:'Max t=5',size:2,fixed:true,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[-18,12]}});b.create('point',[6,32],{name:'t=6',size:2,fixed:true,fillColor:'#3a5a9c',strokeColor:'#3a5a9c',label:{offset:[6,8]}});})();</script>

<details><summary>Haltung dahinter: Wie liest man so einen Verlauf richtig vor?</summary>

Man beschreibt einen Verlauf in **Worten der Anschauung**: *wann* der Pegel fällt, *wann* er steigt,
*wo* die Wendepunkte (Tief- und Höchststand) liegen und *welche Werte* dort herauskommen. Die
„Drehpunkte" sind exakt die Stellen aus Teil (2): bei \( t=1 \) hört das Fallen auf (Minimum), bei
\( t=5 \) hört das Steigen auf (Maximum). Inhaltlich: In der ersten Stunde leert das Becken sich leicht
(der Zufluss ist noch schwach, der Abfluss von \( 10 \) gewinnt), danach füllt es sich kräftig, weil der
Zufluss bis \( 18 \) hochsteigt, und gegen Ende lässt der Zufluss nach, sodass der Abfluss wieder die
Oberhand bekommt.

<details><summary>Die Eckwerte mit Zahlen</summary>

- \( V(1) = 20 - \tfrac23 + 6 - 10 = 16 - \tfrac23 = \tfrac{46}{3} \approx 15{,}3 \) (Minimum).
- \( V(5) = 20 - \tfrac23\cdot 125 + 6\cdot 25 - 50 = 120 - \tfrac{250}{3} = \tfrac{110}{3} \approx 36{,}7 \) (Maximum).
- \( V(6) = 20 - \tfrac23\cdot 216 + 6\cdot 36 - 60 = 20 - 144 + 216 - 60 = 32 \).

Das Becken läuft also nie über und wird in diesem Zeitraum nie leer — der Tiefststand
\( \approx 15{,}3 \) Liter liegt deutlich über \( 0 \).

</details>
</details>
</details>

### AB III — Abfluss ab \( t=4 \) so ändern, dass das Becken bei \( t=6 \) leer ist

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Verfahren anzeigen</summary>

Gefragt ist die **Vorgehensweise** (mit \( t=4 \) ändert sich die Abflussrate auf einen neuen festen
Wert \( a \); bei \( t=6 \) soll das Becken leer sein, also \( V(6)=0 \)). Der Weg in drei Schritten —
das Ergebnis wird mitgerechnet.

**Schritt 1 — Wasserstand bei \( t=4 \) (noch mit altem Abfluss \( 10 \)).** Aus der Bestandsfunktion
von oben:

\[ V(4) = 20 - \tfrac23\cdot 64 + 6\cdot 16 - 40 = 76 - \tfrac{128}{3} = \tfrac{100}{3} \approx 33{,}3 \ \text{Liter}. \]

**Schritt 2 — Bilanz von \( t=4 \) bis \( t=6 \) aufstellen.** In diesen \( 2 \) Stunden kommt der
Zufluss \( \int_4^6 f(t)\,dt \) hinzu und der **neue** Abfluss \( a \) zieht \( a\cdot 2 \) ab. Der
Zufluss-Anteil:

\[ \int_4^6 f(t)\,dt = \Big[-\tfrac23 t^3 + 6t^2\Big]_4^6
   = \big(-144 + 216\big) - \Big(-\tfrac{128}{3} + 96\Big)
   = 72 - \tfrac{160}{3} = \tfrac{56}{3} \approx 18{,}7. \]

**Schritt 3 — Bedingung \( V(6)=0 \) lösen.**

\[ V(6) = \underbrace{\tfrac{100}{3}}_{V(4)} + \underbrace{\tfrac{56}{3}}_{\text{Zufluss}} - 2a = 0
   \;\;\Longrightarrow\;\; \tfrac{156}{3} - 2a = 0 \;\;\Longrightarrow\;\; 52 = 2a \;\;\Longrightarrow\;\; a = 26. \]

**Ergebnis: Ab \( t=4 \) muss der Abfluss auf \( 26 \) Liter pro Stunde erhöht werden, damit das Becken
bei \( t=6 \) leer ist.**

So sieht der Wasserstand mit dieser Umstellung aus (Knick bei \( t=4 \), null bei \( t=6 \)):

<figure>
<div class="jxgbox" id="jxg-k7-ab3" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Wasservolumen mit Abflusswechsel: bis \( t=4 \) wie zuvor (\( V(4)=\tfrac{100}{3}\approx 33{,}3 \)), ab \( t=4 \) stärkerer Abfluss \( 26 \) — der Pegel fällt geradlinig-konvex bis \( V(6)=0 \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k7-ab3',{boundingbox:[-1,42,7,-6],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){if(x<=4){return 20-(2/3)*x*x*x+6*x*x-10*x;}else{return -(2/3)*x*x*x+6*x*x-26*x+84;}},0,6],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[4,100/3],{name:'t=4 Umstellung',size:2,fixed:true,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[-30,14]}});b.create('point',[6,0],{name:'t=6 leer',size:2,fixed:true,fillColor:'#b03a2e',strokeColor:'#b03a2e',label:{offset:[6,-12]}});})();</script>

<details><summary>Haltung dahinter: Warum diese „Bilanz" das Problem löst (ganz von vorn)</summary>

**Bilanz-Idee.** Wir fragen: Wie viel Wasser ist bei \( t=4 \) da, und wie viel muss in den restlichen
\( 2 \) Stunden **netto** verschwinden, damit am Ende \( 0 \) übrig bleibt? Alles, was bei \( t=4 \) im
Becken ist (\( \tfrac{100}{3} \)) **plus** alles, was bis \( t=6 \) noch zufließt (\( \tfrac{56}{3} \)),
muss durch den neuen Abfluss wieder hinaus. Zusammen sind das \( \tfrac{156}{3} = 52 \) Liter in
\( 2 \) Stunden → \( 52 \div 2 = 26 \) Liter pro Stunde.

**Warum nur der Abfluss konstant ist.** Der Zufluss \( f \) bleibt die vorgegebene Kurve; geändert
wird nur die feste Abflussrate. Deshalb taucht der Zufluss als **Integral** auf (er ändert sich mit der
Zeit), der Abfluss aber als **\( a \cdot \) Zeitdauer** (konstantes Tempo mal \( 2 \) Stunden).

<details><summary>Ganz langsam (mit Zahlen): die zweite Integralgrenze</summary>

\( \int_4^6 f\,dt = F(6) - F(4) \) mit \( F(t) = -\tfrac23 t^3 + 6t^2 \):

- \( F(6) = -\tfrac23\cdot 216 + 6\cdot 36 = -144 + 216 = 72 \).
- \( F(4) = -\tfrac23\cdot 64 + 6\cdot 16 = -\tfrac{128}{3} + 96 = \tfrac{-128+288}{3} = \tfrac{160}{3} \).
- Differenz: \( 72 - \tfrac{160}{3} = \tfrac{216-160}{3} = \tfrac{56}{3} \approx 18{,}7 \).

Bilanz: \( \tfrac{100}{3} + \tfrac{56}{3} = \tfrac{156}{3} = 52 \). Geteilt durch \( 2 \) Stunden:
\( a = 26 \) Liter pro Stunde.

</details>

<details><summary>Kontrolle: bleibt das Becken bis \( t=6 \) wirklich gefüllt (nie vorher leer)?</summary>

Ab \( t=4 \) ist die neue Netto-Rate \( f(t) - 26 \). Da der Zufluss nie über \( 18 \) steigt, ist
\( f(t) - 26 < 0 \) für alle \( t \in [4;6] \) — der Pegel fällt **durchgehend**. Er erreicht \( 0 \)
also frühestens am Ende, und unsere Rechnung legt diesen Punkt genau auf \( t=6 \). Das Becken läuft
nicht vorzeitig leer; die Lösung ist physikalisch sinnvoll. (Würde \( 26 \) das Becken zu schnell
leeren, käme \( V \) schon vor \( t=6 \) bei \( 0 \) an — hier passt es exakt.)

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 2 (erst nach dem eigenen Versuch aufklappen)</summary>

- AB I: Nullstellen \( t=0;\,6 \); Hochpunkt \( (3\,|\,18) \); Parabel nach unten geöffnet.
- AB II (1): \( \int_0^1 f = \tfrac{16}{3} \approx 5{,}33 \) Liter in der ersten Stunde.
- AB II (2): Min bei \( t=1 \), Max bei \( t=5 \) (dort \( f=10 \), Netto-Rate wechselt das Vorzeichen).
- AB II (3): \( V(t) = 20 - \tfrac23 t^3 + 6t^2 - 10t \); \( V(3) = 26 \) Liter.
- AB II (4): Start \( 20 \) → Min \( \approx 15{,}3 \) (t=1) → Max \( \approx 36{,}7 \) (t=5) → \( 32 \) (t=6).
- AB III: \( V(4)=\tfrac{100}{3} \), \( \int_4^6 f = \tfrac{56}{3} \); aus \( \tfrac{156}{3} - 2a = 0 \) folgt \( a = 26 \) Liter pro Stunde.

</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Teilaufgabe, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen
kannst. Du musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Geometrie) aufklappen</summary>

- **a) Punktprobe.** Erwartet: **Richtungsvektor** \( \overrightarrow{AB}=(2,-1,2) \) bilden und zeigen,
  dass der Pfeil von \( C \) zu \( A \) **das gleiche** (ein Vielfaches) ist → \( C \) liegt auf \( g \).
  *Rote Flagge:* nur **eine** Koordinate verglichen. *Rückfrage:* „Warum müssen alle drei Zeilen passen?"
- **b) Ebene.** Erwartet: \( A \) **und** \( B \) in \( x_1+2x_2=4 \) einsetzen (\( 4=4 \), \( 4=4 \)) und
  daraus „zwei Punkte drin → ganze Gerade drin" folgern. Für die weitere Ebene: einen zweiten
  Spannvektor (z. B. \( (1,1,1) \)) angeben, der **nicht parallel** zur Geraden ist. *Rückfrage:*
  „Warum reicht es, zwei Punkte zu prüfen?"
- **c) Punkt D.** Erwartet: \( |\overrightarrow{AB}| = \sqrt 9 = 3 \), also \( 9 = 3\cdot 3 \Rightarrow
  t=3 \Rightarrow D(8\,|\,-2\,|\,6) \). *Rote Flagge:* \( 9\cdot\overrightarrow{AB} \) statt
  \( 3\cdot\overrightarrow{AB} \). *Rückfrage:* „Wie lang ist ein Schritt entlang der Geraden?"
- **d) Verfahren.** Erwartet als **beschriebener Weg**: Mittelpunkt \( M \) von \( \overline{AB} \) →
  zu \( \overrightarrow{AB} \) senkrechten Vektor wählen → \( P \) auf der Mittelsenkrechten so legen,
  dass \( |\overline{AP}| = |\overline{AB}| \). *Hinweis für dich:* Hier ist **kein** Zahlenergebnis
  nötig — ein klar beschriebenes Verfahren ist die volle Antwort. *Rückfrage:* „Warum ist \( P \) auf
  der Mittelsenkrechten automatisch von \( A \) und \( B \) gleich weit weg?"

</details>

<details><summary>Leitfaden Teil 2 (Analysis) aufklappen</summary>

- **AB I — Nullstellen/Extrempunkt/Skizze.** Erwartet: \( t \) ausklammern → Nullstellen \( 0 \) und
  \( 6 \); Ableitung null setzen → \( t=3 \), \( f(3)=18 \), Hochpunkt; Parabel nach unten. *Rückfrage:*
  „Woran sieht man, dass es ein Hoch- und kein Tiefpunkt ist?" (Antwort: Vorfaktor \( -2 \).)
- **AB II — Zufluss erste Stunde.** Erwartet: **Integral** \( \int_0^1 f \), Stammfunktion
  \( -\tfrac23 t^3 + 6t^2 \), Ergebnis \( \tfrac{16}{3}\approx 5{,}33 \) Liter. *Rückfrage:* „Warum
  Integral und nicht einfach \( f(1) \) einsetzen?" (Rate vs. Menge.)
- **AB II — Min/Max graphisch.** Erwartet: Linie \( y=10 \) und Schnittpunkte mit \( f \) bei \( t=1 \)
  und \( t=5 \); davor/dazwischen/danach das Vorzeichen der Netto-Rate. Min bei \( t=1 \), Max bei
  \( t=5 \). *Rückfrage:* „Was bedeutet der Schnittpunkt von Zufluss und Abfluss für den Pegel?"
- **AB II — Volumen nach 3 h.** Erwartet: \( V(t)=20 - \tfrac23 t^3 + 6t^2 - 10t \), \( V(3)=26 \).
  *Rote Flagge:* Startwert \( 20 \) vergessen (gäbe \( 6 \)) oder Abfluss vergessen. *Rückfrage:*
  „Woher kommt die \( 20 \) am Anfang?"
- **AB II — Verlauf beschreiben.** Erwartet: Start \( 20 \), Tief bei \( t=1 \) (\( \approx 15{,}3 \)),
  Hoch bei \( t=5 \) (\( \approx 36{,}7 \)), Ende \( 32 \). *Rückfrage:* „Wann leert sich das Becken,
  wann füllt es sich?"
- **AB III — Abfluss anpassen.** Erwartet als **erläutertes Verfahren**: Stand bei \( t=4 \) bestimmen,
  Zufluss \( \int_4^6 f \) addieren, neuen Abfluss \( a \) über die Bilanz \( V(6)=0 \) lösen →
  \( a=26 \) Liter pro Stunde. *Hinweis für dich:* Verlangt ist die **Vorgehensweise**; nennt die
  Person zusätzlich \( 26 \), ist das ein starkes Plus. *Rückfrage:* „Was muss bis \( t=6 \) insgesamt
  abfließen?"

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Wie prüfst du, ob ein Punkt auf einer Geraden liegt — und warum reicht **eine** Koordinate nicht?
- Warum genügt es, **zwei** Punkte einzusetzen, um zu zeigen, dass eine ganze Gerade in einer Ebene liegt?
- Wie kommst du von „Abstand \( 9 \)" zum richtigen Parameter \( t \) auf der Geraden?
- Warum löst die Mittelsenkrechte die Aufgabe mit dem gleichseitigen Dreieck?
- Was ist der Unterschied zwischen der Zuflussrate \( f(t) \) und dem Wasservolumen \( V(t) \) — und wie kommt man vom einen zum anderen?
- Warum liegen das minimale und maximale Wasservolumen genau dort, wo Zufluss und Abfluss gleich groß sind?
