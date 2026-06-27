# Aufgabe 1 — Analysis & Geometrie

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Analysis**, **Teil 2 (Gespräch) aus der Geometrie**. Alles ist
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
> Vektoren, Länge, Skalarprodukt, Kreuzprodukt, Ebenengleichung, Pyramidenvolumen) stehen kompakt im
> [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html). Die Analysis-Werkzeuge findest du
> in den Kapiteln [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Integral-Grundlagen](kap-integral-grundlagen.html) und
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).

---

## Teil 1 — Vortrag (Analysis): Funktionen zuordnen, Terme und Flächen

<div class="aufgabenkasten">

**Die Abbildungen zeigen die Graphen einer ganzrationalen Funktion \( f \), einer trigonometrischen
Funktion \( g \) und einer Exponentialfunktion \( h \).**

**a)** Ordne die Funktionen \( f \), \( g \) und \( h \) den abgebildeten Graphen zu und begründe die
Zuordnung.

**b)** Gib für einen der abgebildeten Graphen einen möglichen Funktionsterm an. Erkläre, wie du dabei
vorgegangen bist.

**c)** Der Graph der ganzrationalen Funktion (Abbildung II) schließt mit der \( x \)-Achse eine Fläche
ein. Beschreibe ein Verfahren, mit dem man den Inhalt dieser Fläche berechnen kann, und gib einen
entsprechenden Rechenausdruck an.

**d)** Gegeben ist die Funktion \( i \) mit \( i(x) = -e^{-x} \). Berechne \( a \) so, dass
\( \displaystyle\int_a^0 i(x)\,dx = -2 \) gilt. Bestimme außerdem eine nichtkonstante ganzrationale
Funktion \( j \) und Werte für \( b \) und \( c \), sodass \( \displaystyle\int_b^c j(x)\,dx = -8 \)
gilt.

</div>

Hier sind die drei Graphen. Spiele mit den Bildern und ordne sie zu, bevor du die Lösung aufklappst.

<div class="graph-row">
<figure>
<div class="jxgbox" id="jxg-k1-abb1" style="width:100%;max-width:320px;aspect-ratio:1/1"></div>
<figcaption>Abbildung I</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k1-abb2" style="width:100%;max-width:320px;aspect-ratio:1/1"></div>
<figcaption>Abbildung II</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k1-abb3" style="width:100%;max-width:320px;aspect-ratio:1/1"></div>
<figcaption>Abbildung III</figcaption>
</figure>
</div>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k1-abb1',{boundingbox:[-3,5.5,5,-1.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 2*Math.exp(-x);},-3,5],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k1-abb2',{boundingbox:[-5,4.5,5,-7],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return -(1/6)*(x-2)*(x-3)*(x+4);},-5,4.2],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k1-abb3',{boundingbox:[-3.5,4,7,-2],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return -2*Math.sin(x)+1;},-3.5,7],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>

### Teilaufgabe a) — Zuordnung

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Man ordnet **über die typische Gestalt** jeder Funktionsklasse zu:

- **\( h \) (Exponentialfunktion) → Abbildung I.** Der Graph ist überall positiv, fällt von links nach
  rechts und nähert sich der \( x \)-Achse, ohne sie je zu erreichen.
- **\( f \) (ganzrationale Funktion) → Abbildung II.** Der Graph hat mehrere Nullstellen, einen „Bauch"
  nach unten und einen nach oben und läuft an beiden Rändern ins Unendliche.
- **\( g \) (trigonometrische Funktion) → Abbildung III.** Der Graph schwingt **periodisch** auf und ab,
  immer zwischen einem festen Größt- und Kleinstwert.

<details><summary>Haltung dahinter: Was ist überhaupt eine „Funktionsklasse", und woran erkenne ich sie?</summary>

Zuerst ganz langsam, was hier gefragt ist. Eine **Funktion** ist eine Rechenvorschrift: Man steckt
eine Zahl \( x \) hinein und bekommt eine Zahl \( y \) heraus. Trägt man alle Paare \( (x \mid y) \) in
ein Koordinatensystem ein, entsteht eine Linie — der **Graph**. Es gibt verschiedene „Sorten" von
Rechenvorschriften, und jede Sorte erzeugt eine **typische Form** von Linie. Genau diese Formen soll
man hier wiedererkennen. Die drei Sorten:

- **Ganzrationale Funktion (Polynom).** Hier wird \( x \) nur **mit sich selbst multipliziert** und mit
  Zahlen verrechnet, z. B. \( x^2 \), \( x^3 \), \( 5x - 4 \). Die höchste Potenz heißt **Grad**. Solche
  Graphen sind „weiche" Kurven mit ein paar Hügeln und Tälern, die an den Rändern (ganz links und ganz
  rechts) immer **steil nach oben oder unten weglaufen** — sie „explodieren" nach außen. Ein \( x^3 \)
  hat bis zu drei Stellen, an denen er die \( x \)-Achse kreuzt (**Nullstellen**). Abbildung II hat
  genau diese Gestalt: mehrere Kreuzungen, ein Tal, ein Hügel, an den Rändern weg ins Unendliche.

- **Exponentialfunktion.** Hier steht \( x \) **oben im Exponenten**, z. B. \( 2^x \) oder \( e^{x} \).
  Die Variable sitzt also „hochgestellt". Das Besondere: So eine Funktion ist (bei positivem Vorfaktor)
  **immer positiv** — der Graph bleibt komplett **oberhalb** der \( x \)-Achse und berührt sie nie. Auf
  der einen Seite schmiegt er sich ganz flach an die Achse an (kommt ihr beliebig nah, erreicht sie aber
  nie), auf der anderen Seite schießt er steil hoch. Abbildung I macht genau das: bleibt über der Achse,
  fällt nach rechts immer flacher, schießt nach links hoch.

- **Trigonometrische Funktion (Sinus/Kosinus).** Diese Funktionen kommen vom Kreis und beschreiben
  **Schwingungen**. Ihr Kennzeichen: Der Graph **wiederholt sich** in immer gleichen Abständen — rauf,
  runter, rauf, runter, endlos, immer zwischen einem festen oberen und unteren Wert. Abbildung III ist
  diese Wellenlinie.

<details><summary>Drei Begriffe, die hier ständig vorkommen — kurz erklärt</summary>

- **Nullstelle:** eine Stelle, an der der Graph die \( x \)-Achse **kreuzt oder berührt**, also wo der
  Funktionswert \( y = 0 \) ist. Anschaulich: „Wo schneidet die Linie die waagerechte Achse?"
- **Asymptote:** eine Linie, der sich der Graph **immer mehr annähert, ohne sie zu erreichen**. Bei der
  e-Funktion ist die \( x \)-Achse so eine Annäherungslinie.
