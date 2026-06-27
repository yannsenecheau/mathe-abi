# Aufgabe 6 — Geometrie & Analysis

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Geometrie**, **Teil 2 (Gespräch) aus der Analysis**. Teil 1 wird
**rechnerfrei** gelöst; in Teil 2 braucht man an einer einzigen Stelle den Taschenrechner (das wird dort
ausdrücklich gesagt), der Rest geht auch im Kopf. Arbeitet die Aufgabe wie eine echte Simulation durch —
eine Person trägt vor, die andere prüft mit dem Lösungsweg und dem
[Prüfer-Leitfaden](#prüfer-leitfaden-für-die-abfragende-person) am Ende mit.

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

> **Werkzeug zum Nachschlagen:** Die wiederkehrenden Vektor- und Geometrie-Werkzeuge (Punkte, Vektoren,
> Länge, Skalarprodukt, Kreuzprodukt, Geraden- und Ebenengleichung, Abstand) stehen kompakt im
> [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html) (u. a. Anker
> [#skalarprodukt](konv-90-werkzeugkasten-geometrie.html#skalarprodukt) und
> [#kreuzprodukt](konv-90-werkzeugkasten-geometrie.html#kreuzprodukt)). Die Analysis-Werkzeuge findest
> du in den Kapiteln [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Funktionsuntersuchung](kap-funktionsuntersuchung.html),
> [Integral-Grundlagen](kap-integral-grundlagen.html),
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html) und
> [Grenzwerte & Randverhalten](kap-grenzwerte-randverhalten.html).

---

## Teil 1 — Vortrag (Geometrie): Lage von Gerade und Ebene

<div class="aufgabenkasten">

**Gegeben sind die Gerade** \( g:\ \vec x = \begin{pmatrix}2\\0\\2\end{pmatrix} + t\cdot\begin{pmatrix}2\\1\\1\end{pmatrix} \) **(\( t\in\mathbb{R} \)) und die Ebene** \( E:\ x_1 + 2x_2 - 4x_3 = 1 \).

**a)** Beschreibe, welche gegenseitige Lage eine Ebene und eine Gerade im Raum haben können und wie man
diese Lage bestimmt.

**b)** Zeige, dass \( g \) und \( E \) parallel sind. Die Gerade \( h \) schneidet \( g \) orthogonal im
Punkt \( P(2\,|\,0\,|\,2) \) und verläuft parallel zur Ebene \( E \). Bestimme eine Gleichung der
Geraden \( h \).

**c)** Bestimme die Koordinaten eines Punktes, der von \( E \) den Abstand \( 3\sqrt{21} \) hat.

**d)** Von allen Geraden, die in der Ebene \( E \) liegen und parallel zu \( g \) verlaufen, ist die
Gerade \( j \) diejenige mit dem geringsten Abstand zur Geraden \( g \). Beschreibe ein Verfahren, mit
dem man eine Gleichung der Geraden \( j \) bestimmen kann.

</div>

> **Vorab, in zwei Sätzen, die beiden Schreibweisen:** Eine **Gerade in Parameterform**
> \( \vec x = \vec p + t\,\vec v \) ist „starte beim Stützpunkt \( \vec p \) und laufe in Richtung des
> Pfeils \( \vec v \) — für jedes \( t \) landest du auf einem anderen Punkt der Geraden". Hier ist der
> Stützpunkt \( P(2|0|2) \) und der **Richtungsvektor** \( \vec v=(2|1|1) \). Eine **Ebene in
> Koordinatenform** \( n_1x_1+n_2x_2+n_3x_3=d \) ist eine Bedingung, die **genau die Punkte der Ebene
> erfüllen**; die drei Zahlen \( (n_1|n_2|n_3) \) bilden den **Normalenvektor** — den Pfeil, der
> senkrecht auf der Ebene steht. Alle Vektor-Werkzeuge stehen im
> [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html).

### Teilaufgabe a) — Gegenseitige Lage von Gerade und Ebene

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Eine Gerade und eine Ebene im Raum haben **genau drei** mögliche Lagen:

- **Die Gerade liegt in der Ebene** (\( g\subset E \)) — jeder Punkt der Geraden gehört zur Ebene.
- **Die Gerade ist echt parallel zur Ebene** — sie hat **keinen** gemeinsamen Punkt mit der Ebene.
- **Die Gerade schneidet die Ebene** in **genau einem** Punkt (dem Durchstoßpunkt).

<figure>
<svg viewBox="0 0 720 235" role="img" aria-label="Drei mögliche Lagen von Gerade und Ebene: g liegt in E, g echt parallel zu E, g schneidet E" style="width:100%;max-width:720px;height:auto;background:#fbf7ef;border-radius:8px">
 <defs>
  <marker id="k6garrow" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#3a5a9c"/></marker>
 </defs>
 <g transform="translate(0,0)">
  <polygon points="45,60 195,40 215,140 65,160" fill="#3a5a9c" fill-opacity="0.08" stroke="#7a7163" stroke-width="1.4"/>
  <text x="58" y="54" font-size="12" fill="#7a7163">E</text>
  <line x1="70" y1="118" x2="205" y2="98" stroke="#3a5a9c" stroke-width="2.2" marker-end="url(#k6garrow)" marker-start="url(#k6garrow)"/>
  <text x="150" y="92" font-size="13" fill="#26324a" font-weight="bold">g</text>
  <text x="130" y="205" font-size="13" fill="#26324a" text-anchor="middle">g liegt in E</text>
 </g>
 <g transform="translate(240,0)">
  <polygon points="45,75 195,55 215,155 65,175" fill="#3a5a9c" fill-opacity="0.08" stroke="#7a7163" stroke-width="1.4"/>
  <text x="58" y="69" font-size="12" fill="#7a7163">E</text>
  <line x1="60" y1="55" x2="205" y2="35" stroke="#3a5a9c" stroke-width="2.2" marker-end="url(#k6garrow)" marker-start="url(#k6garrow)"/>
  <text x="150" y="29" font-size="13" fill="#26324a" font-weight="bold">g</text>
  <text x="130" y="210" font-size="13" fill="#26324a" text-anchor="middle">g echt parallel zu E</text>
 </g>
 <g transform="translate(480,0)">
  <polygon points="45,70 195,50 215,150 65,170" fill="#3a5a9c" fill-opacity="0.08" stroke="#7a7163" stroke-width="1.4"/>
  <text x="58" y="64" font-size="12" fill="#7a7163">E</text>
  <line x1="120" y1="20" x2="150" y2="100" stroke="#3a5a9c" stroke-width="2.2" marker-start="url(#k6garrow)"/>
  <line x1="150" y1="100" x2="180" y2="185" stroke="#3a5a9c" stroke-width="2.2" stroke-dasharray="5 4" marker-end="url(#k6garrow)"/>
  <circle cx="150" cy="100" r="3.5" fill="#d98324"/>
  <text x="156" y="96" font-size="11" fill="#d98324">g ∩ E</text>
  <text x="126" y="34" font-size="13" fill="#26324a" font-weight="bold">g</text>
  <text x="130" y="205" font-size="13" fill="#26324a" text-anchor="middle">g schneidet E</text>
 </g>
</svg>
<figcaption>Die drei Lagen: Gerade in der Ebene · echt parallel (kein gemeinsamer Punkt) · Schnitt in einem Punkt.</figcaption>
</figure>

