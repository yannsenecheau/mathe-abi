# Aufgabe 4 — Analysis & Stochastik

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Analysis**, **Teil 2 (Gespräch) aus der Stochastik**. Alles ist
**rechnerfrei** zu lösen (Teil 1 ausdrücklich „ohne WTR", also ohne Taschenrechner). Arbeitet die
Aufgabe wie eine echte Simulation durch — eine Person trägt vor, die andere prüft mit dem Lösungsweg und
dem [Prüfer-Leitfaden](#prufer-leitfaden-fur-die-abfragende-person) am Ende mit.

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
- Besonderheit bei dieser Aufgabe: **Teil 1** hat im Original einen amtlichen Lösungsschlüssel
  (Erwartungshorizont) — die Ergebnisse stehen also fest. **Teil 2** gibt im Original nur Gesprächs­themen
  vor; die ausgerechneten Lösungen hier sind selbst erarbeitet und vollständig nachgerechnet.

</details>

> **Werkzeug zum Nachschlagen:** Die Analysis-Werkzeuge stehen in den Kapiteln
> [Ableit-Handwerk](kap-ableiten-handwerk.html), [Integral-Grundlagen](kap-integral-grundlagen.html),
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html),
> [Funktionsuntersuchung](kap-funktionsuntersuchung.html),
> [Grundfunktionen](kap-grundfunktionen.html) und
> [Grenzwerte & Randverhalten](kap-grenzwerte-randverhalten.html). Die Stochastik-Werkzeuge
> (Erwartungswert, Normal- und Binomialverteilung) findest du kompakt im
> [Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html) (Anker u. a.
> [`#normalverteilung`](konv-91-werkzeugkasten-stochastik.html#normalverteilung),
> [`#binomialverteilung`](konv-91-werkzeugkasten-stochastik.html#binomialverteilung),
> [`#erwartungswert`](konv-91-werkzeugkasten-stochastik.html#erwartungswert)).

---

## Teil 1 — Vortrag (Analysis): Graph lesen, Stammfunktion deuten, Term zuordnen

<div class="aufgabenkasten">

**Teil 1: Analysis (ohne WTR).** Die Abbildung zeigt den Graphen einer Funktion \( f \).

**a)** Bestimme \( f'(0) \).

**b)** Ermittle \( \displaystyle\int_0^2 f(x)\,dx \).

**c)** \( F \) ist eine Stammfunktion von \( f \). Untersuche mit Hilfe des Graphen von \( f \), ob der
Graph von \( F \) im abgebildeten Bereich Hoch-, Tief- bzw. Wendepunkte besitzt. Gib gegebenenfalls die
entsprechenden Stellen an.

**d)** Entscheide, welche der folgenden Funktionsgleichungen zu \( f \) gehört, und begründe deine
Entscheidung:
\( f_1(x) = (x-2)\,e^{-x} \) ; \( f_2(x) = (x-2)\,e^{x} \) ; \( f_3(x) = x\,e^{x} - 2 \).

**e)** Der Graph der Funktion \( g \) mit \( g(x) = (x-2)^2\,e^{x} \) besitzt den Hochpunkt
\( H(0\,|\,4) \). Skizziere den Graphen von \( g \) und erläutere dein Vorgehen.

</div>

Hier ist der Graph von \( f \), wie ihn das Original zeigt — reproduziert aus dem Funktionsterm, den du
in Teilaufgabe d) selbst findest. Lies erst selbst ab, bevor du die Lösungen aufklappst.

<div class="graph-row">
<figure>
<div class="jxgbox" id="jxg-k4-fa" style="width:100%;max-width:340px;aspect-ratio:1/1"></div>
<figcaption>Graph von \( f \) mit Tangente in \( P(0\,|\,-2) \) — für a)</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k4-fb" style="width:100%;max-width:340px;aspect-ratio:1/1"></div>
<figcaption>Fläche zwischen Graph und \( x \)-Achse von \( 0 \) bis \( 2 \) — für b)</figcaption>
</figure>
</div>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k4-fa',{boundingbox:[-2.6,3.8,3,-3.6],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return (x-2)*Math.exp(x);},-2.6,2.6],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('functiongraph',[function(x){return -x-2;},-1.3,1.3],{strokeColor:'#d98324',strokeWidth:2,dash:2});b.create('point',[0,-2],{name:'P',size:2,fixed:true,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[8,-4]}});})();</script>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k4-fb',{boundingbox:[-2.6,3.8,3,-3.6],axis:true,showCopyright:false,showNavigation:false});var g=b.create('functiongraph',[function(x){return (x-2)*Math.exp(x);},-2.6,2.6],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('integral',[[0,2],g],{fillColor:'#3a5a9c',fillOpacity:0.18,label:{visible:false},curveLeft:{visible:false},curveRight:{visible:false},baseLeft:{visible:false},baseRight:{visible:false}});})();</script>

### Teilaufgabe a) — \( f'(0) \) aus dem Graphen ablesen

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Schritt 1 — Tangente einzeichnen.** Lege im Punkt \( P(0\,|\,f(0)) = P(0\,|\,-2) \) das Lineal so an,
dass es sich an die Kurve **anschmiegt** (die Tangente). Das ist die orange gestrichelte Gerade im Bild.

**Schritt 2 — Steigung der Tangente ablesen.** Geh vom Berührpunkt aus **\( 1 \) nach rechts** und schau,
wie weit die Tangente dabei hoch- oder runtergeht: Sie geht **\( 1 \) nach unten**. Steigung also