- **Periodisch:** „sich in gleichen Abständen wiederholend". Wie die Wellen am Strand oder die Zeiger
  einer Uhr — nach einer festen Strecke sieht alles wieder genau gleich aus.

</details>
</details>
</details>

### Teilaufgabe b) — Funktionsterm angeben

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Es genügt **ein** Graph. Am rundesten lässt sich die **ganzrationale Funktion** \( f \) (Abb. II)
herleiten, weil man ihre Nullstellen ablesen kann.

**Schritt 1 — Nullstellen ablesen.** Der Graph schneidet die \( x \)-Achse bei \( x=-4 \), \( x=2 \)
und \( x=3 \). Aus jeder Nullstelle wird ein **Linearfaktor**:

\[ k(x) = (x-2)(x-3)(x+4). \]

**Schritt 2 — Streckung/Spiegelung bestimmen.** Diese „nackte" Funktion \( k \) hat noch die falsche
Höhe. Wir vergleichen an einer bequemen Stelle, etwa \( x=0 \): Aus dem Graphen liest man
\( f(0) = -4 \) ab, und

\[ k(0) = (-2)\cdot(-3)\cdot 4 = 24. \]

Aus \( 24 \) soll \( -4 \) werden. Der Faktor dafür ist \( \dfrac{-4}{24} = -\dfrac16 \). Das Minus
**spiegelt** an der \( x \)-Achse, der Betrag \( \tfrac16 \) **staucht**. Also

\[ f(x) = -\frac16\,(x-2)(x-3)(x+4). \]

<details><summary>Haltung dahinter: Warum macht eine Nullstelle einen „Faktor"? (ganz von vorn)</summary>

Das ist der Kern dieser Aufgabe, deshalb wirklich langsam.

**Was ist ein Faktor?** Wenn man Dinge **multipliziert**, heißt jedes der multiplizierten Stücke ein
*Faktor*. In \( 3 \cdot 5 \) sind \( 3 \) und \( 5 \) die Faktoren. In \( (x-2)\cdot(x-3)\cdot(x+4) \)
sind die drei Klammern die Faktoren.

**Die eine Regel, auf der alles beruht — der „Satz vom Nullprodukt":** Ein Produkt (eine
Multiplikation) ist **genau dann null, wenn mindestens einer der Faktoren null ist**. Beispiel:
\( 7 \cdot 0 \cdot 4 = 0 \) — sobald *irgendwo* eine Null mitmultipliziert wird, ist das ganze Ergebnis
null. Umgekehrt: Wenn keiner der Faktoren null ist, kann das Produkt nicht null sein.

**Wie hilft das beim Funktionsterm?** Wir wissen aus dem Bild: Bei \( x = 2 \) ist der Funktionswert
null (dort kreuzt der Graph die Achse). Damit unsere Formel an dieser Stelle wirklich null wird, bauen
wir den Faktor \( (x-2) \) ein — denn setzt man \( x = 2 \) ein, wird \( (2-2) = 0 \), und nach der
Regel oben ist dann das ganze Produkt null. Genauso:

- Nullstelle bei \( x = 3 \) → Faktor \( (x-3) \), denn bei \( x=3 \) ist \( (3-3)=0 \).
- Nullstelle bei \( x = -4 \) → Faktor \( (x+4) \), denn bei \( x=-4 \) ist \( (-4+4)=0 \).

Merkregel: **Nullstelle bei \( x_0 \) → Faktor \( (x - x_0) \).** Aufpassen beim Vorzeichen: Die
Nullstelle \( -4 \) liefert \( (x-(-4)) = (x+4) \) — aus „minus minus vier" wird „plus vier".

Drei Nullstellen ergeben also drei Klammern, multipliziert. Weil man drei \( x \)-Klammern
multipliziert, ist die höchste Potenz \( x^3 \) — ein Polynom **dritten Grades**, genau passend zur
Form im Bild.

<details><summary>Schritt 2 ganz langsam: warum noch der Faktor \( -\tfrac16 \)?</summary>

Die drei Klammern sorgen für die richtigen **Nullstellen** — aber nicht automatisch für die richtige
**Höhe** und nicht für die richtige **Richtung** (Bauch oben oder unten). Man stelle sich vor, der
Graph wäre an einer Stelle „zu hoch" oder „auf dem Kopf". Das repariert ein einziger Vorfaktor vor der
Klammer.

Den Vorfaktor findet man mit **einem** weiteren bekannten Punkt. Am bequemsten ist die Stelle
\( x = 0 \), weil man dort sofort den Schnittpunkt mit der senkrechten \( y \)-Achse abliest: im Bild
\( f(0) = -4 \).

Jetzt rechnet man aus, was die nackte Klammer-Funktion an \( x=0 \) liefert:

\[ k(0) = (0-2)\cdot(0-3)\cdot(0+4) = (-2)\cdot(-3)\cdot 4. \]

Minus mal minus ist plus: \( (-2)\cdot(-3) = 6 \), dann \( 6 \cdot 4 = 24 \). Die nackte Funktion ist an
der Stelle also \( 24 \), wir brauchen aber \( -4 \). Welche Zahl macht aus \( 24 \) die \( -4 \)? Man
teilt: \( \dfrac{-4}{24} = -\dfrac16 \). Dieser Faktor leistet zweierlei auf einmal:

- Das **Minuszeichen** dreht den Graphen an der \( x \)-Achse um (aus „Bauch oben" wird „Bauch unten").
- Der **Bruch \( \tfrac16 \)** drückt den Graphen flacher (staucht ihn in der Höhe).

Ergebnis: \( f(x) = -\tfrac16 (x-2)(x-3)(x+4) \). **Probe:** \( f(0) = -\tfrac16 \cdot 24 = -4 \) — passt
zum Bild.

</details>

<details><summary>Typische Falle</summary>

Den Vorfaktor wegzulassen ist der häufigste Fehler. \( (x-2)(x-3)(x+4) \) allein hat zwar die richtigen
Nullstellen, aber die falsche Höhe **und** die falsche Orientierung (Bauch oben statt unten). Ohne den
Abgleich an einem Punkt ist die Lösung unvollständig — in der mündlichen Prüfung würde man hier
nachgefragt.

</details>
</details>

Zur Vollständigkeit die Terme der beiden anderen Graphen (jeweils aus einer Grundfunktion erzeugt):

- **\( g(x) = -2\sin(x) + 1 \)** — \( \sin(x) \) an der \( x \)-Achse gespiegelt (Minus), um den Faktor
  \( 2 \) in \( y \)-Richtung gestreckt, um \( 1 \) nach oben verschoben.
- **\( h(x) = 2\,e^{-x} \)** — \( e^{x} \) an der \( y \)-Achse gespiegelt (\( -x \) im Exponenten), um
  den Faktor \( 2 \) in \( y \)-Richtung gestreckt.