**Wie man die Lage bestimmt.** Man **setzt die Geradengleichung in die Koordinatengleichung der Ebene
ein** und löst nach dem Parameter \( t \) auf. Drei Fälle:

- **Keine Lösung** (eine falsche Aussage wie „\( -6=1 \)") → die Gerade ist **echt parallel**.
- **Genau eine Lösung** für \( t \) → es gibt einen **Schnittpunkt**; \( t \) eingesetzt liefert ihn.
- **Unendlich viele Lösungen** (eine immer wahre Aussage wie „\( 0=0 \)") → die Gerade **liegt in der
  Ebene**.

<details><summary>Haltung dahinter: Was ist eine Ebene, was eine Gerade, und warum entscheidet das Einsetzen über die Lage? (ganz von vorn)</summary>

Langsam und ohne Vorwissen.

**Punkt im Raum.** Ein Ort im Raum wird durch **drei** Zahlen \( (x_1\mid x_2\mid x_3) \) beschrieben:
rechts/links, vorne/hinten, oben/unten. Drei Zahlen, weil der Raum drei Richtungen hat.

**Gerade.** Eine Gerade ist eine unendlich lange, schnurgerade Linie. Die Parameterform
\( \vec x=\vec p+t\,\vec v \) ist eine **Lauf-Vorschrift**: Du stehst beim Stützpunkt \( \vec p \) und
gehst Schritte in Richtung \( \vec v \). Wie viele Schritte, sagt die Zahl \( t \) — bei \( t=0 \) bist
du bei \( \vec p \), bei \( t=1 \) einen Pfeil weiter, bei \( t=-2 \) zwei Pfeile rückwärts. Jeder Wert
von \( t \) ergibt einen anderen Punkt der Geraden.

**Ebene.** Eine Ebene ist eine vollkommen flache, unendlich ausgedehnte Fläche (wie eine unendliche
Tischplatte). Die Koordinatenform \( n_1x_1+n_2x_2+n_3x_3=d \) ist eine **Eintrittskarte**: Setzt man
die drei Koordinaten eines Punktes ein und die Gleichung **stimmt**, liegt der Punkt auf der Ebene;
stimmt sie **nicht**, liegt er daneben.

**Warum klärt Einsetzen die Lage?** Die Punkte der Geraden sind \( \vec p+t\,\vec v \) — alle auf einmal,
durch den einen Buchstaben \( t \) beschrieben. Setzt man diese in die Eintrittskarte der Ebene ein,
entsteht **eine Gleichung in \( t \)**: Sie fragt „für welche Schrittzahl \( t \) liegt der
Geradenpunkt auf der Ebene?".

- Findet man **kein** passendes \( t \) (Widerspruch) → kein Punkt der Geraden trifft die Ebene → **echt
  parallel**.
- Findet man **ein** \( t \) → genau dieser eine Punkt trifft → **Schnittpunkt**.
- Stimmt die Gleichung für **jedes** \( t \) → jeder Geradenpunkt liegt auf der Ebene → **Gerade liegt
  in der Ebene**.

<details><summary>Typische Falle: „parallel" mit „liegt drin" verwechseln</summary>

„Parallel" ist der Oberbegriff für *„die Gerade läuft mit der Ebene mit, ohne sie zu durchstoßen"* — das
trifft auf **zwei** Fälle zu: echt parallel (kein Treffer) **und** Gerade liegt in der Ebene (immer
Treffer). Beim Einsetzen unterscheidet man sie am Ergebnis: **Widerspruch** = echt parallel,
**immer-wahr** = liegt drin. Wer nur „parallel" sagt, hat die halbe Antwort; in der mündlichen Prüfung
wird hier nachgefragt.

</details>
</details>
</details>

### Teilaufgabe b) — Parallelität zeigen und Gerade \( h \) bestimmen

<span class="tag tag-ok">AB I</span> <span class="tag tag-warn">AB II</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Schritt 1 — \( g \parallel E \) nachweisen.** Der Richtungsvektor von \( g \) ist
\( \vec v=(2|1|1) \), der Normalenvektor von \( E \) ist \( \vec n=(1|2|-4) \). Man bildet ihr
**Skalarprodukt**:

\[ \vec v\cdot\vec n=\begin{pmatrix}2\\1\\1\end{pmatrix}\cdot\begin{pmatrix}1\\2\\-4\end{pmatrix}
   = 2\cdot 1+1\cdot 2+1\cdot(-4)=2+2-4=0 . \]

Das Skalarprodukt ist \( 0 \): Der Richtungsvektor steht **senkrecht** auf dem Normalenvektor, also
läuft \( g \) **parallel zur Ebene** (sie kann höchstens noch in \( E \) liegen). Eine Punktprobe mit
dem Stützpunkt \( P(2|0|2) \) zeigt, dass \( g \) **nicht** in \( E \) liegt:

\[ 2+2\cdot 0-4\cdot 2 = 2-8 = -6 \neq 1 . \]

Also ist \( g \) **echt parallel** zu \( E \). \(\checkmark\)

**Schritt 2 — Richtungsvektor von \( h \).** Die Gerade \( h \) soll **zwei** Bedingungen erfüllen:

- \( h \) schneidet \( g \) **orthogonal** → die Richtung von \( h \) steht senkrecht auf \( \vec v=(2|1|1) \).
- \( h \) verläuft **parallel zu \( E \)** → die Richtung von \( h \) steht senkrecht auf \( \vec n=(1|2|-4) \).

Ein Vektor, der auf **beiden** senkrecht steht, ist das **Kreuzprodukt** der beiden:

\[ \vec u=\begin{pmatrix}2\\1\\1\end{pmatrix}\times\begin{pmatrix}1\\2\\-4\end{pmatrix}
   = \begin{pmatrix}1\cdot(-4)-1\cdot 2\\[2pt] 1\cdot 1-2\cdot(-4)\\[2pt] 2\cdot 2-1\cdot 1\end{pmatrix}
   = \begin{pmatrix}-6\\9\\3\end{pmatrix}=3\begin{pmatrix}-2\\3\\1\end{pmatrix}. \]

Man darf den gemeinsamen Faktor \( 3 \) kürzen — das ändert nur die Länge des Pfeils, nicht seine
Richtung. Also nimmt man \( \vec u=(-2|3|1) \).

**Schritt 3 — Gleichung von \( h \).** Die Gerade geht durch \( P(2|0|2) \) mit Richtung \( \vec u \):

\[ h:\ \vec x=\begin{pmatrix}2\\0\\2\end{pmatrix}+t\begin{pmatrix}-2\\3\\1\end{pmatrix},\quad t\in\mathbb{R}. \]

<details><summary>Haltung dahinter: Was ist ein Skalarprodukt, und warum heißt „= 0" senkrecht? (ganz von vorn)</summary>

**Skalarprodukt.** Aus zwei Pfeilen \( \vec a=(a_1|a_2|a_3) \) und \( \vec b=(b_1|b_2|b_3) \) macht man
**eine einzige Zahl**, indem man *zeilenweise multipliziert und alles addiert*:
\( \vec a\cdot\vec b=a_1b_1+a_2b_2+a_3b_3 \). Das Ergebnis ist eine Zahl, kein Pfeil.

**Warum verrät diese Zahl den Winkel?** Das Skalarprodukt misst, wie sehr zwei Pfeile „in dieselbe
Richtung zeigen". Zeigen sie in dieselbe Richtung, ist es groß und positiv; zeigen sie entgegengesetzt,
negativ; stehen sie **im rechten Winkel** zueinander, heben sich die Beiträge **genau zu null** auf.
Merksatz: **Skalarprodukt \( =0 \) bedeutet senkrecht.**

**Was bedeutet das hier?** Der Normalenvektor \( \vec n \) steht senkrecht auf der ganzen Ebene. Steht
nun die Richtung der Geraden senkrecht auf \( \vec n \) (Skalarprodukt \( =0 \)), dann läuft die Gerade
genau **längs** der Ebene mit — sie steigt nicht zur Ebene hin oder von ihr weg. Deshalb folgt aus
\( \vec v\cdot\vec n=0 \): \( g \) ist parallel zur Ebene.

<details><summary>… ganz langsam (mit Zahlen)</summary>

\( \vec v\cdot\vec n \): erstes mal erstes ist \( 2\cdot 1=2 \); zweites mal zweites ist
\( 1\cdot 2=2 \); drittes mal drittes ist \( 1\cdot(-4)=-4 \). Jetzt addieren: \( 2+2=4 \), und
\( 4+(-4)=0 \). Die letzte Zahl ist negativ, weil \( (-4) \) negativ ist — „plus minus vier" ist dasselbe
wie „minus vier". Ergebnis \( 0 \) → senkrecht → parallel.

Die Punktprobe rechnet man genauso stur: \( x_1+2x_2-4x_3 \) mit \( (2|0|2) \): \( 2 + 2\cdot 0 - 4\cdot 2
= 2 + 0 - 8 = -6 \). Die Ebene verlangt aber \( 1 \). Da \( -6 \) nicht \( 1 \) ist, liegt der Punkt — und
damit die ganze parallele Gerade — **neben** der Ebene: echt parallel.

</details>
</details>

<details><summary>Haltung dahinter: Wieso liefert das Kreuzprodukt genau die Richtung von \( h \)?</summary>

\( h \) muss zu **zwei** Pfeilen gleichzeitig senkrecht sein: zu \( \vec v \) (weil \( h \) die Gerade
\( g \) im rechten Winkel kreuzt) und zu \( \vec n \) (weil \( h \) parallel zur Ebene liegt, also wie
\( g \) längs der Ebene mitläuft und damit senkrecht zum Normalenvektor steht).

Das **Kreuzprodukt** \( \vec v\times\vec n \) ist eine feste Rechenvorschrift, deren Ergebnis ein
**neuer Pfeil** ist, der auf **beiden** Ausgangspfeilen senkrecht steht — genau die gesuchte
Eigenschaft. Das Rechenschema (welche Zahlen man kreuzweise multipliziert und subtrahiert) steht im
[Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html#kreuzprodukt).

<details><summary>… ganz langsam (mit Zahlen) — und „orthogonal" kurz erklärt</summary>

**„Orthogonal" heißt „im rechten Winkel", also senkrecht** — wie die Ecke eines Blattes Papier.

Das Kreuzprodukt \( (2|1|1)\times(1|2|-4) \) Zeile für Zeile (Schema „über Kreuz, immer die anderen zwei
Zeilen"):

- **1. Zeile:** \( 1\cdot(-4)-1\cdot 2 = -4-2 = -6 \).
- **2. Zeile:** \( 1\cdot 1-2\cdot(-4) = 1-(-8) = 1+8 = 9 \) (Achtung: „minus mal minus" wird plus).
- **3. Zeile:** \( 2\cdot 2-1\cdot 1 = 4-1 = 3 \).

Ergebnis \( (-6|9|3) \). Alle drei Zahlen sind durch \( 3 \) teilbar, also kürzt man zu \( (-2|3|1) \).
**Probe:** \( (-2|3|1)\cdot(2|1|1)=-4+3+1=0 \;\checkmark \) (senkrecht zu \( g \)) und
\( (-2|3|1)\cdot(1|2|-4)=-2+6-4=0\;\checkmark \) (senkrecht zu \( \vec n \), also parallel zu \( E \)).
Beide Bedingungen erfüllt.

</details>
</details>
</details>

### Teilaufgabe c) — Punkt mit Abstand \( 3\sqrt{21} \) zur Ebene

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Idee:** Der **kürzeste** Weg von einem Punkt zur Ebene führt **in Richtung des Normalenvektors**.
Startet man also auf der Ebene und geht ein Stück in Normalenrichtung, ist die zurückgelegte Strecke
genau der Abstand. Der Normalenvektor \( \vec n=(1|2|-4) \) hat die Länge

\[ |\vec n|=\sqrt{1^2+2^2+(-4)^2}=\sqrt{1+4+16}=\sqrt{21}. \]

Geht man **3 ganze Normalenvektoren** weit, beträgt der Abstand \( 3\cdot|\vec n|=3\sqrt{21} \) — genau
das Gesuchte.

**Schritt 1 — Punkt auf \( E \) wählen.** Bequem ist \( Q(1|0|0) \): Probe \( 1+2\cdot 0-4\cdot 0=1\;\checkmark \).

**Schritt 2 — drei Normalenvektoren addieren.**

\[ \overrightarrow{OR}=\overrightarrow{OQ}+3\,\vec n
   =\begin{pmatrix}1\\0\\0\end{pmatrix}+3\begin{pmatrix}1\\2\\-4\end{pmatrix}
   =\begin{pmatrix}1+3\\0+6\\0-12\end{pmatrix}=\begin{pmatrix}4\\6\\-12\end{pmatrix}. \]

Also hat **\( R(4\,|\,6\,|\,-12) \)** den Abstand \( 3\sqrt{21} \) von \( E \). (Es gibt viele solche
Punkte — jeder Punkt der Form „Ebenenpunkt \( {}\pm 3\,\vec n \)" passt.)

<details><summary>Haltung dahinter: Was ist „der Abstand von einer Ebene", und warum die Normalenrichtung? (ganz von vorn)</summary>

**Abstand Punkt–Ebene** ist die **kürzeste** Verbindung zwischen dem Punkt und der Fläche. Bild: Du
stehst im Zimmer und willst zur Decke — der kürzeste Weg ist **gerade nach oben**, also **senkrecht** zur
Decke. Jeder schräge Weg ist länger. „Senkrecht zur Ebene" ist aber genau die Richtung des
**Normalenvektors**. Deshalb misst man Abstände immer entlang \( \vec n \).

**Warum \( 3\vec n \)?** Ein einzelner Normalenvektor \( \vec n \) hat die Länge \( |\vec n|=\sqrt{21} \).
Hängt man \( 3 \) davon hintereinander, ist die Strecke dreimal so lang: \( 3\sqrt{21} \). Startet man
diesen Marsch **auf** der Ebene (Punkt \( Q \)), landet man bei einem Punkt, der genau \( 3\sqrt{21} \)
entfernt ist.

<details><summary>… ganz langsam (mit Zahlen) — Kontrolle mit der Abstandsformel</summary>

Die Länge: \( 1^2=1 \), \( 2^2=4 \), \( (-4)^2=16 \) (minus mal minus wird plus). Summe
\( 1+4+16=21 \), Wurzel \( \sqrt{21} \).

Gegenprobe mit der **Abstandsformel** (Hesse): Abstand \( =\dfrac{|x_1+2x_2-4x_3-1|}{|\vec n|} \). Für
\( R(4|6|-12) \) oben rein: \( 4+2\cdot 6-4\cdot(-12)=4+12+48=64 \). Dann \( |64-1|=63 \). Teilen durch
\( \sqrt{21} \):

\[ \frac{63}{\sqrt{21}}=\frac{3\cdot 21}{\sqrt{21}}=3\cdot\frac{21}{\sqrt{21}}=3\sqrt{21}\;\checkmark \]

(weil \( \tfrac{21}{\sqrt{21}}=\sqrt{21} \)). Der Abstand stimmt.

</details>

<details><summary>Typische Falle: nicht von einem Ebenenpunkt starten</summary>

Wer einfach „irgendeinen Punkt nimmt und \( 3\vec n \) addiert", bekommt **nicht** den Abstand
\( 3\sqrt{21} \) — das funktioniert nur, wenn der Startpunkt **wirklich auf \( E \)** liegt. Deshalb
zuerst ein \( Q \) suchen, das die Ebenengleichung erfüllt (Punktprobe!), und erst dann
\( 3\vec n \) addieren.

</details>
</details>
</details>

### Teilaufgabe d) — Gerade \( j \) mit dem geringsten Abstand zu \( g \)

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Verfahren anzeigen</summary>

Verlangt ist nur das **Verfahren**. Hier ist es, mit kurzer Begründung und einer Rechnung zur Kontrolle.

**Idee.** Gesucht ist die Gerade in \( E \), die parallel zu \( g \) verläuft und \( g \) am nächsten
ist. Das ist der **„Schatten" von \( g \) auf \( E \)** senkrecht von oben — die orthogonale Projektion.
Man fällt von einem Punkt der Geraden \( g \) das **Lot** auf \( E \) (Marsch in Normalenrichtung) und
legt durch den Fußpunkt eine Gerade parallel zu \( g \).

**Verfahren in drei Schritten:**

1. **Lotgerade aufstellen.** Durch den Stützpunkt \( P(2|0|2) \) von \( g \) eine Gerade \( k \) in
   Richtung des Normalenvektors \( \vec n=(1|2|-4) \) legen:
   \[ k:\ \vec x=\begin{pmatrix}2\\0\\2\end{pmatrix}+s\begin{pmatrix}1\\2\\-4\end{pmatrix}. \]
   (Diese Gerade steht **senkrecht auf \( E \)** und damit auch senkrecht auf \( g \).)
2. **Fußpunkt \( F \) bestimmen** als Schnittpunkt von \( k \) mit \( E \) (Einsetzen, nach \( s \) auflösen).
3. **Gerade \( j \) aufstellen** durch \( F \) mit dem Richtungsvektor von \( g \):
   \[ j:\ \vec x=\overrightarrow{OF}+t\begin{pmatrix}2\\1\\1\end{pmatrix}. \]

**Kontrollrechnung (Schritt 2).** Den Punkt von \( k \), nämlich \( (2+s\,|\,2s\,|\,2-4s) \), in
\( E \) einsetzen:

\[ (2+s)+2(2s)-4(2-4s)=1 \;\Longrightarrow\; 2+s+4s-8+16s=1 \;\Longrightarrow\; 21s-6=1 \;\Longrightarrow\; s=\tfrac13. \]

Eingesetzt: \( F=\big(\tfrac{7}{3}\,\big|\,\tfrac{2}{3}\,\big|\,\tfrac{2}{3}\big) \) (Probe:
\( \tfrac73+2\cdot\tfrac23-4\cdot\tfrac23=\tfrac{7+4-8}{3}=1\;\checkmark \)). Damit

\[ j:\ \vec x=\begin{pmatrix}7/3\\2/3\\2/3\end{pmatrix}+t\begin{pmatrix}2\\1\\1\end{pmatrix}. \]

Der geringste Abstand ist die Länge des Lots: \( |s|\cdot|\vec n|=\tfrac13\sqrt{21}=\tfrac{\sqrt{21}}{3}\approx 1{,}53 \)
— derselbe Wert wie der Abstand der parallelen Geraden \( g \) zur Ebene \( E \).

<figure>
<svg viewBox="0 0 480 360" role="img" aria-label="Gerade g parallel über Ebene E; das Lot von P auf E trifft E im Fußpunkt F; die Gerade j durch F parallel zu g ist die nächstgelegene Gerade in E" style="width:100%;max-width:460px;height:auto;background:#fbf7ef;border-radius:8px">
 <defs>
  <marker id="k6arrow2" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#3a5a9c"/></marker>
 </defs>
 <polygon points="70,250 330,210 400,300 140,340" fill="#3a5a9c" fill-opacity="0.07" stroke="#7a7163" stroke-width="1.4"/>
 <text x="404" y="304" font-size="13" fill="#7a7163">E</text>
 <line x1="95" y1="140" x2="352" y2="100" stroke="#3a5a9c" stroke-width="2.4" marker-end="url(#k6arrow2)"/>
 <text x="358" y="100" font-size="14" fill="#26324a" font-weight="bold">g</text>
 <circle cx="225" cy="120" r="3.2" fill="#3a5a9c"/><text x="205" y="115" font-size="12" fill="#26324a">P</text>
 <line x1="225" y1="120" x2="228" y2="262" stroke="#d98324" stroke-width="1.8" stroke-dasharray="4 3"/>
 <text x="236" y="196" font-size="12" fill="#d98324">Lot (Richtung n)</text>
 <circle cx="228" cy="262" r="3.2" fill="#d98324"/><text x="232" y="280" font-size="12" fill="#26324a">F</text>
 <path d="M228,262 l-13,2 l-2,-13" fill="none" stroke="#7a7163" stroke-width="1"/>
 <line x1="98" y1="282" x2="356" y2="242" stroke="#3a8a5a" stroke-width="2.4"/>
 <text x="360" y="242" font-size="14" fill="#3a8a5a" font-weight="bold">j</text>
</svg>
<figcaption>\( g \) läuft parallel über \( E \). Das Lot von \( P \) trifft \( E \) im Fußpunkt \( F \); die Gerade \( j \) durch \( F \) parallel zu \( g \) ist die nächstgelegene Gerade in \( E \).</figcaption>
</figure>

<details><summary>Haltung dahinter: Warum ist gerade die projizierte Gerade die nächste? (ganz von vorn)</summary>

**Projektion = senkrechter Schatten.** Stell dir \( g \) als waagerechte Stange knapp über einem
geneigten Tisch (\( E \)) vor, parallel zur Tischfläche. Beleuchtet man sie **senkrecht von oben** (in
Normalenrichtung), wirft sie auf den Tisch einen geraden Schatten, der genau unter ihr liegt und
**parallel** zu ihr ist. Dieser Schatten ist \( j \).

**Warum der nächste?** Weil \( g \) parallel zu \( E \) ist, hat **jeder** Punkt von \( g \) denselben
Abstand zur Ebene (die Stange hängt überall gleich hoch). Der senkrechte Schatten verbindet jeden
Stangenpunkt auf **kürzestem** Weg mit dem Tisch. Eine andere Gerade in \( E \), die schräg unter der
Stange läuft, wäre an manchen Stellen weiter weg. Deshalb ist die senkrechte Projektion die Gerade mit
dem **geringsten** Abstand.

**Warum genügt ein einziger Punkt \( P \)?** Weil der Abstand überall gleich ist, reicht es, **einen**
Punkt von \( g \) (den Stützpunkt \( P \)) senkrecht herunterzuloten — sein Fußpunkt \( F \) liegt schon
auf \( j \). Die Richtung von \( j \) ist dieselbe wie die von \( g \) (beide parallel). Stützpunkt
\( F \) + Richtung \( (2|1|1) \) = fertige Geradengleichung.

<details><summary>… ganz langsam (mit Zahlen) — wie der Schnittpunkt \( F \) entsteht</summary>

Die Lotgerade hat die Punkte \( (2+s\,|\,2s\,|\,2-4s) \). „Auf der Ebene" heißt: in
\( x_1+2x_2-4x_3 \) eingesetzt kommt \( 1 \) heraus. Einsetzen:

\( (2+s) + 2\cdot(2s) - 4\cdot(2-4s) \). Klammern auflösen: \( 2+s + 4s - 8 + 16s \). Die
\( s \)-Stücke sammeln: \( s+4s+16s = 21s \). Die Zahlen sammeln: \( 2-8 = -6 \). Also \( 21s - 6 \).
Das soll \( 1 \) sein: \( 21s-6=1 \Rightarrow 21s=7 \Rightarrow s=\tfrac{7}{21}=\tfrac13 \).

Jetzt \( s=\tfrac13 \) in den Lotpunkt: \( x_1=2+\tfrac13=\tfrac73 \); \( x_2=2\cdot\tfrac13=\tfrac23 \);
\( x_3=2-4\cdot\tfrac13=2-\tfrac43=\tfrac{6-4}{3}=\tfrac23 \). Das ist \( F \). Der Abstand ist
\( \tfrac13 \) Normalenvektoren lang: \( \tfrac13\sqrt{21}=\tfrac{\sqrt{21}}{3} \).

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- **a)** Drei Lagen: \( g \) liegt in \( E \) · \( g \) echt parallel zu \( E \) · \( g \) schneidet
  \( E \). Bestimmung: Geradengleichung in die Ebenengleichung einsetzen → Widerspruch = echt parallel,
  eine Lösung = Schnittpunkt, immer wahr = \( g\subset E \).
- **b)** \( \vec v\cdot\vec n=(2|1|1)\cdot(1|2|-4)=0 \Rightarrow g\parallel E \); Punktprobe \( -6\neq 1 \)
  ⇒ echt parallel. \( h:\ \vec x=(2|0|2)+t\,(-2|3|1) \) (Richtung \( =\vec v\times\vec n \)).
- **c)** \( R(4\,|\,6\,|\,-12) \) \( \big(=Q(1|0|0)+3\vec n,\ |\vec n|=\sqrt{21}\big) \).
- **d)** Lot \( k:\ \vec x=(2|0|2)+s\,(1|2|-4) \) → Fußpunkt \( F=(\tfrac73|\tfrac23|\tfrac23) \) →
  \( j:\ \vec x=F+t\,(2|1|1) \); geringster Abstand \( \tfrac{\sqrt{21}}{3}\approx1{,}53 \).

</details>

---

## Teil 2 — Gespräch (Analysis): Schneefallrate im Skigebiet

<div class="aufgabenkasten">

**Input.** Die Funktion \( f \) mit \( f(x)=10x\cdot e^{-0{,}5x} \) beschreibt für \( x\ge 0 \)
modellhaft die **Schneefallrate** in einem Skigebiet (\( x \) in Stunden nach 6 Uhr, \( f(x) \) in cm
pro Stunde). Eine der beiden Abbildungen zeigt den Graphen von \( f \).

**Im Gespräch denkbare Aspekte:**
**(AB I)** den richtigen Graphen zuordnen; die Schneefallrate nach einer Stunde ermitteln; den Zeitpunkt
des stärksten Schneefalls graphisch bestimmen; den Zeitpunkt der stärksten Abnahme der Rate graphisch
ermitteln. **(AB II)** den Zeitpunkt des stärksten Schneefalls berechnen; den Zuwachs an Schneehöhe in
den ersten fünf Stunden graphisch ermitteln. **(AB III)** unter der Annahme, dass die Rate ab
\( x=4 \) konstant abnimmt, rechnerisch den Zeitpunkt bestimmen, zu dem es aufhört zu schneien; unter der
Annahme eines gleichzeitigen Tauens mit \( 2 \) cm pro Stunde die Zeitspanne ermitteln, in der die
Schneehöhe zunimmt.

</div>

> **Vorab, was eine „Rate" ist:** \( f(x) \) gibt **nicht** die Schneehöhe an, sondern wie **schnell**
> der Schnee gerade wächst — in cm **pro Stunde**. Bild: Der Tacho im Auto zeigt die Geschwindigkeit
> (km/h), nicht die gefahrene Strecke (km). Hier ist \( f \) der „Schnee-Tacho", die **Höhe** ist die
> aufsummierte Strecke (das Integral). Diesen Unterschied braucht man für die AB-II- und
> AB-III-Aspekte. Mehr in [Funktionsuntersuchung](kap-funktionsuntersuchung.html) und
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).

**Welcher Graph gehört zu \( f \)?** Spiele mit den Bildern und ordne zu, bevor du die Lösung aufklappst.
Der Unterschied steckt in der **Höhe des höchsten Punktes**.

<div class="graph-row">
<figure>
<div class="jxgbox" id="jxg-k6-abb1" style="width:100%;max-width:320px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 1</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k6-abb2" style="width:100%;max-width:320px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 2</figcaption>
</figure>
</div>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k6-abb1',{boundingbox:[-0.8,9.6,12.6,-1.4],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 10*x*Math.exp(-0.5*x);},0,12.5],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k6-abb2',{boundingbox:[-0.8,9.6,12.6,-1.4],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 11.5*x*Math.exp(-0.5*x);},0,12.5],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>

