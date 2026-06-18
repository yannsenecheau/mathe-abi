# Integral in Sachzusammenhängen

Léona, in diesem Kapitel geht es um die wohl wichtigste Anwendung des Integrals in der mündlichen
Prüfung: Du hast eine **Änderungsrate** gegeben (wie schnell sich etwas ändert) und sollst daraus den
**Bestand** oder die **Gesamtänderung** rekonstruieren. Das klingt abstrakt, ist aber im Kern eine
einzige Idee, die du sicher beherrschen solltest. Wir bauen sie Schritt für Schritt auf — und du
rechnest alles **per Hand**, denn die Prüfung ist hilfsmittelfrei.

<span class="tag tag-ok">Kern-Thema Analysis · Anforderungsbereich AB II</span>

## Die Grundidee: vom Tempo zur Menge

Stell dir vor, jemand sagt dir nur, **wie schnell** sich etwas verändert — wie schnell Wasser in ein
Becken fließt, wie schnell ein Auto fährt, wie schnell sich eine Population vermehrt. Diese „Wie
schnell"-Größe heißt **Änderungsrate**. Die Frage lautet dann: Wie viel hat sich **insgesamt**
angesammelt oder verändert?

Die Antwort gibt das Integral. Ist \( r(t) \) die Änderungsrate einer Größe \( B \) (also
\( r(t) = B'(t) \)), dann ist

\[ \int_{a}^{b} r(t)\,dt \;=\; B(b) - B(a) \;=\; \text{Gesamtänderung von } B \text{ zwischen } a \text{ und } b. \]

Das ist die **Bedeutung des Integrals als rekonstruierte Gesamtänderung**: Du summierst lauter winzige
Änderungen \( r(t)\,dt \) auf und bekommst, wie viel sich von \( a \) bis \( b \) zusammengenommen
getan hat.

<details><summary>Haltung dahinter: warum überhaupt funktioniert das?</summary>

Das **Prinzip**: Über ein winziges Zeitstückchen \( dt \) ändert sich die Größe näherungsweise um
„Rate mal Zeit", also \( r(t)\,dt \). Beispiel: Fließt Wasser gerade mit \( 5\,\tfrac{\text{m}^3}{\text{h}} \)
und betrachtest du \( dt = 0{,}1\,\text{h} \), kommen \( 5 \cdot 0{,}1 = 0{,}5\,\text{m}^3 \) dazu. Das
Integral summiert all diese Stückchen über das ganze Intervall — daraus wird die Gesamtmenge.

<details><summary>Begründung: der Zusammenhang zum Hauptsatz</summary>

Wenn \( r = B' \), dann ist \( B \) eine **Stammfunktion** von \( r \). Der **Hauptsatz der Differential-
und Integralrechnung** sagt: \( \int_a^b r(t)\,dt = \big[B(t)\big]_a^b = B(b) - B(a) \). Genau das ist
die Differenz der Bestände — also die Gesamtänderung. Das Integral „macht das Ableiten rückgängig".

<details><summary>Annahme/Axiom: was setzen wir voraus?</summary>

Damit der Hauptsatz greift, muss \( r \) auf \( [a,b] \) **stetig** sein (keine Sprünge), und \( B \)
muss eine differenzierbare Funktion mit \( B' = r \) sein. In allen Schulaufgaben des Basisfachs ist
das erfüllt; die Ratenfunktionen sind dort durchweg „brave" Funktionen (Polynome, einfache Brüche).
Diese Voraussetzung musst du in der Prüfung nicht beweisen, aber du solltest wissen, **dass** es eine
gibt.

</details>
</details>
</details>

Eine häufige **Falle**: Verwechsle nicht die Rate mit dem Bestand. \( r(2) = 5 \) heißt „im Moment
\( t = 2 \) fließt es mit Tempo 5" — es heißt **nicht**, dass schon 5 da sind. Wie viel da ist,
verrät erst das Integral.

## Vom Bestand zur absoluten Menge: die Konstante

Mit dem Integral bekommst du die **Änderung** des Bestands. Willst du den **absoluten Bestand** zu
einem Zeitpunkt wissen, brauchst du noch einen **Startwert** (Anfangsbestand). Dann gilt

\[ B(t) \;=\; B(0) \;+\; \int_{0}^{t} r(s)\,ds. \]

In Worten: aktueller Bestand = Anfangsbestand + alles, was seit dem Start dazugekommen (oder
abgeflossen) ist.

<details><summary>Haltung dahinter: warum die Integrationsvariable umbenannt ist</summary>

Ich habe im Integral \( s \) statt \( t \) geschrieben, weil \( t \) schon die **obere Grenze** ist.
Dieselbe Buchstabe für Grenze und Laufvariable zu nehmen ist mathematisch unsauber. In der Prüfung
darfst du es meist locker sehen, aber wenn du sauber \( \int_0^t r(s)\,ds \) schreibst, zeigt das
Verständnis. Inhaltlich ist \( s \) nur die „Laufzeit" innerhalb des Integrals.

</details>

## Einheiten: der heimliche Punktelieferant

Einheiten werden in der mündlichen Prüfung gern abgefragt — sie sind leicht und zeigen, ob du die
Sachsituation **verstanden** hast. Die Regel ist mechanisch:

\[ [\,\text{Integralwert}\,] \;=\; [\,\text{Rate}\,] \cdot [\,\text{Variable}\,]. \]

Die Einheit des Integrals ist also **Rate-Einheit mal Einheit der Integrationsvariablen**, weil du im
Integral „Rate mal \( dt \)" aufsummierst.

| Rate \( r(t) \) | Variable | Integral \( \int r\,dt \) |
|---|---|---|
| \( \tfrac{\text{m}^3}{\text{h}} \) (Zufluss) | \( \text{h} \) (Zeit) | \( \text{m}^3 \) (Volumen) |
| \( \tfrac{\text{m}}{\text{s}} \) (Geschwindigkeit) | \( \text{s} \) (Zeit) | \( \text{m} \) (Weg) |
| \( \tfrac{\text{Stück}}{\text{Tag}} \) (Produktionsrate) | \( \text{Tag} \) | \( \text{Stück} \) |

<details><summary>Haltung dahinter: die Einheiten „kürzen" wie Zahlen</summary>

Schreib die Einheit als Bruch und kürze. Beispiel Geschwindigkeit:
\( \tfrac{\text{m}}{\text{s}} \cdot \text{s} = \text{m} \) — die Sekunden heben sich weg, übrig bleibt
Meter, also ein **Weg**. Das ist kein Zufall, sondern spiegelt die Bedeutung: Tempo (Meter pro
Sekunde) über eine Zeitspanne (Sekunden) ergibt eine zurückgelegte Strecke (Meter). Wenn du die
Einheit nicht „auskürzen" kannst, stimmt meist deine Deutung der Aufgabe nicht.

</details>

## Sachaufgabe 1: Wasserbecken mit wechselndem Zufluss

<span class="tag tag-ok">Anforderungsbereich AB II</span>

In ein Becken fließt Wasser, dann sickert es wieder heraus. Die **Zuflussrate** wird modelliert durch

\[ r(t) = 6 - 2t \quad \left(\text{in } \tfrac{\text{m}^3}{\text{h}}, \; 0 \le t \le 4\right). \]

Positives \( r \) bedeutet Zufluss, negatives \( r \) bedeutet Abfluss. Zu Beginn sind \( 5\,\text{m}^3 \)
im Becken.

**Aufgabe (a):** Wie viel Wasser ist nach 3 Stunden **insgesamt zugeflossen**?
**Aufgabe (b):** Wie groß ist die **Gesamtänderung** des Wasserstands über die volle Zeit \( [0,4] \),
und wie viel Wasser ist dann im Becken?

### Lösung Teil (a) — reiner Zufluss bis t = 3

<span class="tag tag-ok">AB II</span>

Bis \( t = 3 \) ist \( r(t) = 6 - 2t \ge 0 \) (denn \( 6 - 2t = 0 \) erst bei \( t = 3 \)). Also fließt
hier nur zu, und die zugeflossene Menge ist das Integral der Rate:

\[ \int_{0}^{3} (6 - 2t)\,dt = \Big[\,6t - t^2\,\Big]_{0}^{3} = (18 - 9) - (0 - 0) = 9 \;\text{m}^3. \]

Es sind also **9 m³ zugeflossen**.

<details><summary>Schritt für Schritt: wie ich die Stammfunktion bilde</summary>

Ich brauche eine Funktion \( R \) mit \( R'(t) = 6 - 2t \). Term für Term mit der **Potenzregel für
Stammfunktionen** (\( t^n \to \tfrac{1}{n+1}t^{n+1} \)):

- aus \( 6 \) wird \( 6t \) (denn \( (6t)' = 6 \)),
- aus \( -2t \) wird \( -2 \cdot \tfrac{1}{2}t^2 = -t^2 \) (denn \( (-t^2)' = -2t \)).

Also \( R(t) = 6t - t^2 \). Eine additive Konstante darf ich weglassen, weil sie sich beim Einsetzen
der Grenzen ohnehin weghebt.

<details><summary>Haltung dahinter: warum darf die Konstante weg?</summary>

Beim bestimmten Integral rechne ich \( R(b) - R(a) \). Hätte ich \( R(t) + C \) genommen, stünde da
\( (R(b)+C) - (R(a)+C) = R(b) - R(a) \) — das \( C \) fällt raus. Bei der **Rekonstruktion des
absoluten Bestands** (Teil b) ist es anders: dort ist der „Startwert" \( B(0) = 5 \) genau diese
Information, die ich **nicht** weglassen darf.

</details>
</details>

<details><summary>Falle: was ist hier mit „Fläche" gemeint?</summary>

Weil \( r \) auf \( [0,3] \) nicht negativ ist, stimmt das Integral hier mit dem **Flächeninhalt**
zwischen Kurve und \( t \)-Achse überein. Das ist nur deshalb so, weil nichts unter die Achse geht.
Sobald die Rate negativ wird (Teil b), darfst du Integral und Flächeninhalt **nicht** mehr
gleichsetzen — dazu gleich mehr.

</details>

### Lösung Teil (b) — Gesamtänderung über das ganze Intervall

<span class="tag tag-ok">AB II</span>

Die **Gesamtänderung** des Bestands ist das Integral der Rate über das volle Intervall — egal welches
Vorzeichen die Rate hat:

\[ \int_{0}^{4} (6 - 2t)\,dt = \Big[\,6t - t^2\,\Big]_{0}^{4} = (24 - 16) - 0 = 8 \;\text{m}^3. \]

Der Wasserstand hat sich über \( [0,4] \) also **um \( +8\,\text{m}^3 \)** geändert. Mit dem
Anfangsbestand \( B(0) = 5 \) sind nach 4 Stunden im Becken:

\[ B(4) = B(0) + \int_{0}^{4} r(t)\,dt = 5 + 8 = 13 \;\text{m}^3. \]

<details><summary>Haltung dahinter: warum das Integral hier kleiner ist als in Teil (a)</summary>

In Teil (a) kamen über \( [0,3] \) ganze \( 9\,\text{m}^3 \) zusammen. Über das ganze Intervall sind
es aber nur \( 8\,\text{m}^3 \). Der Grund: Ab \( t = 3 \) wird \( r(t) = 6 - 2t \) **negativ** — es
fließt wieder ab. Auf \( [3,4] \) gilt

\[ \int_{3}^{4} (6 - 2t)\,dt = \Big[\,6t - t^2\,\Big]_{3}^{4} = (24 - 16) - (18 - 9) = 8 - 9 = -1 \;\text{m}^3, \]

es geht also \( 1\,\text{m}^3 \) wieder verloren. Das Integral über \( [0,4] \) verrechnet Zufluss und
Abfluss automatisch: \( 9 + (-1) = 8 \). Genau das ist die Stärke der Rekonstruktion über das Integral
— **Vorzeichen erledigen die Bilanz für dich**.

<details><summary>Begründung: Gesamtänderung vs. „insgesamt geflossenes Wasser"</summary>

Würde dich jemand fragen, wie viel Wasser **physisch insgesamt durch das Becken bewegt** wurde
(Zufluss-Betrag plus Abfluss-Betrag), müsstest du die Beträge addieren: \( 9 + 1 = 10\,\text{m}^3 \).
Das wäre der **Flächeninhalt** \( \int_0^4 |6-2t|\,dt \). Die **Gesamtänderung des Bestands** ist
dagegen die Bilanz \( 8\,\text{m}^3 \). In der Prüfung ist die Frage „Gesamtänderung" / „wie viel ist
am Ende da" fast immer die **vorzeichenbehaftete** — das normale Integral. Lies die Frage genau.

</details>
</details>

Der Graph zeigt die Rate \( r(t) = 6 - 2t \). Die Fläche **über** der Achse (grün, bis \( t = 3 \)) ist
der Zufluss, die Fläche **unter** der Achse (rot, ab \( t = 3 \)) der Abfluss. Die Bilanz beider ist
die Gesamtänderung.

<div class="jxgbox" id="jxg-zufluss" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-zufluss',{boundingbox:[-0.6,7,4.6,-3],axis:true,showCopyright:false,showNavigation:false});var r=function(t){return 6-2*t;};var cPos=b.create('functiongraph',[r,0,3],{strokeColor:'#2e7d4f',strokeWidth:2.5});var cNeg=b.create('functiongraph',[r,3,4],{strokeColor:'#c0392b',strokeWidth:2.5});b.create('integral',[[0,3],cPos],{fillColor:'#2e7d4f',fillOpacity:0.18,withLabel:false,curveLeft:{visible:false},curveRight:{visible:false},baseLeft:{visible:false},baseRight:{visible:false}});b.create('integral',[[3,4],cNeg],{fillColor:'#c0392b',fillOpacity:0.2,withLabel:false,curveLeft:{visible:false},curveRight:{visible:false},baseLeft:{visible:false},baseRight:{visible:false}});b.create('point',[3,0],{name:'t=3',size:2,fixed:true,color:'#d98324',label:{offset:[6,-12]}});})();</script>

## Sachaufgabe 2: vom Tempo zum Weg

<span class="tag tag-ok">Anforderungsbereich AB I–II</span>

Ein Modellfahrzeug startet bei \( t = 0 \) aus dem Stand. Seine Geschwindigkeit wird beschrieben durch

\[ v(t) = 3t^2 \quad \left(\text{in } \tfrac{\text{m}}{\text{s}}, \; t \ge 0\right). \]

**Aufgabe:** Welche Strecke legt das Fahrzeug in den ersten **2 Sekunden** zurück? Gib auch die
**Einheit** an und begründe sie.

### Lösung

<span class="tag tag-ok">AB I (Rechnung) · AB II (Deutung/Einheit)</span>

Die Geschwindigkeit ist die Änderungsrate des Weges (\( v = s' \)). Der **zurückgelegte Weg** von
\( 0 \) bis \( 2 \) ist daher das Integral der Geschwindigkeit:

\[ s = \int_{0}^{2} 3t^2 \,dt = \Big[\,t^3\,\Big]_{0}^{2} = 2^3 - 0^3 = 8 \;\text{m}. \]

Das Fahrzeug legt in 2 Sekunden **8 Meter** zurück.

<details><summary>Schritt für Schritt: Stammfunktion und Einheit</summary>

**Stammfunktion:** Ich suche \( S \) mit \( S'(t) = 3t^2 \). Mit der Potenzregel wird aus \( t^2 \) der
Term \( \tfrac{1}{3}t^3 \); der Faktor 3 hebt den Bruch auf: \( 3 \cdot \tfrac{1}{3}t^3 = t^3 \). Also
\( S(t) = t^3 \). Probe durch Ableiten: \( (t^3)' = 3t^2 = v(t) \) ✓.

**Einheit:** Die Rate ist in \( \tfrac{\text{m}}{\text{s}} \), integriert wird über die Zeit in
\( \text{s} \). Also \( \tfrac{\text{m}}{\text{s}} \cdot \text{s} = \text{m} \) — das Ergebnis ist ein
**Weg in Metern**. Genau deshalb passt „8 m" und nicht etwa „8 m/s".

<details><summary>Haltung dahinter: warum ist der Weg nicht einfach „Tempo mal Zeit"?</summary>

Bei **konstantem** Tempo wäre Weg = Tempo · Zeit. Hier ist das Tempo aber nicht konstant — es wächst
mit \( t^2 \). Anfangs ist das Fahrzeug langsam, später schnell. „Tempo mal Zeit" mit einem festen
Wert würde danebenliegen. Das Integral macht genau das Richtige: Es summiert die ständig wechselnden
Tempo-Werte über alle Zeitpunkte auf. Bei veränderlicher Rate **ist das Integral der einzige korrekte
Weg**, den Gesamteffekt zu bestimmen.

<details><summary>Probe mit gesundem Menschenverstand</summary>

Das Durchschnittstempo zwischen \( t=0 \) (\( v=0 \)) und \( t=2 \) (\( v=3\cdot 4 = 12\,\tfrac{\text{m}}{\text{s}} \))
liegt grob bei einigen \( \tfrac{\text{m}}{\text{s}} \). Über 2 Sekunden ergibt das eine Strecke in der
Größenordnung weniger Meter — \( 8\,\text{m} \) ist plausibel. Solche **Plausibilitätsprüfungen** sind
in der mündlichen Prüfung Gold wert: Sie fangen Rechenfehler ab und zeigen, dass du das Ergebnis
einordnen kannst.

</details>
</details>
</details>

## Mini-Rezept für die Prüfung

Wenn eine Aufgabe nach Bestand oder Gesamtänderung aus einer Rate fragt, gehst du immer gleich vor:

1. **Erkennen:** Ist die gegebene Funktion eine **Rate** (Tempo, Zufluss, „pro …")? Dann ist die
   gesuchte Gesamtgröße ein **Integral**.
2. **Grenzen festlegen:** von wann bis wann? Das sind \( a \) und \( b \).
3. **Stammfunktion** per Hand bilden (Potenzregel) und Probe durch Ableiten.
4. **Einsetzen:** \( \big[F(t)\big]_a^b = F(b) - F(a) \).
5. **Startwert?** Wird der **absolute Bestand** gefragt, addiere den Anfangswert \( B(0) \).
6. **Einheit** angeben (Rate-Einheit · Variablen-Einheit) und **Ergebnis im Sachkontext deuten**.
7. **Vorzeichen prüfen:** „Gesamtänderung/wie viel am Ende" → normales Integral (mit Vorzeichen);
   „insgesamt bewegte Menge / Gesamtfläche" → Beträge bzw. \( \int |r| \).

<details><summary>Der eine Satz, den du in der Prüfung sagen können solltest</summary>

„Das Integral der Änderungsrate über ein Intervall ist die Gesamtänderung des Bestands in diesem
Intervall; den absoluten Bestand bekomme ich, indem ich den Anfangsbestand addiere." Wenn du diesen
Satz frei und mit einem Beispiel sagen kannst, hast du den Kern dieses Kapitels sicher.

</details>
