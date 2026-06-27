# Aufgabe 3 — Analysis & Geometrie

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Analysis** (eine Sinus-Funktion: verschieben, ableiten, Fläche),
**Teil 2 (Gespräch) aus der Geometrie** (zwei Geraden im Raum: Lage, Abstand, Ebene). Alles ist
**rechnerfrei** zu lösen. Arbeitet die Aufgabe wie eine echte Simulation durch — eine Person trägt
vor, die andere prüft mit dem Lösungsweg und dem
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

> **Werkzeug zum Nachschlagen:** Die Analysis-Werkzeuge (Ableiten, Stammfunktion, Integral, Sinus als
> Grundfunktion) stehen kompakt in den Kapiteln [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Integral-Grundlagen](kap-integral-grundlagen.html),
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html) und
> [Grundfunktionen](kap-grundfunktionen.html). Die wiederkehrenden Vektor- und Geometrie-Werkzeuge
> (Punkte, Vektoren, Länge, Skalarprodukt, Kreuzprodukt, Ebenengleichung) findest du im
> [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html).

---

## Teil 1 — Vortrag (Analysis): Sinus-Funktion verschieben, ableiten, Fläche

<div class="aufgabenkasten">

**Gegeben ist die Funktion \( f \) mit \( f(x) = 2\cdot\sin\!\left(x - \tfrac{\pi}{2}\right) + 3 \).**

**a)** Abbildung 1 zeigt den Graphen von \( f \). Erläutere, wie man den Graphen von \( f \) aus dem
Graphen der Funktion \( g \) mit \( g(x) = \sin(x) \) erhält.

