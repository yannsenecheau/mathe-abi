# Aufgabe 10 — Stochastik & Analysis

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Stochastik**, **Teil 2 (Gespräch) aus der Analysis**. Die rechnerischen
und begrifflichen Schritte werden **rechnerfrei** entwickelt; nur die reinen Wahrscheinlichkeitswerte
der Normalverteilung liefert der GTR bzw. eine Tabelle (das lässt sich nicht von Hand ausrechnen, und
es wird an der jeweiligen Stelle transparent gesagt). Arbeitet die Aufgabe wie eine echte Simulation
durch — eine Person trägt vor, die andere prüft mit dem Lösungsweg und dem
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

> **Werkzeug zum Nachschlagen:** Die wiederkehrenden Stochastik-Werkzeuge (Normalverteilung,
> Erwartungswert, Standardabweichung, Binomialverteilung, Bernoulli-Kette) stehen kompakt im
> [Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html) (Anker u. a.
> [#normalverteilung](konv-91-werkzeugkasten-stochastik.html#normalverteilung),
> [#erwartungswert](konv-91-werkzeugkasten-stochastik.html#erwartungswert),
> [#binomialverteilung](konv-91-werkzeugkasten-stochastik.html#binomialverteilung),
> [#bernoulli-kette](konv-91-werkzeugkasten-stochastik.html#bernoulli-kette)). Die Analysis-Werkzeuge
> findest du in den Kapiteln [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html),
> [Grundfunktionen](kap-grundfunktionen.html) und
> [Funktionsuntersuchung](kap-funktionsuntersuchung.html).

---

## Teil 1 — Vortrag (Stochastik): Normalverteilte Gussteile

<div class="aufgabenkasten">

**Eine Firma stellt Plastikgussteile her, deren Längen um den Normwert \( 100 \) mm schwanken.
Messungen zeigen, dass die Länge \( L \) der Gussteile normalverteilt ist mit dem Erwartungswert
\( \mu = 100 \) und der Standardabweichung \( \sigma = 3{,}4 \) (alle Angaben in mm).**

**a)** Bestimme die Wahrscheinlichkeit, dass die Länge eines Gussteils weniger als \( 95 \) mm beträgt.
Gib ein anderes Ereignis an, welches dieselbe Wahrscheinlichkeit besitzt.

In der Abbildung ist der Graph der zu dieser Situation gehörenden **Glockenkurve** dargestellt.

**b)** Erläutere, wie man mit Hilfe des Graphen den Erwartungswert und die Standardabweichung von
\( L \) bestimmen könnte.

**c)** In der Abbildung ist eine Fläche grau markiert (zwischen \( 96 \) und \( 100 \)). Interpretiere
diese im Sachzusammenhang.

Die Gussteile werden als **mangelhaft** eingestuft, wenn ihre Länge um mehr als \( 5 \) mm vom Normwert
abweicht.

**d)** Begründe, dass die Wahrscheinlichkeit für eine solche Abweichung \( 14\,\% \) beträgt.

**e)** Beschreibe ein Zufallsexperiment im Sachzusammenhang und gib dazu ein Ereignis an, dessen
Wahrscheinlichkeit sich mit dem folgenden Term berechnen lässt:
\[ 0{,}14^{200} + 200\cdot 0{,}14^{199}\cdot 0{,}86 + \binom{200}{2}\cdot 0{,}14^{198}\cdot 0{,}86^{2}. \]

</div>

Hier ist die Glockenkurve mit der grau markierten Fläche aus der Aufgabe. Sie gehört zu **b)** und
**c)**.

<figure>
<div class="jxgbox" id="jxg-k10-glocke-flaeche" style="width:100%;max-width:520px;aspect-ratio:3/2"></div>
<figcaption>Glockenkurve von \( L \sim N(100;\,3{,}4) \). Der Hochpunkt liegt bei \( x=\mu=100 \), die
beiden grünen Punkte sind die <b>Wendestellen</b> bei \( x=\mu\pm\sigma = 96{,}6 \) und \( 103{,}4 \).
Grau: die Fläche zwischen \( 96 \) und \( 100 \).</figcaption>
</figure>

