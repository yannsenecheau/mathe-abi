# Aufgabe 2 — Analysis & Geometrie

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Analysis**, **Teil 2 (Gespräch) aus der Geometrie**. Alles ist
**rechnerfrei** zu lösen. Arbeitet die Aufgabe wie eine echte Simulation durch — eine Person trägt
vor, die andere prüft mit dem Lösungsweg und dem [Prüfer-Leitfaden](#prüfer-leitfaden-für-die-abfragende-person)
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

> **Werkzeug zum Nachschlagen:** Die wiederkehrenden Analysis-Werkzeuge (Ableiten, Stammfunktion,
> Integral, Randverhalten) stehen in den Kapiteln [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Integral-Grundlagen](kap-integral-grundlagen.html),
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html),
> [Grundfunktionen](kap-grundfunktionen.html) und
> [Grenzwerte & Randverhalten](kap-grenzwerte-randverhalten.html). Die Vektor- und Ebenen-Werkzeuge
> (Punkte, Vektoren, Länge, Skalarprodukt, Kreuzprodukt, Ebenengleichung, Hesse-Normalform) findest du
> kompakt im [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html).

---

## Teil 1 — Vortrag (Analysis): Geschwindigkeit von Auto und Motorrad

<div class="aufgabenkasten">

**Die Geschwindigkeit eines Autos auf einer Teststrecke wird beschrieben durch eine Funktion \( f \)
mit \( f(x) = 24 + 24\cdot e^{-0{,}08x} \), \( 0 \le x \le 60 \) (\( x \) in Sekunden, \( f(x) \) in
Meter pro Sekunde).**

**a)** Berechne \( f(0) \) und \( f'(0) \) und \( \displaystyle\int_0^{60} f(x)\,dx \). Deute diese
Werte im Sachzusammenhang.

*Das Auto und ein Motorrad befinden sich zum Zeitpunkt \( x=0 \) nebeneinander und fahren in den
nächsten 60 Sekunden in die gleiche Richtung. Abbildung 1 zeigt den Graphen der Funktion \( f \) und
den Graphen der Funktion \( g \), die die Geschwindigkeit des Motorrads beschreibt.*

**b)** Beschreibe die Bewegungen des Autos und des Motorrads.

**c)** Abbildung 2 stellt für einen Ausschnitt der Fahrt den **Abstand** der beiden Fahrzeuge dar.
Beschreibe, wie man die \( x \)-Koordinate des Punktes \( H \) mithilfe von Abbildung 1 ermitteln
kann. Entscheide, ob die \( y \)-Koordinate von \( H \) größer als 500 ist, und begründe deine
Entscheidung.

**d)** Das Motorrad überholt das Auto zum Zeitpunkt \( x_0 \). Bestimme eine Gleichung, mit der man
bei gegebenem Funktionsterm von \( g \) den Zeitpunkt \( x_0 \) berechnen kann.

</div>

Hier sind die beiden Graphen aus Abbildung 1 (Geschwindigkeiten) und Abbildung 2 (Abstand). Spiele mit
den Bildern, bevor du die Lösungen aufklappst.

<div class="graph-row">
<figure>
<div class="jxgbox" id="jxg-k2-abb1" style="width:100%;max-width:360px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 1 — Geschwindigkeit von Auto (\( f \), durchgezogen) und Motorrad (\( g \), gestrichelt) in m/s über der Zeit \( x \) in s.</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k2-abb2" style="width:100%;max-width:360px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 2 — Abstand der beiden Fahrzeuge in m über der Zeit; der höchste Punkt heißt \( H \).</figcaption>
</figure>
</div>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k2-abb1',{boundingbox:[-6,66,66,-6],axis:true,showCopyright:false,showNavigation:false});
b.create('functiongraph',[function(x){return 24+24*Math.exp(-0.08*x);},0,60],{strokeColor:'#3a5a9c',strokeWidth:2.5});
b.create('functiongraph',[function(x){return 40*(1-Math.exp(-0.15*x));},0,60],{strokeColor:'#d98324',strokeWidth:2.5,dash:2});
b.create('line',[[11.9,0],[11.9,33.3]],{straightFirst:false,straightLast:false,dash:2,strokeColor:'#3a8a5a',strokeWidth:1});
b.create('point',[11.9,33.3],{name:'',size:2,fillColor:'#3a8a5a',strokeColor:'#3a8a5a'});
b.create('text',[30,46,'Graph von g'],{fontSize:12,color:'#d98324'});
b.create('text',[32,21,'Graph von f'],{fontSize:12,color:'#3a5a9c'});
b.create('text',[13,6,'x_s ≈ 12'],{fontSize:11,color:'#3a8a5a'});
})();</script>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k2-abb2',{boundingbox:[-3,260,37,-20],axis:true,showCopyright:false,showNavigation:false});
b.create('functiongraph',[function(x){return -16*x-300*Math.exp(-0.08*x)-(800/3)*Math.exp(-0.15*x)+1700/3;},0,34],{strokeColor:'#3a5a9c',strokeWidth:2.5});
b.create('point',[11.9,215.7],{name:'H',size:2,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[6,10]}});
b.create('text',[15,235,'max. Abstand'],{fontSize:11,color:'#d98324'});
})();</script>

> **Hinweis zu den Bildern.** Der Term von \( g \) ist in der Aufgabe **nicht** gegeben. Die
> gestrichelte Kurve ist nur schematisch so gezeichnet, dass sie zu Abbildung 1 im Original passt
> (Start bei \( 0 \), nähert sich \( 40 \), kreuzt \( f \) bei \( x \approx 12 \)). Für die Lösung
> brauchst du den Term von \( g \) nirgends — du liest aus dem Bild nur **ab**.

### Teilaufgabe a) — \( f(0) \), \( f'(0) \) und das Integral berechnen und deuten

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**\( f(0) \) berechnen.** Einsetzen von \( x=0 \). Wegen \( e^{0}=1 \):

\[ f(0) = 24 + 24\cdot e^{-0{,}08\cdot 0} = 24 + 24\cdot 1 = 48. \]

**Deutung:** Zu Beobachtungsbeginn (\( x=0 \)) fährt das Auto **48 Meter pro Sekunde**.

