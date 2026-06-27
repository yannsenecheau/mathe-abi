# Werkzeugkasten Stochastik

Kompakte Nachschlage-Sammlung der **Wahrscheinlichkeits-Werkzeuge**, die in den Konvolut-Aufgaben
wiederkehren. Jeder Eintrag sagt in zwei Sätzen, *was* das Werkzeug ist, *wann* man es nimmt, und zeigt
die Formel an einem winzigen Beispiel. Gedacht zum Verlinken aus den Aufgaben — und zum schnellen
Auffrischen, wenn ein Begriff im Lösungsweg auftaucht.

<span class="tag tag-ok">Nachschlagewerk — Bausteine, kein Prüfungsstoff „am Stück"</span>

## Zufallsgröße

Eine **Zufallsgröße** \( X \) ordnet jedem Ergebnis eines Zufallsversuchs eine **Zahl** zu — z. B. „die
gewürfelte Augenzahl" oder „Anzahl blauer Kugeln bei 15 Zügen". Eine **Wahrscheinlichkeit** \( P \) ist
eine Zahl zwischen \( 0 \) (unmöglich) und \( 1 \) (sicher), oft als Prozent. \( P(X=2) \) heißt „die
Wahrscheinlichkeit, dass \( X \) den Wert 2 annimmt".

## Laplace-Wahrscheinlichkeit

Wenn alle Ergebnisse **gleich wahrscheinlich** sind, gilt

\[ P(\text{Ereignis}) = \frac{\text{Anzahl der günstigen Ergebnisse}}{\text{Anzahl aller möglichen Ergebnisse}}. \]

*Beispiel.* Würfel: \( P(\text{gerade Zahl}) = \tfrac{3}{6} = \tfrac12 \) (günstig: 2, 4, 6).

## Erwartungswert

Der **Erwartungswert** \( E(X) \) ist der **langfristige Durchschnitt**: Würde man den Versuch sehr oft
wiederholen, läge der Mittelwert der Ergebnisse nahe bei \( E(X) \). Man rechnet **jeden Wert mal seiner
Wahrscheinlichkeit, alles addiert**:

\[ E(X) = \sum x_i\cdot P(X=x_i). \]

*Wichtig:* Der Erwartungswert ist **nicht** „der wahrscheinlichste Wert" und muss selbst gar nicht
vorkommen können. *Beispiel.* Würfel: \( E(X)=1\cdot\tfrac16+2\cdot\tfrac16+\dots+6\cdot\tfrac16 = 3{,}5 \).

<details><summary>Faires Spiel — wozu der Erwartungswert hier?</summary>

Ein Glücksspiel heißt **fair**, wenn der erwartete **Gewinn** (Auszahlung minus Einsatz) gleich
**null** ist — auf lange Sicht gewinnt und verliert niemand. Man bildet also \( E(\text{Gewinn}) \) und
prüft, ob \( 0 \) herauskommt. Ist \( E(\text{Gewinn})<0 \), verliert der Spieler auf Dauer.

</details>

## Bernoulli-Kette

Eine **Bernoulli-Kette** ist ein Versuch, der \( n \)-mal **unabhängig** wiederholt wird und bei dem es
jedes Mal nur **zwei** Ausgänge gibt: „Treffer" (Wahrscheinlichkeit \( p \)) oder „kein Treffer".
Typisch: **Ziehen mit Zurücklegen**. Die drei Bedingungen — fester Versuch, zwei Ausgänge,
gleichbleibendes \( p \), unabhängig — muss man im Gespräch benennen können.

## Binomialverteilung

Zählt \( X \) die **Anzahl der Treffer** in einer Bernoulli-Kette der Länge \( n \) mit
Trefferwahrscheinlichkeit \( p \), so ist \( X \) **binomialverteilt**:

\[ P(X=k) = \binom{n}{k}\,p^{k}\,(1-p)^{\,n-k}, \qquad E(X) = n\cdot p. \]

