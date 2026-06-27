# Werkzeugkasten Geometrie

Kompakte Nachschlage-Sammlung der **Vektor- und Raumgeometrie-Werkzeuge**, die in den
Konvolut-Aufgaben immer wiederkehren. Jeder Eintrag sagt in zwei Sätzen, *was* das Werkzeug ist,
*wann* man es nimmt, und zeigt die Formel an einem winzigen Beispiel. Gedacht zum Verlinken aus den
Aufgaben — und zum schnellen Auffrischen, wenn ein Begriff im Lösungsweg auftaucht.

<span class="tag tag-ok">Nachschlagewerk — kein Prüfungsstoff „am Stück", sondern Bausteine</span>

## Punkt und Vektor

Ein **Punkt** ist ein Ort im Raum mit drei Koordinaten \( P(x_1\mid x_2\mid x_3) \). Ein **Vektor** ist
ein **Pfeil** (eine Bewegung mit Richtung und Länge), geschrieben als Spalte. Den Verbindungspfeil von
\( A \) nach \( B \) rechnet man als **„Ziel minus Start"**:

\[ \overrightarrow{AB} = B - A. \]

*Beispiel.* \( A(1\mid0\mid2),\ B(4\mid2\mid2) \Rightarrow \overrightarrow{AB} = \begin{pmatrix}3\\2\\0\end{pmatrix} \)
(„3 nach \( x_1 \), 2 nach \( x_2 \), 0 nach \( x_3 \)").

## Länge (Betrag) eines Vektors

Die **Länge** eines Pfeils ist der Abstand zwischen Start und Ziel. Man quadriert die drei Zahlen,
addiert sie und zieht die Wurzel — der **Satz des Pythagoras in 3D**:

\[ \left|\begin{pmatrix}a\\b\\c\end{pmatrix}\right| = \sqrt{a^2+b^2+c^2}. \]

*Wozu?* Seitenlängen, Abstände, Nachweis „gleich lang" (z. B. gleichschenklig).
*Beispiel.* \( \left|(2,\,-1,\,2)\right| = \sqrt{4+1+4} = \sqrt{9} = 3 \). (Minus wird beim Quadrieren
zu Plus.)

## Mittelpunkt einer Strecke

Der Mittelpunkt liegt genau zwischen zwei Punkten — man **mittelt** ihre Koordinaten:

\[ M = \tfrac12\,(A + B). \]

*Wozu?* Mitte einer Kante, Mittelpunkt eines Quadrats (über zwei **gegenüberliegende** Ecken),
Symmetrie. *Beispiel.* Mitte von \( A(0\mid0\mid0) \) und \( C(3\mid3\mid0) \) ist
\( M(1{,}5\mid1{,}5\mid0) \).

## Skalarprodukt

Das **Skalarprodukt** zweier Vektoren ist eine **Zahl** (kein Pfeil): zugehörige Zahlen
multiplizieren und addieren.

\[ \vec a \cdot \vec b = a_1b_1 + a_2b_2 + a_3b_3. \]

Zwei Anwendungen:

- **Senkrecht-Test:** \( \vec a \cdot \vec b = 0 \) bedeutet, die beiden Pfeile stehen **rechtwinklig**
  aufeinander (orthogonal).
- **Winkel** zwischen Vektoren: \( \displaystyle \cos\varphi = \frac{\vec a\cdot\vec b}{|\vec a|\,|\vec b|}. \)

*Beispiel.* \( (1,2,1)\cdot(1,1,-3) = 1+2-3 = 0 \) → die beiden stehen senkrecht zueinander.

## Kreuzprodukt

Das **Kreuzprodukt** zweier Vektoren liefert einen **neuen Pfeil**, der auf **beiden** Ausgangspfeilen
senkrecht steht. Genau so findet man einen **Normalenvektor** einer Ebene (zwei Pfeile in der Ebene
nehmen, Kreuzprodukt bilden). Rechenschema (jede Zeile: „über Kreuz" der beiden anderen Zeilen):

\[ \begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}\times\begin{pmatrix}b_1\\b_2\\b_3\end{pmatrix}
   = \begin{pmatrix}a_2b_3 - a_3b_2\\ a_3b_1 - a_1b_3\\ a_1b_2 - a_2b_1\end{pmatrix}. \]

*Tipp.* Das Ergebnis darf man **kürzen** (z. B. \( (12,0,4{,}5)\parallel(8,0,3) \)) — das ändert nur die
Länge, nicht die Richtung, und nur die Richtung zählt für die Ebene.
*Beispiel.* \( (0,3,0)\times(-1{,}5,\,1{,}5,\,4) = (12,\,0,\,4{,}5) \).

## Geradengleichung (Parameterform)

Eine **Gerade** beschreibt man durch einen **Stützpunkt** \( \vec p \) (ein Punkt auf der Geraden) und
einen **Richtungsvektor** \( \vec u \) (in welche Richtung sie läuft):

\[ g:\ \vec x = \vec p + t\cdot \vec u, \quad t\in\mathbb{R}. \]

Jeder Wert von \( t \) liefert einen Punkt der Geraden. *Wozu?* Kanten, Sichtlinien, Lichtstrahlen
(Schattenwurf), Schnittpunkt-Rechnungen.

## Ebenengleichung: Koordinaten- und Normalenform

Eine **Ebene** ist eine unendlich ausgedehnte flache Fläche. Zwei gängige Schreibweisen:

- **Normalenform:** \( \vec n \cdot (\vec x - \vec p) = 0 \) — „der Pfeil von einem Ebenenpunkt \( \vec p \)
  zu jedem anderen Ebenenpunkt steht senkrecht auf dem Normalenvektor \( \vec n \)".
- **Koordinatenform:** \( n_1x_1 + n_2x_2 + n_3x_3 = d \) — die Koeffizienten sind die Komponenten des
  **Normalenvektors** \( \vec n \); die Zahl \( d \) erhält man durch Einsetzen eines bekannten
  Ebenenpunkts.

*Vorgehen.* Normalenvektor (oft per [Kreuzprodukt](#kreuzprodukt)) bestimmen → einen Punkt einsetzen →
\( d \) ablesen. *Beispiel.* \( \vec n=(8,0,3) \), Punkt \( B(3\mid0\mid0) \): \( 8\cdot3+3\cdot0=24 \),
also \( 8x_1+3x_3=24 \).

## Punktprobe

So prüft man, ob ein Punkt **auf** einer Geraden/Ebene liegt: seine Koordinaten **einsetzen** und
schauen, ob die Gleichung **aufgeht**.

*Beispiel.* Liegt \( S(1{,}5\mid1{,}5\mid4) \) auf \( 8x_1+3x_3=24 \)? \( 8\cdot1{,}5+3\cdot4 = 12+12 =
24 \) ✓ — ja. Bei einer Ebene durch drei Punkte ist die Punktprobe **mit allen dreien** die schnelle
Selbstkontrolle.

## Volumen und Oberfläche der Pyramide

- **Volumen:** \( V = \tfrac13\cdot G\cdot h \) — eine Pyramide füllt ein **Drittel** des Quaders mit
  gleicher Grundfläche \( G \) und Höhe \( h \).
- **Oberfläche:** \( O = G + (\text{Summe der Seitenflächen}) \). Bei quadratischer Grundfläche und
  senkrechter Spitze: \( O = G + 4\cdot\tfrac12\cdot(\text{Grundkante})\cdot h_s \), wobei \( h_s \) die
  **Dreieckshöhe** von der Spitze zur Mitte einer Grundkante ist (nicht die Pyramidenhöhe!).

## Winkel zwischen zwei Flächen

Anschaulich über ein **rechtwinkliges Dreieck** an der gemeinsamen Kante; dann
\( \tan\varphi = \dfrac{\text{Gegenkathete}}{\text{Ankathete}} \). Rechnerisch über die
**Normalenvektoren** beider Ebenen mit dem [Skalarprodukt](#skalarprodukt):
\( \cos\varphi = \dfrac{|\vec n_1\cdot \vec n_2|}{|\vec n_1|\,|\vec n_2|} \). Beide Wege sind gültig — das
anschauliche Dreieck ist mündlich oft überzeugender.