### AB I — Graph zuordnen, Rate nach einer Stunde, stärkster Schneefall & stärkste Abnahme (graphisch)

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Graph zuordnen.** Beide Graphen starten in \( (0|0) \), steigen schnell zu einem Hoch und fallen dann
flach aus — die Form ist gleich. Der Unterschied ist die **Höhe des Maximums**. Man rechnet einen
markanten Wert nach, z. B. den Höchstwert bei \( x=2 \):

\[ f(2)=10\cdot 2\cdot e^{-0{,}5\cdot 2}=20\,e^{-1}=\frac{20}{e}\approx 7{,}4 . \]

Der höchste Punkt liegt also bei rund \( 7{,}4 \) cm/h. **Abbildung 1** hat ihr Maximum bei knapp über
\( 7 \) — das passt. Abbildung 2 erreicht etwa \( 8{,}5 \) und scheidet aus. **Antwort: Abbildung 1.**

**Schneefallrate nach einer Stunde.** „Nach einer Stunde" ist \( x=1 \) (also um 7 Uhr):

\[ f(1)=10\cdot 1\cdot e^{-0{,}5}=\frac{10}{\sqrt{e}}\approx 6{,}1 . \]

Eine Stunde nach Beginn schneit es also mit etwa **\( 6{,}1 \) cm pro Stunde** (im Graphen bei \( x=1 \)
ablesbar als \( y\approx 6 \)).

