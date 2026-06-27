# Aufgabe 8 — Geometrie & Analysis

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Geometrie**, **Teil 2 (Gespräch) aus der Analysis**. Alles ist
**rechnerfrei** zu lösen — wo ein Zahlenwert eines Winkels auftaucht, genügt der exakte Ausdruck
(z. B. \( \cos\alpha = \tfrac{1}{\sqrt5} \)), der Dezimalwert ist Nebensache. Arbeitet die Aufgabe wie
eine echte Simulation durch — eine Person trägt vor, die andere prüft mit dem Lösungsweg und dem
[Prüfer-Leitfaden](#prufer-leitfaden-fur-die-abfragende-person) am Ende mit.

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
> Vektoren, Länge, Skalarprodukt, Normalenvektor, Ebenengleichung, Schnittwinkel) stehen kompakt im
> [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html) (u. a.
> [Skalarprodukt](konv-90-werkzeugkasten-geometrie.html#skalarprodukt)). Die Analysis-Werkzeuge für
> Teil 2 findest du in den Kapiteln [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Funktionsuntersuchung](kap-funktionsuntersuchung.html),
> [Integral-Grundlagen](kap-integral-grundlagen.html) und
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).

---

## Teil 1 — Vortrag (Geometrie): Spiegelebene, Ebene zeichnen, Schnittwinkel

<div class="aufgabenkasten">

**a)** Gegeben sind die Punkte \( A(2\,|\,3\,|\,-2) \) und \( B(0\,|\,1\,|\,6) \). Bestimme die
Koordinaten des **Mittelpunkts der Strecke \( AB \)**. \( A \) und \( B \) liegen **spiegelbildlich
bezüglich einer Ebene \( E \)**. Bestimme eine **Koordinatengleichung von \( E \)**.

**Gegeben ist die Ebene \( F:\ 2x_1 + x_2 = 4 \).**

**b)** **Skizziere die Ebene \( F \)** im Koordinatensystem. Ermittle eine **Gleichung der Geraden**,
die sowohl in \( F \) als auch in der \( x_1x_2 \)-Ebene liegt.

**c)** Berechne die **Größe des Winkels**, unter dem \( F \) die \( x_1x_3 \)-Ebene schneidet. Durch
Ersetzen des Koeffizienten \( 2 \) in der Ebenengleichung von \( F \) durch eine reelle Zahl \( a \)
mit \( a\neq 0 \) verändert sich der Schnittwinkel der Ebene mit der \( x_1x_3 \)-Ebene. Bestimme einen
**Wert von \( a \)**, für den dieser Schnittwinkel \( 45^\circ \) groß ist. Untersuche, **welche Größe**
dieser Schnittwinkel für \( a\neq 0 \) annehmen kann.

</div>

> **Vorab, in einem Satz, was ein Koordinatensystem im Raum ist:** Statt nur „rechts/links" und
> „oben/unten" (zwei Zahlen) braucht man im Raum **drei** Zahlen pro Punkt — \( (x_1 \mid x_2 \mid x_3) \)
> —, weil es zusätzlich „vorne/hinten" gibt. Ein Punkt wie \( A(2\,|\,3\,|\,-2) \) heißt: 2 Schritte in
> \( x_1 \)-Richtung, 3 in \( x_2 \), 2 **zurück** in \( x_3 \) (das Minus). Alle Vektor-Werkzeuge stehen
> kompakt im [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html).

### Teilaufgabe a) — Mittelpunkt und Spiegelebene

<span class="tag tag-ok">AB I — Grundkompetenz</span> &nbsp;
<span class="tag tag-warn">AB II — Standardanforderung</span>