<details><summary>Haltung dahinter: Was bedeuten „spiegeln", „strecken", „verschieben" am Graphen?</summary>

Man muss diese Terme nicht herleiten — aber es hilft zu wissen, wie aus einer einfachen
Grundfunktion durch kleine Eingriffe eine neue wird. Es gibt vier typische Eingriffe:

- **Vor die Funktion ein Minus** (z. B. \( -\sin x \)): **Spiegelung an der \( x \)-Achse** — der Graph
  wird nach unten geklappt, jeder Punkt oben wird gleich weit nach unten gesetzt.
- **Ein Faktor vor der Funktion** (z. B. \( 2\sin x \)): **Streckung in die Höhe** — alle Werte werden
  verdoppelt, die Wellen werden doppelt so hoch.
- **Eine Zahl dazuaddiert** (z. B. \( \sin x + 1 \)): **Verschiebung nach oben** — der ganze Graph
  rutscht um \( 1 \) hoch.
- **Ein Minus beim \( x \) im Inneren** (z. B. \( e^{-x} \)): **Spiegelung an der senkrechten
  \( y \)-Achse** — links und rechts werden vertauscht. Deshalb fällt \( e^{-x} \) nach rechts, während
  \( e^{x} \) nach rechts steigt.

So liest man \( g(x) = -2\sin(x)+1 \): nimm die Sinuswelle, klapp sie nach unten (Minus), mach sie
doppelt so hoch (Faktor 2), schieb sie um 1 nach oben (+1).

</details>

</details>

### Teilaufgabe c) — Flächeninhalt: Verfahren und Rechenausdruck

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Der Graph von \( f \) schließt mit der \( x \)-Achse **zwei** Teilflächen ein — eine **unterhalb** der
Achse (zwischen \( x=-4 \) und \( x=2 \)) und eine **oberhalb** (zwischen \( x=2 \) und \( x=3 \)). Das
Verfahren in drei Schritten:

1. **Nullstellen bestimmen** — sie sind die Grenzen der Teilflächen: \( x=-4,\ 2,\ 3 \).
2. **Teilflächen einzeln über Integrale berechnen.** Ein Integral liefert den *orientierten*
   Flächeninhalt; was unterhalb der Achse liegt, kommt negativ heraus. Damit beide Beiträge **positiv**
   in die Fläche eingehen, dreht man das Vorzeichen des unteren Stücks um.
3. **Beträge addieren.**

Als Rechenausdruck:

\[ A = -\int_{-4}^{2} f(x)\,dx \;+\; \int_{2}^{3} f(x)\,dx. \]

<details><summary>Haltung dahinter: Was ist ein Integral, und warum kann eine Fläche „negativ" werden?</summary>

Langsam von vorn. Ein **Integral** \( \int_a^b f(x)\,dx \) ist eine Maschine, die die **Fläche zwischen
dem Graphen und der \( x \)-Achse** zwischen zwei senkrechten Grenzen \( a \) (links) und \( b \)
(rechts) zusammenrechnet. Man kann es sich als „unendlich viele hauchdünne senkrechte Streifen unter
der Kurve, alle aufaddiert" vorstellen.

Der Haken: Das Integral zählt Fläche **mit Vorzeichen** — man nennt das *orientierten* Flächeninhalt.

- Liegt der Graph **über** der \( x \)-Achse, sind die Streifen „positiv hoch" → das Integral wird
  **positiv**.
- Liegt der Graph **unter** der \( x \)-Achse, zeigen die Streifen nach unten → sie zählen **negativ**.

Ein gutes Bild ist ein **Bankkonto**: Fläche über der Achse = Einzahlungen (+), Fläche unter der Achse
= Abhebungen (−). Das Integral nennt am Ende nur den **Kontostand**, also die Differenz — nicht die
Summe der bewegten Beträge.

Für einen echten **Flächeninhalt** (ein Stück Papier, das man ausschneiden und wiegen könnte) will man
aber, dass *jedes* Stück positiv zählt. Deshalb:

1. An jeder Nullstelle **trennen** (dort wechselt der Graph die Seite).
2. Jedes Teilstück einzeln integrieren.
3. Von jedem Teilstück den **Betrag** nehmen (das Minuszeichen vor dem unteren Stück macht genau das)
   und alles addieren.

Hier liegt der Graph zwischen \( -4 \) und \( 2 \) **unter** der Achse — deshalb das Minus vor diesem
Integral, das den negativen Wert ins Positive dreht. Zwischen \( 2 \) und \( 3 \) liegt er **über** der
Achse — dieses Integral ist schon positiv und bleibt, wie es ist.

<details><summary>Typische Falle: alles in einem Integral</summary>

Wer einfach \( \int_{-4}^{3} f(x)\,dx \) bildet (ohne zu trennen), bekommt nur den „Kontostand": Der
negative Teil unter der Achse frisst den positiven Teil teilweise auf. Das ist **nicht** der
Flächeninhalt. Man **muss** an jeder Nullstelle trennen und mit Beträgen arbeiten — das ist die
häufigste Fehlerquelle bei Flächenaufgaben.

</details>

<details><summary>Woher weiß ich, welches Stück unter der Achse liegt?</summary>

Man setzt einen einzigen Probe-\( x \)-Wert aus dem Inneren des Stücks in \( f \) ein und schaut auf das
Vorzeichen. Zwischen \( -4 \) und \( 2 \) z. B. \( x=0 \): \( f(0) = -4 \) (negativ) → Stück liegt
**unter** der Achse → Minus davor. Zwischen \( 2 \) und \( 3 \) z. B. \( x=2{,}5 \): \( f(2{,}5) > 0 \)
→ **über** der Achse → bleibt positiv. Ein einziger Testwert pro Stück genügt.

</details>
</details>

In der mündlichen Prüfung ist hier ausdrücklich nur das **Verfahren + der Ausdruck** verlangt — das
mühsame Ausrechnen der Stammfunktion entfällt.

</details>

### Teilaufgabe d) — Integralgleichungen lösen

<span class="tag tag-warn">AB II / AB III</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Teil 1: \( a \) bestimmen mit \( \displaystyle\int_a^0 -e^{-x}\,dx = -2 \).**

Zuerst eine **Stammfunktion** von \( i(x) = -e^{-x} \). Wegen \( \dfrac{d}{dx}\,e^{-x} = -e^{-x} \) ist

\[ I(x) = e^{-x} \quad\text{eine Stammfunktion von } -e^{-x}. \]

Mit dem Hauptsatz:

\[ \int_a^0 -e^{-x}\,dx = \big[\,e^{-x}\,\big]_a^0 = e^{0} - e^{-a} = 1 - e^{-a}. \]