**b)** Eine der Abbildungen 2 und 3 zeigt den Graphen von \( f' \). Entscheide, in welcher der
Abbildungen der Graph von \( f' \) dargestellt ist, und begründe deine Entscheidung. Begründe außerdem
**ohne Rechnung**, dass \( \displaystyle\int_{-\pi}^{\pi} f'(x)\,dx = 0 \) gilt.

**c)** Berechne das Integral \( \displaystyle\int_{0}^{\pi} \big(5 - f(x)\big)\,dx \) und interpretiere
dein Ergebnis geometrisch.

**d)** Entscheide, ob die folgende Aussage wahr oder falsch ist, und begründe deine Entscheidung:
*„Eine trigonometrische Funktion ist durch die Angabe der Koordinaten eines beliebigen Hochpunktes und
eines beliebigen Tiefpunktes ihres Graphen eindeutig bestimmt."*

</div>

Hier ist zuerst der Graph von \( f \) (Abbildung 1). Spiele mit dem Bild und finde Hoch- und
Tiefpunkte, bevor du die Lösung aufklappst.

<figure>
<div class="jxgbox" id="jxg-k3-abb1" style="width:100%;max-width:520px;aspect-ratio:2/1"></div>
<figcaption>Abbildung 1 — Graph von \( f(x)=2\sin\!\left(x-\tfrac{\pi}{2}\right)+3 \): Tiefpunkte bei \( y=1 \), Hochpunkte bei \( y=5 \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k3-abb1',{boundingbox:[-3.6,6,9.9,-1.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 2*Math.sin(x-Math.PI/2)+3;},-3.5,9.7],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('line',[[-3.5,3],[9.7,3]],{straightFirst:false,straightLast:false,strokeColor:'#7a7163',strokeWidth:1,dash:2});})();</script>

Und hier die beiden Kandidaten für den Graphen von \( f' \). **Genau einer** ist richtig — entscheide
selbst, bevor du aufklappst.

<div class="graph-row">
<figure>
<div class="jxgbox" id="jxg-k3-abb2" style="width:100%;max-width:340px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 2</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k3-abb3" style="width:100%;max-width:340px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 3</figcaption>
</figure>
</div>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k3-abb2',{boundingbox:[-3.6,3.6,9.9,-3.6],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 2*Math.sin(x);},-3.5,9.7],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k3-abb3',{boundingbox:[-3.6,3.6,9.9,-3.6],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return -2*Math.sin(x);},-3.5,9.7],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>

### Teilaufgabe a) — Den Graphen aus \( \sin(x) \) erhalten

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Man liest die drei Veränderungen direkt am Funktionsterm \( f(x) = 2\cdot\sin\!\left(x-\tfrac{\pi}{2}\right)+3 \)
ab und nennt sie der Reihe nach:

- **Faktor \( 2 \) vor dem Sinus → Streckung um den Faktor \( 2 \) in \( y \)-Richtung.** Die Welle wird
  doppelt so hoch; statt zwischen \( -1 \) und \( 1 \) schwingt sie jetzt zwischen \( -2 \) und \( 2 \).
- **\( \left(x-\tfrac{\pi}{2}\right) \) im Inneren → Verschiebung um \( \tfrac{\pi}{2} \) in
  \( x \)-Richtung** (nach **rechts**).
- **\( +3 \) am Ende → Verschiebung um \( 3 \) in \( y \)-Richtung** (nach **oben**). Die Mittellinie der
  Welle liegt damit bei \( y=3 \), und die Welle schwingt zwischen \( 1 \) und \( 5 \).

**Ergebnis:** Streckung um \( 2 \) in \( y \)-Richtung, Verschiebung um \( \tfrac{\pi}{2} \) in
\( x \)-Richtung, Verschiebung um \( 3 \) in \( y \)-Richtung.

<details><summary>Haltung dahinter: Was heißt „den Graphen aus \( g \) erhalten"? (ganz von vorn)</summary>

Zuerst, worum es überhaupt geht. \( g(x)=\sin(x) \) ist die **Grundwelle**: Sie kommt vom Kreis,
**wiederholt sich** in immer gleichen Abständen (das nennt man **periodisch**), schwingt zwischen
\( -1 \) und \( 1 \) und startet bei \( x=0 \) im Wert \( 0 \) ansteigend. Aus dieser einen Grundwelle
kann man durch ein paar kleine Eingriffe jede andere Sinus-Welle bauen. Die Aufgabe verlangt, diese
Eingriffe zu benennen.

Es gibt drei **Stellschrauben**, und man erkennt jede an einer anderen Stelle im Term:

- **Eine Zahl direkt vor dem Sinus** (hier die \( 2 \)) macht die Welle **höher oder flacher** — eine
  *Streckung in die Höhe*. Diese Zahl heißt **Amplitude** (das ist der Abstand von der Mittellinie bis
  zum höchsten Punkt). Aus Amplitude \( 1 \) wird Amplitude \( 2 \): die Welle wird doppelt so hoch.
- **Eine Zahl, die innen vom \( x \) abgezogen wird** (hier \( -\tfrac{\pi}{2} \)) **verschiebt die
  ganze Welle waagerecht**. Das nennt man **Phasenverschiebung**.
- **Eine Zahl, die ganz am Ende dazukommt** (hier \( +3 \)) **hebt die ganze Welle nach oben**. Die
  waagerechte Linie, um die die Welle schwingt (die **Mittellinie**), rutscht von \( y=0 \) auf
  \( y=3 \).

Eine Alltagsanalogie: Stell dir eine Schaukel vor. Die Amplitude ist, **wie weit** sie ausschlägt
(Faktor 2 = doppelt so weit). Die Phasenverschiebung ist, **wann** der Schwung beginnt (etwas später).
Die \( +3 \) ist die **Höhe des ganzen Schaukelgerüsts** über dem Boden.

<details><summary>… ganz langsam (mit Zahlen): woran sieht man das im Bild?</summary>

Prüfen wir die drei Eingriffe an konkreten Punkten nach.

**Tiefpunkt bei \( x=0 \).** Setze \( x=0 \) ein:
\[ f(0) = 2\cdot\sin\!\left(0-\tfrac{\pi}{2}\right) + 3 = 2\cdot\sin\!\left(-\tfrac{\pi}{2}\right) + 3. \]
Nun ist \( \sin\!\left(-\tfrac{\pi}{2}\right) = -1 \) (der Sinus ist an dieser Stelle ganz unten), also
\[ f(0) = 2\cdot(-1) + 3 = -2 + 3 = 1. \]
Im Bild sitzt der Graph bei \( x=0 \) tatsächlich auf seinem **tiefsten** Wert \( y=1 \). Das zeigt
zweierlei auf einmal: die Mittellinie liegt bei \( 3 \) (\( +3 \)-Verschiebung) und die Amplitude ist
\( 2 \) (von \( 3 \) bis \( 1 \) sind es \( 2 \) nach unten).

**Hochpunkt bei \( x=\pi \).** Der Sinus ist am höchsten (\( =1 \)), wenn sein Inneres \( \tfrac{\pi}{2} \)
ist, also wenn \( x-\tfrac{\pi}{2}=\tfrac{\pi}{2} \), das heißt \( x=\pi \). Dann
\[ f(\pi) = 2\cdot 1 + 3 = 5. \]
Im Bild liegt der Hochpunkt bei \( (\pi \mid 5) \). Passt. Dass der erste Hochpunkt erst bei \( \pi \)
statt schon bei \( \tfrac{\pi}{2} \) (wie beim reinen Sinus) kommt, ist genau die **Verschiebung nach
rechts** um \( \tfrac{\pi}{2} \).

</details>

<details><summary>Typische Falle: „minus heißt nach links" — falsch herum</summary>

Bei \( \left(x-\tfrac{\pi}{2}\right) \) denken viele „minus, also nach links". Im **Inneren** der
Funktion ist es **genau umgekehrt**: Ein **Abziehen** verschiebt nach **rechts**, ein **Addieren** nach
links. Eselsbrücke: Die Welle erreicht ihren gewohnten Wert erst, wenn das Innere wieder den alten Wert
hat — und dafür muss \( x \) **größer** sein, also weiter rechts. (Eine Zahl **außerhalb**, wie das
\( +3 \), verschiebt dagegen ganz normal nach oben.)

</details>
</details>
</details>

### Teilaufgabe b) — Welcher Graph ist \( f' \)? Und warum ist das Integral null?

<span class="tag tag-ok">AB I</span> <span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Teil 1: Welche Abbildung zeigt \( f' \)?** Der Graph von \( f' \) ist in **Abbildung 2**
dargestellt.

**Begründung über die Steigung.** Die Ableitung \( f' \) gibt an jeder Stelle die **Steigung** des
Graphen von \( f \) an. An der Stelle \( x_1=\tfrac{\pi}{2} \) steigt der Graph von \( f \) (er ist auf
dem Weg von seinem Tiefpunkt bei \( x=0 \) hinauf zum Hochpunkt bei \( x=\pi \)), hat dort also eine
**positive Steigung**. Damit muss \( f'\!\left(\tfrac{\pi}{2}\right) > 0 \) sein. In **Abbildung 2** ist
der Wert an der Stelle \( \tfrac{\pi}{2} \) tatsächlich **positiv** (dort liegt ein Hochpunkt bei
\( +2 \)); in Abbildung 3 wäre er negativ. Also gehört Abbildung 2 zu \( f' \).

**Teil 2: Warum ist \( \displaystyle\int_{-\pi}^{\pi} f'(x)\,dx = 0 \) — ohne Rechnung?**

Der Graph von \( f' \) ist **punktsymmetrisch zum Ursprung**. Die Fläche zwischen dem Graphen von
\( f' \) und der \( x \)-Achse über dem Intervall \( [-\pi;\,0] \) ist deshalb **genauso groß** wie die
über dem Intervall \( [0;\,\pi] \). Die eine liegt **unterhalb**, die andere **oberhalb** der
\( x \)-Achse. Im Integral zählt die eine negativ, die andere positiv, und weil sie gleich groß sind,
**heben sie sich auf** — das Integral ist \( 0 \).

<details><summary>Haltung dahinter: Was ist die Ableitung, und wie liest man an ihr „Steigung" ab?</summary>

**Ableiten misst Steigung.** Die **Ableitung** \( f' \) einer Funktion \( f \) ist selbst wieder eine
Funktion. Ihr Wert an einer Stelle sagt, **wie steil** der Graph von \( f \) dort ist:

- \( f'>0 \): der Graph von \( f \) **steigt** dort (geht bergauf).
- \( f'<0 \): der Graph von \( f \) **fällt** dort (geht bergab).
- \( f'=0 \): der Graph ist dort **waagerecht** — typisch an Hoch- und Tiefpunkten (der „Gipfel" oder
  das „Tal" ist für einen Moment flach).

Genau über diese drei Regeln entscheidet man, welcher der beiden Bilder zu \( f' \) passt: Man sucht
sich Stellen, an denen man die Steigung von \( f \) sicher kennt, und prüft, ob der Kandidatengraph
dort den passenden Wert hat.

**Der bequemste Prüfpunkt hier: \( x=\tfrac{\pi}{2} \).** Dort klettert \( f \) gerade von unten nach
oben — die Steigung ist klar **positiv**. Also muss der wahre \( f' \)-Graph dort **über** der
\( x \)-Achse liegen. Das tut nur Abbildung 2.

<details><summary>Noch eine Probe: die Tiefpunkte von \( f \)</summary>

\( f \) hat einen **Tiefpunkt** bei \( x=0 \) (dort ist \( f(0)=1 \), der kleinste Wert). An einem
Tiefpunkt ist der Graph für einen Moment waagerecht, also \( f'(0)=0 \). Beide Kandidaten gehen durch
den Ursprung (Wert \( 0 \) bei \( x=0 \)) — das passt also für beide und entscheidet noch nicht. Schaut
man aber **kurz rechts** von \( 0 \): \( f \) steigt (auf dem Weg zum Hochpunkt), also \( f'>0 \) direkt
nach \( 0 \). Nur Abbildung 2 ist direkt rechts von \( 0 \) positiv (sie steigt vom Ursprung an).
Abbildung 3 fällt dort ins Negative — passt nicht.

</details>

<details><summary>Für Neugierige: \( f' \) ausgerechnet (nicht verlangt)</summary>

Mit der **Kettenregel** (innere Ableitung von \( x-\tfrac{\pi}{2} \) ist \( 1 \)) gilt
\[ f'(x) = 2\cdot\cos\!\left(x-\tfrac{\pi}{2}\right) = 2\sin(x). \]
Das ist genau die Welle in Abbildung 2 (eine Sinuswelle mit Amplitude \( 2 \), durch den Ursprung
ansteigend). Für den Vortrag genügt aber die **Steigungs-Begründung** oben; Ausrechnen ist nicht nötig.

</details>
</details>

<details><summary>Haltung dahinter: Warum ist das Integral null? (Symmetrie statt Rechnen)</summary>

**Was ein Integral mit Vorzeichen macht.** Das Integral \( \int_a^b f'(x)\,dx \) rechnet die Fläche
zwischen dem Graphen und der \( x \)-Achse zusammen — aber **mit Vorzeichen**. Fläche **oberhalb** der
Achse zählt **positiv**, Fläche **unterhalb** zählt **negativ**. Ein gutes Bild ist ein **Bankkonto**:
oben = Einzahlung (\( + \)), unten = Abhebung (\( - \)). Am Ende nennt das Integral nur den
**Kontostand**, also die Differenz.

**Punktsymmetrisch zum Ursprung** heißt: Dreht man den Graphen um \( 180^\circ \) um den Nullpunkt,
liegt er wieder genau auf sich selbst. Für eine solche Funktion gilt: Was links vom Nullpunkt unter der
Achse liegt, ist das gespiegelte Gegenstück zu dem, was rechts über der Achse liegt — **gleich groß,
aber mit umgekehrtem Vorzeichen**.

Über \( [-\pi;0] \) liegt der \( f' \)-Graph (das ist \( 2\sin x \)) **unter** der Achse → negativer
Beitrag. Über \( [0;\pi] \) liegt er **über** der Achse → positiver Beitrag, gleich groß. Eine
Einzahlung und eine gleich große Abhebung ergeben Kontostand \( 0 \). Deshalb ist
\( \int_{-\pi}^{\pi} f'(x)\,dx = 0 \) — **ohne** dass man eine Stammfunktion ausrechnen muss.

<details><summary>Die elegante Kurzbegründung (für ein gutes Gespräch)</summary>

Es gibt noch ein zweites Argument, das sogar für **jede** Funktion \( f \) sofort greift: Ein Integral
über die Ableitung gibt die **Gesamtänderung** der Ausgangsfunktion zurück:
\[ \int_{-\pi}^{\pi} f'(x)\,dx = f(\pi) - f(-\pi). \]
Und weil \( f \) die **Periode** \( 2\pi \) hat, ist \( f(\pi)=f(-\pi) \) (beide Stellen liegen genau
eine Periode auseinander, der Funktionswert ist gleich). Die Differenz ist dann \( 0 \). Das ist
ebenfalls „ohne Rechnung" — man muss nur die Periodizität nennen. Beide Begründungen sind voll
gültig; die Symmetrie-Begründung ist die im Erwartungshorizont genannte.

</details>

<details><summary>Typische Falle: \( f' \) mit \( f \) verwechseln</summary>

Ein häufiger Fehler ist, den Graphen von \( f \) selbst für \( f' \) zu halten. Merke: \( f' \) zeigt
die **Steigung** von \( f \), nicht die Höhe. Dort, wo \( f \) einen **Hoch- oder Tiefpunkt** hat
(waagerecht), muss \( f' \) **durch null** gehen. Diese „Nullstellen von \( f' \) unter den
Extrempunkten von \( f \)" sind der schnellste Plausibilitäts-Check.

</details>
</details>
</details>

### Teilaufgabe c) — Integral \( \int_0^\pi (5-f(x))\,dx \) und geometrische Deutung

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Schritt 1 — den Integranden vereinfachen.** Setze \( f \) ein und fasse zusammen:
\[ 5 - f(x) = 5 - \Big(2\sin\!\left(x-\tfrac{\pi}{2}\right) + 3\Big) = 2 - 2\sin\!\left(x-\tfrac{\pi}{2}\right). \]

**Schritt 2 — Stammfunktion bilden.** Eine Stammfunktion von \( 2 \) ist \( 2x \). Eine Stammfunktion
von \( -2\sin\!\left(x-\tfrac{\pi}{2}\right) \) ist \( +2\cos\!\left(x-\tfrac{\pi}{2}\right) \) (die
Stammfunktion von \( \sin \) ist \( -\cos \); das doppelte Minus wird zu Plus). Also
\[ F(x) = 2x + 2\cos\!\left(x-\tfrac{\pi}{2}\right) = 2\left[\,x + \cos\!\left(x-\tfrac{\pi}{2}\right)\right]. \]

**Schritt 3 — Grenzen einsetzen (Hauptsatz).**
\[ \int_0^\pi \big(5-f(x)\big)\,dx = 2\Big[\,x + \cos\!\left(x-\tfrac{\pi}{2}\right)\Big]_0^\pi
   = 2\Big(\pi + \underbrace{\cos\!\left(\tfrac{\pi}{2}\right)}_{=\,0}\Big) - 2\Big(0 + \underbrace{\cos\!\left(-\tfrac{\pi}{2}\right)}_{=\,0}\Big) = 2\pi. \]

**Ergebnis:** \( \displaystyle\int_0^\pi \big(5-f(x)\big)\,dx = 2\pi \).

**Geometrische Interpretation.** Auf \( [0;\pi] \) liegt der Graph von \( f \) **vollständig unterhalb**
der waagerechten Geraden \( y=5 \) (sein größter Wert \( 5 \) wird erst bei \( x=\pi \) erreicht).
Deshalb ist \( 5-f(x)\ge 0 \), und das Integral misst genau die **Fläche zwischen der Geraden
\( y=5 \) und dem Graphen von \( f \)** über dem Intervall \( [0;\pi] \). Diese Fläche hat den Inhalt
\( 2\pi \) Flächeneinheiten (FE) \( \approx 6{,}28 \).

<figure>
<div class="jxgbox" id="jxg-k3-c" style="width:100%;max-width:480px;aspect-ratio:5/4"></div>
<figcaption>Die orange Fläche zwischen der Geraden \( y=5 \) (grün) und dem Graphen von \( f \) (blau) über \( [0;\pi] \) hat den Inhalt \( 2\pi \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k3-c',{boundingbox:[-0.6,6,4.1,-0.8],axis:true,showCopyright:false,showNavigation:false});var ff=function(x){return 2*Math.sin(x-Math.PI/2)+3;};var X=[],Y=[],n=60,i,xx;for(i=0;i<=n;i++){xx=Math.PI*i/n;X.push(xx);Y.push(5);}for(i=n;i>=0;i--){xx=Math.PI*i/n;X.push(xx);Y.push(ff(xx));}b.create('curve',[X,Y],{fillColor:'#d98324',fillOpacity:0.2,strokeWidth:0});b.create('line',[[0,5],[Math.PI,5]],{straightFirst:false,straightLast:false,strokeColor:'#3a8a5a',strokeWidth:2.5});b.create('functiongraph',[ff,-0.5,4],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>

<details><summary>Haltung dahinter: Warum misst „\( \int(5-f) \)" eine Fläche zwischen zwei Linien?</summary>

**Erst der Begriff Integral.** Ein Integral \( \int_a^b (\text{Höhe})\,dx \) addiert unendlich viele
hauchdünne senkrechte Streifen auf — jeder Streifen ist so **hoch** wie der Integrand und unendlich
schmal. Ist der Integrand die **Höhe** zwischen zwei Linien, dann addiert das Integral die Streifen
**zwischen** diesen Linien — und das ist die eingeschlossene Fläche.

**Warum \( 5 - f(x) \) die richtige Höhe ist.** An jeder Stelle \( x \) ist der senkrechte Abstand von
der oberen Linie \( y=5 \) hinunter zum Graphen von \( f \) genau \( (\text{oben}) - (\text{unten}) =
5 - f(x) \). Solange \( f \) **unter** der \( 5 \) bleibt, ist dieser Abstand positiv, und das
Aufaddieren der Streifen liefert eine echte Fläche.

Alltagsbild: \( y=5 \) ist eine waagerechte Decke, \( f \) der wellige Boden darunter. Wie viel
**Luft** ist dazwischen? Man misst an jeder Stelle die Deckenhöhe minus Bodenhöhe (\( 5-f(x) \)) und
addiert alles über \( [0;\pi] \) auf. Heraus kommt \( 2\pi \).

<details><summary>Schritt 2 ganz langsam: Stammfunktion von \( -2\sin\!\left(x-\tfrac{\pi}{2}\right) \)</summary>

Eine **Stammfunktion** ist „Ableiten rückwärts": gesucht ist eine Funktion, deren Ableitung wieder der
Integrand ist. Zwei Bausteine:

- Von der Zahl \( 2 \): Stammfunktion ist \( 2x \) (denn \( (2x)' = 2 \)).
- Von \( -2\sin\!\left(x-\tfrac{\pi}{2}\right) \): Die Stammfunktion von \( \sin(u) \) ist
  \( -\cos(u) \). Hier ist \( u = x-\tfrac{\pi}{2} \) (das Innere). Also ist die Stammfunktion von
  \( \sin\!\left(x-\tfrac{\pi}{2}\right) \) gleich \( -\cos\!\left(x-\tfrac{\pi}{2}\right) \). Davor
  steht noch das \( -2 \):
  \[ -2 \cdot \Big(-\cos\!\left(x-\tfrac{\pi}{2}\right)\Big) = +2\cos\!\left(x-\tfrac{\pi}{2}\right). \]
  **Minus mal Minus ist Plus** — deshalb wird aus dem Sinus mit Minus ein Kosinus mit Plus.

Das innere \( x-\tfrac{\pi}{2} \) bleibt beim Integrieren unverändert, weil seine **Ableitung \( 1 \)**
ist (es gibt keinen zusätzlichen Faktor zu korrigieren). Zusammen:
\( F(x) = 2x + 2\cos\!\left(x-\tfrac{\pi}{2}\right) \).

**Einsetzen, Ziffer für Ziffer.** Bei \( x=\pi \): \( \cos\!\left(\pi-\tfrac{\pi}{2}\right) =
\cos\!\left(\tfrac{\pi}{2}\right) = 0 \), also \( F(\pi) = 2\pi + 2\cdot 0 = 2\pi \). Bei \( x=0 \):
\( \cos\!\left(0-\tfrac{\pi}{2}\right) = \cos\!\left(-\tfrac{\pi}{2}\right) = 0 \), also
\( F(0) = 0 + 2\cdot 0 = 0 \). Differenz: \( 2\pi - 0 = 2\pi \).

</details>

<details><summary>Typische Falle: Vorzeichen und „Fläche nur, wenn eine Linie oben bleibt"</summary>

Zwei Stolpersteine:

1. **Reihenfolge im Integranden.** Man rechnet *obere minus untere* Linie, also \( 5 - f(x) \). Wer
   \( f(x) - 5 \) bildet, bekommt \( -2\pi \) — den richtigen Betrag mit falschem Vorzeichen.
2. **Die obere Linie muss auch wirklich oben bleiben.** Das Ergebnis \( 2\pi \) ist genau dann der
   Flächeninhalt, wenn \( f \) auf dem ganzen Intervall \( \le 5 \) ist. Hier stimmt das (\( f \)
   erreicht die \( 5 \) erst am Rand \( x=\pi \)). Würde die Kurve die Gerade dazwischen kreuzen, müsste
   man wie bei jeder Flächenaufgabe an den Schnittstellen trennen und Beträge addieren.

</details>
</details>
</details>

### Teilaufgabe d) — Wahr oder falsch: Hochpunkt + Tiefpunkt bestimmen die Funktion?

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Die Aussage ist **falsch**.

**Begründung.** Ein Hochpunkt und ein Tiefpunkt legen zwar die **Amplitude** (über den Höhenunterschied)
und die **Mittellinie** fest, aber **nicht die Periode**. Zwischen einem gegebenen Hochpunkt und einem
gegebenen Tiefpunkt können **beliebig viele weitere Extrempunkte** liegen — die Welle kann auf demselben
Weg einmal, dreimal, fünfmal … durchschwingen. Jede dieser Möglichkeiten gehört zu einer **anderen
Periode** und damit zu einer **anderen Funktion**, die trotzdem durch genau denselben Hoch- und denselben
Tiefpunkt verläuft. Die Funktion ist also **nicht eindeutig** bestimmt.

<details><summary>Haltung dahinter: Was legt eine Sinus-Welle eindeutig fest? (ganz von vorn)</summary>

Eine allgemeine Sinus-Funktion hat die Form
\[ y = a\cdot\sin\!\big(b\,(x - c)\big) + d, \]
mit **vier** Stellschrauben:

- **\( a \) — Amplitude:** wie hoch die Welle ausschlägt (halbe Höhe von Tief bis Hoch).
- **\( d \) — Mittellinie:** die waagerechte Linie, um die geschwungen wird.
- **\( b \) — Frequenz/Periode:** wie **eng** die Wellen stehen (große \( b \) → schnelle, enge Wellen).
- **\( c \) — Phasenverschiebung:** wo die Welle waagerecht beginnt.

Um die Funktion **eindeutig** zu kennen, muss man alle vier Schrauben festlegen. Schauen wir, was ein
Hochpunkt \( H \) und ein Tiefpunkt \( T \) hergeben:

- Ihre **\( y \)-Werte** liefern Amplitude und Mittellinie: \( d \) ist der Mittelwert der beiden Höhen,
  \( a \) ist ihr halber Abstand. **Diese zwei Schrauben sind also bestimmt.**
- Ihre **\( x \)-Werte** sagen nur, dass zwischen \( H \) und \( T \) ein **ungerades Vielfaches einer
  halben Periode** liegt (von einem Gipfel zum nächsten Tal ist es eine halbe Periode, zum übernächsten
  Tal anderthalb Perioden, usw.). Das lässt **viele** Perioden zu — die Schrauben \( b \) und \( c \)
  bleiben **offen**.

Weil \( b \) (und damit auch \( c \)) nicht festliegt, gibt es **unendlich viele** Funktionen mit
demselben \( H \) und \( T \). Die Aussage ist deshalb falsch.

<details><summary>… ganz langsam (mit Zahlen): ein konkretes Gegenbeispiel</summary>

Nimm den Hochpunkt \( H(0 \mid 1) \) und den Tiefpunkt \( T(\pi \mid -1) \) (Amplitude \( 1 \),
Mittellinie \( 0 \)).

- **Möglichkeit A:** \( H \) und \( T \) liegen eine **halbe** Periode auseinander. Dann ist die
  Periode \( 2\pi \), und die Funktion ist \( y = \cos(x) \): bei \( x=0 \) oben (\( =1 \)), bei
  \( x=\pi \) unten (\( =-1 \)). ✓
- **Möglichkeit B:** \( H \) und \( T \) liegen **anderthalb** Perioden auseinander. Dann ist die
  Periode \( \tfrac{2}{3}\pi \), und die Funktion ist \( y = \cos(3x) \): bei \( x=0 \) wieder oben
  (\( =1 \)), bei \( x=\pi \) wieder unten (\( \cos(3\pi)=-1 \)). ✓ Dazwischen schwingt sie aber noch
  zweimal extra durch.

Beide Funktionen — \( \cos(x) \) und \( \cos(3x) \) — gehen durch **genau denselben** Hoch- und
Tiefpunkt, sind aber **verschieden**. Damit ist gezeigt: zwei Punkte dieser Art bestimmen die Funktion
nicht eindeutig.

</details>

<details><summary>Typische Falle: „zwei Punkte legen doch alles fest"</summary>

Bei einer **Geraden** stimmt das (zwei Punkte → genau eine Gerade). Bei einer **periodischen** Funktion
nicht: Das Wesen der Welle ist ihre **Wiederholung**, und gerade die **Wiederholrate** (die Periode)
bleibt durch zwei Extrempunkte unbestimmt. Wer „falsch" sagt, sollte deshalb das Stichwort **Periode /
weitere Extrempunkte dazwischen** nennen — daran erkennt die Prüferin die echte Begründung.

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- **a)** Streckung um \( 2 \) in \( y \)-Richtung, Verschiebung um \( \tfrac{\pi}{2} \) in
  \( x \)-Richtung (nach rechts), Verschiebung um \( 3 \) in \( y \)-Richtung (nach oben).
- **b)** \( f' \) ist **Abbildung 2** (denn \( f \) steigt bei \( x=\tfrac{\pi}{2} \), also
  \( f'\!\left(\tfrac{\pi}{2}\right)>0 \)). Das Integral ist \( 0 \), weil der \( f' \)-Graph
  **punktsymmetrisch** ist und sich die gleich großen Flächen ober- und unterhalb der Achse aufheben.
- **c)** \( \int_0^\pi (5-f)\,dx = 2\pi \) FE = Fläche zwischen \( y=5 \) und dem Graphen von \( f \)
  über \( [0;\pi] \).
- **d)** **Falsch** — Hoch- und Tiefpunkt legen die **Periode** nicht fest; dazwischen können beliebig
  viele weitere Extrempunkte liegen.

</details>

---

## Teil 2 — Gespräch (Geometrie): Geraden im Raum — Lage, Abstand, Ebene

<div class="aufgabenkasten">

**Input.**
\[ \text{Gerade } g:\ \vec{x} = \begin{pmatrix}1\\-2\\3\end{pmatrix} + t\cdot\begin{pmatrix}1\\-2\\2\end{pmatrix}\quad (t\in\mathbb{R}); \qquad
   \text{Gerade } h \text{ durch } A(2\,|\,5\,|\,-2)\ \text{und}\ B(6\,|\,2\,|\,-2). \]

Im Gespräch denkbare Aspekte: **(AB I)** eine Gleichung der Geraden \( h \) ermitteln; alle
Bestandteile der Geradengleichung von \( g \) geometrisch deuten; eine Punktprobe durchführen; weitere
Gleichungen von \( g \) angeben. **(AB II)** die gegenseitige Lage von \( g \) und \( h \) bestimmen;
eine weitere Gerade ermitteln, die parallel zu \( g \) ist und \( h \) schneidet; Punkte auf \( g \)
bestimmen, die vom Punkt \( P(1\,|\,-2\,|\,3) \) den Abstand \( 6 \) haben. **(AB III)** eine Gleichung
der Ebene \( E \) bestimmen, die \( g \) enthält und parallel zu \( h \) liegt; eine Gleichung der
Geraden durch einen gegebenen Punkt ermitteln, die \( g \) orthogonal schneidet.

</div>

> **Vorab, in einem Satz, was eine „Gerade im Raum" ist:** Eine Gerade gibt man durch **einen Punkt
> darauf** (den *Stützpunkt*, ein fester Startort) und eine **Richtung** (den *Richtungsvektor*, ein
> Pfeil, der sagt, wohin die Gerade läuft) an. Der **Parameter** \( t \) ist ein Drehregler: Für jeden
> Wert von \( t \) bekommt man genau einen Punkt der Geraden; lässt man \( t \) über alle Zahlen
> laufen, durchläuft man die ganze Gerade. Alle Vektor-Werkzeuge stehen kompakt im
> [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html).

So liegen die beiden Geraden zueinander (schematische Darstellung):

<figure>
<svg viewBox="0 0 470 320" role="img" aria-label="Schematische Lage der windschiefen Geraden g und h im Koordinatensystem" style="width:100%;max-width:480px;height:auto;background:#fbf7ef;border-radius:8px">
  <defs>
    <marker id="ah3" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#7a7163"/></marker>
  </defs>
  <line x1="170" y1="190" x2="170" y2="55"  stroke="#7a7163" stroke-width="1.5" marker-end="url(#ah3)"/>
  <line x1="170" y1="190" x2="415" y2="190" stroke="#7a7163" stroke-width="1.5" marker-end="url(#ah3)"/>
  <line x1="170" y1="190" x2="68"  y2="272" stroke="#7a7163" stroke-width="1.5" marker-end="url(#ah3)"/>
  <text x="156" y="54"  font-size="13" fill="#7a7163">x₃</text>
  <text x="419" y="194" font-size="13" fill="#7a7163">x₂</text>
  <text x="54"  y="280" font-size="13" fill="#7a7163">x₁</text>
  <line x1="120" y1="95" x2="280" y2="255" stroke="#3a5a9c" stroke-width="2.4"/>
  <circle cx="200" cy="175" r="3.5" fill="#3a5a9c"/>
  <text x="208" y="171" font-size="12" fill="#26324a">P(1|−2|3)</text>
  <text x="284" y="261" font-size="13" fill="#3a5a9c" font-weight="bold">g</text>
  <line x1="130" y1="235" x2="213" y2="204" stroke="#d98324" stroke-width="2.4"/>
  <line x1="238" y1="195" x2="360" y2="150" stroke="#d98324" stroke-width="2.4"/>
  <circle cx="130" cy="235" r="3.5" fill="#d98324"/>
  <text x="90"  y="249" font-size="12" fill="#8a5a14">A(2|5|−2)</text>
  <circle cx="360" cy="150" r="3.5" fill="#d98324"/>
  <text x="320" y="142" font-size="12" fill="#8a5a14">B(6|2|−2)</text>
  <text x="364" y="160" font-size="13" fill="#d98324" font-weight="bold">h</text>
</svg>
<figcaption>Schematisch: \( g \) (blau) und \( h \) (orange) verlaufen **windschief** — in der Zeichnung kreuzen sich nur ihre Projektionen, im Raum treffen sie sich nicht (\( g \) läuft an der scheinbaren Kreuzung vorn vorbei).</figcaption>
</figure>

### AB I — Gleichung von \( h \), Bestandteile von \( g \), Punktprobe, weitere Gleichungen

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Eine Gleichung der Geraden \( h \).** \( h \) ist durch zwei Punkte gegeben. Als **Richtungsvektor**
nimmt man den Verbindungspfeil „Ziel minus Start":
\[ \overrightarrow{AB} = B - A = \begin{pmatrix}6\\2\\-2\end{pmatrix} - \begin{pmatrix}2\\5\\-2\end{pmatrix}
   = \begin{pmatrix}4\\-3\\0\end{pmatrix}. \]
Als Stützpunkt nimmt man einen der beiden Punkte, etwa \( A \):
\[ h:\ \vec{x} = \begin{pmatrix}2\\5\\-2\end{pmatrix} + s\cdot\begin{pmatrix}4\\-3\\0\end{pmatrix}\quad (s\in\mathbb{R}). \]

**Geometrische Deutung der Bestandteile von \( g \).** In
\( \vec{x} = \begin{pmatrix}1\\-2\\3\end{pmatrix} + t\begin{pmatrix}1\\-2\\2\end{pmatrix} \) bedeutet:

- **Stützvektor \( \begin{pmatrix}1\\-2\\3\end{pmatrix} \):** der Ortsvektor zu einem festen Punkt
  \( P(1\,|\,-2\,|\,3) \) **auf** der Geraden — der „Ankerpunkt". Für \( t=0 \) ist man genau dort.
- **Richtungsvektor \( \begin{pmatrix}1\\-2\\2\end{pmatrix} \):** der „Schritt" entlang der Geraden. Von
  jedem Geradenpunkt aus landet man durch Addieren dieses Pfeils wieder auf der Geraden; er legt die
  **Richtung** fest. Seine Länge ist \( 3 \) (siehe AB II), das heißt: erhöht man \( t \) um \( 1 \),
  bewegt man sich \( 3 \) Längeneinheiten weiter.
- **Parameter \( t\in\mathbb{R} \):** der Drehregler. Jeder Wert von \( t \) wählt genau einen
  Geradenpunkt; \( t>0 \) und \( t<0 \) gehen in die beiden Richtungen, und alle \( t \) zusammen
  ergeben die ganze unendliche Gerade.

**Punktprobe.** Eine Punktprobe prüft, **ob ein Punkt auf der Geraden liegt**. Beispiel mit
\( Q(3\,|\,-6\,|\,7) \): Man verlangt \( Q = P + t\,\vec{u} \), also je Zeile:
\[ 3 = 1 + t,\qquad -6 = -2 - 2t,\qquad 7 = 3 + 2t. \]
Aus der ersten Zeile \( t=2 \); eingesetzt: zweite Zeile \( -2-2\cdot 2 = -6 \) ✓, dritte Zeile
\( 3+2\cdot 2 = 7 \) ✓. Alle drei Zeilen geben **dasselbe** \( t \) → \( Q \) **liegt auf** \( g \).
Gegenprobe mit \( R(2\,|\,0\,|\,5) \): erste Zeile \( 2=1+t \Rightarrow t=1 \), aber zweite Zeile
\( -2-2\cdot 1 = -4 \neq 0 \) → **Widerspruch**, \( R \) liegt **nicht** auf \( g \).

**Weitere Gleichungen von \( g \).** Dieselbe Gerade kann man mit einem **anderen Stützpunkt** und/oder
einem **anderen (parallelen) Richtungsvektor** schreiben. Zum Beispiel der Geradenpunkt für \( t=-1 \)
ist \( (0\,|\,0\,|\,1) \), und ein gestreckter Richtungsvektor ist \( \begin{pmatrix}-1\\2\\-2\end{pmatrix} \):
\[ g:\ \vec{x} = \begin{pmatrix}0\\0\\1\end{pmatrix} + r\cdot\begin{pmatrix}-1\\2\\-2\end{pmatrix}\quad (r\in\mathbb{R}). \]

<details><summary>Haltung dahinter: Punkt, Vektor, Richtungsvektor — ganz von vorn</summary>

**Punkt und Vektor.** Ein **Punkt** ist ein Ort im Raum, angegeben durch drei Zahlen
\( (x_1\mid x_2\mid x_3) \). Ein **Vektor** ist ein **Pfeil** — eine Bewegung mit Richtung und Länge.
Den Pfeil vom Punkt \( A \) zum Punkt \( B \) schreibt man \( \overrightarrow{AB} \) und rechnet ihn als
**„Ziel minus Start"** aus, also \( B - A \). Man zieht jede Koordinate einzeln ab:
\( (6,2,-2)-(2,5,-2) = (4,-3,0) \).

**Warum „Punkt + Richtung" eine Gerade beschreibt.** Stell dir vor, du stehst an einem festen Ort
(Stützpunkt) und gehst immer wieder denselben Schritt (Richtungsvektor) — vorwärts und rückwärts.
Alle Orte, die du so erreichst, bilden eine **gerade Linie**. Der Parameter \( t \) zählt, wie viele
Schritte (auch halbe oder negative) du gehst.

**Warum ist die Gleichung nicht eindeutig?** Man darf an einem **anderen** Geradenpunkt starten (jeder
Punkt der Geraden taugt als Stützpunkt) und man darf einen **längeren oder gespiegelten** Schritt
wählen, solange er **dieselbe Richtung** behält (also ein Vielfaches von \( \vec{u} \) ist). Die
gezeichnete Linie bleibt dieselbe. Deshalb gibt es unendlich viele richtige Gleichungen derselben
Geraden.

<details><summary>Warum entscheidet eine Punktprobe „alle drei Zeilen gleich"?</summary>

Damit \( Q \) auf \( g \) liegt, muss es **ein einziges** \( t \) geben, das gleichzeitig alle drei
Koordinaten trifft. Man rechnet \( t \) aus der bequemsten Zeile aus und **setzt es zur Probe in die
anderen** ein. Stimmen alle, gehört der Punkt zur Geraden. Scheitert auch nur **eine** Zeile (wie bei
\( R \)), liegt der Punkt daneben. Das ist dieselbe Logik wie „eine Adresse muss in Straße, Hausnummer
und Stadt passen" — eine falsche Angabe genügt, und es ist die falsche Tür.

</details>
</details>
</details>

### AB II — Gegenseitige Lage, parallele Schnittgerade, Abstand 6

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Gegenseitige Lage von \( g \) und \( h \).** Zwei Schritte: erst Richtungen vergleichen, dann auf
Schnittpunkt prüfen.

*Sind die Richtungen parallel?* \( \vec{u}=\begin{pmatrix}1\\-2\\2\end{pmatrix} \) und
\( \vec{v}=\begin{pmatrix}4\\-3\\0\end{pmatrix} \). Ein Vielfaches müsste in **allen** Zeilen mit
demselben Faktor klappen — aber \( \tfrac{1}{4}\neq\tfrac{-2}{-3} \), und in der dritten Zeile steht
\( 2 \) gegen \( 0 \). **Nicht parallel.**

*Schneiden sie sich?* Setze \( g=h \) gleich, das gibt drei Gleichungen:
\[ 1 + t = 2 + 4s\quad(\text{I}),\qquad -2 - 2t = 5 - 3s\quad(\text{II}),\qquad 3 + 2t = -2\quad(\text{III}). \]
Aus (III): \( 3+2t=-2 \Rightarrow t=-\tfrac{5}{2} \). In (I): \( 1-\tfrac{5}{2} = 2 + 4s \Rightarrow
-\tfrac{3}{2}=2+4s \Rightarrow s=-\tfrac{7}{8} \). Diese Werte zur Probe in (II): linke Seite
\( -2-2\cdot\!\left(-\tfrac{5}{2}\right) = -2+5 = 3 \), rechte Seite
\( 5-3\cdot\!\left(-\tfrac{7}{8}\right) = 5+\tfrac{21}{8} = \tfrac{61}{8} \). Wegen \( 3 \neq \tfrac{61}{8} \)
gibt es **keine** gemeinsame Lösung — **kein Schnittpunkt**.

Richtungen nicht parallel **und** kein Schnittpunkt → die Geraden sind **windschief**.

**Eine weitere Gerade, parallel zu \( g \), die \( h \) schneidet.** Man nimmt die **Richtung von
\( g \)** (damit ist die neue Gerade parallel zu \( g \)) und als Stützpunkt einen Punkt **auf
\( h \)** (damit schneidet sie \( h \) garantiert dort). Mit \( A(2\,|\,5\,|\,-2)\in h \):
\[ k:\ \vec{x} = \begin{pmatrix}2\\5\\-2\end{pmatrix} + r\cdot\begin{pmatrix}1\\-2\\2\end{pmatrix}. \]
\( k \) ist parallel zu \( g \) (gleiche Richtung) und schneidet \( h \) im Punkt \( A \). (\( A \) liegt
nicht auf \( g \), also ist \( k \) wirklich eine andere Gerade als \( g \).)

**Punkte auf \( g \) mit Abstand \( 6 \) von \( P(1\,|\,-2\,|\,3) \).** Der Punkt \( P \) ist genau der
**Stützpunkt** von \( g \). Ein allgemeiner Geradenpunkt ist \( X(t)=P+t\,\vec{u} \), und der
Verbindungspfeil ist
\[ \overrightarrow{PX} = X(t)-P = t\cdot\vec{u} = t\cdot\begin{pmatrix}1\\-2\\2\end{pmatrix}. \]
Seine Länge ist
\[ \big|\overrightarrow{PX}\big| = |t|\cdot|\vec{u}| = |t|\cdot\sqrt{1^2+(-2)^2+2^2} = |t|\cdot\sqrt{9} = 3\,|t|. \]
Bedingung \( 3|t|=6 \Rightarrow |t|=2 \Rightarrow t=\pm 2 \). Einsetzen:
\[ t=2:\ X = \begin{pmatrix}1\\-2\\3\end{pmatrix}+2\begin{pmatrix}1\\-2\\2\end{pmatrix} = (3\,|\,-6\,|\,7),\qquad
   t=-2:\ X = (-1\,|\,2\,|\,-1). \]
Die gesuchten Punkte sind \( (3\,|\,-6\,|\,7) \) und \( (-1\,|\,2\,|\,-1) \).

<details><summary>Haltung dahinter: Was heißt „windschief", und wie misst man Abstände? (ganz von vorn)</summary>

**Vier Lagen, die zwei Geraden im Raum haben können.** Anders als in der Ebene (wo sich zwei Geraden
entweder schneiden oder parallel sind) gibt es im Raum **vier** Fälle:

- **identisch** (dieselbe Linie),
- **parallel** (gleiche Richtung, treffen sich nie),
- **schneidend** (kreuzen sich in genau einem Punkt),
- und — nur im Raum möglich — **windschief**: verschiedene Richtungen **und** treffen sich nie. Bild:
  zwei Stromkabel in unterschiedlicher Höhe, die über Kreuz verlaufen, ohne sich zu berühren.

**Der Prüf-Fahrplan** ist genau die Reihenfolge oben: Erst die **Richtungen** vergleichen (parallel
oder nicht), dann (falls nicht parallel) auf **Schnittpunkt** prüfen, indem man die Geradengleichungen
gleichsetzt. Klappt es nicht, sind sie windschief.

<details><summary>Warum genügt die dritte Zeile, um den Widerspruch zu finden?</summary>

Beim Gleichsetzen entstehen drei Gleichungen, aber nur **zwei** Unbekannte (\( t \) und \( s \)). Zwei
Gleichungen reichen, um \( t \) und \( s \) auszurechnen. Die **dritte** Gleichung ist dann eine
**Probe**: Passt sie auch, schneiden sich die Geraden; passt sie nicht, gibt es keinen gemeinsamen
Punkt. Hier war Zeile (III) besonders bequem, weil \( h \) in der dritten Koordinate konstant
\( -2 \) ist (kein \( s \)) — daraus fiel \( t \) sofort heraus. Die übrig bleibende Probe in (II)
schlug fehl → windschief.

</details>

<details><summary>Länge eines Pfeils im Raum — und warum hier so bequem</summary>

Die **Länge** eines Vektors \( (a,b,c) \) ist der Abstand zwischen Start und Ziel und folgt aus dem
**Satz des Pythagoras** in drei Dimensionen: jede Zahl quadrieren, addieren, Wurzel ziehen,
\( \sqrt{a^2+b^2+c^2} \). Für \( \vec{u}=(1,-2,2) \): \( 1+4+4=9 \), also \( |\vec{u}|=\sqrt{9}=3 \) —
eine glatte Zahl.

Das macht den Abstand bequem: Weil \( P \) der **Stützpunkt** ist, ist der Verbindungspfeil zu einem
Geradenpunkt genau \( t\cdot\vec{u} \), und sein Betrag ist \( |t|\cdot 3 \). Aus \( 3|t|=6 \) folgt
sofort \( |t|=2 \). Das **\( |t| \)** (Betrag) sorgt dafür, dass es **zwei** Lösungen gibt — eine in
jede Richtung (\( t=+2 \) und \( t=-2 \)), denn beide liegen gleich weit von \( P \) entfernt.

</details>

<details><summary>Typische Falle: nur eine Richtung mitnehmen</summary>

Wer aus \( 3|t|=6 \) nur \( t=2 \) liest und das \( t=-2 \) vergisst, findet **nur den halben** Punkt.
Abstandsbedingungen führen über den Betrag fast immer auf **zwei** symmetrische Lösungen — beide
angeben.

</details>
</details>
</details>

### AB III — Ebene durch \( g \) parallel zu \( h \), orthogonale Schnittgerade

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Ebene \( E \), die \( g \) enthält und parallel zu \( h \) liegt.** Eine Ebene wird von **zwei
Richtungen** aufgespannt. \( E \) soll \( g \) enthalten → sie nimmt die Richtung von \( g \),
\( \vec{u}=(1,-2,2) \), und einen Punkt von \( g \), z. B. \( P(1\,|\,-2\,|\,3) \). \( E \) soll
parallel zu \( h \) sein → sie nimmt zusätzlich die Richtung von \( h \), \( \vec{v}=(4,-3,0) \).

Für die **Koordinatengleichung** braucht man einen **Normalenvektor** \( \vec{n} \), der auf beiden
Spannrichtungen senkrecht steht. Den liefert das **Kreuzprodukt**
\( \vec{n}=\vec{u}\times\vec{v} \):
\[ \vec{n} = \begin{pmatrix}1\\-2\\2\end{pmatrix}\times\begin{pmatrix}4\\-3\\0\end{pmatrix}
   = \begin{pmatrix}(-2)\cdot 0 - 2\cdot(-3)\\[2pt] 2\cdot 4 - 1\cdot 0\\[2pt] 1\cdot(-3) - (-2)\cdot 4\end{pmatrix}
   = \begin{pmatrix}6\\8\\5\end{pmatrix}. \]
Die rechte Seite bestimmt man durch Einsetzen des Ebenenpunkts \( P \):
\( 6\cdot 1 + 8\cdot(-2) + 5\cdot 3 = 6-16+15 = 5 \). Also
\[ E:\quad 6x_1 + 8x_2 + 5x_3 = 5. \]
**Proben:** Ein zweiter Punkt von \( g \), \( Q(3\,|\,-6\,|\,7) \): \( 18-48+35=5 \) ✓ (\( g \) liegt in
\( E \)). Und \( \vec{n}\cdot\vec{v} = 24-24+0 = 0 \) ✓ — \( h \) verläuft parallel zur Ebene. Setzt man
\( A(2\,|\,5\,|\,-2) \) ein: \( 12+40-10 = 42 \neq 5 \) — \( h \) liegt **nicht in** \( E \), ist also
echt **parallel** zu \( E \).

**Gerade durch einen gegebenen Punkt, die \( g \) orthogonal schneidet.** Das **Verfahren**
(Lotgerade / Lotfußpunkt):

1. Allgemeiner Geradenpunkt \( X(t) = P + t\,\vec{u} \) auf \( g \).
2. Verbindungspfeil vom gegebenen Punkt \( R \) zu \( X(t) \): \( \overrightarrow{RX} = X(t) - R \).
3. **Orthogonalität** verlangen: \( \overrightarrow{RX}\cdot\vec{u} = 0 \). Diese eine Gleichung nach
   \( t \) auflösen liefert den **Lotfußpunkt** \( F=X(t) \) — den Punkt auf \( g \), an dem der
   Verbindungspfeil senkrecht zu \( g \) steht.
4. Die gesuchte Gerade verläuft durch \( R \) und \( F \), Richtung \( \overrightarrow{RF} \).

Im Original sind für \( R \) **keine Koordinaten** angegeben; deshalb hier ein selbst gewähltes
Beispiel, um das Verfahren vollständig durchzurechnen — mit jedem anderen gegebenen Punkt läuft es
identisch ab. **Beispiel \( R(6\,|\,-4\,|\,3) \):**
\[ X(t)-R = \begin{pmatrix}1+t-6\\-2-2t+4\\3+2t-3\end{pmatrix} = \begin{pmatrix}t-5\\2-2t\\2t\end{pmatrix},\qquad
   (X(t)-R)\cdot\vec{u} = (t-5) + (2-2t)(-2) + (2t)(2). \]
Ausmultipliziert: \( (t-5) + (-4+4t) + 4t = 9t - 9 \). Gleich null: \( 9t-9=0 \Rightarrow t=1 \). Also
\[ F = X(1) = (2\,|\,-4\,|\,5),\qquad \overrightarrow{RF} = F-R = \begin{pmatrix}-4\\0\\2\end{pmatrix}\ \parallel\ \begin{pmatrix}-2\\0\\1\end{pmatrix}. \]
Die orthogonale Schnittgerade lautet
\[ m:\ \vec{x} = \begin{pmatrix}6\\-4\\3\end{pmatrix} + r\cdot\begin{pmatrix}-2\\0\\1\end{pmatrix}. \]
**Probe:** \( \overrightarrow{RF}\cdot\vec{u} = (-4)\cdot 1 + 0\cdot(-2) + 2\cdot 2 = 0 \) ✓ (steht
senkrecht auf \( g \)), und \( m \) trifft \( g \) im Punkt \( F(2\,|\,-4\,|\,5) \).

<details><summary>Haltung dahinter: Normalenvektor, Kreuzprodukt, „senkrecht schneiden"</summary>

**Ebene und Normalenvektor.** Eine **Ebene** ist eine vollkommen flache, unendlich ausgedehnte Fläche
(wie eine unendliche Tischplatte). Ein **Normalenvektor** ist ein Pfeil, der **senkrecht** auf dieser
Fläche steht — wie ein Fahnenmast, der gerade aus dem Boden ragt. Sein Nutzen: Seine drei Zahlen sind
**genau** die Koeffizienten \( n_1,n_2,n_3 \) in der Koordinatengleichung
\( n_1x_1+n_2x_2+n_3x_3=d \). Kennt man \( \vec{n} \) und einen Punkt der Ebene, hat man die ganze
Gleichung (die rechte Seite \( d \) kommt aus dem Einsetzen des Punktes).

**Warum das Kreuzprodukt?** Das **Kreuzprodukt** zweier Vektoren ist eine feste Rechenvorschrift, deren
Ergebnis ein **neuer Pfeil** ist, der auf **beiden** Ausgangspfeilen senkrecht steht. Wir füttern es mit
den zwei Spannrichtungen der Ebene (\( \vec{u} \) und \( \vec{v} \)) und bekommen automatisch den
Normalenvektor. Das Rechenschema steht im
[Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html#kreuzprodukt).

**Was „parallel zu \( h \)" für die Ebene heißt.** Die Richtung von \( h \) muss **in** der Ebene
„liegen können", also senkrecht zum Normalenvektor stehen: \( \vec{n}\cdot\vec{v}=0 \). Das haben wir
geprüft (\( 24-24+0=0 \)). Damit \( h \) wirklich **neben** der Ebene liegt und nicht **in** ihr, prüft
man einen Punkt von \( h \): \( A \) erfüllt die Gleichung nicht (\( 42\neq 5 \)), also ist \( h \) echt
parallel.

**„Orthogonal schneiden".** Zwei Geraden schneiden sich **orthogonal**, wenn sie sich in einem Punkt
treffen **und** ihre Richtungen einen rechten Winkel bilden. „Rechter Winkel zwischen Pfeilen" prüft man
mit dem **Skalarprodukt**: ist es \( 0 \), stehen die Pfeile senkrecht aufeinander. Genau das verlangt
Schritt 3: \( \overrightarrow{RX}\cdot\vec{u}=0 \) sucht den einen Geradenpunkt \( F \), für den der
Verbindungspfeil senkrecht zu \( g \) zeigt — den **Lotfußpunkt** (den „kürzesten Draht" von \( R \) zur
Geraden).

<details><summary>… ganz langsam (mit Zahlen): das Skalarprodukt im Beispiel</summary>

Das **Skalarprodukt** zweier Pfeile rechnet man, indem man die Koordinaten paarweise multipliziert und
addiert: \( (a_1,a_2,a_3)\cdot(b_1,b_2,b_3) = a_1b_1+a_2b_2+a_3b_3 \). Hier mit
\( \overrightarrow{RX}=(t-5,\,2-2t,\,2t) \) und \( \vec{u}=(1,-2,2) \):

- \( (t-5)\cdot 1 = t-5 \).
- \( (2-2t)\cdot(-2) = -4 + 4t \) (Vorsicht: \( -2t\cdot(-2) = +4t \), Minus mal Minus ist Plus).
- \( (2t)\cdot 2 = 4t \).

Summe: \( (t-5) + (-4+4t) + 4t = t + 4t + 4t - 5 - 4 = 9t - 9 \). Das soll \( 0 \) sein, also
\( 9t=9 \), \( t=1 \). Der Lotfußpunkt liegt damit beim Parameter \( t=1 \), das ist \( F(2|-4|5) \).

</details>

<details><summary>Hinweis: ohne konkreten Punkt \( R \) bleibt es beim Verfahren</summary>

Das Aufgabenbeispiel nennt nur „einen gegebenen Punkt", **ohne** Zahlen. Die volle Antwort ist deshalb
das **Verfahren** (Schritte 1–4). Sobald ein Punkt \( R(r_1|r_2|r_3) \) konkret vorliegt, setzt man ihn
in \( \overrightarrow{RX}\cdot\vec{u}=0 \) ein, löst nach \( t \) auf, erhält den Fußpunkt \( F \) und
schreibt die Gerade durch \( R \) mit Richtung \( \overrightarrow{RF} \) — genau wie im Beispiel mit
\( R(6|-4|3) \) vorgeführt.

</details>
</details>
</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Teilaufgabe, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen
kannst. Du musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Analysis) aufklappen</summary>

- **a) Graph aus \( \sin(x) \).** Erwartet werden **drei** Veränderungen: **Streckung um 2** (Höhe),
  **Verschiebung um \( \tfrac{\pi}{2} \) nach rechts** (waagerecht), **Verschiebung um 3 nach oben**.
  *Rückfrage:* „In welche Richtung verschiebt das \( -\tfrac{\pi}{2} \) im Inneren — links oder
  rechts?" (Richtig: **rechts**.) *Rote Flagge:* nur „nach links verschoben".
- **b) Welcher Graph ist \( f' \) / Integral null.** Erwartet: **Abbildung 2**, begründet über die
  **positive Steigung** von \( f \) bei \( x=\tfrac{\pi}{2} \) (also \( f'>0 \) dort). Beim Integral:
  **Punktsymmetrie** des \( f' \)-Graphen → gleich große Flächen ober- und unterhalb der Achse heben
  sich auf. *Rückfrage:* „Woran erkennen Sie, dass an dieser Stelle \( f' \) positiv sein muss?"
  *Rote Flagge:* \( f' \) mit \( f \) verwechselt.
- **c) Integral \( \int_0^\pi(5-f) \).** Erwartet: Ergebnis **\( 2\pi \)** und die Deutung als **Fläche
  zwischen der Geraden \( y=5 \) und dem Graphen von \( f \)** über \( [0;\pi] \). *Rückfrage:* „Warum
  ist das Ergebnis hier wirklich eine Fläche und keine Differenz mit Vorzeichen?" (Antwort: weil \( f \)
  dort durchgehend unter \( 5 \) liegt.)
- **d) Wahr/falsch.** Erwartet: **falsch**, weil Hoch- und Tiefpunkt die **Periode** nicht festlegen
  (beliebig viele weitere Extrempunkte dazwischen möglich). *Rückfrage:* „Was an der Funktion bleibt
  durch die zwei Punkte unbestimmt?" (Antwort: **die Periode**.) *Rote Flagge:* „wahr" mit Verweis auf
  „zwei Punkte legen immer alles fest" (das gilt nur für Geraden).

</details>

<details><summary>Leitfaden Teil 2 (Geometrie) aufklappen</summary>

- **AB I — \( h \), Deutung von \( g \), Punktprobe, weitere Gleichungen.** Erwartet:
  \( h:\ \vec{x}=(2|5|-2)+s\,(4|-3|0) \); Deutung **Stützpunkt = fester Ort, Richtungsvektor = Schritt,
  \( t \) = Drehregler**; Punktprobe **alle drei Zeilen mit demselben \( t \)**; weitere Gleichung mit
  anderem Stützpunkt/Vielfachem der Richtung. *Rückfrage:* „Warum gibt es mehrere richtige Gleichungen
  für dieselbe Gerade?"
- **AB II — Lage, parallele Schnittgerade, Abstand 6.** Erwartet: **windschief** (Richtungen nicht
  parallel **und** kein Schnittpunkt — Widerspruch in der Probe-Zeile); Schnittgerade **= Richtung von
  \( g \) + Stützpunkt auf \( h \)**; Abstandspunkte **\( (3|-6|7) \)** und **\( (-1|2|-1) \)** über
  \( 3|t|=6 \). *Rückfrage:* „Warum gibt es **zwei** Punkte mit Abstand 6?" (Antwort: zwei Richtungen
  entlang \( g \).) *Rote Flagge:* nur einen der beiden Punkte nennen.
- **AB III — Ebene, orthogonale Gerade.** Erwartet: \( E:\ 6x_1+8x_2+5x_3=5 \) über **Kreuzprodukt
  \( \vec{u}\times\vec{v} \)** + Punktprobe, plus Kontrolle \( \vec{n}\cdot\vec{v}=0 \); bei der
  orthogonalen Geraden das **Lotfußpunkt-Verfahren** (\( \overrightarrow{RX}\cdot\vec{u}=0 \)).
  *Hinweis für dich:* Für die orthogonale Gerade gibt das Original **keinen** Punkt vor — ein sauber
  **beschriebenes Verfahren** (gern mit Beispielpunkt) ist die volle Antwort. *Rückfrage:* „Womit prüfen
  Sie, dass zwei Geraden senkrecht aufeinander stehen?" (Antwort: **Skalarprodukt = 0**.)

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Welche drei Veränderungen führen von \( \sin(x) \) zu \( f(x)=2\sin\!\left(x-\tfrac{\pi}{2}\right)+3 \),
  und in welche Richtung verschiebt das \( -\tfrac{\pi}{2} \)?
- Woran entscheidest du, welcher Graph \( f' \) ist — und warum ist \( \int_{-\pi}^{\pi} f'\,dx = 0 \),
  ohne zu rechnen?
- Was misst \( \int_0^\pi (5-f(x))\,dx \) geometrisch, und warum ist das hier eine echte Fläche?
- Warum bestimmen ein Hochpunkt und ein Tiefpunkt eine trigonometrische Funktion **nicht** eindeutig?
- Wie prüfst du, ob zwei Geraden im Raum windschief sind — und wie findest du die Punkte auf \( g \) mit
  Abstand 6 von \( P \)?
- Wie kommst du auf die Ebene durch \( g \), die parallel zu \( h \) ist, und womit erkennst du, dass
  zwei Geraden sich orthogonal schneiden?