**\( f'(0) \) berechnen.** Zuerst die Ableitung. Der konstante Summand \( 24 \) hat Ableitung \( 0 \);
der Summand \( 24\,e^{-0{,}08x} \) wird mit der Kettenregel abgeleitet (innere Ableitung \( -0{,}08 \)):

\[ f'(x) = 24\cdot(-0{,}08)\cdot e^{-0{,}08x} = -1{,}92\,e^{-0{,}08x}, \qquad f'(0) = -1{,}92\cdot 1 = -1{,}92. \]

**Deutung:** Die Ableitung der Geschwindigkeit ist die **Beschleunigung**. Zu Beobachtungsbeginn hat
das Auto die Beschleunigung \( -1{,}92\ \tfrac{\text{m}}{\text{s}^2} \). Das Minus heißt: Das Auto wird
**langsamer** (es bremst ab).

**Das Integral berechnen.** Eine **Stammfunktion** von \( f \):

\[ \int \big(24 + 24\,e^{-0{,}08x}\big)\,dx = 24x + \frac{24}{-0{,}08}\,e^{-0{,}08x} = 24x - 300\,e^{-0{,}08x}. \]

Mit dem Hauptsatz von \( 0 \) bis \( 60 \):

\[ \int_0^{60} f(x)\,dx = \Big[\,24x - 300\,e^{-0{,}08x}\,\Big]_0^{60}
= \big(24\cdot 60 - 300\,e^{-4{,}8}\big) - \big(0 - 300\,e^{0}\big). \]

\( e^{-4{,}8} \) ist winzig (\( \approx 0{,}008 \)), also \( 300\,e^{-4{,}8}\approx 2{,}5 \). Damit:

\[ \int_0^{60} f(x)\,dx = 1440 - 2{,}5 + 300 = 1737{,}5 \approx 1737{,}53. \]

**Deutung:** Das Integral der Geschwindigkeit über die Zeit ist die **zurückgelegte Strecke**. Das
Auto legt in den ersten 60 Sekunden ca. **1737,53 m**, also rund **1,7 km** zurück.

<details><summary>Haltung dahinter: Was bedeuten „einsetzen", „Beschleunigung" und „Integral = Strecke"? (ganz von vorn)</summary>

Drei Dinge der Reihe nach, ohne Vorwissen.

**Was heißt „\( f(0) \) berechnen"?** Die Funktion \( f \) ist eine Maschine: Man gibt eine Zeit
\( x \) (in Sekunden) hinein und bekommt die Geschwindigkeit (in Meter pro Sekunde) heraus.
„\( f(0) \)" heißt: Setze die Zeit \( 0 \) ein — also „ganz am Anfang". Wichtig ist nur die Regel
\( e^{0}=1 \): **Alles hoch null ergibt eins.** Deshalb wird aus \( 24\,e^{-0{,}08\cdot 0} \) einfach
\( 24\cdot 1 = 24 \), und zusammen mit dem festen \( 24 \) kommt \( 48 \) heraus.

**Was ist Geschwindigkeit, was ist Beschleunigung?** Die **Geschwindigkeit** sagt, *wie schnell* man
gerade fährt (z. B. 48 Meter in jeder Sekunde). Die **Beschleunigung** sagt, *wie schnell sich die
Geschwindigkeit ändert* — ob man schneller oder langsamer wird. Beim Auto auf dem Tacho: Geschwindigkeit
ist die angezeigte Zahl, Beschleunigung ist, wie der Zeiger gerade wandert. Mathematisch ist
Beschleunigung die **Ableitung** der Geschwindigkeit (die Ableitung misst immer die Änderungsrate). Ein
**negativer** Wert (\( -1{,}92 \)) bedeutet: Der Tacho-Zeiger geht zurück, das Auto bremst.

**Warum ist das Integral die Strecke?** Stell dir vor, du fährst genau eine Sekunde lang konstant 48
m/s — dann legst du 48 m zurück (Geschwindigkeit \( \times \) Zeit \( = \) Strecke). Über die ganze
Fahrt ändert sich die Geschwindigkeit ständig. Das **Integral** zerlegt die Fahrt in unendlich viele
winzige Zeitstücke, multipliziert in jedem Stück „Geschwindigkeit \( \times \) Zeitdauer" und addiert
alles auf. Heraus kommt die **gesamte gefahrene Strecke**. Bildlich ist das die **Fläche unter dem
Geschwindigkeits-Graphen**.

<details><summary>Das Integral ganz langsam (mit Zahlen)</summary>

Die Stammfunktion ist \( 24x - 300\,e^{-0{,}08x} \). „Hauptsatz" heißt: oberen Wert einsetzen, unteren
Wert einsetzen, subtrahieren.

- **Oben (\( x=60 \)):** \( 24\cdot 60 = 1440 \). Und \( -0{,}08\cdot 60 = -4{,}8 \), also
  \( -300\,e^{-4{,}8} \). Die Zahl \( e^{-4{,}8} \) ist sehr klein, etwa \( 0{,}0082 \); mal \( 300 \)
  sind das etwa \( 2{,}5 \). Oberer Wert: \( 1440 - 2{,}5 = 1437{,}5 \).
- **Unten (\( x=0 \)):** \( 24\cdot 0 = 0 \), und \( -300\,e^{0} = -300\cdot 1 = -300 \). Unterer Wert:
  \( 0 - 300 = -300 \).
- **Subtrahieren:** \( 1437{,}5 - (-300) \). Minus mal minus wird plus, also \( 1437{,}5 + 300 = 1737{,}5 \).

Das passt zum offiziellen Wert \( 1737{,}53 \) (mit dem genauen \( e^{-4{,}8} \)). Rund 1,7 km.

</details>

<details><summary>Woher kommt die \( 300 \) in der Stammfunktion?</summary>

Beim „Aufleiten" (Stammfunktion bilden) von \( e^{-0{,}08x} \) muss man durch die innere Zahl
\( -0{,}08 \) **teilen** — das ist die Umkehrung der Kettenregel. Es gilt
\( \tfrac{24}{-0{,}08} = -300 \), denn \( \tfrac{1}{0{,}08} = 12{,}5 \) und \( 24\cdot 12{,}5 = 300 \).
Probe durch Ableiten: \( \tfrac{d}{dx}\big(-300\,e^{-0{,}08x}\big) = -300\cdot(-0{,}08)\,e^{-0{,}08x}
= 24\,e^{-0{,}08x} \) — zurück beim Start, also stimmt die Stammfunktion.

</details>
</details>
</details>

### Teilaufgabe b) — Bewegungen beschreiben

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Das Auto (\( f \)).** Die Geschwindigkeit **nimmt stets ab**, wobei die Abnahme **immer geringer**
wird. Sie startet bei 48 m/s und nähert sich von oben dem Wert 24 m/s, ohne ihn zu unterschreiten.

**Das Motorrad (\( g \)).** Zu Beobachtungsbeginn hat das Motorrad die Geschwindigkeit **0 m/s**. Seine
Geschwindigkeit **nimmt stets zu**, wobei die Zunahme **immer geringer** wird; sie nähert sich von
unten dem Wert 40 m/s.

<details><summary>Haltung dahinter: Wie liest man eine „Bewegung" aus einem Graphen ab?</summary>

Der Graph zeigt auf der senkrechten Achse die **Geschwindigkeit** und auf der waagerechten Achse die
**Zeit**. Man beschreibt eine Bewegung in zwei Schritten:

1. **Geht der Graph rauf oder runter?** Beim Auto fällt die Linie von links nach rechts → das Auto wird
   langsamer (passt zur negativen Beschleunigung aus a). Beim Motorrad steigt die Linie → es wird
   schneller.
2. **Wird die Veränderung stärker oder schwächer?** Beide Linien werden nach rechts immer **flacher**.
   Flach bedeutet: Es ändert sich kaum noch etwas. Also wird beim Auto die Abnahme immer kleiner und
   beim Motorrad die Zunahme immer kleiner — beide laufen auf einen festen Endwert zu (24 bzw. 40).

**Alltagsbild:** Das Auto rollt aus (es bremst, aber immer sanfter und pendelt sich bei einer Rest-
geschwindigkeit ein). Das Motorrad fährt aus dem Stand an, beschleunigt zuerst kräftig und dann immer
gemächlicher, bis es fast eine feste Reisegeschwindigkeit hält.

<details><summary>Typische Falle: Geschwindigkeit mit Strecke verwechseln</summary>

„Die Geschwindigkeit des Autos nimmt ab" heißt **nicht**, dass das Auto rückwärts fährt oder die
Strecke kürzer wird. Solange die Geschwindigkeit **positiv** ist (hier immer mindestens 24 m/s), fährt
das Auto weiter vorwärts — nur eben langsamer. Auf dem Graphen steht die *Geschwindigkeit*, nicht der
*Ort*.

</details>
</details>
</details>

### Teilaufgabe c) — \( x \)-Koordinate von \( H \) bestimmen und \( y_H > 500 \) entscheiden

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**\( x \)-Koordinate von \( H \).** \( H \) ist der **höchste Punkt** der Abstandskurve (der größte
Abstand zwischen den Fahrzeugen). Der Abstand wächst, solange das **Auto schneller** ist als das
Motorrad (\( f > g \)); sobald das **Motorrad schneller** wird (\( g > f \)), schrumpft der Abstand
wieder. Der größte Abstand liegt also genau dort, wo beide **gleich schnell** sind:

> Die \( x \)-Koordinate von \( H \) ist die **Schnittstelle der beiden Graphen** \( f \) und \( g \)
> in Abbildung 1. Man liest sie als \( x_s \approx 12\ \text{s} \) ab.

**Ist die \( y \)-Koordinate von \( H \) größer als 500?** Die \( y \)-Koordinate von \( H \) ist der
**größte Abstand** (in Metern). Er entspricht der **Fläche zwischen den beiden Geschwindigkeits-
Graphen** von \( x=0 \) bis zur Schnittstelle \( x_s \), also \( \int_0^{x_s}\big(f(x)-g(x)\big)\,dx \).

Diese Fläche ist **kleiner als 500**, und das sieht man ohne genaue Rechnung:

- Der Geschwindigkeits-Unterschied \( f-g \) ist **am Anfang am größten**: \( f(0)-g(0)=48-0=48 \).
- Danach **schrumpft** der Unterschied stetig bis auf \( 0 \) an der Schnittstelle.
- Die Fläche liegt deshalb innerhalb eines Dreiecks mit Breite \( x_s\approx 12 \) und Höhe \( 48 \):
  \[ y_H = \int_0^{x_s}(f-g)\,dx \;<\; \tfrac12\cdot x_s\cdot 48 \approx \tfrac12\cdot 12\cdot 48 = 288 < 500. \]

Also ist \( y_H < 500 \). (Der tatsächliche Höchstabstand liegt bei etwa **215 m**.)

<details><summary>Haltung dahinter: Warum ist der Abstand die Fläche zwischen den Geschwindigkeits-Kurven?</summary>

**Strecke = Fläche unter der Geschwindigkeit** (das kennst du aus Teilaufgabe a). Der Weg des Autos
nach \( x \) Sekunden ist die Fläche unter \( f \), der Weg des Motorrads die Fläche unter \( g \).
Beide starten am selben Ort. Der **Abstand** zwischen ihnen ist die **Differenz der zurückgelegten
Wege** — und das ist die Fläche unter \( f \) minus die Fläche unter \( g \), also die **Fläche
zwischen den beiden Kurven**.

Solange \( f \) über \( g \) liegt (Auto schneller), wächst diese Fläche mit jeder Sekunde → der
Abstand wird größer. Genau an der Schnittstelle hört das Wachsen auf (beide gleich schnell, kein
zusätzlicher Vorsprung) — dort ist der Abstand maximal, das ist \( H \). Danach liegt \( g \) über
\( f \) (Motorrad schneller); jetzt holt das Motorrad auf, die Fläche/der Abstand schrumpft.

**Warum die „\( <500 \)"-Abschätzung wasserdicht ist (kurz):** Der Unterschied \( f-g \) startet bei
48 und fällt **nach unten gebogen** (konvex) auf 0. Eine nach unten gebogene Kurve liegt **unter** der
geraden Verbindungslinie von \( (0\mid 48) \) zu \( (x_s\mid 0) \). Die Fläche unter dieser Geraden ist
ein Dreieck mit Inhalt \( \tfrac12\cdot 48\cdot x_s \). Selbst mit einem großzügigen \( x_s\approx 20 \)
wären das nur \( \tfrac12\cdot 48\cdot 20 = 480 < 500 \). Der echte Wert ist noch deutlich kleiner.

<details><summary>Ganz langsam: die Dreiecks-Schranke in Zahlen</summary>

Stell dir den größtmöglichen Vorsprung vor: Das Auto wäre die ganze Zeit bis \( x_s \) um die volle
Anfangsdifferenz \( 48\ \tfrac{\text{m}}{\text{s}} \) schneller. Dann wäre der Vorsprung
\( 48\cdot x_s = 48\cdot 12 = 576\ \text{m} \) — das ist die **Rechteck-Obergrenze** (zu großzügig). In
Wahrheit ist die Differenz nur am Start 48 und sinkt sofort. Im Mittel ist sie höchstens halb so groß,
also \( \approx 24 \); mal \( 12 \) Sekunden ergibt \( \approx 288\ \text{m} \) — die **Dreiecks-
Schranke**. Beide Schranken zeigen: weit unter dem nötigen Vergleichswert ist der Abstand spätestens
mit der Dreiecks-Schranke (288) unter 500.

</details>

<details><summary>Typische Falle: \( H \) mit dem Überholpunkt verwechseln</summary>

\( H \) ist der Punkt des **größten Abstands** (beide gleich schnell, \( f=g \)) — das ist **nicht** der
Moment, in dem das Motorrad das Auto überholt. Beim Überholen ist der Abstand wieder **0** (siehe
Teilaufgabe d). \( H \) liegt früher, ungefähr bei der halben Zeit bis zum Überholen.

</details>
</details>
</details>

### Teilaufgabe d) — Gleichung für den Überholzeitpunkt \( x_0 \)

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Beim **Überholen** hat das Motorrad das Auto eingeholt: Zum Zeitpunkt \( x_0 \) haben **beide Fahrzeuge
genau dieselbe Strecke** zurückgelegt (sie sind wieder nebeneinander, jetzt aber zieht das Motorrad
vorbei). Strecke ist das Integral der Geschwindigkeit, also ist \( x_0 \) Lösung der Gleichung

\[ \int_0^{x_0} f(x)\,dx \;=\; \int_0^{x_0} g(x)\,dx. \]

<details><summary>Haltung dahinter: Was heißt „überholen" mathematisch?</summary>

Beide starten zum Zeitpunkt \( 0 \) **nebeneinander** am selben Ort. Wer vorne liegt, hat die größere
zurückgelegte Strecke. Anfangs ist das Auto schneller und zieht davon (positiver Abstand, vgl. \( H \)).
Dann holt das Motorrad auf. **Überholen** ist der Augenblick, in dem das Motorrad den Vorsprung des
Autos vollständig aufgezehrt hat — beide haben **dieselbe Strecke** zurückgelegt. Genau dann ist der
Abstand wieder null.

Die zurückgelegte Strecke ist jeweils die Fläche unter der Geschwindigkeit, also das Integral von
\( 0 \) bis zur betrachteten Zeit. „Gleiche Strecke" wird damit zu „gleiche Integrale":
\( \int_0^{x_0} f = \int_0^{x_0} g \). Das ist die gesuchte Gleichung. Mit dem Term von \( g \) (der hier
gegeben wäre) könnte man beide Integrale ausrechnen und nach \( x_0 \) auflösen — aus dem Bild läge
\( x_0 \) bei etwa 34 s.

<details><summary>Gleichwertige Schreibweise mit dem Abstand</summary>

Man kann dieselbe Bedingung auch über den Abstand aus Teilaufgabe c) formulieren: „Abstand wieder
null" heißt \( \int_0^{x_0}\big(f(x)-g(x)\big)\,dx = 0 \). Das ist nur die nach einer Seite sortierte
Form derselben Gleichung — die Strecken-Gleichheit \( \int_0^{x_0} f = \int_0^{x_0} g \) ist die
übliche Antwort.