Das setzen wir gleich \( -2 \) und lösen nach \( a \):

\[ 1 - e^{-a} = -2 \;\;\Longrightarrow\;\; e^{-a} = 3 \;\;\Longrightarrow\;\; -a = \ln 3
   \;\;\Longrightarrow\;\; a = -\ln 3. \]

<details><summary>Haltung dahinter: Was ist eine „Stammfunktion", und wie kommt man auf sie? (ganz von vorn)</summary>

Drei Begriffe der Reihe nach.

**Ableiten** misst die **Steigung** eines Graphen — wie stark er an einer Stelle steigt oder fällt. Aus
einer Funktion \( f \) macht man ihre Ableitung \( f' \).

**Eine Stammfunktion ist das Ableiten rückwärts.** Gesucht ist eine Funktion \( I \), deren Ableitung
wieder unser \( i \) ergibt: \( I' = i \). Man „un-leitet" also ab. Das braucht man, weil Integrale
(Flächen) über Stammfunktionen berechnet werden.

**Warum ist \( e^{-x} \) eine Stammfunktion von \( -e^{-x} \)?** Wir prüfen es, indem wir \( e^{-x} \)
**ableiten** und schauen, ob \( -e^{-x} \) herauskommt. Dafür braucht man die **Kettenregel** (siehe
nächster Kasten). Sie liefert \( (e^{-x})' = -e^{-x} \). Genau unser \( i \) — also stimmt es. Probe
durch Ableiten ist hier der sicherste Weg: Wenn das Rückwärts-Ergebnis vorwärts wieder zum Start führt,
war es richtig.

<details><summary>Die Kettenregel — wozu, und wie hier?</summary>

Die **Kettenregel** braucht man, wenn eine Funktion „in einer anderen steckt" — hier steckt das
\( -x \) **im** Exponenten der e-Funktion. Bild: eine **äußere** Funktion (das \( e^{(\text{Kasten})} \))
und eine **innere** Funktion (der Kasten \( = -x \)). Die Regel sagt: Leite außen ab und multipliziere
mit der Ableitung des Inneren.

- Äußere Ableitung: \( e^{(\text{Kasten})} \) bleibt beim Ableiten \( e^{(\text{Kasten})} \) — das ist die
  berühmte Besonderheit der e-Funktion.
- Innere Ableitung: der Kasten ist \( -x \); seine Ableitung ist \( -1 \).
- Multipliziert: \( e^{-x}\cdot(-1) = -e^{-x} \).

Deshalb \( (e^{-x})' = -e^{-x} \). (Ausführlich: [Ableit-Handwerk](kap-ableiten-handwerk.html).)

</details>

<details><summary>Warum darf man am Ende den \( \ln \) nehmen?</summary>

In der Gleichung \( e^{-a} = 3 \) steht das gesuchte \( a \) **oben im Exponenten**. Um es
herunterzuholen, braucht man die **Umkehrung** der e-Funktion — und das ist der **natürliche
Logarithmus** \( \ln \). „Umkehrung" heißt: \( \ln \) macht genau das rückgängig, was \( e^{(\cdot)} \)
tut, so wie Minus das Plus rückgängig macht. Wendet man auf beiden Seiten \( \ln \) an, wird aus
\( e^{-a} = 3 \) die Gleichung \( -a = \ln 3 \), also \( a = -\ln 3 \). (Mehr dazu:
[Grundfunktionen](kap-grundfunktionen.html).)

</details>
</details>

**Teil 2: ganzrationale Funktion \( j \) mit \( \displaystyle\int_b^c j(x)\,dx = -8 \).**

Hier ist **ein passendes Beispiel** gesucht, nicht *die* Lösung. Am einfachsten wählt man
\( j(x) = -x \) und integriert von \( 0 \) bis \( 4 \):

\[ \int_0^4 -x\,dx = \Big[\,-\tfrac12 x^2\,\Big]_0^4 = -\tfrac12\cdot 16 - 0 = -8. \quad\checkmark \]

Also etwa \( j(x) = -x,\ b=0,\ c=4 \).

<details><summary>Haltung dahinter: „bestimme eine Funktion, sodass…" — wie geht man an so eine offene Aufgabe?</summary>

Bei einer **offenen** Aufgabe ist nicht *eine* Lösung gemeint, sondern *irgendeine*, die die Bedingung
erfüllt. Das ist eine Erleichterung: Man darf sich die **einfachste** Funktion bauen, die passt.

Überlegung: Wir brauchen eine **negative** Fläche (\( -8 \)). Eine Gerade, die durch den Ursprung geht
und nach rechts fällt — also \( j(x) = -x \) — liegt rechts von \( 0 \) komplett **unter** der Achse und
erzeugt dort eine negative Fläche. Jetzt muss man nur noch die rechte Grenze \( c \) so wählen, dass
genau \( -8 \) herauskommt; \( c=4 \) trifft es exakt.

**Sicherer Reflex: durch Einsetzen gegenprüfen** (das \( \checkmark \) oben). Man rechnet das Integral
mit den gewählten Werten aus und schaut, ob wirklich \( -8 \) herauskommt. Andere Lösungen sind genauso
richtig — z. B. \( j(x)=-2x,\ b=0,\ c=\sqrt{8} \). Wichtig nur: \( j \) darf **nicht konstant** sein
(eine waagerechte Gerade), denn das war ausdrücklich gefordert; deshalb ist \( j(x)=-x \) die saubere
Wahl. (Stammfunktion-Regeln: [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).)

</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- a) \( f\to \)II (ganzrational), \( g\to \)III (trigonometrisch), \( h\to \)I (exponentiell)
- b) \( f(x) = -\tfrac16(x-2)(x-3)(x+4) \); \( g(x)=-2\sin x+1 \); \( h(x)=2e^{-x} \)
- c) \( A = -\int_{-4}^{2} f\,dx + \int_{2}^{3} f\,dx \) (an Nullstellen trennen, Beträge addieren)
- d) \( a=-\ln 3 \); Beispiel \( j(x)=-x,\ b=0,\ c=4 \)

</details>

---

## Teil 2 — Gespräch (Geometrie): Pyramide mit Lichtquelle

<div class="aufgabenkasten">

**Input.** Eine senkrechte Pyramide mit quadratischer Grundfläche hat die Höhe \( 4 \). Die
Eckpunkte der Grundfläche sind \( A(0\,|\,0\,|\,0) \), \( B(3\,|\,0\,|\,0) \), \( C(3\,|\,3\,|\,0) \),
\( D(0\,|\,3\,|\,0) \); die Spitze heißt \( S \). Im Punkt \( L \) befindet sich eine punktförmige
Lichtquelle.