Der Binomialkoeffizient \( \binom{n}{k} \) („n über k") zählt, **auf wie viele Arten** \( k \) Treffer
auf \( n \) Versuche verteilt sein können. *Beispiel.* 15-mal ziehen, \( p=0{,}6 \):
\( E(X)=15\cdot0{,}6 = 9 \) — im Mittel 9 Treffer.

<details><summary>Kumulierte Wahrscheinlichkeit P(a ≤ X ≤ b)</summary>

„Höchstens \( k \)" schreibt man \( P(X\le k) \). Ein **Bereich** ist die Differenz zweier solcher
Werte:

\[ P(a\le X\le b) = P(X\le b) - P(X\le a-1). \]

*Beispiel.* \( P(5\le X\le 10) = P(X\le 10) - P(X\le 4) \). Solche kumulierten Werte liest man im Abitur
aus der Tabelle/dem Rechner ab.

</details>

## Ziehen ohne Zurücklegen

Wird **ohne Zurücklegen** gezogen (oder ist die Gesamtmenge klein), ändert sich \( p \) von Zug zu Zug —
dann ist \( X \) **nicht** binomialverteilt. Man rechnet über einen **Baum** mit angepassten Brüchen.
*Beispiel.* Aus 10 Personen (4 „passend") 3 ziehen, genau 2 passend:
\( 3\cdot\tfrac{4}{10}\cdot\tfrac{3}{9}\cdot\tfrac{6}{8} = 0{,}30 \) (der Faktor 3 zählt die
Reihenfolgen).

## Normalverteilung

Eine **normalverteilte** Zufallsgröße ist **stetig** (sie kann jeden Wert in einem Bereich annehmen) und
wird durch eine **Glockenkurve** beschrieben. Zwei Kennzahlen steuern sie:

- **Erwartungswert \( \mu \):** Lage der **Symmetrieachse** und des **Hochpunkts** der Glocke.
- **Standardabweichung \( \sigma \):** Maß für die **Breite**. Die **Wendepunkte** der Glocke liegen bei
  \( \mu-\sigma \) und \( \mu+\sigma \). Größeres \( \sigma \) → flacher und breiter.

Wahrscheinlichkeiten sind **Flächen** unter der Kurve: \( P(a\le X\le b) \) ist die Fläche zwischen
\( a \) und \( b \). *Beispiel.* \( P(X\le 21) \) bei \( \mu=20 \) ist etwas mehr als die Hälfte, weil
\( 21 \) knapp rechts der Mitte liegt.

<details><summary>Binomial- gegen Normalverteilung — der Zusammenhang</summary>

Die **Binomialverteilung** ist **diskret** (nur ganze Trefferzahlen, Balkendiagramm); die
**Normalverteilung** ist **stetig** (durchgehende Kurve). Für großes \( n \) sieht die
Binomialverteilung aber fast wie eine Glockenkurve aus — die Normalverteilung ist dann eine gute
Näherung. Gemeinsam: glockenförmig, symmetrisch um den Erwartungswert. Unterschied: einzelne Werte
gegen Flächen.

</details>

## Vierfeldertafel

Eine **Vierfeldertafel** ordnet zwei Ja/Nein-Merkmale (z. B. „Interesse"/„kein Interesse" und
„passend"/„nicht passend") in einer 2×2-Tabelle; die Randfelder sind die Summen. Daraus liest man
Wahrscheinlichkeiten direkt ab und berechnet **bedingte** Wahrscheinlichkeiten (Anteil **innerhalb**
einer Zeile/Spalte).

<details><summary>Bedingte Wahrscheinlichkeit und Unabhängigkeit</summary>

- **Bedingte Wahrscheinlichkeit** \( P_B(A) \) („A, wenn B schon feststeht") = Anteil von A **innerhalb**
  von B: \( \displaystyle P_B(A) = \frac{P(A\cap B)}{P(B)} \).
- **Stochastische Unabhängigkeit:** A und B sind unabhängig, wenn das Eintreten des einen die
  Wahrscheinlichkeit des anderen **nicht** ändert. Test: \( P(A\cap B) = P(A)\cdot P(B) \). Kommt links
  und rechts dasselbe heraus → unabhängig; sonst nicht.

*Beispiel.* \( P(A)=41\%,\ P(B)=37\%,\ P(A\cap B)=22\% \): \( 0{,}41\cdot0{,}37 = 0{,}152 \neq 0{,}22 \)
→ **nicht** unabhängig.

</details>