\[ f'(0) = \frac{\text{Höhenänderung}}{\text{Schrittweite}} = \frac{-1}{1} = -1. \]

**Ergebnis: \( f'(0) \approx -1 \).**

<details><summary>Haltung dahinter: Was ist \( f'(0) \) überhaupt? (ganz von vorn)</summary>

Langsam von vorn. Die **Ableitung** \( f' \) einer Funktion misst an jeder Stelle die **Steigung** des
Graphen — also wie steil er gerade bergauf oder bergab läuft. \( f'(0) \) ist daher einfach die
**Steigung des Graphen genau an der Stelle \( x = 0 \)**.

**Steigung anschaulich.** Steigung heißt: „Wenn ich einen Schritt nach rechts gehe, wie viel geht es
dabei hoch oder runter?" Eine Steigung von \( +2 \) bedeutet „\( 1 \) nach rechts, \( 2 \) nach oben",
eine Steigung von \( -1 \) bedeutet „\( 1 \) nach rechts, \( 1 \) nach unten". Wie bei einer Straße:
Gefälle = negative Steigung.

**Warum die Tangente?** Der Graph ist gekrümmt, an einer Kurve kann man Steigung nicht direkt ablesen.
Trick: Man legt an der gewünschten Stelle eine **Gerade** an, die den Graphen dort gerade berührt und
in dieselbe Richtung zeigt — die **Tangente** (von lateinisch *tangere* = berühren). Diese Gerade hat
an der Berührstelle **genau dieselbe Steigung** wie der Graph. Und die Steigung einer Geraden kann man
bequem mit dem „rechts/hoch"-Dreieck ablesen.

<details><summary>Ganz langsam (mit Zahlen): die Steigung aus zwei Punkten der Tangente</summary>

Steigung einer Geraden \( = \dfrac{\Delta y}{\Delta x} \) („Delta" heißt „Unterschied"): Höhen­unterschied
geteilt durch Rechts-Unterschied. Nimm zwei bequeme Punkte **auf der Tangente**:

- Berührpunkt \( P(0\,|\,-2) \),
- einen Schritt weiter rechts liegt die Tangente bei \( (1\,|\,-3) \).

Damit:

\[ f'(0) = \frac{\Delta y}{\Delta x} = \frac{-3 - (-2)}{1 - 0} = \frac{-3+2}{1} = \frac{-1}{1} = -1. \]

Beachte \( -3 - (-2) = -3 + 2 = -1 \): „minus minus zwei" wird „plus zwei". Ergebnis: Steigung \( -1 \).

</details>

<details><summary>Typische Falle</summary>

Hier ist nicht der **Funktionswert** \( f(0) = -2 \) gefragt (das ist die Höhe des Graphen), sondern die
**Steigung** \( f'(0) = -1 \) (wie schräg er dort liegt). Zweite Falle: die Steigung der Kurve selbst
schätzen zu wollen — immer erst die Tangente einzeichnen und an ihr ablesen. Mehr dazu:
[Ableit-Handwerk](kap-ableiten-handwerk.html).

</details>
</details>
</details>

### Teilaufgabe b) — Integral durch Kästchenzählen

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Zwischen \( x=0 \) und \( x=2 \) liegt der Graph **unter** der \( x \)-Achse (siehe blaue Fläche im
rechten Bild). Ohne Funktionsterm liest man das Integral durch **Kästchenzählen** ab.

**Schritt 1 — Größe eines Kästchens.** Im Original-Koordinatensystem ist jedes kleine Gitterquadrat
\( 0{,}5 \) breit und \( 0{,}5 \) hoch, hat also den Flächeninhalt \( 0{,}5 \cdot 0{,}5 = 0{,}25 \).

**Schritt 2 — Kästchen zählen.** Die eingeschlossene Fläche umfasst rund **\( 17 \) Kästchen** (ganze
und zu ganzen ergänzte Teilkästchen). Flächeninhalt also

\[ A \approx 17 \cdot 0{,}25 = \frac{17}{4} = 4{,}25. \]

**Schritt 3 — Vorzeichen.** Die Fläche liegt **unter** der Achse, das Integral zählt sie deshalb
**negativ**:

\[ \int_0^2 f(x)\,dx \approx -\frac{17}{4} = -4{,}25. \]

**Ergebnis: \( \displaystyle\int_0^2 f(x)\,dx \approx -4{,}25 \).**

<details><summary>Haltung dahinter: Was ist ein Integral, und warum kann es negativ sein?</summary>

Ein **Integral** \( \int_a^b f(x)\,dx \) ist eine Maschine, die die **Fläche zwischen dem Graphen und
der \( x \)-Achse** von der linken Grenze \( a \) bis zur rechten Grenze \( b \) zusammenrechnet. Man
kann sich unendlich viele hauchdünne senkrechte Streifen unter der Kurve vorstellen, alle aufaddiert.

Der Haken: Das Integral zählt Fläche **mit Vorzeichen** (man sagt *orientierter* Flächeninhalt). Ein
gutes Bild ist ein **Bankkonto**:

- Graph **über** der Achse → Streifen zeigen nach oben → zählen **positiv** (Einzahlung).
- Graph **unter** der Achse → Streifen zeigen nach unten → zählen **negativ** (Abhebung).

Zwischen \( 0 \) und \( 2 \) liegt der Graph komplett **unter** der Achse, deshalb kommt ein **negativer**
Wert heraus.

**Kästchenzählen** ist die rechnerfreie Variante: Statt eine Stammfunktion zu suchen, schätzt man die
Fläche, indem man die Gitterquadrate abzählt — volle Kästchen ganz, angeschnittene zu vollen ergänzt
(zwei halbe = eins). Das ergibt hier etwa \( 17 \) Kästchen.

<details><summary>Ganz langsam (mit Zahlen): von 17 Kästchen zu −4,25</summary>

Ein Kästchen ist \( 0{,}5 \times 0{,}5 \). Achtung: \( 0{,}5 \cdot 0{,}5 = 0{,}25 \), nicht \( 0{,}5 \) —
ein Viertelquadrat. Also:

\[ 17 \text{ Kästchen} \cdot 0{,}25 \tfrac{\text{Fläche}}{\text{Kästchen}} = 4{,}25. \]

Dasselbe als Bruch: \( 17 \cdot \tfrac14 = \tfrac{17}{4} = 4{,}25 \). Weil die Fläche unter der Achse
liegt, ein Minus davor: \( -\tfrac{17}{4} = -4{,}25 \).

</details>

<details><summary>Kontrolle mit dem exakten Term (aus Teilaufgabe d)</summary>

Sobald man aus d) weiß, dass \( f(x) = (x-2)e^x \) ist, kann man das Integral exakt nachrechnen. Eine
Stammfunktion ist \( F(x) = (x-3)e^x \) (Probe durch Ableiten: \( F'(x) = e^x + (x-3)e^x = (x-2)e^x \) ✓).
Mit dem Hauptsatz:

\[ \int_0^2 (x-2)e^x\,dx = \big[(x-3)e^x\big]_0^2 = (2-3)e^2 - (0-3)e^0 = -e^2 + 3 \approx -4{,}39. \]

Der abgelesene Wert \( -4{,}25 \) liegt nah dran — die kleine Abweichung kommt vom Schätzen beim
Kästchenzählen. In der Prüfung ist hier **ohne** Taschenrechner gefragt, also ist \( -\tfrac{17}{4} \)
die erwartete Antwort. Mehr zum Hauptsatz: [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).

</details>

<details><summary>Typische Falle</summary>

Das **Minuszeichen vergessen** ist der häufigste Fehler: Die Fläche selbst ist positiv (\( \approx 4{,}25 \)),
aber das **Integral** ist negativ, weil die Fläche unter der Achse liegt. Zweite Falle: die Kästchengröße
falsch ansetzen (\( 1 \times 1 \) statt \( 0{,}5 \times 0{,}5 \)) — dann vervierfacht sich das Ergebnis
fälschlich.

</details>
</details>
</details>

### Teilaufgabe c) — Hoch-, Tief- und Wendepunkte der Stammfunktion \( F \)

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Wichtig ist die Beziehung **\( F' = f \)**: Die Steigung von \( F \) **ist** die Funktion \( f \), die wir
im Bild sehen. Daraus lesen wir alles ab.

**Tiefpunkt von \( F \).** Ein Tief- oder Hochpunkt von \( F \) liegt dort, wo seine Steigung \( F' = f \)
**null wird und das Vorzeichen wechselt**. Der Graph von \( f \) hat nur **eine** Nullstelle, bei
\( x = 2 \), und dort wechselt \( f \) von **minus nach plus** (links der Achse, rechts darüber). Damit
hört \( F \) auf zu fallen und beginnt zu steigen → **Tiefpunkt von \( F \) bei \( x_1 = 2 \)**.

**Kein Hochpunkt.** Für einen Hochpunkt von \( F \) bräuchte man eine Nullstelle von \( f \) mit
Vorzeichenwechsel **von plus nach minus**. Eine solche gibt es im abgebildeten Bereich nicht → **\( F \)
hat dort keinen Hochpunkt**.

**Wendepunkt von \( F \).** Ein Wendepunkt von \( F \) liegt dort, wo seine Steigung \( f \) selbst einen
**Hoch- oder Tiefpunkt** hat (wo \( f \) also am steilsten/flachsten ist). Der Graph von \( f \) hat einen
**Tiefpunkt bei \( x = 1 \)** → **Wendepunkt von \( F \) bei \( x_2 = 1 \)**.

**Ergebnis:** \( F \) hat einen **Tiefpunkt bei \( x = 2 \)**, einen **Wendepunkt bei \( x = 1 \)** und
**keinen Hochpunkt** im abgebildeten Bereich.

<details><summary>Haltung dahinter: Warum verrät der Graph von \( f \) alles über \( F \)?</summary>

Drei Begriffe der Reihe nach.

**Stammfunktion.** \( F \) ist eine Stammfunktion von \( f \), wenn das Ableiten von \( F \) wieder
\( f \) ergibt: \( F' = f \). „Ableiten" liefert die Steigung — also ist \( f \) genau die **Steigung von
\( F \)**. Diesen einen Satz braucht man für die ganze Aufgabe.

**Hoch-/Tiefpunkt.** Ein Hoch- oder Tiefpunkt ist eine Stelle, an der ein Graph aufhört zu steigen und
zu fallen beginnt (oder umgekehrt). Genau dort ist die **Steigung null**. Die Steigung von \( F \) ist
\( f \). Also: Hoch-/Tiefpunkte von \( F \) sitzen bei den **Nullstellen von \( f \)**.

- Wechselt \( f \) dort von **minus nach plus**, fiel \( F \) erst und steigt dann → **Tiefpunkt** (Tal).
- Wechselt \( f \) dort von **plus nach minus**, stieg \( F \) erst und fällt dann → **Hochpunkt** (Gipfel).

„VZW" ist die Abkürzung für **Vorzeichenwechsel**: Der Funktionswert von \( f \) geht beim Durchlaufen
der Stelle von einem Vorzeichen ins andere über.

**Wendepunkt.** Ein Wendepunkt ist eine Stelle, an der sich die **Krümmung** eines Graphen ändert (von
Linkskurve zu Rechtskurve oder umgekehrt) — die Stelle, an der \( F \) am steilsten oder am flachsten
läuft. „Am steilsten" heißt: Die Steigung \( f \) erreicht dort selbst einen **Extremwert** (Hoch- oder
Tiefpunkt von \( f \)). Deshalb: Wendepunkte von \( F \) sitzen bei den **Extremstellen von \( f \)**.

<details><summary>Ganz langsam (mit Zahlen): was am Graphen von \( f \) abgelesen wird</summary>

Drei Beobachtungen direkt aus dem Bild:

1. \( f \) ist links von \( x=2 \) durchweg **negativ** (Graph unter der Achse), bei \( x=2 \) **null**,
   rechts davon **positiv**. → einzige Nullstelle bei \( x=2 \), VZW **\( - \to + \)** → **Tiefpunkt von
   \( F \) bei \( x=2 \)**.
2. Nirgends im Bild wechselt \( f \) von **\( + \to - \)** → **kein Hochpunkt von \( F \)**.
3. \( f \) selbst hat seinen tiefsten Punkt bei \( x=1 \) (dort liegt die Kurve am weitesten unten). Eine
   Extremstelle von \( f \) → **Wendepunkt von \( F \) bei \( x=1 \)**.

Eselsbrücke für die Kette: **\( F \) → ableiten → \( f \) → ableiten → \( f' \).** Nullstellen von \( f \)
steuern die **Extrempunkte** von \( F \); Extremstellen von \( f \) steuern die **Wendepunkte** von
\( F \). (Mehr: [Funktionsuntersuchung](kap-funktionsuntersuchung.html).)

</details>

<details><summary>Typische Falle</summary>

Die Rollen vertauschen: Für die **Extrempunkte** von \( F \) braucht man die **Nullstellen** von \( f \)
(nicht dessen Extremstellen). Für die **Wendepunkte** von \( F \) braucht man die **Extremstellen** von
\( f \). Wer das verwechselt, gibt \( x=1 \) als Tiefpunkt an — falsch. Zweite Falle: einen Tiefpunkt
ohne Vorzeichenwechsel behaupten; ohne VZW liegt nur ein Sattel, kein Extrempunkt vor.

</details>
</details>
</details>

### Teilaufgabe d) — Funktionsterm zuordnen

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Es gehört **\( f_2(x) = (x-2)\,e^{x} \)** zu \( f \). Man zeigt das, indem man die beiden anderen
Kandidaten über **je ein passendes Merkmal des Graphen** ausschließt.

**\( f_3 \) scheidet aus.** Der Graph hat bei \( x=2 \) eine Nullstelle (er schneidet dort die Achse).
Aber

\[ f_3(2) = 2\,e^{2} - 2 \approx 12{,}78 \neq 0. \]

\( f_3 \) ist bei \( x=2 \) nicht null → passt nicht.

**\( f_1 \) scheidet aus.** Am Graphen liegt der tiefste Punkt bei \( x=1 \) deutlich **unter \( -1 \)**
(etwa bei \( -2{,}7 \)). Aber

\[ f_1(1) = (1-2)\,e^{-1} = -\frac{1}{e} \approx -0{,}37 \;>\; -1. \]

\( f_1 \) liegt bei \( x=1 \) viel zu hoch → passt nicht. (Zusätzlich: \( f_1 \) hätte für große \( x \)
den Grenzwert \( 0 \), der Graph schießt aber nach oben weg.)

**\( f_2 \) bleibt und passt.** Probe an den Merkmalen des Graphen:

\[ f_2(0) = (0-2)e^0 = -2 \;\checkmark, \qquad f_2(2) = (2-2)e^2 = 0 \;\checkmark, \]

für \( x \to -\infty \) geht \( f_2 \to 0 \) von unten (Annäherung an die Achse) \( \checkmark \), für
\( x \to +\infty \) geht \( f_2 \to +\infty \) (steiler Anstieg) \( \checkmark \).

**Ergebnis: \( f(x) = f_2(x) = (x-2)\,e^{x} \).**

<details><summary>Haltung dahinter: Wie schließt man Funktionsterme systematisch aus?</summary>

Bei „welcher Term gehört zum Graphen?" sucht man **Unterscheidungsmerkmale**: Eigenschaften, die der
Graph zeigt und die manche Kandidaten erfüllen, andere aber verletzen. Drei besonders nützliche:

- **Nullstellen** (wo schneidet der Graph die \( x \)-Achse?),
- **markante Funktionswerte** (z. B. \( f(0) \), Tiefpunkt-Höhe),
- **Randverhalten** (was passiert für sehr große oder sehr kleine \( x \)?).

Pro Kandidat genügt **ein** verletztes Merkmal zum Ausschluss. Der Übriggebliebene wird zur Sicherheit
an mehreren Merkmalen positiv bestätigt.

**Warum entscheidet das Randverhalten zwischen \( e^{x} \) und \( e^{-x} \)?** Bei \( e^{x} \) wächst der
Exponent mit \( x \) → die Funktion **explodiert** für große \( x \). Bei \( e^{-x} \) wird der Exponent
für große \( x \) stark negativ → die Funktion **geht gegen null**. Der Graph schießt rechts nach oben,
also muss \( e^{x} \) im Term stehen, nicht \( e^{-x} \). (Mehr: [Grenzwerte &
Randverhalten](kap-grenzwerte-randverhalten.html).)

<details><summary>Ganz langsam (mit Zahlen): die beiden Ausschluss-Rechnungen</summary>

**\( f_3(2) \):** \( f_3(x) = x\,e^x - 2 \). Einsetzen von \( x=2 \): \( 2 \cdot e^2 - 2 \). Mit
\( e^2 \approx 7{,}39 \): \( 2 \cdot 7{,}39 = 14{,}78 \), dann \( 14{,}78 - 2 = 12{,}78 \). Das ist klar
**nicht** null, der Graph hat dort aber eine Nullstelle → \( f_3 \) raus.

**\( f_1(1) \):** \( f_1(x) = (x-2)e^{-x} \). Einsetzen von \( x=1 \): \( (1-2)e^{-1} = (-1)\cdot e^{-1} \).
\( e^{-1} = \tfrac{1}{e} \approx 0{,}37 \), also \( (-1)\cdot 0{,}37 = -0{,}37 \). Der Graph liegt bei
\( x=1 \) aber bei etwa \( -2{,}7 \), also viel tiefer → \( f_1 \) raus.

</details>

<details><summary>Typische Falle</summary>

**Nur \( f(0) \) prüfen reicht nicht.** Es gilt \( f_1(0) = f_2(0) = f_3(0) = -2 \) — alle drei laufen
durch \( (0\,|\,-2) \)! Der \( y \)-Achsenschnittpunkt unterscheidet sie also gar nicht. Man **muss** ein
trennendes Merkmal nehmen: die Nullstelle bei \( x=2 \) oder das Randverhalten für große \( x \).

</details>
</details>
</details>

### Teilaufgabe e) — Graph von \( g(x) = (x-2)^2 e^{x} \) skizzieren

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Man skizziert über **markante Punkte** und das **Randverhalten**, ohne eine vollständige Kurvendiskussion
zu rechnen.

**Schritt 1 — Nullstelle.** \( g(x) = 0 \) nur wenn \( (x-2)^2 = 0 \), also bei \( x=2 \). Weil der Faktor
**quadriert** ist (doppelte Nullstelle), **berührt** der Graph die \( x \)-Achse bei \( x=2 \) nur und
durchschneidet sie nicht — dort liegt ein **Tiefpunkt \( T(2\,|\,0) \)**.

**Schritt 2 — Wertebereich.** \( (x-2)^2 \ge 0 \) und \( e^{x} > 0 \), also ist \( g(x) \ge 0 \) **überall**.
Der ganze Graph liegt auf oder über der \( x \)-Achse.

**Schritt 3 — Randverhalten.** Für \( x \to -\infty \) drückt \( e^{x} \to 0 \) die Funktion gegen
\( 0 \) (von oben). Für \( x \to +\infty \) wächst \( g \to +\infty \) (steiler Anstieg).

**Schritt 4 — gegebener Hochpunkt.** Laut Aufgabe ist \( H(0\,|\,4) \) ein Hochpunkt; Probe:
\( g(0) = (0-2)^2 e^0 = 4 \cdot 1 = 4 \) \( \checkmark \).

**Skizze (Form):** von links flach aus \( 0^{+} \) heraus, hoch zum **Hochpunkt \( H(0\,|\,4) \)**,
hinunter bis zur Berührung im **Tiefpunkt \( T(2\,|\,0) \)**, danach **steil nach oben**.

<figure>
<div class="jxgbox" id="jxg-k4-g" style="width:100%;max-width:460px;aspect-ratio:1.4/1"></div>
<figcaption>Graph von \( g(x)=(x-2)^2 e^{x} \): Hochpunkt \( H(0\,|\,4) \), Berührung der Achse im Tiefpunkt \( T(2\,|\,0) \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k4-g',{boundingbox:[-4.6,5.2,4,-1.2],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return (x-2)*(x-2)*Math.exp(x);},-4.6,2.62],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[0,4],{name:'H(0|4)',size:2,fixed:true,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[8,6]}});b.create('point',[2,0],{name:'T(2|0)',size:2,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',label:{offset:[6,-14]}});})();</script>

<details><summary>Haltung dahinter: Wie skizziert man einen Graphen aus wenigen Merkmalen?</summary>

„Skizzieren" heißt nicht „jeden Punkt ausrechnen", sondern ein **Gerüst aus wenigen Schlüssel­merkmalen**
aufbauen und sauber verbinden. Vier Merkmale tragen fast jede Skizze:

- **Nullstellen** — wo trifft der Graph die \( x \)-Achse?
- **Wertebereich / Vorzeichen** — bleibt der Graph oben, unten, oder beides?
- **markante Punkte** — hier der vorgegebene Hochpunkt.
- **Randverhalten** — wohin läuft der Graph ganz links und ganz rechts?

**Doppelte Nullstelle = Berührung.** Steht ein Faktor **quadriert** da, wie \( (x-2)^2 \), so wird er an
der Stelle null, ohne das Vorzeichen zu wechseln (ein Quadrat ist nie negativ). Der Graph **tippt** die
Achse nur an und kehrt auf derselben Seite zurück — eine Berührung, kein Durchschneiden. Bei einer
einfachen Nullstelle dagegen kreuzt der Graph die Achse.

**Warum gewinnt \( e^{x} \) das Randverhalten?** Für \( x \to -\infty \) wird \( (x-2)^2 \) zwar groß,
aber \( e^{x} \) geht **schneller** gegen null — das Produkt geht gegen \( 0 \). Die e-Funktion
„überstimmt" das Polynom. Für \( x \to +\infty \) ziehen beide Faktoren nach oben → steiler Anstieg.

<details><summary>Ganz langsam (mit Zahlen): eine kleine Wertetabelle</summary>

| \( x \) | \( -2 \) | \( 0 \) | \( 1 \) | \( 2 \) | \( 3 \) |
|---|---|---|---|---|---|
| \( g(x) \) | \( 16\,e^{-2}\approx 2{,}2 \) | \( 4 \) | \( e\approx 2{,}7 \) | \( 0 \) | \( e^{3}\approx 20 \) |

So liest man die Werte: \( g(0)=(-2)^2\cdot 1 = 4 \); \( g(2)=0^2\cdot e^2 = 0 \); \( g(3)=1^2\cdot e^3
\approx 20 \) (schon weit oben → steiler Anstieg). Die Tabelle bestätigt die Form: hoch bei \( 0 \),
runter bis zur Berührung bei \( 2 \), dann steil hoch.

</details>

<details><summary>Typische Falle</summary>

Bei \( x=2 \) die Achse **durchschneiden** statt nur **berühren** — falsch, weil \( (x-2)^2 \) eine
doppelte Nullstelle ist. Zweite Falle: den Graphen links unter die Achse zeichnen; wegen \( g(x)\ge 0 \)
bleibt er immer auf oder über der Achse.

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- **a)** \( f'(0) \approx -1 \) (Tangente in \( P(0\,|\,-2) \), Steigung „1 rechts, 1 runter").
- **b)** \( \int_0^2 f\,dx \approx -\tfrac{17}{4} = -4{,}25 \) (≈ 17 Kästchen à 0,25; Minus, da unter der Achse).
- **c)** \( F \): **Tiefpunkt bei \( x=2 \)** (Nullstelle von \( f \), VZW \( -\to+ \)),
  **Wendepunkt bei \( x=1 \)** (Tiefpunkt von \( f \)), **kein Hochpunkt**.
- **d)** \( f(x) = f_2(x) = (x-2)e^{x} \) (\( f_3(2)\neq 0 \), \( f_1(1)=-\tfrac1e>-1 \)).
- **e)** \( g \): \( H(0\,|\,4) \), Berührung/Tiefpunkt \( T(2\,|\,0) \), \( g\ge 0 \), links \( \to 0^+ \),
  rechts \( \to +\infty \).

</details>

---

## Teil 2 — Gespräch (Stochastik): Normalverteilung mit \( \mu = 20,\ \sigma = 4 \)

<div class="aufgabenkasten">

**Input.** Gegeben ist eine normalverteilte Zufallsgröße \( X \) mit \( \mu = 20 \) und \( \sigma = 4 \).
(Das Original zeigt ein leeres Koordinatensystem mit \( x \)-Achse von \( 0 \) bis \( 40 \).)

Im Gespräch denkbare Aspekte:
**(AB I)** Kurve zu \( X \) skizzieren; erläutern, wie \( P(X\le 21) \), \( P(X=21) \) und \( P(X>21) \)
bestimmt werden; einen Sachkontext angeben; beschreiben, wie sich die Kurve bei Änderung von \( \mu \)
ändert.
**(AB II)** Beschreiben, wie sich die Kurve bei Änderung von \( \sigma \) ändert; Gemeinsamkeiten und
Unterschiede von Binomial- und Normalverteilung nennen und erläutern.
**(AB III)** Eine diskret verteilte Zufallsgröße ermitteln, deren Histogramm eine ähnliche Form wie die
Kurve hat.

</div>

> **Vorab, in einem Satz, was eine „normalverteilte Zufallsgröße" ist:** \( X \) ist eine Größe, deren
> Wert vom Zufall abhängt (z. B. ein Messwert), und deren Werte sich **glockenförmig** um einen
> Mittelwert verteilen — die meisten nah am Mittel, wenige weit weg, symmetrisch nach beiden Seiten. Alle
> Werkzeuge dazu stehen im
> [Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html#normalverteilung). **Hinweis:** Für
> Teil 2 gibt das Original nur Gesprächsthemen vor; die folgenden Lösungen sind selbst erarbeitet und
> durchgerechnet.

So sieht die Kurve zu \( X \) aus (das ist zugleich die Lösung des ersten Aspekts):

<figure>
<div class="jxgbox" id="jxg-k4-normal" style="width:100%;max-width:520px;aspect-ratio:1.7/1"></div>
<figcaption>Dichtekurve (Gaußsche Glockenkurve) von \( X \) mit \( \mu=20 \), \( \sigma=4 \): Maximum bei \( 20 \), Wendepunkte bei \( 16 \) und \( 24 \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k4-normal',{boundingbox:[4,0.115,36,-0.018],axis:true,showCopyright:false,showNavigation:false});function dn(x){return (1/(4*Math.sqrt(2*Math.PI)))*Math.exp(-(x-20)*(x-20)/32);}b.create('functiongraph',[dn,5,35],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('line',[[20,0],[20,dn(20)]],{straightFirst:false,straightLast:false,dash:2,strokeColor:'#d98324',strokeWidth:1.5});b.create('point',[16,dn(16)],{name:'',size:1.5,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',withLabel:false});b.create('point',[24,dn(24)],{name:'',size:1.5,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',withLabel:false});b.create('text',[20.4,-0.01,'μ=20'],{fontSize:12,color:'#d98324'});b.create('text',[12.2,-0.01,'16'],{fontSize:11,color:'#3a8a5a'});b.create('text',[24.3,-0.01,'24'],{fontSize:11,color:'#3a8a5a'});})();</script>

### Aspekt 1 (AB I) — Kurve skizzieren

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Die Kurve (oben gezeichnet) ist die **Gaußsche Glockenkurve**. Man skizziert sie über fünf Merkmale:

1. **Symmetrisch** um die senkrechte Achse bei \( x = \mu = 20 \) (linke und rechte Hälfte sind
   Spiegelbilder).
2. **Maximum (höchster Punkt) bei \( x = 20 \)**, mit Höhe \( \tfrac{1}{\sigma\sqrt{2\pi}} =
   \tfrac{1}{4\sqrt{2\pi}} \approx 0{,}10 \).
3. **Wendepunkte bei \( x = \mu \pm \sigma \)**, also bei \( 16 \) und \( 24 \) — dort wechselt die
   Krümmung, die Kurve geht von „nach unten gewölbt" in „nach oben gewölbt" über.
4. **Asymptotisch** zur \( x \)-Achse: Nach beiden Seiten kommt die Kurve der Achse beliebig nah, ohne
   sie zu erreichen.
5. **Gesamtfläche unter der Kurve \( = 1 \)** (entspricht \( 100\,\% \) Wahrscheinlichkeit).

Als grobe Orientierung dient die **\( 68\text{–}95\text{–}99{,}7\,\% \)-Regel** (Sigma-Regel): rund
\( 68\,\% \) der Werte liegen in \( [\,16;\,24\,] \), rund \( 95\,\% \) in \( [\,12;\,28\,] \), rund
\( 99{,}7\,\% \) in \( [\,8;\,32\,] \).

<details><summary>Haltung dahinter: Was zeigt diese Kurve eigentlich? (ganz von vorn)</summary>

**Zufallsgröße.** Eine **Zufallsgröße** \( X \) ist eine Zahl, deren Wert vom Zufall abhängt — etwa das
Gewicht einer zufällig herausgegriffenen Packung. „Normalverteilt" beschreibt, **wie wahrscheinlich**
welche Werte sind.

**Dichtekurve statt Balken.** \( X \) kann hier **jeden** Zwischenwert annehmen (z. B. \( 20{,}3 \) oder
\( 17{,}81 \)), nicht nur ganze Zahlen. Man kann deshalb keine einzelnen Wahrscheinlichkeits-Balken
zeichnen, sondern eine durchgehende Kurve — die **Dichte**. Bei ihr steckt die Wahrscheinlichkeit in der
**Fläche**: Die Fläche unter der Kurve über einem Bereich ist die Wahrscheinlichkeit, dass \( X \) in
diesem Bereich landet. Weil \( X \) **irgendeinen** Wert annimmt, ist die **Gesamtfläche \( = 1 \)**.

**\( \mu \) und \( \sigma \).** \( \mu \) (mü) ist der **Erwartungswert** — der Mittelwert, um den alles
streut; hier \( 20 \), genau unter dem höchsten Punkt. \( \sigma \) (sigma) ist die
**Standardabweichung** — ein Maß für die **Breite** der Streuung; hier \( 4 \). Praktisch: Bei \( \mu \pm
\sigma \) (also \( 16 \) und \( 24 \)) sitzen die Wendepunkte, und dazwischen liegen rund zwei Drittel
aller Werte. (Mehr: [Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html#erwartungswert).)

<details><summary>Ganz langsam (mit Zahlen): die Höhe des Gipfels</summary>

Die Formel für die Gipfelhöhe ist \( \tfrac{1}{\sigma\sqrt{2\pi}} \). Mit \( \sigma=4 \) und
\( \sqrt{2\pi}\approx 2{,}51 \):

\[ \frac{1}{4 \cdot 2{,}51} = \frac{1}{10{,}03} \approx 0{,}0997 \approx 0{,}10. \]

Deshalb reicht die \( y \)-Achse im Bild nur bis etwa \( 0{,}1 \) — eine Glockenkurve ist flach. Die
Werte \( 16 \) und \( 24 \) für die Wendepunkte sind einfach \( 20-4 \) und \( 20+4 \).

</details>

<details><summary>Typische Falle</summary>

Die Höhe der Kurve mit einer Wahrscheinlichkeit verwechseln. Der Gipfelwert \( \approx 0{,}10 \) ist
**keine** Wahrscheinlichkeit, sondern eine **Dichte**; Wahrscheinlichkeiten sind immer **Flächen** unter
der Kurve, nie einzelne Höhen.

</details>
</details>
</details>

### Aspekt 2 (AB I) — \( P(X\le 21) \), \( P(X=21) \), \( P(X>21) \)

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**\( P(X=21) = 0 \).** Bei einer stetigen (kontinuierlichen) Zufallsgröße hat ein **einzelner Wert**
keine Fläche (ein Strich ist unendlich dünn) → die Wahrscheinlichkeit für genau \( 21 \) ist **null**.

**\( P(X\le 21) \) — Fläche links von \( 21 \).** Das ist die Fläche unter der Glockenkurve **links** von
\( x=21 \) (im Bild blau). Man berechnet sie, indem man **standardisiert** und die Tabelle der
Standardnormalverteilung \( \Phi \) (bzw. den GTR-Befehl) nutzt:

\[ z = \frac{21 - \mu}{\sigma} = \frac{21-20}{4} = 0{,}25, \qquad
   P(X\le 21) = \Phi(0{,}25) \approx 0{,}599. \]

**\( P(X>21) \) — Gegenwahrscheinlichkeit.** Was nicht links liegt, liegt rechts:

\[ P(X>21) = 1 - P(X\le 21) \approx 1 - 0{,}599 = 0{,}401. \]

**Ergebnisse:** \( P(X=21)=0 \); \( P(X\le 21)\approx 0{,}599 \) (rund \( 59{,}9\,\% \));
\( P(X>21)\approx 0{,}401 \) (rund \( 40{,}1\,\% \)).

<figure>
<div class="jxgbox" id="jxg-k4-normal-p" style="width:100%;max-width:520px;aspect-ratio:1.7/1"></div>
<figcaption>\( P(X\le 21) \) ist die Fläche links von \( x=21 \) (blau). Wegen der leichten Rechtslage von \( 21 \) gegenüber \( \mu=20 \) etwas mehr als die Hälfte.</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k4-normal-p',{boundingbox:[4,0.115,36,-0.018],axis:true,showCopyright:false,showNavigation:false});function dn(x){return (1/(4*Math.sqrt(2*Math.PI)))*Math.exp(-(x-20)*(x-20)/32);}var g=b.create('functiongraph',[dn,5,35],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('integral',[[5,21],g],{fillColor:'#3a5a9c',fillOpacity:0.18,label:{visible:false},curveLeft:{visible:false},curveRight:{visible:false},baseLeft:{visible:false},baseRight:{visible:false}});b.create('line',[[21,0],[21,dn(21)]],{straightFirst:false,straightLast:false,dash:2,strokeColor:'#d98324',strokeWidth:1.5});b.create('text',[21.3,-0.01,'21'],{fontSize:11,color:'#d98324'});})();</script>

<details><summary>Haltung dahinter: Warum ist \( P(X=21)=0 \), und was heißt „standardisieren"?</summary>

**Warum genau \( 21 \) die Wahrscheinlichkeit \( 0 \) hat.** Wahrscheinlichkeit ist hier **Fläche** unter
der Kurve. Über einem einzelnen Punkt (\( x=21 \), Breite \( 0 \)) gibt es keine Fläche — ein Rechteck
mit Breite null hat Flächeninhalt null. Also \( P(X=21)=0 \). Das klingt seltsam („der Wert 21 kommt doch
vor!"), gilt aber für **jede** stetige Größe: Sinnvoll fragt man immer nach einem **Bereich** („zwischen
\( 20{,}5 \) und \( 21{,}5 \)"), nie nach einem exakten Wert. Nebeneffekt: \( P(X<21)=P(X\le 21) \), das
einzelne \( 21 \) ändert nichts.

**Standardisieren.** Für jedes \( \mu \) und \( \sigma \) eine eigene Tabelle wäre unpraktisch. Trick:
Man rechnet jeden Wert um in „**wie viele Standardabweichungen vom Mittel** ist er entfernt?":

\[ z = \frac{x-\mu}{\sigma}. \]

Hier ist \( 21 \) um \( 1 \) über dem Mittel \( 20 \), und \( 1 \) ist ein Viertel von \( \sigma=4 \),
also \( z=0{,}25 \). Diese \( z \)-Welt hat immer \( \mu=0 \) und \( \sigma=1 \) (die
**Standardnormalverteilung**), und für sie gibt es **eine** feste Tabelle der Funktion \( \Phi \)
(„Phi"). \( \Phi(z) \) liefert direkt die Fläche links von \( z \). Mit GTR genügt der Befehl
`normalcdf(untere Grenze, 21, 20, 4)`.

<details><summary>Ganz langsam (mit Zahlen): von z zur Wahrscheinlichkeit</summary>

\( z = \dfrac{21-20}{4} = \dfrac{1}{4} = 0{,}25 \). Tabelle: \( \Phi(0{,}25) \approx 0{,}5987 \), gerundet
\( 0{,}599 \). Weil \( 21 \) **rechts** vom Mittel \( 20 \) liegt, ist die linke Fläche etwas **mehr** als
die Hälfte — \( 0{,}599 \) passt (knapp über \( 0{,}5 \)). Gegenwahrscheinlichkeit:
\( 1 - 0{,}599 = 0{,}401 \).

</details>

<details><summary>Typische Falle</summary>

\( P(X=21) \) für eine positive Zahl halten (etwa für den Dichtewert \( \approx 0{,}10 \)) — bei stetigen
Größen ist es **immer \( 0 \)**. Zweite Falle: beim \( z \)-Wert durch \( \sigma^2=16 \) statt durch
\( \sigma=4 \) teilen; standardisiert wird mit \( \sigma \), nicht mit der Varianz.

</details>
</details>
</details>

### Aspekt 3 (AB I) — Sachkontext angeben

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Beispiel-Sachkontext.** Eine Abfüllanlage füllt Gewürzdosen. Das **Füllgewicht \( X \)** (in Gramm)
schwankt um den Sollwert; im Mittel sind es \( \mu = 20 \) g, mit einer Standardabweichung von
\( \sigma = 4 \) g. Dann ist \( P(X\le 21) \) die Wahrscheinlichkeit, eine Dose mit höchstens \( 21 \) g
zu erwischen.

**Warum passt hier die Normalverteilung?** Das Füllgewicht ist ein **stetiger Messwert** (beliebige
Zwischenwerte möglich), die Abweichungen sind **symmetrisch** um den Sollwert (zu viel und zu wenig etwa
gleich häufig), und sie entstehen aus **vielen kleinen unabhängigen Einflüssen** (Maschinenvibration,
Temperatur, Materialschwankung). Genau dann ergibt sich erfahrungsgemäß eine Glockenkurve.

Weitere passende Kontexte: Körpergrößen einer Personengruppe, Messfehler beim Wiegen, Punktzahlen in
einer großen Klausur, Längen gefertigter Werkstücke.

<details><summary>Haltung dahinter: Woran erkennt man, dass „normalverteilt" ein gutes Modell ist?</summary>

Die Normalverteilung ist ein gutes Modell, wenn drei Dinge zusammenkommen:

- **stetige Größe** — man misst (Gewicht, Länge, Zeit), zählt nicht ab.
- **symmetrische Streuung** — Abweichungen nach oben und unten sind etwa gleich häufig; ein einzelner
  typischer Mittelwert, um den sich alles drängt.
- **viele kleine, unabhängige Ursachen** — keine einzelne dominiert. Der **Zentrale Grenzwertsatz** sagt:
  Summieren sich viele kleine zufällige Einflüsse, entsteht näherungsweise eine Glockenkurve. Das ist der
  tiefere Grund, warum die Normalverteilung in Natur und Technik so oft auftaucht.

Werte **nahe am Mittel** sind am wahrscheinlichsten (hoher Kurventeil), **extreme** Abweichungen selten
(flache Ränder) — genau das Bild der Glockenkurve.

<details><summary>Typische Falle</summary>

Einen **diskreten Zählkontext** als Beispiel nennen, etwa „Anzahl der Treffer bei 10 Würfen". Das ist
ein Fall für die **Binomialverteilung**, nicht für die Normalverteilung. Für die Normalverteilung eine
**Messgröße** wählen.

</details>
</details>
</details>

### Aspekt 4 (AB I) — Kurve bei Änderung von \( \mu \)

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

\( \mu \) bestimmt die **Lage** der Kurve. Ändert man \( \mu \), **verschiebt** sich die ganze Kurve
**waagerecht**, ohne ihre Form zu ändern:

- **größeres \( \mu \)** → Kurve wandert nach **rechts**,
- **kleineres \( \mu \)** → Kurve wandert nach **links**.

Höhe und Breite bleiben gleich; nur die Symmetrieachse sitzt nun bei der neuen Stelle \( x=\mu \).

<figure>
<div class="jxgbox" id="jxg-k4-normal-mu" style="width:100%;max-width:520px;aspect-ratio:1.9/1"></div>
<figcaption>Ändern von \( \mu \) verschiebt die Kurve seitlich (hier \( \mu=14 \), \( 20 \), \( 26 \), jeweils \( \sigma=4 \)) — gleiche Form, andere Lage.</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k4-normal-mu',{boundingbox:[2,0.115,40,-0.018],axis:true,showCopyright:false,showNavigation:false});function dn(x,m){return (1/(4*Math.sqrt(2*Math.PI)))*Math.exp(-(x-m)*(x-m)/32);}b.create('functiongraph',[function(x){return dn(x,14);},2,38],{strokeColor:'#3a8a5a',strokeWidth:2,dash:2});b.create('functiongraph',[function(x){return dn(x,20);},2,38],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('functiongraph',[function(x){return dn(x,26);},2,38],{strokeColor:'#d98324',strokeWidth:2,dash:2});})();</script>

<details><summary>Haltung dahinter: Warum nur verschieben?</summary>

\( \mu \) ist der **Mittelwert** — der Ort, um den die Werte streuen. Verschiebt man den Mittelwert, zieht
man den ganzen „Schwerpunkt" der Verteilung mit; die **Streuung** (Breite) bleibt davon unberührt, denn
die regelt \( \sigma \). Bild: Du nimmst dieselbe Glocke und stellst sie an eine andere Stelle des Tisches
— Form unverändert, nur der Standort wechselt. In der Formel steckt \( \mu \) nur im Teil \( (x-\mu) \),
der die Kurve seitlich positioniert.

</details>
</details>

### Aspekt 5 (AB II) — Kurve bei Änderung von \( \sigma \)

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

\( \sigma \) bestimmt die **Breite** der Kurve. Ändert man \( \sigma \), wird die Glocke breiter oder
schmaler — bei festem Mittelpunkt \( \mu \):

- **größeres \( \sigma \)** → Kurve wird **breiter und flacher** (Werte streuen weiter),
- **kleineres \( \sigma \)** → Kurve wird **schmaler und höher** (Werte drängen sich enger um \( \mu \)).

Der Mittelpunkt bei \( x=\mu \) und die **Gesamtfläche \( =1 \)** bleiben immer gleich. Die Wendepunkte
sitzen weiterhin bei \( \mu\pm\sigma \), wandern mit \( \sigma \) nach außen oder innen.

<figure>
<div class="jxgbox" id="jxg-k4-normal-sigma" style="width:100%;max-width:520px;aspect-ratio:1.7/1"></div>
<figcaption>Ändern von \( \sigma \) verändert Breite und Höhe (hier \( \sigma=2 \), \( 4 \), \( 8 \), jeweils \( \mu=20 \)) — die Fläche bleibt stets \( 1 \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k4-normal-sigma',{boundingbox:[4,0.225,36,-0.03],axis:true,showCopyright:false,showNavigation:false});function dn(x,s){return (1/(s*Math.sqrt(2*Math.PI)))*Math.exp(-(x-20)*(x-20)/(2*s*s));}b.create('functiongraph',[function(x){return dn(x,2);},5,35],{strokeColor:'#3a8a5a',strokeWidth:2,dash:2});b.create('functiongraph',[function(x){return dn(x,4);},5,35],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('functiongraph',[function(x){return dn(x,8);},5,35],{strokeColor:'#d98324',strokeWidth:2,dash:2});})();</script>

<details><summary>Haltung dahinter: Warum wird die Kurve flacher, wenn sie breiter wird?</summary>

\( \sigma \) ist die **Standardabweichung** — wie weit die Werte typischerweise vom Mittel abweichen. Ein
großes \( \sigma \) heißt „viel Streuung", die Werte verteilen sich über einen weiten Bereich.

Der entscheidende Zwang ist die **konstante Gesamtfläche \( = 1 \)**: Es muss ja \( 100\,\% \) aller Werte
geben, egal wie breit die Glocke ist. Verteilt sich dieselbe Fläche über einen **breiteren** Bereich,
muss die Kurve zwangsläufig **niedriger** werden — wie ein Stück Teig, das beim Breitwalzen dünner wird.
Umgekehrt: schmaler → höher. Deshalb ändern sich Breite und Höhe immer **gegenläufig**.

<details><summary>Ganz langsam (mit Zahlen): die Gipfelhöhe \( \tfrac{1}{\sigma\sqrt{2\pi}} \)</summary>

Die Gipfelhöhe ist umgekehrt proportional zu \( \sigma \):

- \( \sigma=2 \): \( \dfrac{1}{2\sqrt{2\pi}} \approx 0{,}20 \) (hoch, schmal),
- \( \sigma=4 \): \( \dfrac{1}{4\sqrt{2\pi}} \approx 0{,}10 \) (mittel),
- \( \sigma=8 \): \( \dfrac{1}{8\sqrt{2\pi}} \approx 0{,}05 \) (flach, breit).

Doppeltes \( \sigma \) → halbe Höhe. Die Wendepunkte liegen bei \( 20\pm 2 \), \( 20\pm 4 \),
\( 20\pm 8 \) — sie rücken mit \( \sigma \) nach außen.

</details>

<details><summary>Typische Falle</summary>

Glauben, ein größeres \( \sigma \) hebe die Kurve an. Es ist umgekehrt: größeres \( \sigma \) macht sie
**breiter und niedriger**. Höhe und Breite bewegen sich gegenläufig, damit die Fläche \( 1 \) bleibt.

</details>
</details>
</details>

### Aspekt 6 (AB II) — Binomial- und Normalverteilung vergleichen

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Gemeinsamkeiten.**

- Beide sind **Wahrscheinlichkeitsverteilungen**; die Gesamtwahrscheinlichkeit ist \( 1 \) (Summe aller
  Balken \( = 1 \) bzw. Gesamtfläche \( = 1 \)).
- Beide haben einen **Erwartungswert \( \mu \)** und eine **Standardabweichung \( \sigma \)**.
- Beide sind **glockenähnlich**: Die Binomialverteilung ist für \( p=0{,}5 \) symmetrisch, für große
  \( n \) allgemein glockenförmig.
- Für große \( n \) lässt sich die Binomialverteilung **durch die Normalverteilung annähern** (Satz von
  de Moivre–Laplace); Faustregel **Laplace-Bedingung** \( \sigma = \sqrt{n\,p\,(1-p)} > 3 \).

**Unterschiede.**

| Merkmal | Binomialverteilung | Normalverteilung |
|---|---|---|
| Art | **diskret** (nur \( 0,1,2,\dots,n \)) | **stetig** (jeder reelle Wert) |
| Darstellung | **Balken** (Histogramm) | **Dichtekurve** (Glocke) |
| \( P(X=k) \) | **positiv**, \( \binom{n}{k}p^k(1-p)^{n-k} \) | \( P(X=x) = 0 \), Wahrscheinlichkeit \( = \) Fläche |
| Wertebereich | endlich, \( 0 \) bis \( n \) | unendlich, \( -\infty \) bis \( +\infty \) |
| Parameter | \( n \) und \( p \) | \( \mu \) und \( \sigma \) |

<details><summary>Haltung dahinter: diskret gegen stetig — der Kernunterschied</summary>

**Diskret** heißt: \( X \) kann nur **abzählbare** Werte annehmen, hier ganze Zahlen — „Anzahl der
Treffer bei \( n \) Versuchen". Jeder einzelne Wert hat eine **eigene, positive** Wahrscheinlichkeit, man
zeichnet sie als **Balken**. \( P(X=k) \) ist sinnvoll und ausrechenbar.

**Stetig** heißt: \( X \) kann **jeden** Zwischenwert annehmen — „gemessenes Gewicht". Einzelwerte haben
Wahrscheinlichkeit \( 0 \), die Wahrscheinlichkeit steckt in **Flächen** unter einer Kurve.

**Die Brücke.** Erhöht man bei der Binomialverteilung \( n \), werden die Balken zahlreicher und schmaler;
ihre Umrisslinie nähert sich immer mehr einer **Glocke**. Ist \( \sigma=\sqrt{np(1-p)}>3 \), passt die
Normalverteilung schon gut. So wird die stetige Normalverteilung zum **Grenzfall** der diskreten
Binomialverteilung — der Grund, warum man eine umständliche Binomialrechnung oft durch die einfachere
Normalverteilung ersetzt. (Mehr:
[Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html#binomialverteilung).)

</details>
</details>

### Aspekt 7 (AB III) — Diskrete Verteilung mit ähnlichem Histogramm

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Gesucht ist eine **diskrete** Verteilung, deren Histogramm der Glocke \( N(20;4) \) gleicht. Die
natürliche Wahl ist eine **Binomialverteilung**, deren Erwartungswert und Standardabweichung mit der
Normalverteilung übereinstimmen.

**Schritt 1 — Bedingungen aufstellen.** Für \( X\sim B(n;p) \) gilt \( \mu = n\,p \) und
\( \sigma = \sqrt{n\,p\,(1-p)} \). Wir fordern \( \mu=20 \) und \( \sigma=4 \), also

\[ n\,p = 20, \qquad n\,p\,(1-p) = \sigma^2 = 16. \]

**Schritt 2 — auflösen.** Teilt man die zweite durch die erste Gleichung, kürzt sich \( np \):

\[ \frac{n\,p\,(1-p)}{n\,p} = \frac{16}{20} \;\Longrightarrow\; 1-p = 0{,}8 \;\Longrightarrow\; p = 0{,}2. \]

Dann \( n = \dfrac{20}{p} = \dfrac{20}{0{,}2} = 100. \)

**Schritt 3 — Ergebnis und Probe.** \( X\sim B(100;\,0{,}2) \). Probe:
\( \mu = 100\cdot 0{,}2 = 20 \) \( \checkmark \); \( \sigma=\sqrt{100\cdot 0{,}2\cdot 0{,}8}=\sqrt{16}=4 \)
\( \checkmark \). Wegen \( \sigma=4>3 \) (Laplace-Bedingung erfüllt) hat das Histogramm tatsächlich eine
glockenähnliche Form, zentriert bei \( 20 \) mit derselben Streuung.

**Ergebnis: \( X\sim B(100;\,0{,}2) \).**

<figure>
<div class="jxgbox" id="jxg-k4-hist" style="width:100%;max-width:520px;aspect-ratio:1.7/1"></div>
<figcaption>Histogramm der Binomialverteilung \( B(100;\,0{,}2) \) (blaue Balken) mit überlagerter Glockenkurve \( N(20;4) \) (orange) — gleiche Lage, gleiche Breite.</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k4-hist',{boundingbox:[6,0.115,34,-0.014],axis:true,showCopyright:false,showNavigation:false});var P=Math.pow(0.8,100);var pr=[P];for(var k=1;k<=100;k++){P=P*((100-k+1)/k)*0.25;pr[k]=P;}for(var j=9;j<=31;j++){var h=pr[j];b.create('polygon',[[j-0.5,0],[j+0.5,0],[j+0.5,h],[j-0.5,h]],{fillColor:'#3a5a9c',fillOpacity:0.22,vertices:{visible:false},borders:{strokeColor:'#3a5a9c',strokeWidth:0.8},withLabel:false,fixed:true,highlight:false});}b.create('functiongraph',[function(x){return (1/(4*Math.sqrt(2*Math.PI)))*Math.exp(-(x-20)*(x-20)/32);},6,34],{strokeColor:'#d98324',strokeWidth:2.5});})();</script>

<details><summary>Haltung dahinter: Warum gerade die Binomialverteilung, und warum diese Werte?</summary>

Eine Verteilung wird in ihrer **groben Form** von zwei Kennzahlen bestimmt: **wo** sie sitzt
(Erwartungswert \( \mu \)) und **wie breit** sie streut (Standardabweichung \( \sigma \)). Wenn eine
diskrete Verteilung dieselbe Mitte und dieselbe Breite wie die Glocke haben soll, passt man genau diese
beiden Größen an.

Die **Binomialverteilung** \( B(n;p) \) (Modell für „\( k \) Treffer bei \( n \) unabhängigen Versuchen
mit Trefferchance \( p \)") ist dafür ideal, weil ihre Kennzahlen einfache Formeln haben: \( \mu=np \) und
\( \sigma=\sqrt{np(1-p)} \). Zwei Gleichungen, zwei Unbekannte \( n \) und \( p \) — eindeutig lösbar.

Dass am Ende ein **großes** \( n=100 \) herauskommt, ist der eigentliche Grund für die Ähnlichkeit: Bei
vielen Versuchen werden die Balken zahlreich und schmal, ihre Hüllkurve nähert sich der Glocke. Die
**Laplace-Bedingung \( \sigma>3 \)** ist genau die Daumenregel dafür, dass die Annäherung gut ist — hier
mit \( \sigma=4 \) erfüllt.

<details><summary>Ganz langsam (mit Zahlen): die Auflösung des Gleichungssystems</summary>

Aus \( np=20 \) und \( np(1-p)=16 \): Die zweite Gleichung ist die erste, **mal \( (1-p) \)**. Also muss
\( (1-p) \) gerade der Faktor sein, der \( 20 \) auf \( 16 \) bringt:

\[ 1-p = \frac{16}{20} = 0{,}8 \;\Longrightarrow\; p = 1 - 0{,}8 = 0{,}2. \]

Dann aus \( np=20 \): \( n = \dfrac{20}{0{,}2} = 100 \). Kontrolle der Streuung:
\( np(1-p) = 100\cdot 0{,}2\cdot 0{,}8 = 16 \), Wurzel \( \sqrt{16}=4=\sigma \) \( \checkmark \).

</details>

<details><summary>Hinweis: andere Lösungen sind denkbar</summary>

Verlangt ist „**eine** diskrete Verteilung", nicht *die* einzige. \( B(100;\,0{,}2) \) ist die sauberste
und naheliegendste Antwort, weil ihre beiden Kennzahlen exakt passen. Im Prinzip taugt jede diskrete
Verteilung mit \( \mu\approx 20 \) und \( \sigma\approx 4 \) und einem glockenförmigen Histogramm; die
Binomialverteilung ist hier der erwartete Standardweg.

</details>
</details>
</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Teilaufgabe, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen kannst.
Du musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Analysis) aufklappen</summary>

- **a) \( f'(0) \).** Erwartet: **Tangente** in \( P(0\,|\,-2) \) einzeichnen, Steigung ablesen („1 nach
  rechts, 1 nach unten") → \( f'(0)\approx -1 \). *Rückfrage:* „Was misst \( f'(0) \) — die Höhe oder die
  Steigung des Graphen?" *Rote Flagge:* die Antwort \( -2 \) (das ist \( f(0) \), nicht \( f'(0) \)).
- **b) Integral.** Erwartet: **Kästchen zählen** (≈ 17 à 0,25), Ergebnis \( -\tfrac{17}{4}=-4{,}25 \),
  **mit Minus**, weil die Fläche unter der Achse liegt. *Rückfrage:* „Warum kommt ein negativer Wert
  heraus?" *Rote Flagge:* positives Ergebnis \( +4{,}25 \) ohne Vorzeichen-Begründung.
- **c) Graph von \( F \).** Erwartet: \( F'=f \); **Tiefpunkt bei \( x=2 \)** (Nullstelle von \( f \) mit
  Wechsel \( -\to+ \)), **Wendepunkt bei \( x=1 \)** (Tiefpunkt von \( f \)), **kein Hochpunkt**.
  *Rückfrage:* „Wo am Graphen von \( f \) erkennt man einen Tiefpunkt von \( F \)?" *Rote Flagge:* Hoch-
  und Tiefpunkte von \( f \) mit denen von \( F \) verwechseln.
- **d) Zuordnung.** Erwartet: \( f_2(x)=(x-2)e^x \); Begründung über **Nullstelle bei \( x=2 \)**
  (\( f_3(2)\neq 0 \)) und **Tiefpunktlage/Randverhalten** (\( f_1 \) liegt zu hoch bzw. fällt für große
  \( x \) auf 0). *Rückfrage:* „Reicht es, \( f(0) \) zu prüfen?" (Antwort: nein, alle drei geben \( -2 \).)
- **e) Graph von \( g \).** Erwartet: **Nullstelle/Berührung bei \( x=2 \)** (doppelt), \( g\ge 0 \),
  links \( \to 0 \), rechts \( \to +\infty \), Hochpunkt \( H(0\,|\,4) \). *Rückfrage:* „Schneidet oder
  berührt der Graph bei \( x=2 \) die Achse, und warum?"

</details>

<details><summary>Leitfaden Teil 2 (Stochastik) aufklappen</summary>

- **Kurve skizzieren.** Erwartet: **Glocke**, symmetrisch um \( 20 \), Maximum bei \( 20 \), Wendepunkte
  bei \( 16 \) und \( 24 \), Fläche \( =1 \). *Rückfrage:* „Wofür steht die Fläche unter der Kurve?"
- **\( P(X\le 21) \), \( P(X=21) \), \( P(X>21) \).** Erwartet: \( P(X=21)=0 \) (stetig!),
  \( P(X\le 21) \) als **Fläche links von 21** (\( \approx 0{,}599 \)), \( P(X>21)=1-P(X\le 21)
  \approx 0{,}401 \). *Rückfrage:* „Warum ist die Wahrscheinlichkeit für genau 21 gleich null?"
- **Sachkontext.** Erwartet: eine **Messgröße** (Füllgewicht, Körpergröße, Messfehler) mit \( \mu=20 \),
  \( \sigma=4 \). *Rote Flagge:* ein Zählkontext (Trefferzahl) — das wäre binomial.
- **\( \mu \) ändern.** Erwartet: Kurve **verschiebt sich seitlich**, Form bleibt. *Rückfrage:* „Ändert
  sich dabei die Breite?"
- **\( \sigma \) ändern.** Erwartet: größeres \( \sigma \) → **breiter und flacher**, kleineres →
  schmaler und höher, Fläche bleibt \( 1 \). *Rückfrage:* „Warum wird die Kurve flacher, wenn sie breiter
  wird?"
- **Binomial gegen Normal.** Erwartet: **diskret gegen stetig**, Balken gegen Fläche, \( P(X=k)>0 \)
  gegen \( P(X=x)=0 \); Normalverteilung als **Näherung** der Binomialverteilung für große \( n \).
- **AB III — diskrete Verteilung.** Erwartet: **\( B(100;\,0{,}2) \)** über \( np=20 \) und
  \( np(1-p)=16 \); Probe \( \mu=20 \), \( \sigma=4 \). *Hinweis für dich:* Andere passende Verteilungen
  sind erlaubt; die Binomialverteilung ist der Standardweg.

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Wie liest du \( f'(0) \) aus einem Graphen ab, und was bedeutet dieser Wert anschaulich?
- Warum ist \( \int_0^2 f(x)\,dx \) hier negativ, und wie kommst du ohne Rechner an den Zahlenwert?
- Welche Stelle am Graphen von \( f \) liefert einen Tiefpunkt von \( F \), und welche einen Wendepunkt?
- Warum genügt es nicht, \( f(0) \) zu prüfen, um den richtigen Funktionsterm zu finden?
- Wie verändert sich die Glockenkurve, wenn du \( \mu \) änderst — und wie, wenn du \( \sigma \) änderst?
- Warum ist \( P(X=21)=0 \), und wie bestimmst du \( P(X\le 21) \)?
- Wie findest du eine Binomialverteilung, deren Histogramm der Glocke \( N(20;4) \) gleicht?
</content>
</invoke>