</details>

<details><summary>Typische Falle: \( f(x_0)=g(x_0) \) statt der Integrale</summary>

\( f(x_0)=g(x_0) \) (gleiche **Geschwindigkeit**) beschreibt den Punkt \( H \) aus Teilaufgabe c), also
den größten Abstand — **nicht** das Überholen. Überholen heißt gleiche **Strecke**, und Strecke ist das
**Integral**. Die richtige Gleichung enthält deshalb Integrale, keine bloßen Funktionswerte.

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- a) \( f(0)=48 \) (Anfangsgeschwindigkeit 48 m/s); \( f'(x)=-1{,}92\,e^{-0{,}08x} \), \( f'(0)=-1{,}92 \)
  (Anfangsbeschleunigung \( -1{,}92\ \tfrac{\text{m}}{\text{s}^2} \), Auto bremst);
  \( \int_0^{60} f\,dx = \big[24x-300e^{-0{,}08x}\big]_0^{60} \approx 1737{,}53 \) (≈ 1,7 km Strecke).
- b) Auto: Geschwindigkeit nimmt stets ab, Abnahme immer geringer (48 → 24). Motorrad: startet bei 0,
  nimmt stets zu, Zunahme immer geringer (0 → 40).
- c) \( x_H = \) Schnittstelle von \( f \) und \( g \) (\( \approx 12 \) s); \( y_H = \int_0^{x_s}(f-g)\,dx
  < \tfrac12\cdot 12\cdot 48 = 288 < 500 \), also **nein**, \( y_H \) ist nicht größer als 500 (≈ 215 m).