**Zeitpunkt des stärksten Schneefalls (graphisch).** Am stärksten schneit es, wo die Rate \( f \) am
**größten** ist — am **höchsten Punkt** des Graphen. Den liest man bei \( x=2 \) ab. Das sind \( 2 \)
Stunden nach 6 Uhr, also **um 8 Uhr**.

**Zeitpunkt der stärksten Abnahme der Rate (graphisch).** Gesucht ist, wo die Rate am schnellsten
**fällt** — die Stelle, an der der Graph nach dem Hoch **am steilsten bergab** läuft. Diese steilste
Abstiegsstelle (der Wendepunkt des fallenden Astes) liegt bei etwa \( x=4 \), also **um 10 Uhr**.

<details><summary>Haltung dahinter: „stärkster Schneefall" vs. „stärkste Abnahme" — was liest man wo ab?</summary>

Hier werden zwei Dinge leicht verwechselt. Beide liest man am **selben** Graphen \( f \) ab, aber an
**verschiedenen** Stellen.

- **Stärkster Schneefall** fragt: *Wann ist die Rate am größten?* → höchster **Punkt** des Graphen
  (Hochpunkt). Anschaulich: Wann fällt am meisten Schnee pro Stunde? Antwort: am Gipfel der Kurve,
  \( x=2 \).