<script>
(function(){
var mu=100, s=3.4;
function phi(x){return Math.exp(-((x-mu)*(x-mu))/(2*s*s))/(s*Math.sqrt(2*Math.PI));}
var b=JXG.JSXGraph.initBoard('jxg-k10-glocke-flaeche',{boundingbox:[83,0.142,117,-0.022],axis:true,showCopyright:false,showNavigation:false});
var area=b.create('curve',[[],[]],{strokeWidth:0,fillColor:'#9aa7bd',fillOpacity:0.55});
area.updateDataArray=function(){var dx=[],dy=[],n=80,a=96,c=100;dx.push(a);dy.push(0);for(var i=0;i<=n;i++){var x=a+(c-a)*i/n;dx.push(x);dy.push(phi(x));}dx.push(c);dy.push(0);this.dataX=dx;this.dataY=dy;};
b.create('functiongraph',[phi,84,116],{strokeColor:'#3a5a9c',strokeWidth:2.5});
b.create('line',[[100,0],[100,phi(100)]],{straightFirst:false,straightLast:false,strokeColor:'#d98324',dash:2,strokeWidth:1.5});
b.create('text',[100.6,0.128,'x = &mu; = 100'],{fontSize:11,color:'#d98324'});
b.create('point',[96.6,phi(96.6)],{name:'',size:2,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',fixed:true});
b.create('point',[103.4,phi(103.4)],{name:'',size:2,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',fixed:true});
b.create('text',[83.6,0.092,'Wendestellen x = &mu; &plusmn; &sigma;'],{fontSize:11,color:'#3a8a5a'});
b.create('text',[95.0,-0.018,'96'],{fontSize:11,color:'#444'});
b.create('text',[99.3,-0.018,'100'],{fontSize:11,color:'#444'});
b.update();
})();
</script>

Und hier dieselbe Kurve mit den **beiden Randflächen** (Schwänzen) für \( L<95 \) und \( L>105 \). Sie
gehört zu **a)** und **d)**.

<figure>
<div class="jxgbox" id="jxg-k10-glocke-tails" style="width:100%;max-width:520px;aspect-ratio:3/2"></div>
<figcaption>Die beiden Randflächen liegen <b>spiegelbildlich</b> zum Mittelwert \( 100 \): die linke bei
\( L<95 \), die rechte bei \( L>105 \). Beide haben denselben Inhalt \( \approx 0{,}071 \).</figcaption>
</figure>

<script>
(function(){
var mu=100, s=3.4;
function phi(x){return Math.exp(-((x-mu)*(x-mu))/(2*s*s))/(s*Math.sqrt(2*Math.PI));}
var b=JXG.JSXGraph.initBoard('jxg-k10-glocke-tails',{boundingbox:[83,0.142,117,-0.022],axis:true,showCopyright:false,showNavigation:false});
function mkArea(a,c){var ar=b.create('curve',[[],[]],{strokeWidth:0,fillColor:'#c98a4a',fillOpacity:0.55});ar.updateDataArray=function(){var dx=[],dy=[],n=70;dx.push(a);dy.push(0);for(var i=0;i<=n;i++){var x=a+(c-a)*i/n;dx.push(x);dy.push(phi(x));}dx.push(c);dy.push(0);this.dataX=dx;this.dataY=dy;};return ar;}
mkArea(84,95); mkArea(105,116);
b.create('functiongraph',[phi,84,116],{strokeColor:'#3a5a9c',strokeWidth:2.5});
b.create('line',[[100,0],[100,phi(100)]],{straightFirst:false,straightLast:false,strokeColor:'#7a7163',dash:2,strokeWidth:1.2});
b.create('text',[85.0,0.052,'P(L < 95)'],{fontSize:11,color:'#a85a1a'});
b.create('text',[106.0,0.052,'P(L > 105)'],{fontSize:11,color:'#a85a1a'});
b.create('text',[93.7,-0.018,'95'],{fontSize:11,color:'#444'});
b.create('text',[104.0,-0.018,'105'],{fontSize:11,color:'#444'});
b.update();
})();
</script>

### Teilaufgabe a) — Wahrscheinlichkeit und ein gleich wahrscheinliches Ereignis

<span class="tag tag-ok">AB I — Grundkompetenz</span> <span class="tag tag-warn">AB II (zweiter Teil)</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Wahrscheinlichkeit \( P(L<95) \).** Der Wert \( 95 \) liegt \( 5 \) mm **unter** dem Mittelwert
\( 100 \). In Standardabweichungen gemessen sind das \( \tfrac{95-100}{3{,}4} = \tfrac{-5}{3{,}4}
\approx -1{,}47 \) Standardabweichungen. Den zugehörigen Flächeninhalt unter der Glockenkurve liefert
der GTR (Befehl `normalcdf`) bzw. die Tabelle der Standardnormalverteilung:

\[ P(L<95) \approx 0{,}071. \]

**Ein gleich wahrscheinliches Ereignis.** Die Glockenkurve ist **spiegelsymmetrisch** zur senkrechten
Linie durch den Mittelwert \( 100 \). Der Punkt, der zu \( 95 \) spiegelbildlich liegt, ist \( 105 \)
(beide \( 5 \) mm vom Mittelwert entfernt). Die linke Randfläche \( L<95 \) ist deshalb genauso groß wie
die rechte Randfläche \( L>105 \). Also:

\[ \boxed{\,L>105\,}\qquad\text{mit}\qquad P(L>105) = P(L<95) \approx 0{,}071. \]

<details><summary>Haltung dahinter: Was ist eine Normalverteilung, ein Erwartungswert, eine Standardabweichung? (ganz von vorn)</summary>

Zuerst die drei Grundbegriffe, ganz ohne Vorwissen.

**Zufallsgröße.** Man misst etwas, dessen Ergebnis vom Zufall abhängt — hier die **Länge \( L \)** eines
zufällig herausgegriffenen Gussteils. Mal ist es etwas länger, mal etwas kürzer.

**Normalverteilung / Glockenkurve.** Wenn viele kleine, unabhängige Schwankungen zusammenkommen (kleine
Ungenauigkeiten in der Maschine, im Material, in der Temperatur …), häufen sich die Messwerte in der
Mitte und werden nach außen hin seltener. Trägt man auf, *wie häufig* welche Länge vorkommt, entsteht
die berühmte **Glockenkurve**: in der Mitte hoch, nach beiden Seiten symmetrisch abfallend. „\( L \) ist
normalverteilt" heißt genau: Die Häufigkeit der Längen folgt dieser Glockenform.

**Erwartungswert \( \mu \) (sprich „mü").** Das ist der **Mittelwert** — der Wert, um den alles
schwankt, hier der Normwert \( 100 \) mm. Er sitzt genau unter dem **höchsten Punkt** der Glocke.
Anschauung: Würde man die Glockenfläche aus Pappe ausschneiden, balancierte sie genau auf einer Spitze
bei \( x=100 \).

**Standardabweichung \( \sigma \) (sprich „sigma").** Sie misst, **wie breit** die Glocke ist — also wie
stark die Längen typischerweise vom Mittelwert abweichen. Klein = schmale, hohe Glocke (alle Teile fast
gleich lang); groß = breite, flache Glocke (große Streuung). Hier \( \sigma = 3{,}4 \) mm.

**Wahrscheinlichkeit = Fläche.** Bei einer Glockenkurve ist die **Wahrscheinlichkeit** eines
Längenbereichs gleich dem **Flächeninhalt** unter der Kurve über diesem Bereich. Die ganze Fläche unter
der Glocke ist \( 1 \) (= \( 100\,\% \), irgendeine Länge kommt sicher heraus). \( P(L<95) \) ist also
die Fläche **links von \( 95 \)** — der linke Glockenschwanz im Bild oben.

<details><summary>Warum man den Zahlenwert nicht von Hand ausrechnen kann — und was man trotzdem von Hand macht</summary>

Die Glockenkurve hat eine Formel mit der e-Funktion, deren Fläche sich **nicht** mit einer einfachen
Stammfunktion bestimmen lässt. Deshalb liefert den reinen Zahlenwert \( 0{,}071 \) der GTR oder eine
Tabelle. **Von Hand** macht man zweierlei, und genau das zählt in der mündlichen Prüfung:

1. **Standardisieren** — ausrechnen, *wie viele Standardabweichungen* der Wert \( 95 \) vom Mittelwert
   entfernt ist: \( \tfrac{95-100}{3{,}4}\approx -1{,}47 \). So wird jede Normalverteilung vergleichbar.
2. **Symmetrie nutzen** — für das gleich wahrscheinliche Ereignis braucht man **gar keinen** Rechner:
   der zu \( 95 \) spiegelbildliche Wert ist \( 105 \), also \( P(L>105)=P(L<95) \).

</details>

<details><summary>Typische Falle</summary>

Beim gesuchten gleich wahrscheinlichen Ereignis greifen viele zu \( L<105 \) statt \( L>105 \).
\( L<105 \) wäre fast die **ganze** linke Glockenhälfte plus Mitte — eine große Wahrscheinlichkeit, nicht
\( 0{,}071 \). Entscheidend ist der **gespiegelte Schwanz**: gleich weit vom Mittelwert weg und auf der
**anderen** Seite, also \( L>105 \). Eselsbrücke: spiegeln heißt „gleicher Abstand, andere Richtung,
gleiches Schwanzstück".

</details>
</details>
</details>

### Teilaufgabe b) — Erwartungswert und Standardabweichung aus dem Graphen ablesen

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Erwartungswert \( \mu \).** Er sitzt unter der **Maximumstelle** (dem höchsten Punkt) der
Glockenkurve. Man liest also die \( x \)-Koordinate des Hochpunkts ab:

\[ x_1 = \mu = 100. \]

**Standardabweichung \( \sigma \).** Die Glockenkurve hat zwei **Wendestellen** — Stellen, an denen die
Kurve von einer Rechtskurve in eine Linkskurve übergeht. Sie liegen genau bei \( \mu-\sigma \) (links)
und \( \mu+\sigma \) (rechts). Liest man die **linke Wendestelle** \( x_2 \) ab, folgt

\[ x_2 = \mu-\sigma \;\;\Longrightarrow\;\; \sigma = \mu - x_2 = 100 - 96{,}6 = 3{,}4. \]

<details><summary>Haltung dahinter: Was ist eine „Wendestelle", und warum verrät sie \( \sigma \)?</summary>

**Maximumstelle.** Der höchste Punkt der Glocke. Weil die Glocke symmetrisch um den Mittelwert gebaut
ist, sitzt der höchste Punkt **genau über dem Mittelwert**. Deshalb: \( x \)-Wert des Gipfels ablesen
\( = \mu \). Im Bild oben markiert die orange Linie diesen Gipfel bei \( 100 \).

**Wendestelle — was ist das?** Stell dir vor, du fährst mit dem Auto die Glockenkurve von links nach
rechts ab. Anfangs (im linken Schwanz) machst du eine **Linkskurve** (die Kurve wird steiler, krümmt
sich nach oben). Oben am Gipfel und kurz davor lenkst du **rechts** (die Kurve ist nach unten gewölbt).
Die **Wendestelle** ist genau der Punkt, an dem du von Links- auf Rechtslenken umstellst — wo sich die
Krümmung umdreht. Eine Glocke hat zwei solche Umschaltpunkte, je einer auf jeder Seite.

**Warum bei \( \mu\pm\sigma \)?** Das ist eine feste Eigenschaft **jeder** Normalverteilung: Die beiden
Wendestellen liegen immer **genau eine Standardabweichung** vom Mittelwert entfernt. Das ist praktisch,
weil man \( \sigma \) so direkt aus dem Bild „abgreifen" kann: vom Gipfel waagerecht nach links bis zur
Wendestelle laufen — diese Strecke ist \( \sigma \). Im Bild oben sind die Wendestellen die grünen
Punkte bei \( 96{,}6 \) und \( 103{,}4 \); der Abstand zum Gipfel \( 100 \) ist jeweils \( 3{,}4 = \sigma \).

<details><summary>Ganz langsam (mit Zahlen): \( \sigma \) aus der linken Wendestelle</summary>

Angenommen, du liest die linke Wendestelle bei \( x_2 = 96{,}6 \) ab. Es gilt \( x_2 = \mu-\sigma \).
Setze \( \mu=100 \) ein: \( 96{,}6 = 100 - \sigma \). Stelle nach \( \sigma \) um — addiere \( \sigma \)
auf beiden Seiten und ziehe \( 96{,}6 \) ab: \( \sigma = 100 - 96{,}6 = 3{,}4 \). Genau die angegebene
Standardabweichung. (Mit der rechten Wendestelle \( 103{,}4 \) geht es genauso: \( \sigma = 103{,}4-100
= 3{,}4 \).)

</details>
</details>
</details>

### Teilaufgabe c) — Deutung der grauen Fläche

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Die graue Fläche liegt unter der Glockenkurve **zwischen \( 96 \) und \( 100 \)**. Bei einer
Normalverteilung ist eine solche Fläche immer eine **Wahrscheinlichkeit**. Also:

> Der Inhalt der grauen Fläche entspricht der **Wahrscheinlichkeit, dass ein Plastikgussteil eine Länge
> zwischen \( 96 \) mm und \( 100 \) mm besitzt**, also \( P(96 \le L \le 100) \).

<details><summary>Haltung dahinter: Warum ist „Fläche" hier dasselbe wie „Wahrscheinlichkeit"?</summary>

Bei einer stetigen Größe wie der Länge \( L \) (sie kann *jeden* Zwischenwert annehmen, nicht nur
ganze Zahlen) lässt sich die Wahrscheinlichkeit nicht durch Abzählen bestimmen. Stattdessen gilt die
Grundregel: **Die Wahrscheinlichkeit, dass \( L \) in einen bestimmten Bereich fällt, ist gleich der
Fläche unter der Glockenkurve über diesem Bereich.** Die gesamte Fläche unter der Glocke ist \( 1 \)
(= \( 100\,\% \)); ein Teilstück davon ist der entsprechende Wahrscheinlichkeits-Anteil.

Die graue Fläche reicht von \( 96 \) (etwas links vom Mittelwert) bis \( 100 \) (genau der Mittelwert).
Im Sachzusammenhang heißt das: **Wie wahrscheinlich ist es, ein Gussteil zu ziehen, das zwischen
\( 96 \) mm und \( 100 \) mm lang ist?** Genau das ist die Deutung — eine Zahl muss man nicht angeben,
nur den Sachbezug benennen.

<details><summary>Typische Falle</summary>

Zwei Fehler sind hier verbreitet. Erstens die **Grenzen verwechseln** (etwa „zwischen \( 96 \) und
\( 104 \)" sagen, weil man symmetrisch denkt) — es zählt, was wirklich grau ist, hier \( 96 \) bis
\( 100 \). Zweitens die Fläche als **Anzahl** statt als **Wahrscheinlichkeit** deuten („so viele Teile
sind zwischen \( 96 \) und \( 100 \)"). Die Fläche ist ein **Anteil/eine Wahrscheinlichkeit**; eine
Stückzahl bekäme man erst, wenn man sie mit der produzierten Menge multipliziert.

</details>
</details>
</details>

### Teilaufgabe d) — Mangelhaft mit Wahrscheinlichkeit 14 % begründen

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

„Mangelhaft" heißt: Die Länge weicht um **mehr als \( 5 \) mm** vom Normwert \( 100 \) ab, also
\( L<95 \) **oder** \( L>105 \). Die Gegenwahrscheinlichkeit ist „nicht mangelhaft", nämlich
\( 95 \le L \le 105 \). Deshalb:

\[ p = P(\text{mangelhaft}) = 1 - P(95 \le L \le 105). \]

Den mittleren Anteil liefert der GTR: \( P(95 \le L \le 105) \approx 0{,}859 \). Also

\[ p = 1 - 0{,}859 \approx 0{,}141 \approx 14\,\%. \]

**Gegenprobe über die zwei Schwänze** (nutzt direkt das Ergebnis aus a): Mangelhaft sind die beiden
Randflächen zusammen,

\[ p = P(L<95) + P(L>105) \approx 0{,}071 + 0{,}071 = 0{,}142 \approx 14\,\%. \quad\checkmark \]

<details><summary>Haltung dahinter: „weicht um mehr als 5 mm ab" — wie wird daraus eine Wahrscheinlichkeit?</summary>

**Den Sachsatz in Mathe übersetzen.** „Um mehr als \( 5 \) mm vom Normwert \( 100 \) abweichen" heißt:
Der Abstand zwischen \( L \) und \( 100 \) ist größer als \( 5 \). Das passiert auf **zwei** Arten —
entweder ist das Teil zu kurz (\( L<95 \)) oder zu lang (\( L>105 \)). Beides zusammen ist „mangelhaft".

**Der Trick mit der Gegenwahrscheinlichkeit.** Statt die beiden Schwänze einzeln zu addieren, ist es
oft bequemer, das **Mittelstück** zu betrachten — „nicht mangelhaft" ist \( 95 \le L \le 105 \) — und
von \( 1 \) abzuziehen. Denn jedes Teil ist **entweder** mangelhaft **oder** nicht; beide Anteile
ergeben zusammen \( 1 \) (= \( 100\,\% \)). Also: mangelhaft \( = 1 - \) nicht mangelhaft.

**Warum beide Wege dasselbe liefern.** Das Mittelstück und die zwei Schwänze füllen zusammen die ganze
Glocke. \( 1 - 0{,}859 = 0{,}141 \) ist also dieselbe Zahl wie \( 0{,}071+0{,}071 = 0{,}142 \) (die
winzige Differenz kommt nur vom Runden).

<details><summary>Ganz langsam (mit Zahlen): die Subtraktion \( 1 - 0{,}859 \)</summary>

\( 1{,}000 - 0{,}859 \): Ziehe ziffernweise von rechts ab. \( 0-9 \) geht nicht, also borgen:
\( 10-9=1 \) (letzte Stelle), in der Hunderterstelle nach dem Komma bleibt nach dem Borgen \( 9 \), und
\( 9-5=4 \); in der Zehntelstelle bleibt \( 9 \), und \( 9-8=1 \); vor dem Komma \( 0-0=0 \). Ergebnis
\( 0{,}141 \). Das sind \( 14{,}1\,\% \), gerundet \( 14\,\% \).

</details>

<details><summary>Typische Falle</summary>

Verbreitet ist, „\( 5 \) mm Abweichung" als \( 95 \le L \le 105 \) **mit** den Grenzen zur Mangelhaftigkeit
zu zählen oder das „mehr als" zu übersehen. Genau \( 5 \) mm Abweichung (also \( L=95 \) oder \( L=105 \))
gilt **noch nicht** als mangelhaft — erst *mehr* als \( 5 \) mm. Bei der stetigen Normalverteilung
spielt das für den Zahlenwert keine Rolle (einzelne Punkte haben Wahrscheinlichkeit \( 0 \)), aber im
Aufschreiben gehört das „nicht mangelhaft" als \( 95 \le L \le 105 \) sauber benannt.

</details>
</details>
</details>

### Teilaufgabe e) — Zufallsexperiment und Ereignis zum Term

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Im Term steckt eine **Binomialverteilung**. Lies die Bausteine:

- \( 0{,}14 \) ist die Wahrscheinlichkeit, dass **ein** Gussteil mangelhaft ist (aus Teil d).
- \( 0{,}86 = 1-0{,}14 \) ist die Wahrscheinlichkeit, dass es **nicht** mangelhaft ist.
- Der Exponent zeigt: Es geht um \( n=200 \) Teile.

Die drei Summanden sind genau die Wahrscheinlichkeiten für \( 200 \), \( 199 \) und \( 198 \) mangelhafte
Teile:

\[
\underbrace{0{,}14^{200}}_{P(X=200)}
+\underbrace{200\cdot 0{,}14^{199}\cdot 0{,}86}_{P(X=199)}
+\underbrace{\binom{200}{2}\cdot 0{,}14^{198}\cdot 0{,}86^{2}}_{P(X=198)}
= P(X\ge 198).
\]

**Zufallsexperiment.** Der laufenden Produktion werden **\( 200 \) Gussteile zufällig entnommen**;
\( X \) zählt, wie viele davon mangelhaft sind. Dann ist \( X \) binomialverteilt mit \( n=200 \) und
\( p=0{,}14 \), kurz \( X\sim B(200;\,0{,}14) \).

**Ereignis.** „**Mindestens \( 198 \) der \( 200 \) Gussteile sind mangelhaft**" (also \( X\ge 198 \)).

<details><summary>Haltung dahinter: Was ist eine Binomialverteilung, und woher kommen die drei Bausteine?</summary>

**Bernoulli-Versuch.** Ein Versuch mit nur zwei Ausgängen — hier „mangelhaft" (Treffer, Wahrscheinlichkeit
\( p=0{,}14 \)) oder „nicht mangelhaft" (kein Treffer, \( q=1-p=0{,}86 \)). Ein einzelnes Gussteil prüfen
ist so ein Versuch.

**Bernoulli-Kette / Binomialverteilung.** Wiederholt man denselben Versuch \( n \)-mal unabhängig und
zählt die Treffer, ist die Trefferzahl \( X \) **binomialverteilt**. Die Wahrscheinlichkeit für genau
\( k \) Treffer ist

\[ P(X=k) = \binom{n}{k}\, p^{k}\, q^{\,n-k}. \]

Diese Formel hat drei Teile, und genau die erkennt man im Aufgaben-Term:

- \( p^{k} \): \( k \) Teile **sind** mangelhaft (jedes mit Wahrscheinlichkeit \( 0{,}14 \)).
- \( q^{\,n-k} \): die übrigen \( n-k \) Teile sind **nicht** mangelhaft (jedes mit \( 0{,}86 \)).
- \( \binom{n}{k} \) („\( n \) über \( k \)"): die **Anzahl der Möglichkeiten**, *welche* \( k \) der
  \( 200 \) Teile die mangelhaften sind. Denn es ist egal, ob das erste und dritte Teil mangelhaft sind
  oder das zweite und fünfte — alle diese Anordnungen führen zur selben Trefferzahl und müssen
  mitgezählt werden.

**Die drei Summanden im Term** sind \( k=200 \), \( k=199 \), \( k=198 \):

\[
\begin{aligned}
k=200:&\quad \binom{200}{200}0{,}14^{200}0{,}86^{0} = 0{,}14^{200}\quad(\tbinom{200}{200}=1,\ 0{,}86^{0}=1),\\
k=199:&\quad \binom{200}{199}0{,}14^{199}0{,}86^{1} = 200\cdot 0{,}14^{199}\cdot 0{,}86\quad(\tbinom{200}{199}=200),\\
k=198:&\quad \binom{200}{198}0{,}14^{198}0{,}86^{2} = \tbinom{200}{2}\cdot 0{,}14^{198}\cdot 0{,}86^{2}.
\end{aligned}
\]

Addiert man die Wahrscheinlichkeiten für \( 198 \), \( 199 \) **und** \( 200 \) Treffer, erhält man die
Wahrscheinlichkeit für **„\( 198 \) oder mehr"**, also \( P(X\ge 198) \) — „mindestens \( 198 \)".

<details><summary>Ganz langsam (mit Zahlen): warum \( \binom{200}{199}=200 \) und \( \binom{200}{198}=\binom{200}{2} \)?</summary>

\( \binom{200}{199} \) ist die Anzahl der Möglichkeiten, \( 199 \) Teile aus \( 200 \) als mangelhaft
auszuwählen. \( 199 \) auswählen heißt: **genau eines weglassen** — und dafür gibt es \( 200 \)
Möglichkeiten (jedes der \( 200 \) Teile kann das eine gute sein). Deshalb \( \binom{200}{199}=200 \).

\( \binom{200}{198} \): \( 198 \) mangelhaft auswählen heißt **genau zwei gute weglassen**. Zwei aus
\( 200 \) auszuwählen geht auf \( \binom{200}{2} = \tfrac{200\cdot 199}{2} = \tfrac{39800}{2} = 19900 \)
Arten. Deshalb \( \binom{200}{198}=\binom{200}{2}=19900 \). (Allgemein \( \binom{n}{k}=\binom{n}{n-k} \):
„\( k \) auswählen" ist gleichbedeutend mit „\( n-k \) weglassen".)

</details>

<details><summary>Typische Falle</summary>

Den Term als „\( P(X\le 2) \) **gute** Teile" zu lesen, ist im Kern dasselbe Ereignis, aber Vorsicht
bei der Sprache: \( 0{,}14 \) gehört zu **mangelhaft**, \( 0{,}86 \) zu **nicht mangelhaft**. Wer die
Rollen vertauscht („mindestens \( 198 \) sind in Ordnung"), beschreibt das **falsche** Ereignis. Der
hoch stehende Exponent \( 200 \) bzw. \( 199 \) sitzt bei \( 0{,}14 \) — also zählen wir die
**mangelhaften** Teile, und „mindestens \( 198 \) mangelhaft" ist die richtige Formulierung.

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- **a)** \( P(L<95)\approx 0{,}071 \); gleich wahrscheinlich: \( L>105 \) (Symmetrie um \( 100 \)).
- **b)** \( \mu \) = Maximumstelle \( = 100 \); \( \sigma \) aus der Wendestelle \( x_2=\mu-\sigma \), also
  \( \sigma = 100-96{,}6 = 3{,}4 \).
- **c)** Graue Fläche \( = P(96\le L\le 100) \) (Länge zwischen \( 96 \) mm und \( 100 \) mm).
- **d)** \( p = 1 - P(95\le L\le 105) \approx 0{,}141 \approx 14\,\% \); Gegenprobe \( 0{,}071+0{,}071 \approx 0{,}14 \).
- **e)** \( X\sim B(200;\,0{,}14) \); Ereignis „mindestens \( 198 \) der \( 200 \) Teile mangelhaft",
  \( P(X\ge 198) \).

</details>

---

## Teil 2 — Gespräch (Analysis): Sinusfunktion zuordnen und vernetzen

<div class="aufgabenkasten">

**Input.** Gegeben sind die Funktion \( f \) mit \( f(x) = -3\sin(2x) - 1 \) sowie vier Graphen
(Abbildung 1–4).

Im Gespräch denkbare Aspekte:

- **(AB I)** Charakteristische Eigenschaften des Graphen von \( f \) nennen, die man **ohne Rechnung**
  dem Funktionsterm entnehmen kann; einen der vier Graphen \( f \) zuordnen.
- **(AB II)** Zu **Abbildung 2** gehört eine trigonometrische Funktion \( g \) mit
  \( \displaystyle\int_0^{\pi/2} g(x)\,dx = -3 \). Bestimme den Wert von
  \( \displaystyle\int_0^{3\pi/2} g(x)\,dx \) **ohne weitere Rechnung**. Bestimme außerdem eine
  Stammfunktion \( F \) von \( f \). Untersuche die Symmetrieeigenschaften des Graphen von \( f' \).
- **(AB III)** Erläutere, dass die Anzahl der Schnittpunkte einer **Ursprungsgerade** mit dem Graphen
  von \( g \) **nicht gerade** (z. B. \( 266 \)) sein kann (Symmetrie). Leite
  \( \displaystyle\int_{-1}^{1} f(x)\,dx = -2 \) her, ausgehend von der Symmetrie der Sinuskurve.

</div>

Hier sind die vier Graphen. Ordne zu, **bevor** du die Lösung aufklappst: Welcher gehört zu
\( f(x) = -3\sin(2x)-1 \)?

<div class="graph-row">
<figure>
<div class="jxgbox" id="jxg-k10-abb1" style="width:100%;max-width:260px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 1</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k10-abb2" style="width:100%;max-width:260px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 2</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k10-abb3" style="width:100%;max-width:260px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 3</figcaption>
</figure>
<figure>
<div class="jxgbox" id="jxg-k10-abb4" style="width:100%;max-width:260px;aspect-ratio:1/1"></div>
<figcaption>Abbildung 4</figcaption>
</figure>
</div>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k10-abb1',{boundingbox:[-2.6,3.4,5.6,-4.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return -3*Math.sin(2*x)-1;},-2.6,5.6],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k10-abb2',{boundingbox:[-2.6,3.4,5.6,-4.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return -3*Math.sin(2*x);},-2.6,5.6],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k10-abb3',{boundingbox:[-2.6,3.4,5.6,-4.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 3*Math.sin(2*x)-1;},-2.6,5.6],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k10-abb4',{boundingbox:[-2.6,3.4,5.6,-4.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return -3*Math.sin(x)-1;},-2.6,5.6],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>

### AB I — Eigenschaften aus dem Term und Zuordnung

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Eigenschaften, die man direkt am Term \( f(x) = -3\sin(2x)-1 \) abliest** (ohne zu rechnen):

- **Periodisch** (es ist eine Sinusfunktion). Die **Periode** ist \( \tfrac{2\pi}{2} = \pi \), weil im
  Inneren der Faktor \( 2 \) steht (er staucht die Welle auf die halbe Länge gegenüber dem normalen
  \( \sin x \) mit Periode \( 2\pi \)).
- **Amplitude \( 3 \)** (der Vorfaktor \( -3 \), Betrag \( 3 \)): Die Welle schwingt um \( 3 \) nach oben
  und unten um ihre Mittellinie.
- **Mittellinie \( y=-1 \)** (das angehängte \( -1 \) verschiebt alles um \( 1 \) nach unten).
- Daraus der **Wertebereich** \( [-4;\,2] \): größter Wert \( -1+3 = 2 \), kleinster Wert \( -1-3 = -4 \).
- **\( y \)-Achsenabschnitt** \( f(0) = -3\sin(0)-1 = -1 \).
- **Bei \( x=0 \) fallend**: Wegen des **Minus** vor dem Sinus geht der Graph an der \( y \)-Achse nach
  **unten** und erreicht kurz danach (bei \( x=\tfrac{\pi}{4}\approx 0{,}79 \)) den **Tiefpunkt** \( -4 \).
- **Punktsymmetrisch zum Punkt \( (0\,|\,-1) \)** (der Sinusanteil ist punktsymmetrisch zum Ursprung,
  die Verschiebung um \( -1 \) hebt das Symmetriezentrum auf \( (0\,|\,-1) \)).

**Zuordnung: \( f \) gehört zu Abbildung 1.** Jede falsche Abbildung scheidet an genau einem Merkmal aus:

- **Abbildung 4** scheidet aus: Ihre Welle ist **doppelt so breit** (Periode \( 2\pi \) statt \( \pi \)) —
  sie zeigt nur eine breite Mulde. \( f \) hat wegen des Faktors \( 2 \) die Periode \( \pi \).
- **Abbildung 2** scheidet aus: Ihre Welle schwingt **symmetrisch um die \( x \)-Achse** (Mittellinie
  \( y=0 \), Werte von \( -3 \) bis \( 3 \)). \( f \) ist um \( 1 \) nach unten verschoben (Mittellinie
  \( y=-1 \), Werte von \( -4 \) bis \( 2 \)).
- **Abbildung 3** scheidet aus: Sie läuft an der \( y \)-Achse **aufwärts** (Hochpunkt kurz rechts von
  \( 0 \)). \( f \) läuft wegen des Minus **abwärts** (Tiefpunkt kurz rechts von \( 0 \)).
- **Abbildung 1** passt in allen Punkten: Periode \( \pi \), Mittellinie \( y=-1 \), Werte \( [-4;\,2] \),
  bei \( x=0 \) der Wert \( -1 \) und **fallend** mit Tiefpunkt direkt rechts daneben.

<details><summary>Haltung dahinter: Wie liest man Periode, Amplitude und Verschiebung aus einem Sinusterm? (ganz von vorn)</summary>

Eine allgemeine Sinusfunktion sieht so aus: \( a\cdot\sin(b\,x) + d \). Jeder der drei Bausteine
\( a \), \( b \), \( d \) steuert eine sichtbare Eigenschaft des Graphen. Geht man sie der Reihe nach
durch, kann man den Graphen „im Kopf" zeichnen.

**\( d \) — die Mittellinie (Verschiebung nach oben/unten).** Der reine Sinus pendelt um die
\( x \)-Achse (um \( y=0 \)). Das \( +d \) hebt oder senkt die **ganze** Welle. Bei \( f \) ist
\( d=-1 \): Die Welle pendelt um die waagerechte Linie \( y=-1 \). Bild: die Wasseroberfläche, um die
die Wellen schwappen, liegt bei \( -1 \).

**\( a \) — die Amplitude (Höhe der Welle) und die Richtung.** Der Betrag \( |a| \) sagt, **wie weit**
die Welle über und unter die Mittellinie ausschlägt. Bei \( f \) ist \( |a|=3 \): \( 3 \) nach oben
(bis \( -1+3=2 \)) und \( 3 \) nach unten (bis \( -1-3=-4 \)). Das **Vorzeichen** von \( a \) sagt die
**Richtung**: Ein positives \( a \) startet bei \( x=0 \) steigend, ein **negatives** \( a \) (hier
\( -3 \)) startet **fallend** — die Welle ist an der Mittellinie gespiegelt.

**\( b \) — die Periode (Breite der Welle).** \( b \) staucht oder streckt die Welle in
\( x \)-Richtung. Eine volle Welle des normalen \( \sin \) braucht die Strecke \( 2\pi \). Mit dem
Faktor \( b \) braucht sie nur noch \( \tfrac{2\pi}{b} \). Bei \( f \) ist \( b=2 \), also Periode
\( \tfrac{2\pi}{2}=\pi\approx 3{,}14 \) — die Welle ist **halb so breit** wie beim normalen Sinus.

<details><summary>Ganz langsam (mit Zahlen): Höchst- und Tiefwert, Wert bei \( x=0 \)</summary>

Der Sinus liefert immer Werte zwischen \( -1 \) und \( +1 \). Setze diese Extremfälle ein:

- Größter Funktionswert: wenn \( \sin(2x) = -1 \) (das Minus dreht es um!), dann
  \( f = -3\cdot(-1) - 1 = 3 - 1 = 2 \).
- Kleinster Funktionswert: wenn \( \sin(2x) = +1 \), dann \( f = -3\cdot 1 - 1 = -3 - 1 = -4 \).
- Bei \( x=0 \): \( \sin(2\cdot 0) = \sin 0 = 0 \), also \( f(0) = -3\cdot 0 - 1 = -1 \).

So bekommt man ohne Skizze die Eckdaten: pendelt zwischen \( -4 \) und \( 2 \), startet bei \( -1 \).

</details>

<details><summary>Typische Falle</summary>

Der häufigste Fehler ist die **Periode**: Viele lesen aus \( \sin(2x) \) eine Periode \( 2 \) oder
\( 2\pi \) ab. Richtig ist \( \tfrac{2\pi}{2}=\pi \) — der innere Faktor steht im **Nenner**. Zweite
Falle: das **Vorzeichen** von \( a \) übersehen und Abbildung 3 (steigend bei \( 0 \)) statt Abbildung 1
(fallend bei \( 0 \)) wählen. Das Minus vor dem Sinus dreht die Startrichtung um.

</details>
</details>
</details>

### AB II — Integral von \( g \) (Symmetrie), Stammfunktion von \( f \), Symmetrie von \( f' \)

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

#### (1) Wert von \( \displaystyle\int_0^{3\pi/2} g(x)\,dx \) ohne weitere Rechnung

Aus Abbildung 2 liest man ab: \( g \) ist eine Sinuswelle mit **Periode \( \pi \)** und **Mittellinie
\( y=0 \)** (sie schwingt symmetrisch um die \( x \)-Achse). Gegeben ist
\( \displaystyle\int_0^{\pi/2} g(x)\,dx = -3 \). Zerlege das gesuchte Integral:

\[ \int_0^{3\pi/2} g\,dx = \underbrace{\int_0^{\pi/2} g\,dx}_{=\,-3} \;+\; \int_{\pi/2}^{3\pi/2} g\,dx. \]

Das Intervall \( \left[\tfrac{\pi}{2};\,\tfrac{3\pi}{2}\right] \) hat die Länge \( \pi \) — also **genau
eine volle Periode**. Über eine volle Periode einer um die \( x \)-Achse schwingenden Sinuskurve sind
die Fläche oberhalb und unterhalb der Achse **gleich groß**, sie heben sich auf:

\[ \int_{\pi/2}^{3\pi/2} g\,dx = 0 \quad\Longrightarrow\quad
   \boxed{\;\int_0^{3\pi/2} g\,dx = -3 + 0 = -3.\;} \]

<details><summary>Haltung dahinter: Was ist ein Integral, und warum ist es über eine volle Sinus-Periode null?</summary>

**Integral = orientierte Fläche.** Ein Integral \( \int_a^b g\,dx \) misst die Fläche zwischen dem
Graphen und der \( x \)-Achse — aber **mit Vorzeichen**: Fläche **über** der Achse zählt positiv, Fläche
**unter** der Achse negativ. Bild eines Bankkontos: über der Achse Einzahlungen, unter der Achse
Abhebungen; das Integral nennt nur den **Kontostand** (die Differenz).

**Volle Periode.** Eine Sinuswelle, die um die \( x \)-Achse schwingt, hat in jeder vollen Periode genau
einen „Berg" über der Achse und ein gleich großes „Tal" unter der Achse. Einzahlung und Abhebung sind
gleich groß — der Kontostand ändert sich über eine volle Periode um \( 0 \). Genau deshalb darf man das
Stück von \( \tfrac{\pi}{2} \) bis \( \tfrac{3\pi}{2} \) (Länge \( \pi \) = eine Periode) einfach
weglassen: Es trägt nichts bei. Übrig bleibt das schon bekannte erste Stück, also \( -3 \). Das ist
gemeint mit „ohne weitere Rechnung": Man nutzt **Periodizität und Symmetrie** statt eine Stammfunktion.

<details><summary>Typische Falle</summary>

Verlockend ist die Annahme „dreimal so langes Intervall, also dreimal der Wert" — das ergäbe \( -9 \)
und ist **falsch**. Das stimmt nur, wenn jedes gleich lange Stück denselben Beitrag liefert; hier heben
sich aber zwei der drei Halbperioden gegenseitig auf. Sicherer Blick: \( \left[\tfrac{\pi}{2};
\tfrac{3\pi}{2}\right] \) ist eine **ganze** Periode \( \Rightarrow \) Beitrag \( 0 \).

</details>
</details>

#### (2) Eine Stammfunktion \( F \) von \( f \)

Gesucht ist ein \( F \) mit \( F' = f \), also \( F'(x) = -3\sin(2x) - 1 \). Summandenweise „rückwärts
ableiten":

- Stammfunktion von \( -3\sin(2x) \): Eine Stammfunktion von \( \sin(2x) \) ist \( -\tfrac12\cos(2x) \)
  (der Faktor \( \tfrac12 \) gleicht die innere Ableitung \( 2 \) aus). Mit dem \( -3 \) davor:
  \( -3\cdot\left(-\tfrac12\cos(2x)\right) = \tfrac{3}{2}\cos(2x) \).
- Stammfunktion von \( -1 \): das ist \( -x \).

\[ \boxed{\,F(x) = \tfrac{3}{2}\cos(2x) - x.\,} \]

**Probe durch Ableiten:** \( F'(x) = \tfrac32\cdot\big(-\sin(2x)\big)\cdot 2 - 1 = -3\sin(2x) - 1 = f(x). \)
\( \checkmark \)

<details><summary>Haltung dahinter: Was ist eine Stammfunktion, und woher der Faktor \( \tfrac12 \)?</summary>

**Ableiten** misst die Steigung einer Funktion. Eine **Stammfunktion** ist das **Ableiten rückwärts**:
gesucht ist die Funktion \( F \), deren Ableitung wieder unser \( f \) ergibt. Man „un-leitet" ab.

**Sinus und Kosinus rückwärts.** Beim Ableiten gilt \( (\cos x)' = -\sin x \). Rückwärts heißt das: eine
Stammfunktion von \( \sin x \) ist \( -\cos x \) (das Minus muss mit, damit beim Vorwärts-Ableiten das
Vorzeichen wieder stimmt).

**Der Faktor \( \tfrac12 \) — die Kettenregel rückwärts.** Im Term steht nicht \( \sin x \), sondern
\( \sin(2x) \): innen sitzt \( 2x \). Würde man \( -\cos(2x) \) ableiten, käme durch die **Kettenregel**
ein zusätzlicher Faktor \( 2 \) heraus (Ableitung des Inneren \( 2x \) ist \( 2 \)) — also
\( +2\sin(2x) \), das ist doppelt so viel wie gewollt. Damit am Ende genau \( \sin(2x) \) erscheint,
schreibt man als Stammfunktion \( -\tfrac12\cos(2x) \): Der Faktor \( \tfrac12 \) frisst die \( 2 \) aus
der Kettenregel auf. (Mehr dazu: [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).)

**Warum die Probe?** Die Stammfunktion ist der sicherste Selbsttest: Leitet man das Ergebnis vorwärts ab
und kommt der Ausgangsterm \( f \) heraus, war alles richtig. Genau das zeigt die Probe oben.

<details><summary>Typische Falle</summary>

Den Faktor \( \tfrac12 \) zu vergessen ist der Klassiker (\( F(x)=\tfrac{3}{}\dots \) ohne Ausgleich der
inneren \( 2 \)). Zweite Falle: das **Vorzeichen**. Aus \( \sin \) wird beim Aufleiten \( -\cos \); mit
dem \( -3 \) davor dreht sich das Minus zu Plus, daher \( +\tfrac32\cos(2x) \). Ein falsches Vorzeichen
fällt bei der Ableitungsprobe sofort auf.

</details>
</details>

#### (3) Symmetrie des Graphen von \( f' \)

Leite \( f \) ab: \( f'(x) = -3\cdot\cos(2x)\cdot 2 = -6\cos(2x). \)

\( f' \) ist also ein reiner Kosinus (mal Zahl). Der Kosinus ist eine **gerade** Funktion, d. h.
\( \cos(-2x) = \cos(2x) \). Damit gilt

\[ f'(-x) = -6\cos(-2x) = -6\cos(2x) = f'(x). \]

Aus \( f'(-x) = f'(x) \) folgt: **Der Graph von \( f' \) ist achsensymmetrisch zur \( y \)-Achse.**

<figure>
<div class="jxgbox" id="jxg-k10-fstrich" style="width:100%;max-width:420px;aspect-ratio:3/2"></div>
<figcaption>Graph von \( f'(x) = -6\cos(2x) \): spiegelbildlich zur \( y \)-Achse (linke und rechte Seite
sind identisch).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k10-fstrich',{boundingbox:[-3.6,7,3.6,-7],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return -6*Math.cos(2*x);},-3.6,3.6],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('line',[[0,-7],[0,7]],{straightFirst:true,straightLast:true,strokeColor:'#d98324',dash:2,strokeWidth:1});})();</script>

<details><summary>Haltung dahinter: „gerade" und „ungerade" Funktionen — was heißt das am Graphen?</summary>

Es gibt zwei besonders übersichtliche Arten von Symmetrie:

- **Achsensymmetrie zur \( y \)-Achse** (man sagt: die Funktion ist **gerade**). Bedeutung am Graphen:
  Die linke Hälfte ist das **Spiegelbild** der rechten an der senkrechten \( y \)-Achse — wie ein Bild
  und sein Spiegel. Rechnerisch: \( h(-x) = h(x) \) (an der Stelle \( -x \) derselbe \( y \)-Wert wie bei
  \( +x \)). Typisches Beispiel: der Kosinus.
- **Punktsymmetrie zum Ursprung** (die Funktion ist **ungerade**). Der Graph sieht nach einer
  \( 180^\circ \)-Drehung um den Ursprung wieder gleich aus. Rechnerisch: \( h(-x) = -h(x) \). Typisches
  Beispiel: der Sinus.

**Hier:** \( f'(x) = -6\cos(2x) \) ist ein Kosinus, also **gerade** \( \Rightarrow \) achsensymmetrisch
zur \( y \)-Achse. Schöner Zusammenhang: \( f \) selbst ist **punktsymmetrisch** zum Punkt
\( (0\,|\,-1) \) (Sinusanteil), und die Ableitung einer solchen punktsymmetrischen Funktion wird
**achsensymmetrisch**. Das \( -1 \) aus \( f \) fällt beim Ableiten weg (Ableitung einer Konstanten ist
\( 0 \)), deshalb bleibt mit \( -6\cos(2x) \) eine sauber achsensymmetrische Funktion übrig. Im Bild oben
sieht man es direkt: links und rechts der orangefarbenen \( y \)-Achse verläuft die Kurve identisch.

<details><summary>Ganz langsam (mit Zahlen): die Probe \( f'(-x)=f'(x) \)</summary>

Nimm eine Teststelle, etwa \( x=0{,}9 \): \( f'(0{,}9) = -6\cos(1{,}8) \). Und an der Spiegelstelle
\( x=-0{,}9 \): \( f'(-0{,}9) = -6\cos(-1{,}8) \). Weil \( \cos(-1{,}8)=\cos(1{,}8) \) (Kosinus ist
gerade), ist \( f'(-0{,}9) = -6\cos(1{,}8) = f'(0{,}9) \) — beide Stellen liefern denselben Wert
(\( \approx 1{,}36 \)). Genau das ist Achsensymmetrie.

</details>

<details><summary>Typische Falle</summary>

\( f \) und \( f' \) haben **unterschiedliche** Symmetrie — das verwirrt oft. \( f \) ist
*punkt*symmetrisch (zu \( (0\,|\,-1) \)), \( f' \) ist *achsen*symmetrisch (zur \( y \)-Achse). Wer von
\( f \) auf \( f' \) schließt, muss daran denken: Beim Ableiten wird aus „punktsymmetrisch um einen Punkt
auf der \( y \)-Achse" → „achsensymmetrisch zur \( y \)-Achse". Außerdem entscheidet allein der Sinus-/
Kosinus-Charakter; die Konstante \( -1 \) verschwindet beim Ableiten.

</details>
</details>
</details>

### AB III — Schnittpunkt-Parität und \( \int_{-1}^{1} f\,dx = -2 \)

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Herleitung anzeigen</summary>

#### (1) Warum eine Ursprungsgerade \( g \) nie in gerade vielen Punkten schneidet

Zu Abbildung 2 gehört \( g \) mit \( g(x) = -3\sin(2x) \) (Mittellinie \( y=0 \)). Diese Funktion ist
**punktsymmetrisch zum Ursprung** (ungerade), denn

\[ g(-x) = -3\sin(-2x) = -3\cdot\big(-\sin(2x)\big) = 3\sin(2x) = -g(x). \]

Eine **Ursprungsgerade** \( y = m\,x \) ist ebenfalls punktsymmetrisch zum Ursprung. Daraus folgt für die
Schnittpunkte:

- **Der Ursprung \( (0\,|\,0) \) ist immer ein Schnittpunkt:** \( g(0) = 0 \), und jede Ursprungsgerade
  läuft durch \( (0\,|\,0) \).
- **Alle anderen Schnittpunkte treten paarweise auf:** Ist \( x_0 \neq 0 \) eine Schnittstelle, so ist
  auch \( -x_0 \) eine — beide Graphen sind ja punktsymmetrisch zum Ursprung, also liegt zu jedem
  Schnittpunkt der gespiegelte ebenfalls auf beiden.

Damit ist die Gesamtzahl der Schnittpunkte \( = 1 \) (Ursprung) \( + \) eine **gerade** Zahl (die Paare)
\( = \) **ungerade**. Eine **gerade** Anzahl wie \( 266 \) ist deshalb unmöglich.

<figure>
<div class="jxgbox" id="jxg-k10-parity" style="width:100%;max-width:440px;aspect-ratio:1/1"></div>
<figcaption>\( g(x) = -3\sin(2x) \) (blau) und eine Ursprungsgerade (orange). Der Ursprung ist immer ein
Schnittpunkt; jeder weitere Schnittpunkt rechts hat einen gespiegelten Partner links.</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k10-parity',{boundingbox:[-4.6,4,4.6,-4],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return -3*Math.sin(2*x);},-4.6,4.6],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('line',[[0,0],[1,0.6]],{straightFirst:true,straightLast:true,strokeColor:'#d98324',strokeWidth:2});b.create('point',[0,0],{name:'',size:2,fillColor:'#b03a2e',strokeColor:'#b03a2e',fixed:true});})();</script>

<details><summary>Haltung dahinter: Was ist eine Ursprungsgerade, und wie führt Symmetrie zu „ungerade"?</summary>

**Ursprungsgerade.** Eine Gerade, die durch den **Ursprung** \( (0\,|\,0) \) geht, also
\( y = m\,x \) (kein \( +b \), kein Achsenabschnitt). Sie ist selbst punktsymmetrisch zum Ursprung: zu
jedem ihrer Punkte \( (x\,|\,mx) \) liegt der gespiegelte \( (-x\,|\,-mx) \) auch auf ihr.

**Die Paar-Idee.** Beide Linien — die Sinuskurve \( g \) und die Gerade — sehen nach einer
\( 180^\circ \)-Drehung um den Ursprung wieder gleich aus. Wenn sich zwei solche Linien an einer Stelle
\( x_0 \) schneiden, dann schneiden sie sich (durch dieselbe Drehung) auch an der gespiegelten Stelle
\( -x_0 \). Schnittpunkte abseits des Ursprungs kommen deshalb **immer zu zweit** — wie Schuhe, die es
nur paarweise gibt.

**Der eine Sonderpunkt.** Die Stelle \( x_0 = 0 \) ist ihr **eigener** Spiegelpunkt (\( -0 = 0 \)). Sie
bildet kein Paar, sondern steht allein. Und sie **ist** ein Schnittpunkt, weil \( g(0)=0 \) und die
Gerade durch den Ursprung läuft. Zählt man zusammen: viele **Paare** (gerade Anzahl) plus der **eine**
Ursprung — macht zusammen eine **ungerade** Zahl. Eine gerade Zahl wie \( 266 \) kann nie herauskommen.

<details><summary>Typische Falle</summary>

Der ganze Beweis steht und fällt mit dem **Ursprungspunkt**. Würde \( g \) **nicht** durch den Ursprung
gehen (etwa bei \( f \) mit der Verschiebung \( -1 \)), wäre dieser eine Extrapunkt weg, und die Anzahl
könnte gerade sein. Genau deshalb ist die Aussage für \( g \) (Mittellinie \( y=0 \), durch den Ursprung)
formuliert — nicht für \( f \). Wer das übersieht, „beweist" die Behauptung für die falsche Funktion.

</details>
</details>

#### (2) Herleitung von \( \displaystyle\int_{-1}^{1} f(x)\,dx = -2 \) aus der Symmetrie

Zerlege \( f(x) = -3\sin(2x) - 1 \) im Integral in zwei Teile:

\[ \int_{-1}^{1} f\,dx = \underbrace{\int_{-1}^{1} -3\sin(2x)\,dx}_{(A)} \;+\; \underbrace{\int_{-1}^{1} (-1)\,dx}_{(B)}. \]

**Teil \( (A) \).** Der Sinusanteil \( -3\sin(2x) \) ist **ungerade** (punktsymmetrisch zum Ursprung).
Das Integral einer ungeraden Funktion über ein **zum Nullpunkt symmetrisches** Intervall \( [-1;\,1] \)
ist \( 0 \): Die Fläche links der \( y \)-Achse (über der Achse) ist genauso groß wie die Fläche rechts
(unter der Achse), mit umgekehrtem Vorzeichen — sie heben sich auf. Also \( (A) = 0 \).

**Teil \( (B) \).** Die konstante \( -1 \) erzeugt ein Rechteck der Höhe \( -1 \) über der Breite von
\( -1 \) bis \( 1 \) (Breite \( 2 \)):

\[ \int_{-1}^{1} (-1)\,dx = (-1)\cdot\big(1-(-1)\big) = (-1)\cdot 2 = -2. \]

Zusammen:

\[ \int_{-1}^{1} f\,dx = 0 + (-2) = \boxed{-2.} \]

<details><summary>Haltung dahinter: Warum ist das Integral einer ungeraden Funktion über \( [-a;a] \) null?</summary>

**Ungerade Funktion = punktsymmetrisch zum Ursprung.** Für \( -3\sin(2x) \) gilt: Wo der Graph links der
\( y \)-Achse **über** der \( x \)-Achse liegt, liegt er rechts spiegelbildlich gleich weit **unter** der
Achse (und umgekehrt).

**Integral zählt mit Vorzeichen.** Fläche über der Achse zählt positiv, Fläche unter der Achse negativ.
Auf \( [-1;\,0] \) liefert \( -3\sin(2x) \) ein positives Flächenstück, auf \( [0;\,1] \) ein genauso
großes negatives — beide haben denselben Betrag, aber entgegengesetztes Vorzeichen. Summe \( 0 \). Das
ist die „Symmetrie der Sinuskurve", auf die die Aufgabe abzielt: Der schwingende Anteil trägt über das
symmetrische Intervall **nichts** bei.

**Übrig bleibt der Sockel.** Nur die Verschiebung \( -1 \) zählt — und die ist ein simples Rechteck:
Höhe \( -1 \), Breite \( 2 \), Fläche \( -2 \). Anschauung: \( f \) pendelt um die Linie \( y=-1 \); über
das symmetrische Intervall mittelt sich das Pendeln weg, und es bleibt der mittlere Wert \( -1 \) mal die
Breite \( 2 \).

<details><summary>Ganz langsam (mit Zahlen): das Rechteck-Integral und das Vorzeichen</summary>

\( \int_{-1}^{1}(-1)\,dx \): Die Breite des Intervalls ist „rechte Grenze minus linke Grenze",
also \( 1 - (-1) \). Minus mal minus wird plus: \( 1 - (-1) = 1 + 1 = 2 \). Die Höhe ist \( -1 \). Fläche
\( = \) Höhe \( \cdot \) Breite \( = (-1)\cdot 2 = -2 \). Das Vorzeichen ist negativ, weil die konstante
Linie \( y=-1 \) **unter** der \( x \)-Achse liegt.

</details>

<details><summary>Typische Falle</summary>

Manche wollen für \( (A) \) doch eine Stammfunktion bilden — das ist erlaubt, aber unnötig und
fehleranfällig. Die Aufgabe sagt ausdrücklich „**ausgehend von der Symmetrie**": Der saubere Weg ist die
Aussage „ungerade Funktion über symmetrisches Intervall \( \Rightarrow 0 \)". Zweite Falle: die Breite
als \( 1 \) statt \( 2 \) ansetzen (das Intervall reicht von \( -1 \) bis \( 1 \), ist also \( 2 \) breit)
— dann käme fälschlich \( -1 \) heraus.

</details>
</details>
</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Teilaufgabe, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen kannst.
Du musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Stochastik) aufklappen</summary>

- **a) Wahrscheinlichkeit + gleiches Ereignis.** Erwartet: \( P(L<95)\approx 0{,}071 \) (Wert vom GTR/aus
  der Tabelle, mit Hinweis aufs Standardisieren) **und** das gespiegelte Ereignis \( L>105 \) mit
  Begründung über die **Symmetrie** der Glocke um \( 100 \). *Rückfrage:* „Warum hat \( L>105 \) genau
  dieselbe Wahrscheinlichkeit?" *Rote Flagge:* \( L<105 \) statt \( L>105 \).
- **b) \( \mu \) und \( \sigma \) ablesen.** Erwartet: \( \mu \) = **Maximumstelle** (\( =100 \));
  \( \sigma \) = Abstand von der **Wendestelle** zum Gipfel, \( x_2=\mu-\sigma \Rightarrow \sigma=3{,}4 \).
  *Rückfrage:* „Was ist eine Wendestelle, und wo liegt sie bei der Glocke?"
- **c) Graue Fläche deuten.** Erwartet: Die Fläche ist eine **Wahrscheinlichkeit**, nämlich
  \( P(96\le L\le 100) \) — „Länge zwischen \( 96 \) und \( 100 \) mm". *Rote Flagge:* die Fläche als
  Stückzahl statt als Wahrscheinlichkeit deuten.
- **d) 14 % begründen.** Erwartet: mangelhaft \( = L<95 \) oder \( L>105 \); \( p = 1-P(95\le L\le 105)
  \approx 0{,}141 \) (oder \( 0{,}071+0{,}071 \)). *Rückfrage:* „Welcher Bereich ist ‚nicht mangelhaft',
  und wie kommst du von ihm auf die \( 14\,\% \)?"
- **e) Term deuten.** Erwartet: \( X\sim B(200;\,0{,}14) \) als Stichprobe von \( 200 \) Teilen; die drei
  Summanden \( = P(X=200,199,198) \); Ereignis „**mindestens \( 198 \) mangelhaft**". *Rückfrage:* „Wofür
  steht der Faktor \( \binom{200}{2} \)?" *Rote Flagge:* \( 0{,}14 \) den **guten** Teilen zuordnen.

</details>

<details><summary>Leitfaden Teil 2 (Analysis) aufklappen</summary>

- **AB I — Eigenschaften & Zuordnung.** Erwartet: **Periode \( \pi \)** (Faktor \( 2 \) innen),
  **Amplitude \( 3 \)**, **Mittellinie \( y=-1 \)**, Werte \( [-4;\,2] \), \( f(0)=-1 \) **fallend**;
  Zuordnung zu **Abbildung 1**. *Rückfrage:* „Woran scheiden Abbildung 2, 3 und 4 jeweils aus?"
  *Rote Flagge:* Periode als \( 2\pi \); Abbildung 3 (steigend) gewählt.
- **AB II — Integral, Stammfunktion, Symmetrie von \( f' \).** Erwartet: \( \int_0^{3\pi/2} g\,dx = -3 \)
  mit Begründung „\( [\tfrac{\pi}{2};\tfrac{3\pi}{2}] \) ist **eine ganze Periode** \( \Rightarrow 0 \)";
  Stammfunktion \( F(x)=\tfrac32\cos(2x)-x \) (mit Ableitungsprobe); \( f'(x)=-6\cos(2x) \) ist
  **achsensymmetrisch** zur \( y \)-Achse. *Rückfrage:* „Warum nicht \( -9 \) beim Integral?" / „Woher
  kommt der Faktor \( \tfrac12 \) in der Stammfunktion?"
- **AB III — Schnittpunkt-Parität & \( \int_{-1}^{1} f = -2 \).** Erwartet: \( g \) ist **ungerade** und
  geht durch den **Ursprung**; Schnittpunkte abseits des Ursprungs **paarweise** \( \Rightarrow \) Summe
  ungerade, also nie \( 266 \). Beim Integral: Sinusanteil **ungerade** \( \Rightarrow 0 \) über
  \( [-1;1] \); Rechteck \( (-1)\cdot 2 = -2 \). *Rückfrage:* „Welche Rolle spielt der Ursprung bei der
  Schnittpunkt-Zahl?" *Hinweis für dich:* Die Symmetrie-Argumente sind die volle Antwort — langes Rechnen
  ist hier nicht nötig.

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Wie findest du zu \( P(L<95) \) ein gleich wahrscheinliches Ereignis — und warum funktioniert das?
- Woran erkennst du im Glockenkurven-Bild den Erwartungswert \( \mu \) und die Standardabweichung
  \( \sigma \)?
- Was bedeutet die graue Fläche zwischen \( 96 \) und \( 100 \) im Sachzusammenhang?
- Über welche zwei Wege kommst du auf die \( 14\,\% \) für „mangelhaft"?
- Wie liest du am Term \( f(x)=-3\sin(2x)-1 \) Periode, Amplitude, Mittellinie und das Verhalten bei
  \( x=0 \) ab — und welcher Graph gehört dazu?
- Warum ist \( \int_0^{3\pi/2} g\,dx = -3 \) und nicht \( -9 \)?
- Warum kann eine Ursprungsgerade die Sinuskurve \( g \) nie in gerade vielen Punkten schneiden, und
  warum ist \( \int_{-1}^{1} f\,dx = -2 \) ganz ohne Stammfunktion?