So liegen die beiden Punkte zur gesuchten Spiegelebene (schematisch, „von der Seite" betrachtet):

<figure>
<svg viewBox="0 0 480 300" role="img" aria-label="Schema: A und B liegen spiegelbildlich zur Ebene E, M ist der Mittelpunkt von AB" style="width:100%;max-width:480px;height:auto;background:#fbf7ef;border-radius:8px">
  <defs><marker id="k8ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#7a7163"/></marker></defs>
  <line x1="240" y1="40" x2="240" y2="252" stroke="#3a5a9c" stroke-width="2.4"/>
  <text x="248" y="54" font-size="13" fill="#3a5a9c" font-weight="bold">Ebene E (Spiegel)</text>
  <line x1="95" y1="150" x2="385" y2="150" stroke="#26324a" stroke-width="1.6"/>
  <path d="M240,134 L256,134 L256,150" fill="none" stroke="#7a7163" stroke-width="1.2"/>
  <circle cx="95" cy="150" r="4.5" fill="#d98324"/><text x="62" y="139" font-size="12" fill="#26324a">A(2|3|−2)</text>
  <circle cx="385" cy="150" r="4.5" fill="#d98324"/><text x="352" y="139" font-size="12" fill="#26324a">B(0|1|6)</text>
  <circle cx="240" cy="150" r="3.8" fill="#3a5a9c"/><text x="216" y="172" font-size="12" fill="#26324a">M(1|2|2)</text>
  <text x="142" y="143" font-size="11.5" fill="#3a8a5a">gleich weit</text>
  <text x="282" y="143" font-size="11.5" fill="#3a8a5a">gleich weit</text>
  <path d="M118,178 C180,210 300,210 362,178" fill="none" stroke="#b03a2e" stroke-width="1.3" stroke-dasharray="4 3" marker-end="url(#k8ah)"/>
  <text x="172" y="230" font-size="12" fill="#b03a2e">Spiegelung an E bildet A auf B ab</text>
</svg>
<figcaption>Die Spiegelebene \( E \) steht senkrecht auf \( AB \) und geht genau durch den Mittelpunkt \( M \).</figcaption>
</figure>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Schritt 1 — Mittelpunkt \( M \) der Strecke \( AB \).** Den Mittelpunkt bekommt man, indem man die
Ortsvektoren der Endpunkte addiert und halbiert:

\[ \overrightarrow{OM} = \tfrac12\big(\overrightarrow{OA} + \overrightarrow{OB}\big)
   = \tfrac12\left(\begin{pmatrix}2\\3\\-2\end{pmatrix} + \begin{pmatrix}0\\1\\6\end{pmatrix}\right)
   = \tfrac12\begin{pmatrix}2\\4\\4\end{pmatrix}
   = \begin{pmatrix}1\\2\\2\end{pmatrix},
   \qquad \text{also } M(1\,|\,2\,|\,2). \]

**Schritt 2 — Normalenvektor der Spiegelebene.** Spiegelt man \( A \) an der Ebene \( E \) und landet
genau auf \( B \), dann steht die Verbindung \( \overrightarrow{AB} \) **senkrecht** auf \( E \) — sie
ist ein **Normalenvektor**:

\[ \overrightarrow{AB} = B - A = \begin{pmatrix}0-2\\1-3\\6-(-2)\end{pmatrix} = \begin{pmatrix}-2\\-2\\8\end{pmatrix}. \]

Man darf diesen Vektor durch \( -2 \) teilen — das ändert nur die Länge, nicht die Richtung:

\[ \vec n = \begin{pmatrix}1\\1\\-4\end{pmatrix}. \]

**Schritt 3 — Koordinatengleichung aufstellen.** Mit dem Normalenvektor steht die linke Seite fest:
\( x_1 + x_2 - 4x_3 = d \). Die rechte Zahl \( d \) findet man, indem man einen bekannten Ebenenpunkt
einsetzt — \( E \) geht durch \( M(1|2|2) \):

\[ 1 + 2 - 4\cdot 2 = 3 - 8 = -5. \]

\[ \boxed{\,E:\ x_1 + x_2 - 4x_3 = -5\,} \]

<details><summary>Haltung dahinter: Was ist ein Vektor, und warum ist der Mittelpunkt der „Durchschnitt"? (ganz von vorn)</summary>

Ganz langsam, ohne Vorwissen.

**Punkt und Ortsvektor.** Ein **Punkt** ist ein Ort im Raum, festgelegt durch drei Zahlen
\( (x_1\mid x_2\mid x_3) \). Den **Ortsvektor** \( \overrightarrow{OA} \) kann man sich als Pfeil vom
Ursprung \( O(0|0|0) \) zum Punkt \( A \) vorstellen; seine drei Zahlen sind genau die Koordinaten von
\( A \). Rechnen tut man mit den drei Zahlen einzeln (Zeile für Zeile).

**Mittelpunkt = Durchschnitt zweier Orte.** Der Punkt genau zwischen zwei Orten liegt bei ihrem
**Durchschnitt**: addieren und durch zwei teilen. Bei einer einzelnen Zahl ist der Wert zwischen
\( 2 \) und \( 0 \) genau \( \tfrac{2+0}{2}=1 \). Im Raum macht man das einfach für alle drei
Koordinaten gleichzeitig.

<details><summary>… ganz langsam (mit Zahlen)</summary>

\( A=(2,3,-2) \), \( B=(0,1,6) \). Erst Zeile für Zeile addieren:

- \( x_1 \): \( 2+0 = 2 \)
- \( x_2 \): \( 3+1 = 4 \)
- \( x_3 \): \( -2 + 6 = 4 \) (eine Schuld von 2 plus ein Guthaben von 6 ergibt 4)

Das ergibt \( (2,4,4) \). Jetzt halbieren (jede Zahl durch 2): \( (1,2,2) \). Also \( M(1\,|\,2\,|\,2) \).

</details>
</details>

<details><summary>Haltung dahinter: Warum ist \( \overrightarrow{AB} \) der Normalenvektor, und woher kommt das \( d=-5 \)?</summary>

Das ist der Kern dieser Aufgabe, deshalb wirklich Stück für Stück.

**Was heißt „spiegelbildlich bezüglich \( E \)"?** Stell dir \( E \) als senkrechten Spiegel vor.
Spiegelt man Punkt \( A \) daran, landet er bei \( B \). Bei einem Spiegel gilt immer zweierlei: (1) Der
Spiegel steht **senkrecht** auf der Verbindungslinie zwischen Original und Spiegelbild. (2) Der Spiegel
schneidet diese Linie **genau in der Mitte** (Original und Bild sind gleich weit vom Spiegel entfernt).
Genau diese beiden Tatsachen liefern uns alles, was wir brauchen.

**Vektor \( \overrightarrow{AB} \) als „Ziel minus Start".** Den Pfeil von \( A \) nach \( B \) rechnet
man als \( B - A \), Zeile für Zeile. Aus Punkt 1 oben (Spiegel senkrecht zur Verbindung) folgt: dieser
Pfeil steht senkrecht auf \( E \) — er ist ein **Normalenvektor** (ein Pfeil, der wie ein Fahnenmast
senkrecht aus der Ebene ragt).

**Was bringt der Normalenvektor?** Eine **Koordinatengleichung** einer Ebene hat die Form
\( n_1 x_1 + n_2 x_2 + n_3 x_3 = d \). Das Schöne: Die drei Zahlen des Normalenvektors sind **genau** die
Koeffizienten \( n_1, n_2, n_3 \) vor den \( x \). Kennt man den Normalenvektor, ist die linke Seite
fertig — es fehlt nur noch die einzelne Zahl \( d \) auf der rechten Seite.

**Warum darf man durch \( -2 \) teilen?** Ein Normalenvektor zeigt nur eine **Richtung** an; seine Länge
ist egal. \( (-2,-2,8) \) und \( (1,1,-4) \) zeigen in dieselbe Richtung (alle Zahlen durch \( -2 \)
geteilt). Die kürzeren Zahlen rechnen sich angenehmer.

<details><summary>… ganz langsam (mit Zahlen): wie kommt \( d=-5 \) heraus?</summary>

Aus Punkt 2 oben (Spiegel durch die Mitte) wissen wir: \( E \) geht durch \( M(1|2|2) \). Die Gleichung
\( x_1 + x_2 - 4x_3 = d \) muss also stimmen, wenn man die Koordinaten von \( M \) einsetzt. Einsetzen:

\[ \underbrace{1}_{x_1} + \underbrace{2}_{x_2} - 4\cdot \underbrace{2}_{x_3}. \]

Zuerst \( 4\cdot 2 = 8 \). Dann \( 1 + 2 = 3 \). Dann \( 3 - 8 = -5 \) (man schuldet mehr, als man hat,
deshalb negativ). Also \( d = -5 \) und \( E:\ x_1 + x_2 - 4x_3 = -5 \).

</details>

<details><summary>Typische Falle</summary>

Zwei Stolperstellen. Erstens das **Vorzeichen** im Mittelpunkt: \( -2 + 6 = 4 \), nicht \( -8 \) oder
\( 8 \) — Plus und Minus sauber verrechnen. Zweitens den **Punkt für \( d \)**: Man muss \( M \)
einsetzen (den Mittelpunkt, der wirklich auf der Ebene liegt), **nicht** \( A \) oder \( B \) — die
liegen ja gerade *nicht* auf dem Spiegel, sondern davor und dahinter.

</details>
</details>
</details>

### Teilaufgabe b) — Ebene \( F \) zeichnen und Schnittgerade mit der \( x_1x_2 \)-Ebene

<span class="tag tag-ok">AB I — Grundkompetenz</span> &nbsp;
<span class="tag tag-warn">AB II — Standardanforderung</span>

So sieht die Ebene \( F:\ 2x_1+x_2=4 \) im Koordinatensystem aus (schematisches Schrägbild):

<figure>
<svg viewBox="0 0 470 340" role="img" aria-label="Schrägbild der Ebene F, die senkrecht über der Spurgeraden durch S1(2|0|0) und S2(0|4|0) steht" style="width:100%;max-width:480px;height:auto;background:#fbf7ef;border-radius:8px">
  <defs><marker id="k8bh" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#7a7163"/></marker></defs>
  <line x1="180" y1="240" x2="180" y2="48"  stroke="#7a7163" stroke-width="1.5" marker-end="url(#k8bh)"/>
  <line x1="180" y1="240" x2="432" y2="240" stroke="#7a7163" stroke-width="1.5" marker-end="url(#k8bh)"/>
  <line x1="180" y1="240" x2="68"  y2="322" stroke="#7a7163" stroke-width="1.5" marker-end="url(#k8bh)"/>
  <text x="166" y="46"  font-size="13" fill="#7a7163">x₃</text>
  <text x="436" y="244" font-size="13" fill="#7a7163">x₂</text>
  <text x="56"  y="328" font-size="13" fill="#7a7163">x₁</text>
  <polygon points="144,266 300,240 300,128 144,154" fill="#3a5a9c" fill-opacity="0.12" stroke="#3a5a9c" stroke-width="1.6"/>
  <line x1="144" y1="266" x2="300" y2="240" stroke="#d98324" stroke-width="2.6"/>
  <circle cx="144" cy="266" r="3.8" fill="#3a5a9c"/><text x="92" y="284" font-size="12" fill="#26324a">S₁(2|0|0)</text>
  <circle cx="300" cy="240" r="3.8" fill="#3a5a9c"/><text x="306" y="236" font-size="12" fill="#26324a">S₂(0|4|0)</text>
  <text x="214" y="120" font-size="14" fill="#3a5a9c" font-weight="bold">F</text>
  <text x="120" y="306" font-size="12" fill="#d98324">Schnittgerade g</text>
</svg>
<figcaption>\( F \) enthält kein \( x_3 \), steht also senkrecht über ihrer Spurgeraden \( g \) und verläuft parallel zur \( x_3 \)-Achse.</figcaption>
</figure>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Schritt 1 — \( F \) verstehen und zeichnen.** In \( F:\ 2x_1 + x_2 = 4 \) kommt **kein \( x_3 \)** vor.
Das bedeutet: \( x_3 \) darf jeden Wert haben — die Ebene läuft **parallel zur \( x_3 \)-Achse** (sie
steht „senkrecht" über einer Linie am Boden). Zum Zeichnen reichen die beiden **Spurpunkte** in der
Grundebene:

- Schnitt mit der \( x_1 \)-Achse \( (x_2 = 0,\ x_3 = 0) \): \( 2x_1 = 4 \Rightarrow x_1 = 2 \), also
  \( S_1(2\,|\,0\,|\,0) \).
- Schnitt mit der \( x_2 \)-Achse \( (x_1 = 0,\ x_3 = 0) \): \( x_2 = 4 \), also \( S_2(0\,|\,4\,|\,0) \).

Durch \( S_1 \) und \( S_2 \) zieht man die **Spurgerade** und „klappt" die Ebene als senkrechte Wand
nach oben (siehe Bild).

**Schritt 2 — Gerade, die in \( F \) **und** in der \( x_1x_2 \)-Ebene liegt.** Die \( x_1x_2 \)-Ebene
ist der Boden \( (x_3 = 0) \). Die gesuchte Gerade liegt in beiden Flächen — das ist genau die
Spurgerade durch \( S_1 \) und \( S_2 \). Man schreibt sie als **Stützpunkt plus Richtungsvektor**:

\[ \overrightarrow{S_1S_2} = S_2 - S_1 = \begin{pmatrix}0-2\\4-0\\0-0\end{pmatrix} = \begin{pmatrix}-2\\4\\0\end{pmatrix}, \]

\[ \boxed{\,g:\ \vec x = \begin{pmatrix}2\\0\\0\end{pmatrix} + t\begin{pmatrix}-2\\4\\0\end{pmatrix},\quad t\in\mathbb{R}\,} \]

<details><summary>Haltung dahinter: Wieso ist \( 2x_1+x_2=4 \) eine ganze Ebene und keine Gerade?</summary>

Das verwirrt oft, deshalb langsam.

**Im Raum braucht man drei Koordinaten.** Eine Gleichung mit \( x_1, x_2, x_3 \) schränkt die erlaubten
Punkte ein. Eine **einzige** Gleichung lässt noch eine ganze **Fläche** zu (eine Ebene), erst **zwei**
Gleichungen zusammen ergeben eine **Linie** (Gerade).

**Warum die Ebene hier „steht".** In \( 2x_1 + x_2 = 4 \) fehlt \( x_3 \). Über jedem Punkt der
Bodenlinie \( 2x_1+x_2=4 \) ist also **jede Höhe** \( x_3 \) erlaubt. Stapelt man alle diese Höhen
übereinander, entsteht eine senkrechte **Wand**. Bild: ein Bauzaun, der einer Linie auf dem Boden folgt
und beliebig hoch sein darf.

**Spurpunkt = wo die Ebene eine Achse durchstößt.** Setzt man zwei der drei Koordinaten null, landet
man auf einer Achse; die Gleichung verrät dann den dritten Wert. So findet man \( S_1 \) und \( S_2 \)
mit ganz wenig Rechnung.

<details><summary>… ganz langsam (mit Zahlen): die beiden Spurpunkte</summary>

Für \( S_1 \) auf der \( x_1 \)-Achse setze \( x_2=0 \): aus \( 2x_1 + 0 = 4 \) wird \( 2x_1 = 4 \),
also \( x_1 = \tfrac{4}{2} = 2 \) → \( S_1(2|0|0) \). Für \( S_2 \) auf der \( x_2 \)-Achse setze
\( x_1=0 \): aus \( 2\cdot 0 + x_2 = 4 \) wird \( x_2 = 4 \) → \( S_2(0|4|0) \). Probe für die Gerade:
Setzt man \( t=0 \), erhält man \( S_1(2|0|0) \); setzt man \( t=1 \), erhält man
\( (2,0,0)+(-2,4,0) = (0,4,0) = S_2 \). Beide gewünschten Punkte liegen also auf \( g \). ✓

</details>

<details><summary>Typische Falle</summary>

\( F \) für eine Gerade zu halten, weil die Gleichung „so einfach" aussieht. Im Raum ist eine einzelne
lineare Gleichung **immer** eine Ebene. Und der **Richtungsvektor** der Schnittgeraden ist
\( S_2 - S_1 = (-2,4,0) \), nicht \( S_1 - S_2 = (2,-4,0) \) — beide zeigen zwar entlang derselben
Geraden, aber achte beim Aufschreiben darauf, welchen Stützpunkt du nimmst (hier \( S_1 \)).

</details>
</details>
</details>

### Teilaufgabe c) — Schnittwinkel mit der \( x_1x_3 \)-Ebene

<span class="tag tag-ok">AB I — Grundkompetenz</span> &nbsp;
<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

Schaut man von oben auf den Boden (Blick entlang der \( x_3 \)-Achse), erscheinen beide Ebenen als
Linien — und der Winkel zwischen diesen Linien **ist** der gesuchte Schnittwinkel:

<figure>
<svg viewBox="0 0 430 300" role="img" aria-label="Draufsicht: Spur von F und Spur der x1x3-Ebene schneiden sich unter etwa 63,4 Grad" style="width:100%;max-width:440px;height:auto;background:#fbf7ef;border-radius:8px">
  <defs><marker id="k8ch" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#7a7163"/></marker></defs>
  <line x1="60" y1="250" x2="402" y2="250" stroke="#7a7163" stroke-width="1.5" marker-end="url(#k8ch)"/>
  <line x1="60" y1="250" x2="60"  y2="42"  stroke="#7a7163" stroke-width="1.5" marker-end="url(#k8ch)"/>
  <text x="406" y="254" font-size="13" fill="#7a7163">x₁</text>
  <text x="46"  y="44"  font-size="13" fill="#7a7163">x₂</text>
  <text x="232" y="268" font-size="11.5" fill="#7a7163">Spur der x₁x₃-Ebene (x₂=0)</text>
  <line x1="156" y1="250" x2="60" y2="58" stroke="#3a5a9c" stroke-width="2.6"/>
  <circle cx="156" cy="250" r="3.8" fill="#3a5a9c"/><text x="150" y="270" font-size="12" fill="#26324a">S₁(2|0)</text>
  <circle cx="60" cy="58" r="3.8" fill="#3a5a9c"/><text x="68" y="56" font-size="12" fill="#26324a">S₂(0|4)</text>
  <text x="96" y="150" font-size="12" fill="#3a5a9c" font-weight="bold">Spur von F</text>
  <path d="M126,250 A30,30 0 0 1 143,223" fill="none" stroke="#b03a2e" stroke-width="1.8"/>
  <text x="86" y="232" font-size="12" fill="#b03a2e" font-weight="bold">≈ 63,4°</text>
</svg>
<figcaption>Beide Ebenen stehen senkrecht (enthalten die \( x_3 \)-Richtung); deshalb zeigt die Draufsicht den Schnittwinkel direkt.</figcaption>
</figure>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Schritt 1 — Normalenvektoren beider Ebenen.** Der Winkel zwischen zwei Ebenen ist der Winkel
zwischen ihren Normalenvektoren.

- \( F:\ 2x_1 + x_2 = 4 \) hat den Normalenvektor \( \vec n_F = \begin{pmatrix}2\\1\\0\end{pmatrix} \).
- Die \( x_1x_3 \)-Ebene ist \( x_2 = 0 \); ihr Normalenvektor ist
  \( \vec n_2 = \begin{pmatrix}0\\1\\0\end{pmatrix} \) (sie steht senkrecht zur \( x_2 \)-Richtung).

**Schritt 2 — Winkel über das Skalarprodukt.**

\[ \cos\alpha = \frac{\big|\vec n_F \cdot \vec n_2\big|}{|\vec n_F|\,\cdot\,|\vec n_2|}
   = \frac{\left|\,2\cdot 0 + 1\cdot 1 + 0\cdot 0\,\right|}{\sqrt{2^2+1^2+0^2}\,\cdot\,\sqrt{0^2+1^2+0^2}}
   = \frac{1}{\sqrt5\,\cdot\,1} = \frac{1}{\sqrt5}. \]

\[ \boxed{\,\alpha = \arccos\!\frac{1}{\sqrt5} \approx 63{,}4^\circ\,} \]

**Schritt 3 — Wert von \( a \) für \( 45^\circ \).** Ersetzt man die \( 2 \) durch \( a \), wird der
Normalenvektor \( \begin{pmatrix}a\\1\\0\end{pmatrix} \), und

\[ \cos\alpha = \frac{|a\cdot 0 + 1\cdot 1 + 0|}{\sqrt{a^2+1}\cdot 1} = \frac{1}{\sqrt{a^2+1}}. \]

Für \( \alpha = 45^\circ \) ist \( \cos 45^\circ = \tfrac{1}{\sqrt2} \), also

\[ \frac{1}{\sqrt{a^2+1}} = \frac{1}{\sqrt2} \;\Longrightarrow\; a^2+1 = 2 \;\Longrightarrow\; a^2 = 1
   \;\Longrightarrow\; \boxed{\,a = \pm 1\,}. \]

**Schritt 4 — Welche Winkel sind für \( a\neq 0 \) möglich?** Für \( a\neq 0 \) ist \( a^2 > 0 \), also
\( a^2+1 > 1 \) und damit

\[ 0 < \frac{1}{\sqrt{a^2+1}} < 1. \]

\( \cos\alpha \) liegt also echt zwischen \( 0 \) und \( 1 \). Dazu gehören **alle Winkel mit**
\( \boxed{\,0^\circ < \alpha < 90^\circ\,} \). Die Grenzen \( 0^\circ \) und \( 90^\circ \) werden nie
erreicht: \( 90^\circ \) bräuchte \( a = 0 \) (ausgeschlossen), \( 0^\circ \) bräuchte \( a \to \infty \).

<details><summary>Haltung dahinter: Was ist das Skalarprodukt, und warum liefert es einen Winkel?</summary>

Ohne Vorwissen, Schritt für Schritt.

**Skalarprodukt.** Zwei Vektoren \( \vec u, \vec v \) kann man auf eine bestimmte Weise „multiplizieren":
man multipliziert sie **zeilenweise** und addiert die drei Produkte zu **einer einzigen Zahl**:
\( \vec u\cdot\vec v = u_1v_1 + u_2v_2 + u_3v_3 \). Diese Zahl misst, wie sehr die beiden Pfeile in
dieselbe Richtung zeigen.

**Länge eines Vektors.** Die Länge \( |\vec u| \) ist \( \sqrt{u_1^2+u_2^2+u_3^2} \) — der Satz des
Pythagoras in drei Dimensionen (alle Komponenten quadrieren, addieren, Wurzel ziehen).

**Die Winkelformel.** Es gilt \( \vec u\cdot\vec v = |\vec u|\,|\vec v|\cos\varphi \), wobei
\( \varphi \) der Winkel zwischen den Pfeilen ist. Stellt man nach \( \cos\varphi \) um, erhält man die
Formel oben. Den **Betrag** \( |\dots| \) im Zähler setzt man, damit immer der **spitze** Winkel
herauskommt (ein Winkel zwischen Flächen wird üblicherweise als spitzer Winkel angegeben).

**Warum gerade die Normalenvektoren?** Der Winkel zwischen zwei Wänden ist derselbe wie der Winkel
zwischen ihren beiden „Fahnenmasten" (Normalenvektoren). Das ist bequemer, als die Flächen selbst
abzumessen. Den Rechenweg fürs Skalarprodukt findest du im
[Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html#skalarprodukt).

<details><summary>… ganz langsam (mit Zahlen): \( \cos\alpha = \tfrac{1}{\sqrt5} \)</summary>

Zähler: \( \vec n_F\cdot\vec n_2 = 2\cdot 0 + 1\cdot 1 + 0\cdot 0 \). Das mittlere Produkt ist
\( 1\cdot 1 = 1 \), die anderen beiden sind \( 0 \). Summe \( = 1 \). Betrag \( |1| = 1 \).

Nenner: \( |\vec n_F| = \sqrt{2^2+1^2+0^2} = \sqrt{4+1+0} = \sqrt5 \). Und
\( |\vec n_2| = \sqrt{0+1+0} = 1 \). Produkt \( \sqrt5\cdot 1 = \sqrt5 \).

Also \( \cos\alpha = \tfrac{1}{\sqrt5} \approx \tfrac{1}{2{,}236} \approx 0{,}447 \). Den Winkel selbst
holt die Umkehrtaste \( \arccos \) (auf dem Rechner „\( \cos^{-1} \)") zurück: \( \alpha\approx 63{,}4^\circ \).

</details>
</details>

<details><summary>Haltung dahinter: Warum zeigt die Draufsicht den Winkel direkt — und die Anschauung für \( a=\pm1 \)?</summary>

**Beide Ebenen sind „senkrecht".** \( F \) enthält kein \( x_3 \), die \( x_1x_3 \)-Ebene auch nicht in
dem Sinne, dass sie die \( x_3 \)-Richtung **enthält** — beide laufen parallel zur \( x_3 \)-Achse,
stehen also lotrecht über dem Boden. Schaut man von oben (entlang \( x_3 \)) auf den Boden, schrumpft
jede solche Wand zu einer **Linie** (ihrer Spur). Der Winkel zwischen den beiden Wänden ist dann genau
der Winkel zwischen ihren beiden Bodenlinien — das ist das obere Bild.

**Spur von \( F \):** die Linie \( 2x_1 + x_2 = 4 \) durch \( S_1(2|0) \) und \( S_2(0|4) \). **Spur der
\( x_1x_3 \)-Ebene:** die \( x_1 \)-Achse selbst (dort ist \( x_2 = 0 \)). Der Winkel zwischen diesen
beiden Linien ist \( \arctan 2 \approx 63{,}4^\circ \) — derselbe Wert wie über das Skalarprodukt
(\( \arccos\tfrac{1}{\sqrt5} \)). Zwei Wege, dasselbe Ergebnis.

**Warum \( a=\pm1 \) genau \( 45^\circ \) gibt.** Die Spur \( a x_1 + x_2 = 4 \) trifft die
\( x_1 \)-Achse bei \( \tfrac{4}{a} \) und die \( x_2 \)-Achse bei \( 4 \). Ein \( 45^\circ \)-Winkel
zur \( x_1 \)-Achse entsteht genau dann, wenn diese beiden Spurpunkte **gleich weit** vom Ursprung
entfernt sind (gleichschenklig-rechtwinkliges Dreieck): \( \left|\tfrac{4}{a}\right| = 4 \), also
\( |a| = 1 \), \( a = \pm 1 \). Das passt zur Rechnung in Schritt 3.

<details><summary>Typische Falle</summary>

Zwei klassische Fehler. Erstens: für den Ebenenwinkel die **Richtungsvektoren** statt der
**Normalenvektoren** nehmen — beim Schnitt zweier Ebenen rechnet man mit den Normalenvektoren.
Zweitens: bei Schritt 4 glauben, auch \( 0^\circ \) oder \( 90^\circ \) seien möglich. Sind sie nicht:
\( a\neq 0 \) sperrt die \( 90^\circ \) aus, und \( 0^\circ \) (parallele Ebenen) gäbe es nur im
Grenzfall \( a\to\infty \). Es kommen also **alle** Winkel **echt zwischen** \( 0^\circ \) und
\( 90^\circ \) vor.

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- a) \( M(1\,|\,2\,|\,2) \); Normalenvektor \( \overrightarrow{AB}=(-2,-2,8)\parallel(1,1,-4) \);
  \( E:\ x_1 + x_2 - 4x_3 = -5 \)
- b) Spurpunkte \( S_1(2|0|0),\ S_2(0|4|0) \); \( g:\ \vec x = (2,0,0) + t\,(-2,4,0) \)
- c) \( \cos\alpha = \tfrac{1}{\sqrt5},\ \alpha\approx 63{,}4^\circ \); \( 45^\circ \) für \( a=\pm 1 \);
  für \( a\neq 0 \) sind **alle** Winkel \( 0^\circ < \alpha < 90^\circ \) möglich

</details>

---

## Teil 2 — Gespräch (Analysis): Bergstollen

<div class="aufgabenkasten">

**Input.** Der Querschnitt eines Bergstollens wird beschrieben durch die \( x \)-Achse (Boden) und den
Teil des Graphen der Funktion \( f \) mit \( f(x) = 8 - \tfrac12 x^2 \), der **oberhalb** der
\( x \)-Achse verläuft (die Stollenwände).

Im Gespräch denkbare Aspekte: **(AB I)** Achsen skalieren und die Form des Graphen erklären; den
**Winkel** berechnen, den die Wände mit dem Boden einschließen; die **Stellen** ermitteln, an denen die
Wände am steilsten verlaufen. **(AB II)** aus den Ableitungen auf Eigenschaften des Graphen schließen;
der Stollen ist \( 50\,\text{m} \) lang und läuft **voll** mit Wasser — das **Wasservolumen**
bestimmen. **(AB III)** der Stollen ist \( 50\,\text{m} \) lang und es steht \( 3{,}5\,\text{m} \) hoch
Wasser — das **Wasservolumen** bestimmen; ein **würfelförmiger Behälter** soll auf einer Seitenfläche
im Stollen stehen — die **maximal mögliche Breite** ermitteln.

</div>

So sieht der Stollenquerschnitt aus. Spiele mit dem Bild, bevor du die Lösungen aufklappst.

<div class="jxgbox" id="jxg-k8-stollen" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k8-stollen',{boundingbox:[-5.5,9.2,5.5,-1.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 8-0.5*x*x;},-4,4],{strokeColor:'#3a5a9c',strokeWidth:2.6});b.create('point',[0,8],{name:'Scheitel (0|8)',size:2,fixed:true,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[8,2]}});b.create('point',[-4,0],{name:'(-4|0)',size:2,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',label:{offset:[-8,-16]}});b.create('point',[4,0],{name:'(4|0)',size:2,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',label:{offset:[0,-16]}});})();</script>

### AB I — Form, Wandwinkel, steilste Stellen

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Form und Achsen.** \( f(x) = 8 - \tfrac12 x^2 \) ist eine **nach unten geöffnete Parabel**. Der
höchste Punkt (Scheitel) liegt bei \( (0\,|\,8) \): \( f(0) = 8 \). Die Wände treffen den Boden in den
**Nullstellen**:

\[ 8 - \tfrac12 x^2 = 0 \;\Longrightarrow\; \tfrac12 x^2 = 8 \;\Longrightarrow\; x^2 = 16
   \;\Longrightarrow\; x = \pm 4. \]

Der Stollen ist also am Boden \( 8\,\text{m} \) breit (von \( x=-4 \) bis \( x=4 \)) und in der Mitte
\( 8\,\text{m} \) hoch. Achsen in Metern skalieren, beide gleich. Die Form ist symmetrisch zur
\( y \)-Achse, oben flach gerundet, zu den Seiten hin immer steiler.

**Winkel der Wände mit dem Boden.** Die **Steigung** der Wand ist die Ableitung \( f'(x) = -x \). Am
Fußpunkt \( x = 4 \) ist \( f'(4) = -4 \); der Betrag \( 4 \) ist die Steilheit. Der Winkel \( \beta \)
zwischen Wand und (waagerechtem) Boden erfüllt

\[ \tan\beta = |f'(4)| = 4 \;\Longrightarrow\; \beta = \arctan 4 \approx 76{,}0^\circ. \]

Bei \( x = -4 \) ist \( f'(-4) = 4 \) — aus Symmetriegründen derselbe Winkel \( \approx 76^\circ \).

**Steilste Stellen.** Die Steilheit ist \( |f'(x)| = |x| \). Auf dem Bereich der Wände
\( (-4 \le x \le 4) \) wird \( |x| \) am **größten an den Rändern** \( x = \pm 4 \). Die Wände sind also
**dort am steilsten, wo sie auf den Boden treffen**; ganz oben am Scheitel \( (x=0) \) ist die Wand
waagerecht (Steigung \( 0 \)).

Hier die beiden Tangenten an den Fußpunkten (gestrichelt) mit dem Wandwinkel:

<div class="jxgbox" id="jxg-k8-tangente" style="width:100%;max-width:480px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k8-tangente',{boundingbox:[-5.5,9.2,5.5,-2],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 8-0.5*x*x;},-4,4],{strokeColor:'#3a5a9c',strokeWidth:2.6});b.create('functiongraph',[function(x){return -4*x+16;},3.3,4.5],{strokeColor:'#d98324',strokeWidth:2,dash:2});b.create('functiongraph',[function(x){return 4*x+16;},-4.5,-3.3],{strokeColor:'#d98324',strokeWidth:2,dash:2});b.create('text',[3.4,1.2,'≈ 76°']);b.create('text',[-4.8,1.2,'≈ 76°']);})();</script>

<details><summary>Haltung dahinter: Was ist eine Parabel, und woran sieht man „nach unten geöffnet, flacher"?</summary>

Schritt für Schritt.

**Parabel.** Der Graph einer Funktion mit einem \( x^2 \) ist eine **Parabel** — eine symmetrische
U-Form. Das Vorzeichen vor dem \( x^2 \) entscheidet über die Öffnung: **plus** öffnet nach oben (Tal),
**minus** nach unten (Hügel). Hier steht \( -\tfrac12 x^2 \), also ein Minus → die Parabel öffnet nach
unten, sie ist ein „Hügel" mit Spitze oben.

**Der Faktor \( \tfrac12 \).** Eine Standardparabel wäre \( x^2 \). Der Faktor \( \tfrac12 < 1 \) drückt
alle Werte auf die Hälfte — die Parabel wird **flacher / breiter**. Die \( +8 \) am Anfang schiebt den
ganzen Hügel um \( 8 \) nach oben, deshalb sitzt der Scheitel bei Höhe \( 8 \).

**Nullstelle.** Eine Stelle, an der der Graph die \( x \)-Achse trifft (Funktionswert \( 0 \)). Hier:
Wo berührt die Stollenwand den Boden? Bei \( x = \pm 4 \).

<details><summary>… ganz langsam (mit Zahlen): die Nullstellen</summary>

Ansatz \( 8 - \tfrac12 x^2 = 0 \). Bringe \( \tfrac12 x^2 \) auf die andere Seite: \( 8 = \tfrac12 x^2 \).
Mal \( 2 \) auf beiden Seiten: \( 16 = x^2 \). Welche Zahl quadriert ergibt \( 16 \)? Sowohl \( 4 \)
(\( 4\cdot4=16 \)) als auch \( -4 \) (\( (-4)\cdot(-4)=16 \), Minus mal Minus ist Plus). Also
\( x = 4 \) **und** \( x = -4 \) — die beiden Wandfüße, \( 8\,\text{m} \) auseinander.

</details>
</details>

<details><summary>Haltung dahinter: Warum ist die Ableitung die Steigung, und woher der Winkel?</summary>

**Ableitung = Steigung.** Die **Ableitung** \( f'(x) \) gibt an jeder Stelle an, wie **steil** der Graph
dort ansteigt oder abfällt. Eine positive Zahl heißt „bergauf", eine negative „bergab", \( 0 \) heißt
„waagerecht". Für \( f(x) = 8 - \tfrac12 x^2 \) ist die Ableitung \( f'(x) = -x \) (die Rechenregeln
dazu stehen im [Ableit-Handwerk](kap-ableiten-handwerk.html)).

**Steigung → Winkel mit dem Tangens.** Eine Steigung von \( 4 \) bedeutet: \( 4 \) Schritte hoch je
\( 1 \) Schritt zur Seite. Der **Tangens** verbindet diesen „Höhe pro Breite"-Wert mit einem Winkel:
\( \tan(\text{Winkel}) = \tfrac{\text{Höhe}}{\text{Breite}} = \tfrac{4}{1} = 4 \). Den Winkel selbst holt
die Umkehrung \( \arctan \) (Taste „\( \tan^{-1} \)") zurück: \( \arctan 4 \approx 76^\circ \). Steiler
geht es bei dieser Parabel nicht — \( 76^\circ \) ist schon recht nah an einer senkrechten Wand
(\( 90^\circ \)).

<details><summary>… ganz langsam (mit Zahlen): \( f'(4) \)</summary>

\( f'(x) = -x \). An der Stelle \( x = 4 \) einsetzen: \( f'(4) = -4 \). Das Minus heißt „bergab" (von
links nach rechts gelesen läuft die rechte Wand nach unten). Für den **Winkel** zählt nur die Steilheit,
also der Betrag \( |-4| = 4 \). Daher \( \tan\beta = 4 \) und \( \beta \approx 76^\circ \).

</details>

<details><summary>Typische Falle</summary>

Die Steigung \( 4 \) **als** Winkel auszugeben („der Winkel ist \( 4^\circ \)"). Eine Steigung ist
**kein** Winkel — man muss \( \arctan \) anwenden. Und für den Winkel die Steigung als Betrag nehmen
(\( |-4| = 4 \)), sonst käme ein negativer „Winkel" heraus.

</details>
</details>
</details>

### AB II — Eigenschaften aus den Ableitungen, Volumen bei vollem Stollen

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Aus den Ableitungen auf Eigenschaften schließen.** Mit \( f'(x) = -x \) und \( f''(x) = -1 \):

- \( f'(x) = 0 \) nur bei \( x = 0 \) → einzige Stelle mit waagerechter Tangente (Kandidat für einen
  Hoch-/Tiefpunkt).
- \( f''(0) = -1 < 0 \) → an dieser Stelle ein **Hochpunkt**. Da \( f''(x) = -1 \) **überall** negativ
  ist, ist der Graph durchgehend **rechtsgekrümmt** (eine nach unten gewölbte Kuppel) und hat **keine
  Wendestelle**.
- \( f'(x) > 0 \) für \( x < 0 \) (Graph steigt), \( f'(x) < 0 \) für \( x > 0 \) (Graph fällt) → der
  Stollen steigt bis zur Mitte an und fällt dann wieder. Genau ein höchster Punkt: der Scheitel
  \( (0\,|\,8) \).

**Volumen bei vollem Stollen.** Das Volumen ist **Querschnittsfläche \( \times \) Länge**. Die
Querschnittsfläche \( A \) ist die Fläche zwischen Parabel und Boden, also das Integral von \( f \) über
\( -4 \) bis \( 4 \). Eine **Stammfunktion** von \( f(x) = 8 - \tfrac12 x^2 \) ist

\[ F(x) = 8x - \tfrac{1}{6}x^3. \]

\[ A = \int_{-4}^{4}\!\Big(8 - \tfrac12 x^2\Big)\,dx = \Big[\,8x - \tfrac16 x^3\,\Big]_{-4}^{4}
   = \tfrac{64}{3} - \Big(\!-\tfrac{64}{3}\Big) = \frac{128}{3} \approx 42{,}67\ (\text{m}^2). \]

Mit der Länge \( 50\,\text{m} \):

\[ V = A \cdot 50 = \frac{128}{3}\cdot 50 = \frac{6400}{3} \approx 2133{,}3\ (\text{m}^3). \]

Die Querschnittsfläche, die hier integriert wird (blau):

<div class="jxgbox" id="jxg-k8-voll" style="width:100%;max-width:480px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k8-voll',{boundingbox:[-5.5,9.2,5.5,-1.5],axis:true,showCopyright:false,showNavigation:false});var xs=[],ys=[],i,x,N=80;for(i=0;i<=N;i++){x=-4+8*i/N;xs.push(x);ys.push(8-0.5*x*x);}b.create('curve',[xs,ys],{fillColor:'#3a8ad9',fillOpacity:0.25,strokeColor:'#3a5a9c',strokeWidth:2.6});b.create('text',[-1.3,3.2,'Wasser (voll)']);})();</script>

<details><summary>Haltung dahinter: Was sagen \( f' \) und \( f'' \) über den Graphen?</summary>

Zwei Werkzeuge, die man am Graphen „ablesen" kann, ohne ihn zu sehen.

**Erste Ableitung \( f' \) — die Steigung.** Wo \( f' > 0 \), geht es bergauf; wo \( f' < 0 \), bergab;
wo \( f' = 0 \), ist eine waagerechte Stelle (möglicher Gipfel oder Talboden). Hier: \( f'(x) = -x \) ist
für negative \( x \) positiv (steigt) und für positive \( x \) negativ (fällt) — typischer Hügel.

**Zweite Ableitung \( f'' \) — die Krümmung.** \( f'' \) misst, ob sich der Graph nach oben oder unten
wölbt. \( f'' < 0 \) heißt „nach unten gewölbt" (Kuppel, wie ein umgedrehter Eimer); \( f'' > 0 \) heißt
„nach oben gewölbt" (Schüssel). An einer waagerechten Stelle entscheidet das Vorzeichen von \( f'' \):
\( f'' < 0 \) → **Hochpunkt**. Hier ist \( f''(x) = -1 \) **immer** negativ → reine Kuppel, keine
Wendestelle, einziger Hochpunkt am Scheitel. (Mehr zu diesem Ablesen:
[Funktionsuntersuchung](kap-funktionsuntersuchung.html).)

</details>

<details><summary>Haltung dahinter: Was ist ein Integral, und warum Fläche \( \times \) Länge?</summary>

Langsam von vorn.

**Integral = Fläche unter dem Graphen.** Das Integral \( \int_a^b f(x)\,dx \) rechnet die Fläche
zwischen dem Graphen und der \( x \)-Achse zwischen den senkrechten Grenzen \( a \) und \( b \) zusammen
— man stellt sich unendlich viele hauchdünne senkrechte Streifen vor, alle aufaddiert.

**Stammfunktion.** Um ein Integral auszurechnen, braucht man eine **Stammfunktion** \( F \): eine
Funktion, deren Ableitung wieder \( f \) ergibt (\( F' = f \)). Das ist „Ableiten rückwärts". Aus
\( 8 \) wird beim Aufleiten \( 8x \); aus \( -\tfrac12 x^2 \) wird \( -\tfrac12\cdot\tfrac{x^3}{3} =
-\tfrac16 x^3 \). Probe durch Ableiten führt zurück zu \( f \). (Regeln:
[Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).)

**Hauptsatz.** Den Flächenwert bekommt man als \( F(\text{obere Grenze}) - F(\text{untere Grenze}) \).

**Warum Fläche \( \times \) Länge?** Der Stollen ist ein „Prisma": überall derselbe Querschnitt, nur
\( 50\,\text{m} \) lang in die Tiefe gezogen. Solch ein Körper hat das Volumen
\( \text{Querschnittsfläche} \times \text{Länge} \) — wie ein Stapel von \( 50 \) gleichen
\( 1\,\text{m} \)-Scheiben.

<details><summary>… ganz langsam (mit Zahlen): das Integral</summary>

Obere Grenze \( x=4 \): \( F(4) = 8\cdot 4 - \tfrac16\cdot 4^3 = 32 - \tfrac{64}{6} = 32 - \tfrac{32}{3}
= \tfrac{96}{3} - \tfrac{32}{3} = \tfrac{64}{3} \).

Untere Grenze \( x=-4 \): \( F(-4) = 8\cdot(-4) - \tfrac16\cdot(-4)^3 = -32 - \tfrac{-64}{6}
= -32 + \tfrac{32}{3} = -\tfrac{64}{3} \) (Achtung: \( (-4)^3 = -64 \), das Minus davor dreht es um).

Differenz: \( \tfrac{64}{3} - \big(\!-\tfrac{64}{3}\big) = \tfrac{128}{3} \approx 42{,}67\,\text{m}^2 \).
Mal \( 50 \): \( \tfrac{128}{3}\cdot 50 = \tfrac{6400}{3} \approx 2133{,}3\,\text{m}^3 \).

</details>
</details>
</details>

### AB III — Wasservolumen bei \( 3{,}5\,\text{m} \) und größter Würfel

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Wasservolumen bei \( 3{,}5\,\text{m} \) Wasserstand.** Steht das Wasser nur \( 3{,}5\,\text{m} \)
hoch, ist die Wasseroberfläche eine waagerechte Linie auf Höhe \( y = 3{,}5 \). Wo trifft sie die Wand?

\[ 8 - \tfrac12 x^2 = 3{,}5 \;\Longrightarrow\; \tfrac12 x^2 = 4{,}5 \;\Longrightarrow\; x^2 = 9
   \;\Longrightarrow\; x = \pm 3. \]

Die Wasserfläche ist die volle Querschnittsfläche **minus** dem leeren Bogen oben (zwischen
Wasserspiegel und Decke, für \( -3 \le x \le 3 \)):

\[ A_{\text{leer}} = \int_{-3}^{3}\!\big(f(x) - 3{,}5\big)\,dx
   = \int_{-3}^{3}\!\Big(4{,}5 - \tfrac12 x^2\Big)\,dx
   = \Big[\,4{,}5\,x - \tfrac16 x^3\,\Big]_{-3}^{3} = 9 - (-9) = 18. \]

\[ A_{\text{Wasser}} = \frac{128}{3} - 18 = \frac{74}{3} \approx 24{,}67\ (\text{m}^2),\qquad
   V = \frac{74}{3}\cdot 50 = \frac{3700}{3} \approx 1233{,}3\ (\text{m}^3). \]

<div class="jxgbox" id="jxg-k8-wasser35" style="width:100%;max-width:480px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k8-wasser35',{boundingbox:[-5.5,9.2,5.5,-1.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 8-0.5*x*x;},-4,4],{strokeColor:'#3a5a9c',strokeWidth:2});var xs=[],ys=[],i,x,N=40;for(i=0;i<=N;i++){x=-4+i/N;xs.push(x);ys.push(8-0.5*x*x);}xs.push(3);ys.push(3.5);for(i=0;i<=N;i++){x=3+i/N;xs.push(x);ys.push(8-0.5*x*x);}b.create('curve',[xs,ys],{fillColor:'#3a8ad9',fillOpacity:0.28,strokeColor:'#3a8ad9',strokeWidth:1});b.create('line',[[-3,3.5],[3,3.5]],{straightFirst:false,straightLast:false,strokeColor:'#2a6aa8',strokeWidth:1.6,dash:2});b.create('text',[-1.4,1.6,'Wasser 3,5 m']);})();</script>

**Größter würfelförmiger Behälter.** Ein Würfel mit Kantenlänge \( s \) steht auf dem Boden; sein
Querschnitt in der Stollenebene ist ein **Quadrat** der Seite \( s \). Aus Symmetrie stellt man ihn
mittig (von \( x=-\tfrac{s}{2} \) bis \( x=\tfrac{s}{2} \), von \( y=0 \) bis \( y=s \)). Die kritischen
Punkte sind die **oberen Ecken** \( \big(\pm\tfrac{s}{2}\,\big|\,s\big) \): sie müssen unter der Decke
liegen, also \( f\!\big(\tfrac{s}{2}\big) \ge s \). Der größte Würfel erfüllt es mit Gleichheit:

\[ 8 - \tfrac12\Big(\tfrac{s}{2}\Big)^2 = s \;\Longrightarrow\; 8 - \frac{s^2}{8} = s
   \;\Longrightarrow\; 64 - s^2 = 8s \;\Longrightarrow\; s^2 + 8s - 64 = 0. \]

Mit der \( pq \)- bzw. Mitternachtsformel:

\[ s = \frac{-8 + \sqrt{8^2 + 4\cdot 64}}{2} = \frac{-8 + \sqrt{320}}{2} = -4 + 4\sqrt5
   = 4\big(\sqrt5 - 1\big) \approx 4{,}94\ (\text{m}). \]

(Die zweite Lösung \( -4 - 4\sqrt5 \) ist negativ und scheidet als Länge aus.)

\[ \boxed{\,s_{\max} = 4\big(\sqrt5 - 1\big) \approx 4{,}94\ \text{m}\,} \]

<div class="jxgbox" id="jxg-k8-wuerfel" style="width:100%;max-width:480px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k8-wuerfel',{boundingbox:[-5.5,9.2,5.5,-1.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 8-0.5*x*x;},-4,4],{strokeColor:'#3a5a9c',strokeWidth:2.6});b.create('polygon',[[-2.472,0],[2.472,0],[2.472,4.944],[-2.472,4.944]],{fillColor:'#d98324',fillOpacity:0.18,borders:{strokeColor:'#d98324',strokeWidth:2},vertices:{visible:false}});b.create('text',[-2.3,5.6,'Breite s ≈ 4,94 m']);})();</script>

<details><summary>Haltung dahinter: Warum nur bis \( x=\pm 3 \) integrieren — und nicht einfach skalieren?</summary>

Der gefährliche Reflex wäre: „voller Stollen ergab \( 2133\,\text{m}^3 \), bei \( 3{,}5 \) von \( 8 \)
Metern sind es eben \( \tfrac{3{,}5}{8} \) davon." Das ist **falsch**, weil der Stollen unten breiter ist
als oben — die unteren Schichten fassen mehr Wasser pro Höhenmeter.

**So sieht die Wasserfläche wirklich aus.** Unten füllt das Wasser den ganzen Boden. Für \( |x| \le 3 \)
reicht es bis zur waagerechten Oberfläche \( y = 3{,}5 \) (die Decke ist dort höher). Für
\( 3 \le |x| \le 4 \) ist die Wand bereits niedriger als \( 3{,}5 \), dort begrenzt die **Wand** das
Wasser. Bequemer rechnet man deshalb: **ganze Querschnittsfläche minus dem leeren Bogen** oben. Der
leere Bogen ist die Fläche zwischen Decke und Wasserspiegel, \( \int_{-3}^{3}(f(x)-3{,}5)\,dx = 18 \).

<details><summary>… ganz langsam (mit Zahlen): die leere Fläche</summary>

\( f(x) - 3{,}5 = 8 - \tfrac12 x^2 - 3{,}5 = 4{,}5 - \tfrac12 x^2 \). Stammfunktion
\( 4{,}5\,x - \tfrac16 x^3 \). Bei \( x=3 \): \( 4{,}5\cdot 3 - \tfrac16\cdot 27 = 13{,}5 - 4{,}5 = 9 \).
Bei \( x=-3 \): \( 4{,}5\cdot(-3) - \tfrac16\cdot(-27) = -13{,}5 + 4{,}5 = -9 \). Differenz
\( 9 - (-9) = 18 \). Also \( A_{\text{Wasser}} = \tfrac{128}{3} - 18 = \tfrac{74}{3} \approx 24{,}67 \),
und \( V = \tfrac{74}{3}\cdot 50 = \tfrac{3700}{3} \approx 1233{,}3\,\text{m}^3 \).

</details>

<details><summary>Typische Falle</summary>

Das volle Volumen einfach mit \( \tfrac{3{,}5}{8} \) zu multiplizieren. Weil der Querschnitt nach oben
schmaler wird, stimmt das nicht — man **muss** integrieren (oder die leere Fläche abziehen).

</details>
</details>

<details><summary>Haltung dahinter: Wie kommt man auf \( f\!\big(\tfrac{s}{2}\big) = s \)?</summary>

**Das Quadrat soll in den Stollen passen.** Ein Würfel, der auf einer Fläche steht, zeigt im Querschnitt
ein Quadrat der Seite \( s \): Breite \( s \), Höhe \( s \). Mittig gestellt reicht es von
\( x=-\tfrac{s}{2} \) bis \( x=\tfrac{s}{2} \) und von \( y=0 \) bis \( y=s \).

**Die obere Ecke ist der Engpass.** Weil die Decke eine nach unten gewölbte Kuppel ist und in der Mitte
am höchsten, stoßen zuerst die **oberen äußeren Ecken** an. Diese Ecken liegen bei
\( \big(\tfrac{s}{2}\,\big|\,s\big) \). Damit sie unter der Decke bleiben, muss die Decke dort mindestens
so hoch sein wie die Ecke: \( f\!\big(\tfrac{s}{2}\big) \ge s \). Der **größte** Würfel berührt die Decke
genau — Gleichheit.

**Warum mittig?** Schiebt man den Würfel zur Seite, kommt eine obere Ecke näher an die niedrigere Wand
und stößt früher an. Mittig ist der meiste Platz da. Aus Gleichheit wird eine quadratische Gleichung.

<details><summary>… ganz langsam (mit Zahlen): die quadratische Gleichung lösen</summary>

\( f\!\big(\tfrac{s}{2}\big) = 8 - \tfrac12\big(\tfrac{s}{2}\big)^2 = 8 - \tfrac12\cdot\tfrac{s^2}{4}
= 8 - \tfrac{s^2}{8} \). Gleichsetzen mit \( s \): \( 8 - \tfrac{s^2}{8} = s \). Mal \( 8 \):
\( 64 - s^2 = 8s \). Alles auf eine Seite: \( s^2 + 8s - 64 = 0 \). Mitternachtsformel mit
\( a=1, b=8, c=-64 \): Diskriminante \( b^2 - 4ac = 64 + 256 = 320 \), und \( \sqrt{320} = \sqrt{64\cdot5}
= 8\sqrt5 \). Also \( s = \tfrac{-8 + 8\sqrt5}{2} = -4 + 4\sqrt5 \approx -4 + 8{,}94 = 4{,}94 \). Probe:
\( \tfrac{s}{2} \approx 2{,}47 \), \( f(2{,}47) = 8 - \tfrac12\cdot 6{,}1 \approx 4{,}94 = s \). ✓

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 2 (erst nach dem eigenen Versuch aufklappen)</summary>

- **AB I:** Parabel nach unten, Scheitel \( (0|8) \), Nullstellen \( x=\pm 4 \) (Boden \( 8\,\text{m} \)
  breit, Mitte \( 8\,\text{m} \) hoch). Wandwinkel: \( \tan\beta = |f'(4)| = 4 \), \( \beta\approx 76^\circ \).
  Am steilsten an den Wandfüßen \( x=\pm 4 \).
- **AB II:** \( f'(x)=-x \) (Hochpunkt bei \( 0 \)), \( f''(x)=-1<0 \) (durchweg Kuppel, keine
  Wendestelle). Voller Stollen: \( A = \tfrac{128}{3} \), \( V = \tfrac{6400}{3} \approx 2133{,}3\,\text{m}^3 \).
- **AB III:** Wasser \( 3{,}5\,\text{m} \): \( A_{\text{Wasser}} = \tfrac{74}{3} \),
  \( V = \tfrac{3700}{3} \approx 1233{,}3\,\text{m}^3 \). Größter Würfel:
  \( s = 4(\sqrt5-1) \approx 4{,}94\,\text{m} \).

</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Teilaufgabe, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen
kannst. Du musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Geometrie) aufklappen</summary>

- **a) Mittelpunkt & Spiegelebene.** Erwartet: \( M(1|2|2) \) als **Durchschnitt** von \( A \) und
  \( B \); \( \overrightarrow{AB} \) (bzw. \( (1,1,-4) \)) als **Normalenvektor**; \( M \) eingesetzt
  ergibt \( E:\ x_1 + x_2 - 4x_3 = -5 \). *Rückfrage:* „Warum steht \( \overrightarrow{AB} \) senkrecht
  auf \( E \)?" (Antwort: Spiegelung — die Verbindung Original–Bild trifft den Spiegel senkrecht.) *Rote
  Flagge:* \( A \) oder \( B \) statt \( M \) zum Bestimmen von \( d \) einsetzen.
- **b) Ebene zeichnen & Schnittgerade.** Erwartet: \( F \) ist eine **Ebene parallel zur
  \( x_3 \)-Achse**; Spurpunkte \( S_1(2|0|0) \), \( S_2(0|4|0) \); Gerade
  \( \vec x = (2,0,0) + t\,(-2,4,0) \). *Rückfrage:* „Wieso ist \( 2x_1 + x_2 = 4 \) eine Ebene und keine
  Gerade?" (Antwort: eine einzelne Gleichung im Raum beschreibt eine Fläche; \( x_3 \) ist frei.)
- **c) Schnittwinkel.** Erwartet: Normalenvektoren \( (2,1,0) \) und \( (0,1,0) \), Skalarprodukt,
  \( \cos\alpha = \tfrac{1}{\sqrt5} \approx 63{,}4^\circ \); für \( 45^\circ \) ist \( a=\pm 1 \); für
  \( a\neq 0 \) sind **alle** Winkel \( 0^\circ < \alpha < 90^\circ \) möglich. *Rückfrage:* „Welche
  Vektoren benutzt du für den Winkel zwischen zwei Ebenen?" (Antwort: die **Normalenvektoren**.) *Rote
  Flagge:* behaupten, \( 0^\circ \) oder \( 90^\circ \) seien erreichbar.

</details>

<details><summary>Leitfaden Teil 2 (Analysis) aufklappen</summary>

- **AB I — Form, Winkel, steilste Stellen.** Erwartet: nach unten geöffnete Parabel, Scheitel
  \( (0|8) \), Nullstellen \( \pm 4 \); Wandwinkel über \( \tan\beta = |f'(4)| = 4 \Rightarrow \approx
  76^\circ \); am steilsten an den **Wandfüßen** \( x=\pm 4 \). *Rückfrage:* „Wie wird aus der Steigung
  ein Winkel?" (Antwort: \( \arctan \).) *Rote Flagge:* die Steigung \( 4 \) direkt als „\( 4^\circ \)".
- **AB II — Ableitungen & volles Volumen.** Erwartet: \( f'=-x \) (Hochpunkt bei \( 0 \)),
  \( f''=-1<0 \) (Kuppel, keine Wendestelle); Volumen = **Querschnittsfläche \( \times \) Länge**,
  \( A = \tfrac{128}{3} \), \( V \approx 2133\,\text{m}^3 \). *Rückfrage:* „Warum reicht es, die
  Querschnittsfläche mit \( 50 \) zu multiplizieren?" (Antwort: gleicher Querschnitt über die ganze
  Länge.)
- **AB III — Teilfüllung & Würfel.** Erwartet: Wasserspiegel trifft Wand bei \( x=\pm 3 \);
  Wasserfläche = volle Fläche **minus** leerem Bogen, \( V \approx 1233\,\text{m}^3 \); Würfelkante aus
  \( f\!\big(\tfrac{s}{2}\big)=s \Rightarrow s = 4(\sqrt5-1)\approx 4{,}94\,\text{m} \). *Rote Flagge:*
  das Volumen einfach mit \( \tfrac{3{,}5}{8} \) skalieren. *Rückfrage:* „Welche Ecke des Würfels stößt
  zuerst an die Decke?" (Antwort: die obere äußere Ecke.)

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Wie findest du die Spiegelebene zweier Punkte — welcher Vektor ist der Normalenvektor und welcher
  Punkt liegt sicher auf der Ebene?
- Warum ist \( 2x_1 + x_2 = 4 \) im Raum eine Ebene, und wie zeichnest du sie mit zwei Spurpunkten?
- Mit welchen Vektoren berechnest du den Winkel zwischen zwei Ebenen, und warum steht ein Betrag im
  Zähler?
- Wie wird bei der Stollenwand aus der Steigung \( f'(4) \) ein Winkel mit dem Boden?
- Warum darfst du das Wasservolumen bei \( 3{,}5\,\text{m} \) **nicht** durch einfaches Skalieren des
  vollen Volumens bestimmen?