Im Gespräch denkbare Aspekte: **(AB I)** Koordinaten von \( S \), Pyramidenvolumen,
Koordinatengleichung einer Seitenfläche. **(AB II)** Gleichschenkligkeit eines Seitendreiecks,
Verfahren für die Oberfläche, Formel für den Winkel zwischen Grund- und Seitenfläche. **(AB III)**
Ebenen, die die Pyramide in zwei volumengleiche Teile zerlegen; Prüfung, ob ein Punkt im Inneren
liegt; Untersuchung eines Schattenwurfs.

</div>

> **Vorab, in einem Satz, was ein Koordinatensystem im Raum ist:** Statt nur „rechts/links" und
> „oben/unten" (zwei Zahlen) braucht man im Raum **drei** Zahlen pro Punkt — \( (x_1 \mid x_2 \mid x_3) \)
> —, weil es zusätzlich „vorne/hinten" gibt. Ein Punkt wie \( B(3\,|\,0\,|\,0) \) heißt: 3 Schritte in
> \( x_1 \)-Richtung, 0 in \( x_2 \), 0 in \( x_3 \). Alle Vektor-Werkzeuge stehen kompakt im
> [Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html).

So liegt die Pyramide im Koordinatensystem (schematische Darstellung):

<figure>
<svg viewBox="0 0 470 340" role="img" aria-label="Schrägbild der quadratischen Pyramide ABCD mit Spitze S und Lichtquelle L" style="width:100%;max-width:480px;height:auto;background:#fbf7ef;border-radius:8px">
  <defs>
    <marker id="ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#7a7163"/></marker>
  </defs>
  <line x1="180" y1="230" x2="180" y2="60"  stroke="#7a7163" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="180" y1="230" x2="420" y2="230" stroke="#7a7163" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="180" y1="230" x2="70"  y2="320" stroke="#7a7163" stroke-width="1.5" marker-end="url(#ah)"/>
  <text x="166" y="58"  font-size="13" fill="#7a7163">x₃</text>
  <text x="424" y="234" font-size="13" fill="#7a7163">x₂</text>
  <text x="58"  y="326" font-size="13" fill="#7a7163">x₁</text>
  <polygon points="180,230 114,290 228,290 294,230" fill="#3a5a9c" fill-opacity="0.08" stroke="#3a5a9c" stroke-width="1.6"/>
  <line x1="114" y1="290" x2="204" y2="100" stroke="#3a5a9c" stroke-width="1.6"/>
  <line x1="228" y1="290" x2="204" y2="100" stroke="#3a5a9c" stroke-width="1.6"/>
  <line x1="294" y1="230" x2="204" y2="100" stroke="#3a5a9c" stroke-width="1.6"/>
  <line x1="180" y1="230" x2="204" y2="100" stroke="#3a5a9c" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.7"/>
  <line x1="204" y1="260" x2="204" y2="100" stroke="#d98324" stroke-width="1.3" stroke-dasharray="3 3"/>
  <circle cx="204" cy="260" r="2.5" fill="#d98324"/>
  <text x="210" y="250" font-size="12" fill="#d98324">M (Mitte), Höhe 4</text>
  <circle cx="180" cy="230" r="3" fill="#3a5a9c"/><text x="158" y="224" font-size="12" fill="#26324a">A(0|0|0)</text>
  <circle cx="114" cy="290" r="3" fill="#3a5a9c"/><text x="60"  y="305" font-size="12" fill="#26324a">B(3|0|0)</text>
  <circle cx="228" cy="290" r="3" fill="#3a5a9c"/><text x="212" y="308" font-size="12" fill="#26324a">C(3|3|0)</text>
  <circle cx="294" cy="230" r="3" fill="#3a5a9c"/><text x="300" y="224" font-size="12" fill="#26324a">D(0|3|0)</text>
  <circle cx="204" cy="100" r="3.5" fill="#3a5a9c"/><text x="212" y="98" font-size="13" fill="#26324a" font-weight="bold">S(1,5|1,5|4)</text>
  <text x="406" y="82" font-size="15" fill="#b03a2e">✦</text><text x="400" y="81" font-size="12" fill="#b03a2e" text-anchor="end">L (Lichtquelle)</text>
</svg>
<figcaption>Schematisches Schrägbild — die Spitze \( S \) liegt senkrecht über der Mitte \( M \) der Grundfläche.</figcaption>
</figure>

### AB I — Koordinaten von \( S \), Volumen, Seitenfläche

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Koordinaten der Spitze \( S \).** „Senkrechte Pyramide" heißt: Die Spitze liegt **lotrecht über dem
Mittelpunkt** der Grundfläche. Der Mittelpunkt \( M \) des Quadrats ist der Durchschnitt der
gegenüberliegenden Ecken:

\[ M = \tfrac12\big(A + C\big) = \tfrac12\big((0,0,0)+(3,3,0)\big) = (1{,}5\,|\,1{,}5\,|\,0). \]

Die Höhe \( 4 \) wird in \( x_3 \)-Richtung aufgesetzt:

\[ S = (1{,}5\,|\,1{,}5\,|\,4). \]

**Pyramidenvolumen** mit \( V = \tfrac13\cdot G\cdot h \). Die Grundfläche ist ein Quadrat mit
Seitenlänge \( 3 \), also \( G = 3\cdot 3 = 9 \), und \( h=4 \):

\[ V = \tfrac13\cdot 9\cdot 4 = 12. \]

**Koordinatengleichung einer Seitenfläche** (Beispiel: die Fläche durch \( B,\,C,\,S \)). Man braucht
einen **Normalenvektor** \( \vec n \), der auf zwei Kantenvektoren der Fläche senkrecht steht:

\[ \overrightarrow{BC} = \begin{pmatrix}0\\3\\0\end{pmatrix},\qquad
   \overrightarrow{BS} = \begin{pmatrix}-1{,}5\\1{,}5\\4\end{pmatrix}. \]

Das **Kreuzprodukt** liefert \( \vec n \):

\[ \vec n = \overrightarrow{BC}\times\overrightarrow{BS}
   = \begin{pmatrix}3\cdot4 - 0\cdot1{,}5\\ 0\cdot(-1{,}5)-0\cdot4\\ 0\cdot1{,}5-3\cdot(-1{,}5)\end{pmatrix}
   = \begin{pmatrix}12\\0\\4{,}5\end{pmatrix}
   \;\parallel\; \begin{pmatrix}8\\0\\3\end{pmatrix}. \]

Einsetzen des Punktes \( B(3|0|0) \) bestimmt die rechte Seite: \( 8\cdot3 + 3\cdot0 = 24 \). Also

\[ E_{BCS}:\quad 8x_1 + 3x_3 = 24. \]

<details><summary>Haltung dahinter: Was sind Vektor, Ebene und Normalenvektor? (ganz von vorn)</summary>

Schritt für Schritt, ohne Vorwissen.