- d) \( x_0 \) löst \( \displaystyle\int_0^{x_0} f(x)\,dx = \int_0^{x_0} g(x)\,dx \) (gleiche Strecke).

</details>

---

## Teil 2 — Gespräch (Geometrie): zwei Ebenen \( E \) und \( F \)

<div class="aufgabenkasten">

**Input.** Gegeben sind zwei Ebenen:

\[ E:\ 2x_1 - x_2 + 3x_3 = 6, \qquad F:\ 2x_1 - x_2 = 6. \]

Im Gespräch denkbare Aspekte:
**(AB I)** Lage von \( E \) mit Hilfe von **Spurpunkten** veranschaulichen; **Punktprobe** und Ablesen
des **Normalenvektors**; **besondere Lage von \( F \)** angeben.
**(AB II)** Beziehung zwischen der **Anzahl der Spurpunkte** und der besonderen Lage einer Ebene;
**vektorielle (Parameter-)Darstellung** von \( E \) und geometrische Bedeutung ihrer Bestandteile;
**Abstand** verschiedener Objekte zu \( E \); Gleichung einer zu \( E \) **orthogonalen bzw. parallelen
Ebene**; **Spiegeln einer Geraden** an \( E \).
**(AB III)** besondere **Ausschnitte** von \( E \) in Parameterform (z. B. Parameter aus \( [0;1] \));
**gemeinsame Punkte** der Ebenen \( E \) und \( F \).

</div>

> **Vorab, in einem Satz, was eine „Ebene" ist:** Eine **Ebene** ist eine vollkommen flache, unendlich
> ausgedehnte Fläche im Raum — wie eine unendlich große Tischplatte, die irgendwie schräg im Raum
> hängt. Eine **Koordinatengleichung** wie \( 2x_1 - x_2 + 3x_3 = 6 \) ist eine Regel, die **genau die
> Punkte \( (x_1\mid x_2\mid x_3) \) beschreibt, die auf dieser Tischplatte liegen**: Setzt man einen
> Punkt der Ebene ein, stimmt die Gleichung; setzt man einen Punkt daneben ein, stimmt sie nicht. Alle
> Werkzeuge dazu im [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html).

So liegt die Ebene \( E \) im Koordinatensystem — gezeichnet über ihre drei **Spurpunkte** (die Stellen,
an denen sie die Achsen durchstößt):

<figure>
<svg viewBox="0 0 480 360" role="img" aria-label="Ebene E als Spurdreieck durch die Spurpunkte auf den drei Koordinatenachsen, mit Normalenvektor" style="width:100%;max-width:480px;height:auto;background:#fbf7ef;border-radius:8px">
  <defs>
    <marker id="ahE" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#7a7163"/></marker>
    <marker id="ahN" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#d98324"/></marker>
  </defs>
  <!-- Achsen -->
  <line x1="250" y1="230" x2="250" y2="150" stroke="#7a7163" stroke-width="1.5" marker-end="url(#ahE)"/>
  <line x1="60"  y1="230" x2="348" y2="230" stroke="#7a7163" stroke-width="1.5" marker-end="url(#ahE)"/>
  <line x1="250" y1="230" x2="146" y2="298" stroke="#7a7163" stroke-width="1.5" marker-end="url(#ahE)"/>
  <text x="234" y="148" font-size="13" fill="#7a7163">x₃</text>
  <text x="352" y="234" font-size="13" fill="#7a7163">x₂</text>
  <text x="128" y="308" font-size="13" fill="#7a7163">x₁</text>
  <text x="256" y="246" font-size="12" fill="#7a7163">O</text>
  <!-- Spurdreieck -->
  <polygon points="190,269 94,230 250,178" fill="#3a5a9c" fill-opacity="0.10" stroke="#3a5a9c" stroke-width="1.7"/>
  <!-- Normalenvektor aus dem Schwerpunkt -->
  <line x1="178" y1="226" x2="142" y2="197" stroke="#d98324" stroke-width="1.8" marker-end="url(#ahN)"/>
  <text x="150" y="190" font-size="12" fill="#d98324" font-weight="bold">n⃗</text>
  <!-- Spurpunkte -->
  <circle cx="250" cy="178" r="3.5" fill="#3a5a9c"/><text x="258" y="174" font-size="12" fill="#26324a" font-weight="bold">S₃(0|0|2)</text>
  <circle cx="94"  cy="230" r="3.5" fill="#3a5a9c"/><text x="46"  y="250" font-size="12" fill="#26324a" font-weight="bold">S₂(0|−6|0)</text>
  <circle cx="190" cy="269" r="3.5" fill="#3a5a9c"/><text x="198" y="283" font-size="12" fill="#26324a" font-weight="bold">S₁(3|0|0)</text>
</svg>
<figcaption>Schematisches Schrägbild — das <b>Spurdreieck</b> der Ebene \( E \) durch die drei Spurpunkte \( S_1(3\,|\,0\,|\,0) \), \( S_2(0\,|\,-6\,|\,0) \), \( S_3(0\,|\,0\,|\,2) \). Der orange Pfeil ist der Normalenvektor \( \vec n=(2\,|\,-1\,|\,3) \).</figcaption>
</figure>

### AB I — Spurpunkte & Lage von \( E \), Normalenvektor, besondere Lage von \( F \)

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Spurpunkte von \( E \) (Lage veranschaulichen).** Ein **Spurpunkt** ist die Stelle, an der die Ebene
eine **Koordinatenachse** durchstößt. Auf einer Achse sind die beiden anderen Koordinaten null:

- **\( x_1 \)-Achse** (\( x_2=x_3=0 \)): \( 2x_1 = 6 \Rightarrow x_1 = 3 \), also \( S_1(3\,|\,0\,|\,0) \).
- **\( x_2 \)-Achse** (\( x_1=x_3=0 \)): \( -x_2 = 6 \Rightarrow x_2 = -6 \), also \( S_2(0\,|\,-6\,|\,0) \).
- **\( x_3 \)-Achse** (\( x_1=x_2=0 \)): \( 3x_3 = 6 \Rightarrow x_3 = 2 \), also \( S_3(0\,|\,0\,|\,2) \).

Verbindet man die drei Spurpunkte, erhält man das **Spurdreieck** (siehe Bild oben). Es zeigt
anschaulich, wie schräg \( E \) im Raum liegt. \( E \) trifft **alle drei** Achsen → \( E \) liegt in
**allgemeiner Lage** (keine Achse, keine Koordinatenebene ist parallel).

**Punktprobe.** Eine **Punktprobe** prüft, ob ein Punkt auf \( E \) liegt: Koordinaten einsetzen und
schauen, ob \( 6 \) herauskommt.

- \( P(1\,|\,2\,|\,2) \): \( 2\cdot 1 - 2 + 3\cdot 2 = 2 - 2 + 6 = 6 \) ✓ → \( P \) **liegt auf** \( E \).
- Ursprung \( O(0\,|\,0\,|\,0) \): \( 2\cdot 0 - 0 + 3\cdot 0 = 0 \neq 6 \) → \( O \) liegt **nicht** auf
  \( E \).

**Normalenvektor ablesen.** Bei einer Koordinatengleichung \( n_1 x_1 + n_2 x_2 + n_3 x_3 = d \) sind
die **Vorzahlen vor \( x_1, x_2, x_3 \)** genau die Koordinaten des Normalenvektors. Man liest direkt ab:

\[ \vec n_E = \begin{pmatrix}2\\-1\\3\end{pmatrix}. \]

**Besondere Lage von \( F \).** \( F:\ 2x_1 - x_2 = 6 \) schreibt man vollständig als
\( 2x_1 - x_2 + 0\cdot x_3 = 6 \). Der Normalenvektor ist also

\[ \vec n_F = \begin{pmatrix}2\\-1\\0\end{pmatrix}. \]

Die **dritte Komponente ist null**: Der Normalenvektor hat keinen Anteil in \( x_3 \)-Richtung, steht
also waagerecht. Eine Fläche, deren Mast waagerecht zeigt, steht **senkrecht aufgerichtet**. Konkret:

> **\( F \) ist parallel zur \( x_3 \)-Achse.** In der Gleichung kommt \( x_3 \) nicht vor — man darf
> \( x_3 \) beliebig wählen, der Punkt bleibt auf \( F \). \( F \) trifft die \( x_3 \)-Achse deshalb
> **nicht** (nur \( S_1(3\,|\,0\,|\,0) \) und \( S_2(0\,|\,-6\,|\,0) \) sind Spurpunkte; auf der
> \( x_3 \)-Achse ergäbe sich \( 0=6 \), ein Widerspruch).

<details><summary>Haltung dahinter: Spurpunkt, Normalenvektor und „besondere Lage" — ganz von vorn</summary>

**Warum „die anderen Koordinaten null"?** Die \( x_1 \)-Achse besteht aus allen Punkten der Form
\( (x_1\mid 0\mid 0) \) — man bewegt sich nur entlang der ersten Richtung, die beiden anderen Werte
bleiben null. Sucht man den Schnittpunkt der Ebene mit dieser Achse, setzt man \( x_2=0 \) und
\( x_3=0 \) in die Ebenengleichung ein. Übrig bleibt eine einfache Gleichung in \( x_1 \). Das ist der
Spurpunkt auf der \( x_1 \)-Achse. Genauso für die beiden anderen Achsen. Drei Achsen → bis zu drei
Spurpunkte → das Spurdreieck, an dem man die Lage „sieht".

**Normalenvektor = Fahnenmast.** Der **Normalenvektor** ist ein Pfeil, der **senkrecht auf der Ebene
steht** — wie ein Fahnenmast, der gerade aus einer schrägen Dachfläche ragt. Sein Witz: Seine drei
Zahlen sind **genau** die Vorzahlen in der Ebenengleichung. Deshalb kann man ihn ohne Rechnung
**ablesen**: \( 2x_1 - x_2 + 3x_3 = 6 \) → \( \vec n = (2\mid -1\mid 3) \). (Vorsicht beim Vorzeichen:
\( -x_2 \) bedeutet \( -1 \) als zweite Komponente.)

**„Besondere Lage".** Eine Ebene hat eine besondere Lage, wenn sie zu einer Achse oder zu einer
Koordinatenebene **parallel** ist. Das erkennt man an **Nullen** im Normalenvektor: Fehlt eine Richtung
im Normalenvektor (hier \( x_3 \)), so steht der Mast in dieser Richtung „flach", und die Ebene läuft
parallel zu dieser Achse. Bei \( F \) fehlt \( x_3 \) → \( F \) ist parallel zur \( x_3 \)-Achse.

<details><summary>Alltagsbild für \( F \) parallel zur \( x_3 \)-Achse</summary>

Stell dir die \( x_1x_2 \)-Ebene als **Fußboden** vor und die \( x_3 \)-Achse als **Senkrechte nach
oben**. Die Gleichung \( 2x_1 - x_2 = 6 \) beschreibt im Fußboden eine **Gerade** (die Spurgerade).
\( F \) ist die **Wand**, die genau über dieser Bodengerade **senkrecht hochgezogen** ist. Eine Wand
läuft parallel zur senkrechten Richtung — deshalb \( F\parallel x_3 \)-Achse. Die Höhe \( x_3 \) ist
der Wand egal, sie steht überall gleich.

</details>

<details><summary>Punktprobe ganz langsam (mit Zahlen)</summary>

Für \( P(1\mid 2\mid 2) \): Ersetze in \( 2x_1 - x_2 + 3x_3 \) die Buchstaben durch die Zahlen von
\( P \): \( x_1=1,\ x_2=2,\ x_3=2 \).
\( 2\cdot 1 = 2 \); dann \( -x_2 = -2 \); dann \( 3\cdot 2 = 6 \). Addieren: \( 2 - 2 + 6 = 6 \). Auf der
rechten Seite steht ebenfalls \( 6 \) → die Gleichung **stimmt** → \( P \) liegt auf \( E \). Käme
etwas anderes als \( 6 \) heraus, läge \( P \) daneben.

</details>
</details>
</details>

### AB II — Spurpunkt-Zahl ↔ Lage, Parameterform, Abstände, parallele/orthogonale Ebene, Spiegelung

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**1) Beziehung zwischen Anzahl der Spurpunkte und besonderer Lage.** Die Zahl der Spurpunkte verrät die
Lage der Ebene:

| Spurpunkte | Lage der Ebene | Beispiel |
|---|---|---|
| **3** | allgemeine (schräge) Lage, schneidet alle drei Achsen | \( E:\ 2x_1-x_2+3x_3=6 \) |
| **2** | **parallel zu einer Achse** (eine Vorzahl ist 0) | \( F:\ 2x_1-x_2=6 \) (∥ \( x_3 \)-Achse) |
| **1** | **parallel zu einer Koordinatenebene** (zwei Vorzahlen sind 0) | \( x_3=2 \) (∥ \( x_1x_2 \)-Ebene) |

Merksatz: **Je mehr Nullen im Normalenvektor, desto „besonderer" die Lage und desto weniger Spurpunkte.**
\( E \) hat drei Spurpunkte (schräg), \( F \) zwei (parallel zu einer Achse).

**2) Parameterform (vektorielle Darstellung) von \( E \).** Man braucht **einen Punkt** der Ebene
(Stützvektor) und **zwei** verschiedene Richtungen, die **in** der Ebene liegen (Spannvektoren). Als
Stützpunkt nimmt man \( S_1(3\,|\,0\,|\,0) \). Zwei Richtungen, die senkrecht zu \( \vec n=(2\mid -1\mid 3) \)
stehen (also in \( E \) liegen), sind z. B. \( (1\mid 2\mid 0) \) und \( (0\mid 3\mid 1) \) — Probe:
\( (1\mid 2\mid 0)\cdot\vec n = 2-2+0 = 0 \) ✓, \( (0\mid 3\mid 1)\cdot\vec n = 0-3+3 = 0 \) ✓.

\[ E:\quad \vec x = \begin{pmatrix}3\\0\\0\end{pmatrix} + s\begin{pmatrix}1\\2\\0\end{pmatrix}
+ t\begin{pmatrix}0\\3\\1\end{pmatrix}, \qquad s,t\in\mathbb{R}. \]

**Geometrische Bedeutung der Bestandteile:**

- **Stützvektor \( (3\mid 0\mid 0) \):** ein fester „Ankerpunkt" auf der Ebene (hier der Spurpunkt auf
  der \( x_1 \)-Achse). Er heftet die Ebene im Raum fest.
- **Spannvektoren \( (1\mid 2\mid 0) \) und \( (0\mid 3\mid 1) \):** zwei nicht-parallele Richtungen, die
  *innerhalb* der Ebene liegen. Vom Anker aus erreicht man jeden Ebenenpunkt, indem man ein Stück in die
  erste und ein Stück in die zweite Richtung geht.
- **Parameter \( s, t \):** sagen, **wie weit** man in jede Richtung geht. Laufen \( s, t \) durch alle
  reellen Zahlen, überstreicht man die **ganze** (unendliche) Ebene.