- **Stärkste Abnahme der Rate** fragt: *Wann sinkt die Rate am schnellsten?* → steilste **abfallende
  Stelle** des Graphen. Anschaulich: Wann lässt der Schneefall am rasantesten nach? Das ist nicht der
  Gipfel (dort ist die Kurve flach), sondern weiter rechts, wo es am steilsten bergab geht — bei
  \( x\approx 4 \).

Eselsbrücke: „am stärksten schneit es" = **höchster Punkt**; „am stärksten lässt es nach" = **steilster
Abhang**.

<details><summary>Was ist ein „Wendepunkt", und warum ist er die steilste Abstiegsstelle?</summary>

Ein **Wendepunkt** ist die Stelle, an der eine Kurve ihre **Krümmungsrichtung** wechselt — von
„Linkskurve" zu „Rechtskurve" (oder umgekehrt). Beim Bergfahren ist das der Moment, in dem die Straße
aufhört, immer steiler zu werden, und anfängt, wieder flacher zu werden. Genau dort, am Übergang, ist die
Steigung **am extremsten** — beim fallenden Ast also **am stärksten negativ**, sprich am steilsten
bergab. Deshalb fällt die Rate genau am Wendepunkt am schnellsten. (Rechnerisch bestimmt man ihn über
\( f''(x)=0 \); siehe AB III. Hier genügt das **Ablesen** der steilsten Stelle.)