**Punkt und Vektor.** Ein **Punkt** ist ein Ort im Raum, angegeben durch drei Zahlen
\( (x_1\mid x_2\mid x_3) \). Ein **Vektor** ist ein **Pfeil** — eine Bewegung von einem Punkt zu einem
anderen, mit Richtung und Länge. Den Pfeil vom Punkt \( B \) zum Punkt \( C \) schreibt man
\( \overrightarrow{BC} \) und rechnet ihn als „Ziel minus Start" aus: \( C - B \). Beispiel:
\( \overrightarrow{BC} = (3,3,0) - (3,0,0) = (0,3,0) \) — also „3 Schritte in \( x_2 \)-Richtung".

**Ebene.** Eine **Ebene** ist eine vollkommen flache, unendlich ausgedehnte Fläche (wie eine
unendliche Tischplatte). Eine Seitenfläche der Pyramide liegt in so einer Ebene. Eine
**Koordinatengleichung** der Ebene ist eine Regel der Form \( n_1 x_1 + n_2 x_2 + n_3 x_3 = d \), die
**genau die Punkte beschreibt, die auf der Ebene liegen** — setzt man einen Ebenenpunkt ein, stimmt die
Gleichung; setzt man einen Punkt daneben ein, stimmt sie nicht.

**Normalenvektor.** Das ist ein Pfeil, der **senkrecht auf der Ebene steht** — wie ein Fahnenmast, der
gerade aus dem Boden ragt. Sein Nutzen: Die drei Zahlen des Normalenvektors sind **genau** die
Koeffizienten \( n_1, n_2, n_3 \) in der Ebenengleichung. Kennt man den Normalenvektor und einen Punkt
der Ebene, hat man die ganze Gleichung.

<details><summary>Wieso liefert das „Kreuzprodukt" einen senkrechten Pfeil?</summary>