**3) Abstand verschiedener Objekte zu \( E \).** Werkzeug ist die **Hesse-Normalform**: Der Abstand
eines Punktes \( P(p_1\mid p_2\mid p_3) \) von \( E \) ist

\[ d(P,E) = \frac{\big|\,2p_1 - p_2 + 3p_3 - 6\,\big|}{|\vec n_E|},\qquad |\vec n_E| = \sqrt{2^2+(-1)^2+3^2} = \sqrt{14}. \]

Beispiele:

- **Punkt** \( O(0\mid 0\mid 0) \): \( d = \dfrac{|0-0+0-6|}{\sqrt{14}} = \dfrac{6}{\sqrt{14}} = \dfrac{3\sqrt{14}}{7} \approx 1{,}60 \).
- **Parallele Ebene** \( E':\ 2x_1 - x_2 + 3x_3 = 20 \) (gleicher Normalenvektor): Abstand der beiden
  Ebenen \( = \dfrac{|20-6|}{\sqrt{14}} = \dfrac{14}{\sqrt{14}} = \sqrt{14}\approx 3{,}74 \).
- **Parallele Gerade** zu \( E \) (Richtung steht senkrecht auf \( \vec n \)): hat überall denselben
  Abstand; man rechnet den Abstand **eines** Geradenpunkts mit derselben Formel.

Wichtig: Nur **parallele** Objekte haben einen festen Abstand zu \( E \). Schneidet ein Objekt die
Ebene, ist der Abstand \( 0 \).

**4) Parallele bzw. orthogonale Ebene zu \( E \).**

- **Parallel:** gleicher Normalenvektor \( (2\mid -1\mid 3) \), nur die rechte Zahl ändern. Beispiel
  durch \( P(1\mid 1\mid 1) \): \( 2+(-1)+3 = 4 \), also \( 2x_1 - x_2 + 3x_3 = 4 \). (Allgemein:
  \( 2x_1 - x_2 + 3x_3 = c \) mit \( c\neq 6 \).)
- **Orthogonal:** zwei Ebenen stehen senkrecht zueinander, wenn ihre **Normalenvektoren senkrecht**
  zueinander stehen (Skalarprodukt \( 0 \)). Man wählt einen Normalenvektor \( \vec m \) mit
  \( \vec m\cdot\vec n_E = 0 \), z. B. \( \vec m=(1\mid 2\mid 0) \) (denn \( 1\cdot 2 + 2\cdot(-1) + 0\cdot 3 = 0 \)).
  Beispiel-Ebene: \( x_1 + 2x_2 = 0 \). (Es gibt **unendlich viele** solche orthogonalen Ebenen.)

**5) Spiegeln einer Geraden an \( E \).** Eine Gerade spiegelt man, indem man ihre Punkte spiegelt. Am
elegantesten: **Stützpunkt spiegeln** und **Richtungsvektor spiegeln**. Wie man einen Punkt \( P \) an
\( E \) spiegelt, zeigt das Schema:

<figure>
<svg viewBox="0 0 460 270" role="img" aria-label="Spiegelung eines Punktes an einer Ebene: Lot vom Punkt auf die Ebene, Lotfußpunkt, gleich weit auf die andere Seite" style="width:100%;max-width:480px;height:auto;background:#fbf7ef;border-radius:8px">
  <!-- Ebene E von der Seite (Kante) -->
  <line x1="70" y1="180" x2="390" y2="100" stroke="#3a5a9c" stroke-width="2.2"/>
  <text x="300" y="96" font-size="13" fill="#3a5a9c" font-weight="bold">Ebene E (von der Seite)</text>
  <!-- Lotgerade P - F - P' -->
  <line x1="192" y1="57" x2="236" y2="231" stroke="#7a7163" stroke-width="1.4" stroke-dasharray="5 4"/>
  <!-- rechter Winkel am Fuss -->
  <rect x="207" y="135" width="14" height="14" fill="none" stroke="#7a7163" stroke-width="1" transform="rotate(-14 214 144)"/>
  <!-- Punkte -->
  <circle cx="192" cy="57" r="4" fill="#d98324"/><text x="172" y="52" font-size="13" fill="#26324a" font-weight="bold">P</text>
  <circle cx="214" cy="144" r="3.5" fill="#3a5a9c"/><text x="224" y="140" font-size="12" fill="#26324a">F (Lotfußpunkt)</text>
  <circle cx="236" cy="231" r="4" fill="#d98324"/><text x="246" y="236" font-size="13" fill="#26324a" font-weight="bold">P′ (Spiegelpunkt)</text>
  <text x="160" y="104" font-size="12" fill="#7a7163">d</text>
  <text x="244" y="190" font-size="12" fill="#7a7163">d</text>