</details>
</details>
</details>

### AB II — Stärksten Schneefall berechnen, Zuwachs der Schneehöhe (graphisch)

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Zeitpunkt des stärksten Schneefalls berechnen.** Der Höchstwert der Rate ist dort, wo die
**Ableitung** \( f' \) null wird (waagerechte Tangente). Mit der **Produktregel** und der **Kettenregel**:

\[ f(x)=10x\,e^{-0{,}5x}\;\Longrightarrow\; f'(x)=10\,e^{-0{,}5x}+10x\cdot(-0{,}5)\,e^{-0{,}5x}
   = e^{-0{,}5x}\,(10-5x). \]

Der Faktor \( e^{-0{,}5x} \) ist **nie** null, also entscheidet die Klammer:

\[ 10-5x=0 \;\Longrightarrow\; x=2 . \]

Vorzeichenwechsel von \( + \) nach \( - \) ⇒ Hochpunkt. Es schneit am stärksten bei **\( x=2 \) (um 8
Uhr)** mit \( f(2)=\tfrac{20}{e}\approx 7{,}4 \) cm/h. (Das bestätigt das Ablesen aus AB I.)

**Zuwachs der Schneehöhe in den ersten fünf Stunden (graphisch).** Die Schneehöhe ist die
**aufsummierte** Rate, also die **Fläche unter dem Graphen** von \( x=0 \) bis \( x=5 \). „Graphisch"
heißt: die Kästchen unter der Kurve zählen.

<figure>
<div class="jxgbox" id="jxg-k6-flaeche" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Schneehöhe nach 5 Stunden = Fläche unter der Ratenkurve von \( x=0 \) bis \( x=5 \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k6-flaeche',{boundingbox:[-0.8,9.6,12.6,-1.4],axis:true,showCopyright:false,showNavigation:false});var f=function(x){return 10*x*Math.exp(-0.5*x);};var xs=[0],ys=[0];for(var i=0;i<=60;i++){var x=5*i/60;xs.push(x);ys.push(f(x));}xs.push(5);ys.push(0);b.create('curve',[xs,ys],{strokeWidth:0,fillColor:'#d98324',fillOpacity:0.20});b.create('functiongraph',[f,0,12.5],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('line',[[5,0],[5,7]],{straightFirst:false,straightLast:false,strokeColor:'#7a7163',strokeWidth:1,dash:2});})();</script>

Ein Kästchen ist \( 1 \) Stunde breit und \( 1 \) cm/h hoch, steht also für \( 1\,\text{cm/h}\times
1\,\text{h}=1 \) **cm Schnee**. Zählt man die Kästchen unter der Kurve bis \( x=5 \), kommt man auf
**etwa \( 28\text{–}29 \) cm**. In den ersten fünf Stunden wächst die Schneehöhe also um rund
\( 28 \) cm.

<details><summary>Haltung dahinter: Warum ist die Fläche unter der Rate die Schneehöhe? (ganz von vorn)</summary>

**Ableitung = Steigung.** Die Ableitung \( f' \) misst, wie steil ein Graph an einer Stelle ist. Am
**Hochpunkt** ist der Graph für einen Moment waagerecht — die Steigung ist \( 0 \). Deshalb sucht man
Hoch- und Tiefpunkte über \( f'(x)=0 \).

**Fläche unter der Rate = Gesamtmenge.** Eine Rate sagt „so viel pro Stunde". Multipliziert man Rate mal
Zeit, bekommt man eine **Menge**: \( 6\ \tfrac{\text{cm}}{\text{h}}\times 2\ \text{h}=12\ \text{cm} \).
Genau das macht die Fläche unter der Kurve — sie multipliziert in jedem schmalen Streifen „Höhe (Rate)
mal Breite (Zeitstückchen)" und summiert alles auf. Ergebnis: die in dieser Zeit gefallene **Schneehöhe**.
Bild: Auf dem Bankkonto ist die Rate „Euro pro Tag"; die Fläche darunter ist das insgesamt
angesammelte Geld. (Mehr: [Integral-Grundlagen](kap-integral-grundlagen.html).)

<details><summary>… ganz langsam (mit Zahlen) — Kontrolle des Kästchen-Zählens</summary>

Kästchen zählen ist eine Schätzung; zur Kontrolle kann man die Fläche **exakt** als Integral rechnen.
Eine Stammfunktion von \( f(x)=10x\,e^{-0{,}5x} \) ist (per partieller Integration)
\( F(x)=-20\,(x+2)\,e^{-0{,}5x} \). Probe durch Ableiten ergibt wieder \( f \). Dann

\[ \int_0^5 f(x)\,dx=F(5)-F(0)=-20\cdot 7\cdot e^{-2{,}5}-\big(-20\cdot 2\cdot e^{0}\big)
   =40-140\,e^{-2{,}5}\approx 28{,}5 . \]

Das passt zu den gezählten \( \approx 28\text{–}29 \) Kästchen. (In der Prüfung ist hier ausdrücklich nur
das **Zählen** gefragt; die exakte Rechnung dient nur der Kontrolle.)

</details>

<details><summary>Typische Falle: Höhe mit Rate verwechseln</summary>

\( f(5)\approx 4{,}1 \) ist die **Rate** um 11 Uhr (cm pro Stunde), **nicht** die Schneehöhe. Die Höhe
nach 5 Stunden ist die **Fläche** \( \approx 28 \) cm. Wer den Funktionswert \( f(5) \) als Schneehöhe
angibt, verwechselt Tacho mit Kilometerstand.

</details>
</details>
</details>

### AB III — Wann hört es auf zu schneien? · Wann wächst die Schneehöhe trotz Tauen?

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Verfahren anzeigen</summary>

**Annahme 1: Ab \( x=4 \) nimmt die Rate konstant ab — wann hört es auf zu schneien?** „Konstant
abnehmen" heißt: Die Rate fällt ab \( x=4 \) geradlinig (linear) weiter — und zwar mit der Steigung, die
sie **im Punkt \( x=4 \)** gerade hat. Das ist die **Tangente** an \( f \) in \( x=4 \). Es hört auf zu
schneien, wenn die Rate \( 0 \) erreicht — also dort, wo diese Tangente die \( x \)-Achse trifft.

Man braucht den Funktionswert und die Steigung bei \( x=4 \):

\[ f(4)=40\,e^{-2},\qquad f'(4)=e^{-2}\,(10-5\cdot 4)=-10\,e^{-2}. \]

Tangente: \( y=f(4)+f'(4)\,(x-4) \). Nullsetzen und nach \( x \) auflösen:

\[ 0=f(4)+f'(4)\,(x-4)\;\Longrightarrow\; x=4-\frac{f(4)}{f'(4)}=4-\frac{40\,e^{-2}}{-10\,e^{-2}}=4+4=8 . \]

Die \( e^{-2} \) kürzen sich weg — es bleibt das saubere Ergebnis \( x=8 \). Es hört also bei
**\( x=8 \), das heißt um 14 Uhr**, auf zu schneien.

<figure>
<div class="jxgbox" id="jxg-k6-tangente" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Ab \( x=4 \) ersetzt die Tangente (orange) die Kurve. Sie trifft die \( x \)-Achse bei \( x=8 \) — dann ist die Rate 0.</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k6-tangente',{boundingbox:[-0.8,9.6,12.6,-1.4],axis:true,showCopyright:false,showNavigation:false});var f=function(x){return 10*x*Math.exp(-0.5*x);};b.create('functiongraph',[f,0,12.5],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('line',[[4,40*Math.exp(-2)],[8,0]],{strokeColor:'#d98324',strokeWidth:2,dash:0,straightFirst:true,straightLast:true});b.create('point',[4,40*Math.exp(-2)],{name:'x=4',size:2,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',label:{offset:[8,12],fontSize:11}});b.create('point',[8,0],{name:'Stopp x=8',size:2,fixed:true,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[6,-12],fontSize:11}});})();</script>

**Annahme 2: Es taut gleichzeitig mit \( 2 \) cm pro Stunde — wann wächst die Schneehöhe?** Jetzt
laufen zwei Raten gegeneinander: Es schneit mit \( f(x) \) und es taut mit \( 2 \). Die **Netto-Rate**
der Schneehöhe ist \( f(x)-2 \). Die Höhe **wächst**, solange die Netto-Rate **positiv** ist, also
solange

\[ f(x)>2 \qquad\Longleftrightarrow\qquad 10x\,e^{-0{,}5x}>2 . \]

**Verfahren:** Man bestimmt die beiden Schnittstellen der Kurve \( f \) mit der waagerechten Linie
\( y=2 \). Dazwischen liegt \( f \) **über** \( 2 \), dort wächst die Höhe; davor und danach taut es netto
weg. Die Gleichung \( 10x\,e^{-0{,}5x}=2 \) ist **nicht** von Hand auflösbar (das \( x \) steckt
gleichzeitig als Faktor und im Exponenten) — man löst sie mit dem **Taschenrechner** (GTR, numerisch).
Das liefert

\[ x_1\approx 0{,}22 \qquad\text{und}\qquad x_2\approx 7{,}15 . \]

Die Schneehöhe nimmt also **zwischen \( x_1\approx 0{,}22 \) und \( x_2\approx 7{,}15 \)** zu — eine
Zeitspanne von

\[ x_2-x_1\approx 7{,}15-0{,}22 = 6{,}93\ \text{Stunden}\ (\text{rund }6\tfrac{9}{10}\ \text{h}). \]

In Uhrzeit: von etwa \( 6{:}13 \) Uhr bis etwa \( 13{:}09 \) Uhr.

<figure>
<div class="jxgbox" id="jxg-k6-tauen" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Schneehöhe wächst, solange die Rate \( f \) über der Taurate \( y=2 \) liegt (oranger Bereich, \( x_1\approx0{,}22 \) bis \( x_2\approx7{,}15 \)).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k6-tauen',{boundingbox:[-0.8,9.6,12.6,-1.4],axis:true,showCopyright:false,showNavigation:false});var f=function(x){return 10*x*Math.exp(-0.5*x);};var x1=0.2237,x2=7.1543;var xs=[],ys=[];for(var i=0;i<=80;i++){var x=x1+(x2-x1)*i/80;xs.push(x);ys.push(f(x));}xs.push(x2);ys.push(2);xs.push(x1);ys.push(2);b.create('curve',[xs,ys],{strokeWidth:0,fillColor:'#d98324',fillOpacity:0.18});b.create('functiongraph',[f,0,12.5],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('line',[[0,2],[1,2]],{strokeColor:'#3a8a5a',strokeWidth:1.8,dash:2});b.create('point',[x1,2],{name:'',size:1.5,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a'});b.create('point',[x2,2],{name:'',size:1.5,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a'});b.create('text',[8.3,2.6,'y = 2 (Tauen)'],{fontSize:11,color:'#3a8a5a'});})();</script>

<details><summary>Haltung dahinter: Was ist eine Tangente, und warum löst „Netto-Rate" die zweite Frage? (ganz von vorn)</summary>

**Tangente.** Eine Tangente ist die Gerade, die sich an einer Stelle **schmiegend** an die Kurve legt —
sie hat dort denselben Punkt und dieselbe **Steigung** wie die Kurve. „Die Rate nimmt ab \( x=4 \)
konstant ab" bedeutet genau: Ab \( x=4 \) machen wir aus der gebogenen Kurve eine **gerade** Fortsetzung
mit der Steigung, die sie bei \( x=4 \) gerade hat — also die Tangente. Eine fallende Gerade trifft
irgendwann die \( x \)-Achse; dort ist die Rate \( 0 \) → es schneit nicht mehr. Den Treffer findet man,
indem man die Tangentengleichung gleich \( 0 \) setzt.

**Netto-Rate.** Wenn zwei Vorgänge gleichzeitig wirken — Schnee fällt (\( +f \)), Schnee taut
(\( -2 \)) —, zählt für die **Höhe** nur ihre Differenz, die Netto-Rate \( f(x)-2 \). Bild: Wasser läuft
in eine Wanne (Zufluss \( f \)) und gleichzeitig durch den Abfluss heraus (\( 2 \)). Der Wasserstand
**steigt** nur, wenn **mehr hinein- als hinausläuft**, also wenn \( f(x)>2 \). Die Grenzen dieses
Zeitfensters sind die Stellen, an denen Zufluss und Abfluss gleich groß sind: \( f(x)=2 \).

<details><summary>… ganz langsam (mit Zahlen) — warum \( x=8 \) so glatt herauskommt</summary>

Tangentengleichung allgemein: \( y=f(4)+f'(4)\,(x-4) \). Wir wollen \( y=0 \), also
\( f'(4)\,(x-4)=-f(4) \), das heißt \( x-4=-\dfrac{f(4)}{f'(4)} \).

Jetzt die Werte: \( f(4)=40\,e^{-2} \) und \( f'(4)=-10\,e^{-2} \). Der Bruch:
\( \dfrac{f(4)}{f'(4)}=\dfrac{40\,e^{-2}}{-10\,e^{-2}} \). Der Faktor \( e^{-2} \) steht oben **und** unten
und kürzt sich weg, übrig bleibt \( \dfrac{40}{-10}=-4 \). Also \( x-4=-(-4)=4 \), und damit
\( x=4+4=8 \). Genau \( 8 \) Stunden nach 6 Uhr = **14 Uhr**.

</details>

<details><summary>Typische Falle: bei der Tau-Frage ein „sauberes" \( x \) erzwingen wollen</summary>

Die Gleichung \( 10x\,e^{-0{,}5x}=2 \) hat **keine** schöne Lösung von Hand — das \( x \) steckt als
Faktor *und* im Exponenten. Hier ist der sachliche Weg: Verfahren beschreiben (Schnittstellen mit
\( y=2 \), Bereich dazwischen), die Zahlen mit dem GTR holen (\( x_1\approx0{,}22 \), \( x_2\approx7{,}15 \))
und die Zeitspanne als Differenz angeben. Wer hier „algebraisch umstellt", verrennt sich.

</details>
</details>
</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Teilaufgabe, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen kannst.
Du musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Geometrie) aufklappen</summary>

- **a) Lage Gerade/Ebene.** Gut: **drei** Fälle genannt (in der Ebene · echt parallel · Schnittpunkt)
  **und** das Verfahren „Geraden- in Ebenengleichung **einsetzen**, nach \( t \) auflösen". *Rückfrage:*
  „Woran erkennen Sie beim Einsetzen den Unterschied zwischen *echt parallel* und *liegt in der Ebene*?"
  (Antwort: Widerspruch vs. immer wahre Aussage.) *Rote Flagge:* nur zwei Fälle, „liegt in der Ebene"
  vergessen.
- **b) Parallelität + Gerade \( h \).** Erwartet: **Skalarprodukt** Richtung·Normale \( =0 \) ⇒ parallel,
  plus **Punktprobe** \( -6\neq 1 \) ⇒ echt parallel; für \( h \) die Richtung über das **Kreuzprodukt**
  \( (2|1|1)\times(1|2|-4)=(-6|9|3)\parallel(-2|3|1) \), Stützpunkt \( P(2|0|2) \). *Rückfrage:* „Warum
  muss die Richtung von \( h \) auf *beiden* Vektoren senkrecht stehen?" (orthogonal zu \( g \) **und**
  parallel zu \( E \)).
- **c) Punkt mit Abstand \( 3\sqrt{21} \).** Erwartet: \( |\vec n|=\sqrt{21} \); einen **Punkt auf \( E \)**
  wählen (\( Q(1|0|0) \)) und **\( 3\vec n \)** addieren → \( R(4|6|-12) \). *Rückfrage:* „Warum starten
  Sie ausgerechnet auf der Ebene?" *Rote Flagge:* \( 3\vec n \) zu einem beliebigen Punkt addiert.
- **d) Gerade \( j \).** Hier zählt das **beschriebene Verfahren**: **Lot** von einem \( g \)-Punkt auf
  \( E \) (Gerade in **Normalenrichtung**), **Fußpunkt \( F \)** als Schnitt mit \( E \), dann \( j \)
  durch \( F \) mit der **Richtung von \( g \)**. *Hinweis für dich:* Es ist nur das Verfahren verlangt —
  eine saubere Beschreibung ist die volle Antwort; die konkreten Zahlen (\( F=(\tfrac73|\tfrac23|\tfrac23) \))
  sind Bonus. *Rückfrage:* „Warum ist gerade der senkrechte Schatten von \( g \) die nächstgelegene
  Gerade?"

</details>

<details><summary>Leitfaden Teil 2 (Analysis) aufklappen</summary>

- **Graph zuordnen.** Erwartet: einen Wert nachrechnen (z. B. \( f(2)=\tfrac{20}{e}\approx 7{,}4 \)) und
  die **Höhe des Maximums** vergleichen → **Abbildung 1**. *Rückfrage:* „Welche Stelle haben Sie
  verglichen, und warum?"
- **Rate nach 1 h / stärkster Schneefall (graphisch).** Erwartet: \( f(1)\approx 6{,}1 \) cm/h;
  stärkster Schneefall am **höchsten Punkt**, \( x=2 \) (8 Uhr). *Rückfrage:* „Geben \( f \)-Werte eine
  Höhe oder eine Geschwindigkeit an?" (Rate, cm pro Stunde.)
- **Stärkste Abnahme (graphisch).** Erwartet: **steilste abfallende Stelle** (Wendepunkt), \( x\approx 4 \)
  (10 Uhr) — *nicht* der Gipfel. *Rote Flagge:* den Hochpunkt \( x=2 \) nennen.
- **Stärksten Schneefall berechnen.** Erwartet: \( f'(x)=e^{-0{,}5x}(10-5x)=0 \) ⇒ \( x=2 \), weil
  \( e^{-0{,}5x}\neq 0 \). *Rückfrage:* „Warum kann nur die Klammer null werden?"
- **Zuwachs Schneehöhe erste 5 h (graphisch).** Erwartet: **Fläche** unter der Kurve von 0 bis 5,
  Kästchen zählen ≈ **28–29 cm**. *Rote Flagge:* \( f(5)\approx 4 \) als „Höhe" angeben (das ist die
  Rate). *Rückfrage:* „Wofür steht ein einzelnes Kästchen in cm?"
- **AB III — Aufhören / Tauen.** Erwartet: für das Aufhören die **Tangente in \( x=4 \)**, Nullstelle bei
  **\( x=8 \) (14 Uhr)**; fürs Tauen die **Netto-Rate \( f(x)-2 \)**, wachsend solange \( f(x)>2 \),
  Schnittstellen mit \( y=2 \) per **GTR** (\( x_1\approx 0{,}22 \), \( x_2\approx 7{,}15 \)), Zeitspanne
  \( \approx 6{,}9 \) h. *Hinweis für dich:* Dass \( f(x)=2 \) nur numerisch (GTR) lösbar ist, ist
  korrekt und kein Fehler. *Rückfrage:* „Warum wächst die Schneehöhe genau dann, wenn \( f \) über der
  Linie \( y=2 \) liegt?"

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Welche drei Lagen kann eine Gerade zu einer Ebene haben, und wie unterscheidest du sie beim Einsetzen?
- Warum bedeutet „Richtungsvektor · Normalenvektor \( =0 \)", dass die Gerade parallel zur Ebene läuft?
- Wie findest du einen Punkt in vorgegebenem Abstand zu einer Ebene — und warum musst du dabei *auf* der
  Ebene starten?
- Woran erkennst du im Graphen den Zeitpunkt des *stärksten Schneefalls* und den der *stärksten Abnahme*
  der Rate — und warum sind das verschiedene Stellen?
- Warum ist die Schneehöhe die *Fläche* unter der Ratenkurve, und nicht ein einzelner Funktionswert?
- Wie bestimmst du den Zeitpunkt, zu dem es bei konstanter Abnahme ab \( x=4 \) aufhört zu schneien?