Das **Kreuzprodukt** zweier Vektoren ist eine feste Rechenvorschrift, die als Ergebnis einen **neuen
Pfeil** liefert, der auf **beiden** Ausgangspfeilen senkrecht steht. Genau das brauchen wir: Wir nehmen
zwei Pfeile, die **in** der Seitenfläche liegen (\( \overrightarrow{BC} \) und
\( \overrightarrow{BS} \)), und das Kreuzprodukt gibt uns automatisch einen Pfeil senkrecht zur Fläche
— den Normalenvektor. Das Rechenschema (welche Zahlen man wie multipliziert und subtrahiert) steht im
[Werkzeugkasten Geometrie](konv-90-werkzeugkasten-geometrie.html#kreuzprodukt).

Dass man am Ende \( (12,0,4{,}5) \) auf \( (8,0,3) \) **kürzt**, ändert nur die *Länge* des Pfeils,
nicht seine *Richtung* — und nur die Richtung zählt für die Ebene. Kürzen macht die Zahlen handlicher.

</details>

<details><summary>Probe: so prüfst du eine Ebenengleichung sofort</summary>

Eine Ebenengleichung ist richtig, wenn **alle drei** definierenden Punkte sie erfüllen. Einsetzen:
\( C(3|3|0): 8\cdot3+3\cdot0 = 24 \) ✓; \( S(1{,}5|1{,}5|4): 8\cdot1{,}5 + 3\cdot4 = 12+12 = 24 \) ✓.
Dass \( x_2 \) in der Gleichung **fehlt**, ist kein Fehler: Die Fläche \( BCS \) ist parallel zur
\( x_2 \)-Achse, deshalb taucht \( x_2 \) nicht auf. Diese Punktprobe ist deine schnelle
Selbstkontrolle.

</details>
</details>

<details><summary>Haltung dahinter: Warum liegt \( S \) über dem Mittelpunkt, und woher die Volumenformel?</summary>

**„Senkrechte" Pyramide.** Stell dir einen Zeltmast vor, der genau in der Mitte des quadratischen
Zeltbodens **gerade nach oben** steht. Die Zeltspitze ist dann lotrecht über der Bodenmitte. Genau das
meint „senkrechte Pyramide". Deshalb hat \( S \) dieselben \( x_1 \)- und \( x_2 \)-Werte wie die Mitte
\( M \) (nämlich \( 1{,}5 \) und \( 1{,}5 \)) und obendrauf die Höhe \( 4 \) in \( x_3 \)-Richtung.

**Mittelpunkt als Durchschnitt.** Den Mittelpunkt einer Strecke findet man, indem man die beiden
Endpunkte addiert und halbiert (der „Durchschnitt" zweier Orte liegt genau dazwischen). Beim Quadrat
nimmt man zwei **gegenüberliegende** Ecken, hier \( A \) und \( C \): \( \tfrac12(A+C) \).

**Volumenformel \( V=\tfrac13\,G\,h \).** Eine Pyramide füllt genau **ein Drittel** des Quaders (der
„Schachtel") aus, der dieselbe Grundfläche \( G \) und dieselbe Höhe \( h \) hat. Daher das
\( \tfrac13 \). Hier: Grundfläche \( G = 3\cdot 3 = 9 \) (Quadrat mit Seite 3), Höhe \( h=4 \), also
\( V = \tfrac13 \cdot 9 \cdot 4 = 12 \).

</details>
</details>

### AB II — Gleichschenkligkeit, Oberfläche, Neigungswinkel

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Gleichschenkligkeit eines Seitendreiecks** (z. B. \( BCS \)). Wir vergleichen die beiden
Schenkellängen \( |\overline{SB}| \) und \( |\overline{SC}| \):

\[ \overrightarrow{SB} = \begin{pmatrix}1{,}5\\-1{,}5\\-4\end{pmatrix},\quad
   |\overline{SB}| = \sqrt{1{,}5^2+1{,}5^2+4^2} = \sqrt{20{,}5}; \]
\[ \overrightarrow{SC} = \begin{pmatrix}1{,}5\\1{,}5\\-4\end{pmatrix},\quad
   |\overline{SC}| = \sqrt{1{,}5^2+1{,}5^2+4^2} = \sqrt{20{,}5}. \]

Beide sind gleich lang, also ist das Dreieck \( BCS \) **gleichschenklig** (Spitze \( S \)).

<details><summary>Haltung dahinter: Was heißt „gleichschenklig", und wie misst man eine Länge im Raum?</summary>

**Gleichschenklig** heißt: Ein Dreieck hat **zwei gleich lange Seiten** (die „Schenkel"). Es genügt
also zu zeigen, dass zwei Seiten dieselbe Länge haben.

**Länge eines Pfeils im Raum.** Die Länge \( |\overrightarrow{SB}| \) eines Vektors ist der **Abstand**
zwischen Start und Ziel. Man bekommt sie mit dem **Satz des Pythagoras**, nur in drei Dimensionen: Man
**quadriert jede der drei Zahlen, addiert sie und zieht die Wurzel**:

\[ |\;(a,b,c)\;| = \sqrt{a^2+b^2+c^2}. \]

Für \( \overrightarrow{SB} = (1{,}5,\,-1{,}5,\,-4) \): \( 1{,}5^2 = 2{,}25 \), \( (-1{,}5)^2 = 2{,}25 \)
(Minus mal Minus wird Plus!), \( (-4)^2 = 16 \). Summe \( 2{,}25+2{,}25+16 = 20{,}5 \), also Länge
\( \sqrt{20{,}5} \). Für \( \overrightarrow{SC} \) kommt durch das gleiche Rechnen exakt dasselbe
heraus — die beiden Seiten sind gleich lang.

<details><summary>Warum sind sogar alle vier Seitenkanten gleich lang?</summary>

Weil die Spitze **senkrecht über dem Mittelpunkt** sitzt, ist sie von allen vier Eckpunkten gleich weit
entfernt — wie der Mittelpunkt eines Kreises von allen Randpunkten. Die vier Seitenkanten
\( SA, SB, SC, SD \) sind deshalb alle gleich lang. Damit ist **jedes** der vier Seitendreiecke
gleichschenklig, und die ganze Pyramide ist gleichmäßig um ihre Höhe gebaut. Das darf man im Gespräch so
begründen — oft schneller als das Nachrechnen.

</details>
</details>

**Verfahren für die Oberfläche.** Die Oberfläche besteht aus der **quadratischen Grundfläche** und
**vier kongruenten** (deckungsgleichen) Seitendreiecken:

\[ O = G + 4\cdot A_{\triangle}. \]

Für ein Seitendreieck braucht man die **Höhe des Dreiecks** \( h_s \) (von \( S \) auf die Mitte einer
Grundkante). Mitte von \( BC \) ist \( M_{BC}(3\,|\,1{,}5\,|\,0) \), und

\[ h_s = |\overline{S\,M_{BC}}| = \sqrt{(3-1{,}5)^2 + 0^2 + 4^2} = \sqrt{1{,}5^2+4^2} = \sqrt{18{,}25}. \]

Damit \( A_{\triangle} = \tfrac12\cdot 3\cdot \sqrt{18{,}25} \) und

\[ O = 9 + 4\cdot\tfrac12\cdot 3\cdot \sqrt{18{,}25} = 9 + 6\sqrt{18{,}25}. \]

<details><summary>Haltung dahinter: Warum diese Bausteine für die Oberfläche?</summary>

Die **Oberfläche** ist die Summe aller Flächen, die den Körper „außen" begrenzen — wie viel Papier man
bräuchte, um die Pyramide einzupacken. Eine quadratische Pyramide hat **fünf** Außenflächen: unten das
**Quadrat** (Grundfläche \( G \)) und ringsum **vier gleiche Dreiecke**.

Die Fläche eines Dreiecks ist \( \tfrac12 \cdot \text{Grundseite} \cdot \text{Höhe} \). Die Grundseite
ist eine Quadratkante (\( =3 \)). Die **Höhe des Dreiecks** \( h_s \) ist *nicht* die Pyramidenhöhe,
sondern die Strecke von der Spitze \( S \) **senkrecht hinunter zur Mitte der Grundkante**. Diese misst
man wieder als Pfeillänge (Pythagoras): von \( S(1{,}5|1{,}5|4) \) zur Kantenmitte \( M_{BC}(3|1{,}5|0) \)
ergibt \( \sqrt{18{,}25} \). Vier solche Dreiecke plus das Quadrat ergeben \( O = 9 + 6\sqrt{18{,}25} \).

</details>

**Winkel zwischen Grund- und Seitenfläche.** Anschaulich über das **rechtwinklige Dreieck** aus
Pyramidenhöhe \( h=4 \) (senkrecht) und dem halben Grundkanten-Abstand vom Mittelpunkt
\( \tfrac{3}{2}=1{,}5 \) (waagerecht). Der Neigungswinkel \( \varphi \) erfüllt

\[ \tan\varphi = \frac{h}{1{,}5} = \frac{4}{1{,}5} = \frac{8}{3}\;\;\Longrightarrow\;\;
   \varphi = \arctan\!\frac{8}{3} \approx 69{,}4^\circ. \]

<details><summary>Haltung dahinter: Was ist der „Tangens", und woher kommt das rechtwinklige Dreieck?</summary>

**Winkel zwischen zwei Flächen** misst man dort, wo sie zusammenstoßen — wie weit man die eine Fläche
„aufklappen" muss, um zur anderen zu kommen (wie der Öffnungswinkel eines Buchdeckels gegen den Tisch).

Man baut sich ein passendes **rechtwinkliges Dreieck**: Lote von der Spitze \( S \) senkrecht hinunter
zum Grundflächen-Mittelpunkt \( M \) (das ist die Pyramidenhöhe \( h=4 \)) und von \( M \) waagerecht
zur Mitte einer Grundkante (Strecke \( 1{,}5 \)). Diese beiden stehen senkrecht aufeinander; die
schräge Seitenfläche schließt mit dem Boden genau den Winkel \( \varphi \) an dieser Ecke ein.

**Tangens.** In einem rechtwinkligen Dreieck verbindet der Tangens den Winkel mit zwei Seiten:
\( \tan(\text{Winkel}) = \dfrac{\text{Gegenkathete}}{\text{Ankathete}} \) — also „gegenüberliegende Seite
geteilt durch anliegende Seite". Hier ist die Höhe \( 4 \) gegenüber dem Winkel, die Strecke \( 1{,}5 \)
liegt am Winkel an: \( \tan\varphi = \tfrac{4}{1{,}5} = \tfrac{8}{3} \). Den Winkel selbst holt man mit
der Umkehrung \( \arctan \) (auf dem Rechner „\( \tan^{-1} \)") zurück: \( \varphi \approx 69{,}4^\circ \).
(In der hilfsmittelfreien Prüfung genügt es, **\( \tan\varphi = \tfrac{8}{3} \)** anzugeben und zu
erklären — der Zahlenwert ist Nebensache.)

</details>
</details>

### AB III — Halbierung, Innen-Test, Schattenwurf

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Verfahren anzeigen</summary>

Diese Aspekte verlangen vor allem **beschreiben und begründen**, nicht langes Rechnen.

**Ebenen, die das Volumen halbieren.** Jede Ebene, die durch die **Spitze \( S \)** und durch den
**Mittelpunkt \( M \)** der Grundfläche geht (also die Höhe enthält) und die Grundfläche in zwei
flächengleiche Hälften schneidet, zerlegt die Pyramide in zwei volumengleiche Teile — z. B. die Ebene
durch \( S \) und die Mitten zweier gegenüberliegender Grundkanten oder die Ebene durch \( S \) und eine
Diagonale der Grundfläche.

**Liegt ein Punkt \( P \) im Inneren?** Man beschreibt die Pyramide durch ihre **begrenzenden Ebenen**
(Grundfläche + vier Seitenflächen). \( P \) liegt im Inneren, wenn er bei **jeder** dieser Ebenen auf
derselben Seite liegt wie das Pyramideninnere. Das prüft man, indem man \( P \) in jede Ebenengleichung
einsetzt und das **Vorzeichen** mit dem eines bekannten Innenpunkts (etwa \( M \)) vergleicht.

**Schattenwurf.** Die punktförmige Lichtquelle \( L \) wirft den Schatten als **Zentralprojektion** auf
die Grundebene (\( x_3=0 \)): Für die Spitze \( S \) bildet man die **Gerade durch \( L \) und \( S \)**
und bestimmt deren **Durchstoßpunkt** mit der Ebene \( x_3=0 \). Dieser Durchstoßpunkt ist der Schatten
von \( S \).

<details><summary>Haltung dahinter: die drei Ideen in Alltagssprache</summary>

- **Halbieren.** Eine Ebene, die durch die Spitze **und** die Bodenmitte geht, schneidet die Pyramide
  symmetrisch durch — beide Hälften haben dieselbe Höhe und gleich große Grundstücke, also nach
  \( V=\tfrac13 G h \) dasselbe Volumen. Bild: einen quadratischen Pudding mittig senkrecht
  durchschneiden — beide Stücke gleich groß.
- **Innen oder außen?** Eine Fläche teilt den Raum in zwei Seiten. Setzt man einen Punkt in die
  Ebenengleichung ein, verrät das **Vorzeichen** (plus oder minus, größer oder kleiner als \( d \)), auf
  welcher Seite er liegt. Ein Punkt ist im Inneren, wenn er bei **allen fünf** Begrenzungsflächen auf
  derselben Seite liegt wie ein sicher innen liegender Vergleichspunkt.
- **Schatten.** Licht von einem Punkt strahlt geradlinig. Der Schatten eines Eckpunkts liegt dort, wo
  der Lichtstrahl von \( L \) durch diesen Eckpunkt auf den Boden trifft. Mathematisch: Gerade durch
  \( L \) und den Punkt, dann Schnittpunkt mit dem Boden \( x_3=0 \).

<details><summary>Hinweis: ohne konkrete Koordinaten von \( L \) bleibt es beim Verfahren</summary>

Das Aufgabenbeispiel gibt \( L \) nur als Lage im Bild an, **ohne** Zahlenwerte. Deshalb ist hier nur
das **Vorgehen** zu beschreiben. Sobald \( L \) mit Koordinaten gegeben wäre, etwa
\( L(l_1|l_2|l_3) \), setzt man \( \vec x = L + t\,(S-L) \), löst die dritte Zeile
\( l_3 + t\,(4-l_3) = 0 \) nach \( t \) auf und setzt \( t \) in die ersten beiden Zeilen ein — das
liefert den Schattenpunkt von \( S \).

</details>
</details>
</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Teilaufgabe, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen
kannst. Du musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Analysis) aufklappen</summary>

- **a) Zuordnung.** Gut ist jede Antwort, die die **Klassen an ihrer Gestalt** festmacht: e-Funktion =
  „bleibt positiv, nähert sich der Achse"; Polynom = „Nullstellen, läuft ins Unendliche"; trig =
  „schwingt periodisch". *Rückfrage, falls nur zugeordnet ohne Begründung:* „Woran genau erkennen Sie
  die Exponentialfunktion?"
- **b) Funktionsterm.** Erwartet: **Nullstellen ablesen → Linearfaktoren**, dann **ein Punkt** (meist
  \( f(0) \)) für den Vorfaktor; Ergebnis \( f(x)=-\tfrac16(x-2)(x-3)(x+4) \). *Rückfrage:* „Warum
  brauchen Sie überhaupt noch den Faktor \( -\tfrac16 \)?" (Antwort: richtige Höhe **und** Spiegelung.)
- **c) Fläche.** Erwartet: **an den Nullstellen trennen**, Beträge addieren, Minus vor dem Stück unter
  der Achse. *Rote Flagge:* ein einziges Integral \( \int_{-4}^{3} \) ohne Trennen. *Rückfrage:*
  „Was misst ein Integral, wenn der Graph unter der Achse liegt?"
- **d) Integralgleichungen.** Erwartet: Stammfunktion \( e^{-x} \), sauberes Auflösen mit \( \ln \) →
  \( a=-\ln 3 \); beim zweiten Teil **irgendein** passendes Beispiel mit Probe. *Rückfrage:* „Können
  Sie Ihr \( j \) durch Einsetzen bestätigen?"