</svg>
<figcaption>Spiegelung an \( E \): vom Punkt \( P \) senkrecht (in Richtung \( \vec n \)) auf die Ebene loten, Lotfußpunkt \( F \), dann gleich weit (\( d \)) auf die andere Seite zu \( P' \).</figcaption>
</figure>

**Beispiel — Spiegelung der \( x_1 \)-Achse** \( g:\ \vec x = \begin{pmatrix}0\\0\\0\end{pmatrix}
+ r\begin{pmatrix}1\\0\\0\end{pmatrix} \).

*Stützpunkt \( O(0\mid 0\mid 0) \) spiegeln.* Lotgerade durch \( O \) in Richtung \( \vec n=(2\mid -1\mid 3) \):
\( \vec x = (2r\mid -r\mid 3r) \). Einsetzen in \( E \): \( 2(2r) -(-r) + 3(3r) = 4r + r + 9r = 14r = 6
\Rightarrow r = \tfrac{3}{7} \). Lotfußpunkt
\( F = \big(\tfrac{6}{7}\,\big|\,-\tfrac{3}{7}\,\big|\,\tfrac{9}{7}\big) \). Der Spiegelpunkt liegt
doppelt so weit: \( O' = 2F - O = \big(\tfrac{12}{7}\,\big|\,-\tfrac{6}{7}\,\big|\,\tfrac{18}{7}\big) \).

*Richtung \( \vec u=(1\mid 0\mid 0) \) spiegeln.* Beim Spiegeln dreht sich nur der Anteil **senkrecht zur
Ebene** um; Formel \( \vec u' = \vec u - 2\,\dfrac{\vec u\cdot\vec n}{\vec n\cdot\vec n}\,\vec n \). Mit
\( \vec u\cdot\vec n = 2 \) und \( \vec n\cdot\vec n = 14 \):
\( \vec u' = (1\mid 0\mid 0) - 2\cdot\tfrac{2}{14}(2\mid -1\mid 3) = \big(\tfrac{3}{7}\,\big|\,\tfrac{2}{7}\,\big|\,-\tfrac{6}{7}\big)\ \parallel\ (3\mid 2\mid -6) \).

Gespiegelte Gerade:
\[ g':\quad \vec x = \begin{pmatrix}12/7\\-6/7\\18/7\end{pmatrix} + r\begin{pmatrix}3\\2\\-6\end{pmatrix}. \]

*Probe:* Die Original-Achse trifft \( E \) in \( S_1(3\mid 0\mid 0) \); dieser Punkt muss beim Spiegeln
**fest** bleiben. Setzt man \( r=\tfrac{3}{7} \) in \( g' \) ein, kommt \( (3\mid 0\mid 0) \) heraus ✓.

<details><summary>Haltung dahinter: die fünf Werkzeuge in Alltagssprache</summary>

- **Skalarprodukt \( \vec a\cdot\vec b \):** zwei Vektoren komponentenweise multiplizieren und addieren
  (\( a_1b_1+a_2b_2+a_3b_3 \)). Sein Nutzen hier: **\( =0 \) heißt „stehen senkrecht aufeinander".** So
  prüft man, ob eine Richtung in einer Ebene liegt (senkrecht zum Mast) oder ob zwei Ebenen orthogonal
  sind. Schema im [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html#skalarprodukt).
- **Parameterform.** Eine Ebene als „Ankerpunkt plus zwei Richtungen". Bild: Du stehst am Anker und
  darfst in zwei festen Richtungen beliebig weit laufen — die Menge aller erreichbaren Orte ist die
  ganze Ebene.
- **Hesse-Normalform / Abstand.** Setzt man einen Punkt in \( 2x_1-x_2+3x_3-6 \) ein, sagt das Ergebnis,
  *wie weit weg* und *auf welcher Seite* der Punkt liegt. Teilt man durch die Länge des Normalenvektors
  \( \sqrt{14} \), wird daraus der echte **Abstand** in Längeneinheiten. Auf \( E \) selbst kommt \( 0 \)
  heraus.
- **Parallel vs. orthogonal.** *Parallel* = „gleich gekippt": gleicher Normalenvektor, nur
  verschoben (andere rechte Zahl). *Orthogonal* = „über Eck": die Normalenvektoren stehen senkrecht
  zueinander.
- **Spiegeln.** Wie ein Spiegel an der Wand: vom Objekt **senkrecht zur Wand** loten, am Auftreffpunkt
  (Lotfußpunkt) genauso weit weiter — das ist das Spiegelbild. Eine Gerade spiegelt man, indem man
  Anker und Richtung spiegelt (oder zwei ihrer Punkte).

<details><summary>Spiegelung des Punktes \( O \) ganz langsam (mit Zahlen)</summary>

1. **Lotgerade aufstellen:** von \( O \) in Richtung Mast \( \vec n=(2\mid -1\mid 3) \), also Punkte
   \( (2r\mid -r\mid 3r) \).
2. **Schnitt mit \( E \):** in \( 2x_1 - x_2 + 3x_3 = 6 \) einsetzen: \( 2\cdot 2r = 4r \);
   \( -(-r) = +r \); \( 3\cdot 3r = 9r \). Summe \( 4r + r + 9r = 14r \). Gleichsetzen mit \( 6 \):
   \( 14r = 6 \Rightarrow r = \tfrac{6}{14} = \tfrac{3}{7} \).
3. **Lotfußpunkt \( F \):** \( r=\tfrac37 \) einsetzen: \( (2\cdot\tfrac37\mid -\tfrac37\mid 3\cdot\tfrac37)
   = (\tfrac67\mid -\tfrac37\mid \tfrac97) \).
4. **Verdoppeln zum Spiegelpunkt:** \( F \) liegt auf halbem Weg von \( O \) nach \( O' \), also
   \( O' = 2F - O = (\tfrac{12}{7}\mid -\tfrac{6}{7}\mid \tfrac{18}{7}) \).
5. **Kontrolle über den Abstand:** \( O \) hatte den Wert \( 0-6=-6 \) in \( 2x_1-x_2+3x_3-6 \);
   \( O' \) liefert \( 2\cdot\tfrac{12}{7} + \tfrac67 + 3\cdot\tfrac{18}{7} - 6 = \tfrac{24+6+54-42}{7}
   = \tfrac{42}{7} = +6 \). Gleicher Betrag, anderes Vorzeichen → gleich weit auf der anderen Seite. ✓

</details>

<details><summary>Typische Falle: nur den Punkt spiegeln und die Richtung vergessen</summary>

Wer beim Spiegeln einer Geraden nur den Stützpunkt spiegelt und den **alten** Richtungsvektor behält,
bekommt eine falsche Gerade (außer die Gerade läge zufällig parallel zur Ebene). Die Richtung muss
**mitgespiegelt** werden. Sicherer Alternativweg: **zwei** Punkte der Geraden einzeln spiegeln und durch
die zwei Bildpunkte die neue Gerade legen.

</details>
</details>
</details>

### AB III — besondere Ausschnitte von \( E \), gemeinsame Punkte von \( E \) und \( F \)

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Verfahren anzeigen</summary>

**1) Besondere Ausschnitte von \( E \) in Parameterform (Parameter z. B. aus \( [0;1] \)).** In der
Parameterform \( \vec x = A + s\,\vec u + t\,\vec v \) wählt man bisher \( s,t\in\mathbb{R} \) und erhält
die **ganze** Ebene. Schränkt man die Parameter auf ein Intervall ein, schneidet man ein **Stück** der
Ebene heraus:

- \( s,t\in[0;1] \): das **Parallelogramm** mit der Ecke \( A \) und den Seiten \( \vec u, \vec v \).
- \( s\in[0;1],\ t=0 \): die **Strecke** von \( A \) nach \( A+\vec u \).
- \( s\ge 0,\ t\ge 0 \): eine **Viertel-Ebene** (rechtwinkliger Ausschnitt ab der Ecke \( A \)).
- \( s,t\ge 0,\ s+t\le 1 \): das **Dreieck** \( A,\ A+\vec u,\ A+\vec v \).

Konkret für \( E:\ \vec x = (3\mid 0\mid 0) + s(1\mid 2\mid 0) + t(0\mid 3\mid 1) \) liefert
\( s,t\in[0;1] \) das Parallelogramm mit den vier Ecken

\[ A(3\,|\,0\,|\,0),\quad A+\vec u\,(4\,|\,2\,|\,0),\quad A+\vec v\,(3\,|\,3\,|\,1),\quad A+\vec u+\vec v\,(4\,|\,5\,|\,1). \]

Alle vier erfüllen \( 2x_1 - x_2 + 3x_3 = 6 \) (Punktprobe), liegen also auf \( E \) — es ist ein
ebenes Parallelogramm-Stück mitten in \( E \).

**2) Gemeinsame Punkte der Ebenen \( E \) und \( F \).** Zwei nicht-parallele Ebenen schneiden sich in
einer **Geraden** (der Schnittgeraden). Da \( \vec n_E=(2\mid -1\mid 3) \) und \( \vec n_F=(2\mid -1\mid 0) \)
**nicht** parallel sind, gibt es eine Schnittgerade. Am schnellsten subtrahiert man die Gleichungen:

\[ E - F:\quad (2x_1 - x_2 + 3x_3) - (2x_1 - x_2) = 6 - 6 \;\;\Longrightarrow\;\; 3x_3 = 0 \;\;\Longrightarrow\;\; x_3 = 0. \]

Die gemeinsamen Punkte liegen also in der Ebene \( x_3=0 \) (dem „Boden") und erfüllen \( 2x_1 - x_2 = 6 \).
Setzt man \( x_1 = r \), folgt \( x_2 = 2r - 6 \), \( x_3 = 0 \):

\[ g_{E\cap F}:\quad \vec x = \begin{pmatrix}0\\-6\\0\end{pmatrix} + r\begin{pmatrix}1\\2\\0\end{pmatrix}, \qquad r\in\mathbb{R}. \]

*Kontrolle:* Der Punkt \( (0\mid -6\mid 0) \) erfüllt beide Gleichungen
(\( E:\ 0+6+0=6 \) ✓, \( F:\ 0+6=6 \) ✓); die Richtung \( (1\mid 2\mid 0) \) steht senkrecht auf
**beiden** Normalenvektoren (\( (1\mid 2\mid 0)\cdot\vec n_E = 2-2+0=0 \) ✓,
\( (1\mid 2\mid 0)\cdot\vec n_F = 2-2+0=0 \) ✓). Die Schnittgerade geht durch die beiden gemeinsamen
Spurpunkte \( S_1(3\mid 0\mid 0) \) und \( S_2(0\mid -6\mid 0) \) — genau die Spurgerade im Boden.

<details><summary>Haltung dahinter: Ausschnitte und Schnittgerade — von Grund auf</summary>

**Warum schneidet ein Parameter-Intervall ein Stück aus?** Mit \( s,t\in\mathbb{R} \) darf man vom Anker
\( A \) **unbegrenzt** in beide Richtungen laufen → die ganze unendliche Ebene. Begrenzt man die
Schrittweite, etwa \( 0\le s\le 1 \) und \( 0\le t\le 1 \), kommt man höchstens **einen** Schritt
\( \vec u \) und **einen** Schritt \( \vec v \) weit. Alle erreichbaren Punkte füllen genau das
**Parallelogramm**, das \( \vec u \) und \( \vec v \) vom Anker aus aufspannen. Wählt man stattdessen
\( s+t\le 1 \), bleibt man im halben Parallelogramm — einem **Dreieck**. So lassen sich gezielt
endliche Flächenstücke einer Ebene beschreiben (etwa eine Wand mit Rand statt einer unendlichen Fläche).

**Warum ist der Schnitt eine Gerade, und warum funktioniert das Subtrahieren?** Jede Ebene ist eine
Bedingung an die Punkte; zwei Ebenen sind zwei Bedingungen gleichzeitig. Im Raum bleibt dann eine
**Gerade** voller Punkte übrig, die beide erfüllen (wie die Kante, an der zwei Wände zusammenstoßen).
Subtrahiert man die zwei Gleichungen, fallen die gemeinsamen Teile (\( 2x_1 \) und \( -x_2 \)) weg, und
es bleibt eine einfache neue Bedingung \( 3x_3=0 \), also \( x_3=0 \). Zusammen mit einer der
Originalgleichungen beschreibt das die Schnittgerade.

<details><summary>Eleganter Gegencheck: Richtung über das Kreuzprodukt</summary>

Die Richtung der Schnittgeraden steht senkrecht auf **beiden** Normalenvektoren — genau das liefert das
**Kreuzprodukt** \( \vec n_E\times\vec n_F \):
\[ \begin{pmatrix}2\\-1\\3\end{pmatrix}\times\begin{pmatrix}2\\-1\\0\end{pmatrix}
= \begin{pmatrix}(-1)\cdot 0 - 3\cdot(-1)\\ 3\cdot 2 - 2\cdot 0\\ 2\cdot(-1) - (-1)\cdot 2\end{pmatrix}
= \begin{pmatrix}3\\6\\0\end{pmatrix}\ \parallel\ \begin{pmatrix}1\\2\\0\end{pmatrix}. \]
Dasselbe Ergebnis wie oben. (Kreuzprodukt-Schema:
[Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html#kreuzprodukt).)

</details>

<details><summary>Typische Falle: aus \( x_3=0 \) eine ganze Ebene machen</summary>

\( x_3=0 \) allein ist die Boden-Ebene, **nicht** die Schnittgerade. Man braucht **beide** Bedingungen
zusammen: \( x_3=0 \) **und** \( 2x_1 - x_2 = 6 \). Erst beide zusammen ergeben die Gerade. Wer nur eine
behält, beschreibt zu viele Punkte.

</details>
</details>
</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Aspekt, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen kannst. Du
musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Analysis) aufklappen</summary>

- **a) Werte berechnen und deuten.** Erwartet: \( f(0)=48 \) („Anfangsgeschwindigkeit 48 m/s"),
  \( f'(0)=-1{,}92 \) („Anfangsbeschleunigung \( -1{,}92\ \tfrac{\text{m}}{\text{s}^2} \), Auto bremst"),
  Integral \( \approx 1737{,}53 \) („Strecke in 60 s, ≈ 1,7 km"). *Rückfrage:* „Was bedeutet das Minus
  bei \( f'(0) \)?" (Antwort: Auto wird langsamer.) *Rote Flagge:* das Integral als „Geschwindigkeit"
  statt als „Strecke" deuten.
- **b) Bewegungen.** Erwartet: Auto wird **langsamer**, Abnahme **immer geringer** (48 → 24); Motorrad
  startet bei **0**, wird **schneller**, Zunahme **immer geringer** (0 → 40). *Rückfrage:* „Auf welchen
  Wert läuft jede Geschwindigkeit langfristig zu?"
- **c) Punkt \( H \).** Erwartet: \( x_H = \) **Schnittstelle der beiden Graphen** (gleiche
  Geschwindigkeit); \( y_H = \) **Fläche zwischen den Kurven** und damit **kleiner als 500** (grob über
  Dreieck \( \tfrac12\cdot 12\cdot 48 \approx 288 \)). *Rote Flagge:* \( H \) als Überholpunkt deuten.
  *Rückfrage:* „Warum ist gerade an der Schnittstelle der Abstand am größten?"
- **d) Überholgleichung.** Erwartet: gleiche **Strecke** → \( \int_0^{x_0} f = \int_0^{x_0} g \).
  *Rote Flagge:* \( f(x_0)=g(x_0) \) (das ist Punkt \( H \), nicht das Überholen). *Rückfrage:* „Was ist
  beim Überholen gleich — die Geschwindigkeit oder die Strecke?"

</details>

<details><summary>Leitfaden Teil 2 (Geometrie) aufklappen</summary>

- **AB I — Spurpunkte / Punktprobe / Normalenvektor / Lage von \( F \).** Erwartet: drei Spurpunkte
  \( (3\mid 0\mid 0),\ (0\mid -6\mid 0),\ (0\mid 0\mid 2) \); Normalenvektor \( (2\mid -1\mid 3) \)
  **abgelesen**; \( F \) **parallel zur \( x_3 \)-Achse** (weil \( x_3 \) fehlt). *Rückfrage:* „Woran
  sieht man im Normalenvektor die besondere Lage von \( F \)?" (Antwort: dritte Komponente \( 0 \).)
- **AB II — Spurpunkt-Zahl / Parameterform / Abstand / parallel-orthogonal / Spiegeln.** Erwartet: 3
  Spurpunkte = schräg, 2 = parallel zu einer Achse, 1 = parallel zu einer Koordinatenebene;
  Parameterform mit **einem Stützpunkt + zwei Spannvektoren**; Abstand über **Hesse-Normalform**
  (\( |\dots|/\sqrt{14} \)); parallel = **gleicher** Normalenvektor, orthogonal = Normalenvektoren
  **senkrecht** (Skalarprodukt \( 0 \)); Spiegeln = **Lot fällen, Lotfußpunkt, gleich weit weiter**.
  *Rückfrage:* „Wie prüfst du schnell, ob eine Richtung in \( E \) liegt?" (Antwort: Skalarprodukt mit
  \( \vec n \) ist \( 0 \).)
- **AB III — Ausschnitte / gemeinsame Punkte.** Hier zählt **sauberes Erklären**: \( s,t\in[0;1] \)
  liefert ein **Parallelogramm**; \( s+t\le 1 \) ein Dreieck. Gemeinsame Punkte von \( E,F \) =
  **Schnittgerade**; durch **Subtrahieren** kommt \( x_3=0 \), zusammen mit \( 2x_1-x_2=6 \) ergibt sich
  \( \vec x=(0\mid -6\mid 0)+r(1\mid 2\mid 0) \). *Rückfrage:* „Warum ist der Schnitt eine Gerade und
  kein einzelner Punkt?"

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Warum ist \( \int_0^{60} f\,dx \) die zurückgelegte **Strecke** und nicht eine Geschwindigkeit?
- Wo liegt der Punkt \( H \) (größter Abstand) im Verhältnis zum Überholpunkt \( x_0 \), und warum?
- Wie liest du den **Normalenvektor** einer Ebene direkt aus ihrer Koordinatengleichung ab?
- Woran erkennst du an \( F:\ 2x_1 - x_2 = 6 \), dass die Ebene parallel zur \( x_3 \)-Achse liegt?
- Wie spiegelst du einen Punkt an einer Ebene — welche drei Schritte sind das?
- Wie bestimmst du die **gemeinsamen Punkte** zweier Ebenen, und warum ist das Ergebnis eine Gerade?