</details>

<details><summary>Leitfaden Teil 2 (Geometrie) aufklappen</summary>

- **\( S \), Volumen, Seitenfläche.** Erwartet: \( S \) über **Mittelpunkt + Höhe**
  \( (1{,}5|1{,}5|4) \); \( V=\tfrac13\cdot9\cdot4=12 \); Ebene über **Normalenvektor** (Kreuzprodukt)
  + Punktprobe. *Rückfrage:* „Warum liegt \( S \) genau über dem Mittelpunkt?" (Antwort: „senkrechte"
  Pyramide.)
- **Gleichschenkligkeit / Oberfläche / Winkel.** Erwartet: zwei Kantenlängen gleich (\( \sqrt{20{,}5} \));
  Oberfläche = Quadrat + 4 Dreiecke; Winkel über das **rechtwinklige Dreieck** Höhe/\( 1{,}5 \),
  \( \tan\varphi=\tfrac{8}{3} \). *Rückfrage:* „Welches kleine Dreieck benutzen Sie für den
  Neigungswinkel?"
- **AB III.** Hier zählt **sauberes Erklären**: Halbierung durch eine Ebene **durch die Höhe**;
  Innen-Test über **Vorzeichen in allen Begrenzungsebenen**; Schatten als **Gerade \( LS \) ∩
  Grundebene**. *Hinweis für dich:* Für den Schatten fehlen Zahlen zu \( L \) — ein **beschriebenes
  Verfahren** ist hier die volle Antwort.

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Woran erkennst du in einem Satz, ob ein Graph exponentiell, ganzrational oder trigonometrisch ist?
- Wie kommst du von den Nullstellen eines Graphen zu seinem Funktionsterm — und was fehlt dann noch?
- Warum musst du bei der Fläche an den Nullstellen trennen?
- Wie bestimmst du die Spitze \( S \) einer senkrechten Pyramide, und warum?
- Welches rechtwinklige Dreieck liefert den Winkel zwischen Grund- und Seitenfläche?
