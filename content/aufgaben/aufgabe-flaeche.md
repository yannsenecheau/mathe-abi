# Aufgabe: Fläche & Bestand

Diese Aufgabe ist nah an dem, was dich in der mündlichen Prüfung erwartet. Sie hat drei Teile,
die aufeinander aufbauen: erst die Fläche zwischen einem Graphen und der \( x \)-Achse, dann die Fläche
<b>zwischen zwei Graphen</b>, und am Ende eine <b>Bestands-Rekonstruktion</b> aus einer Änderungsrate.
Alles rechnerfrei — also alles per Hand, ohne Taschenrechner.

<div class="meta-row">
<span>Schwerpunkt: Integralrechnung</span>
<span>Hilfsmittel: keine (rechnerfrei)</span>
<span>Tipp: erst selbst rechnen, dann aufklappen</span>
</div>

> So nutzt du die Aufgabe: Lies die Teilaufgabe, rechne <b>zuerst selbst</b> auf einem Blatt, und klappe
> erst danach die Lösung auf. Achte besonders auf die <i>Haltung</i>-Kästen — dort steht, <b>warum</b>
> ein Schritt gemacht wird und welche Falle dabei lauert.

## Teil A — Fläche zwischen Graph und x-Achse <span class="tag tag-ok">AB I</span>

Gegeben ist die Funktion \( f(x) = 4 - x^2 \). Berechne den Inhalt der Fläche, die der Graph von \( f \)
mit der \( x \)-Achse einschließt.

<div class="jxgbox" id="jxg-flaeche-a" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-flaeche-a',{boundingbox:[-3.2,5.2,3.2,-1.6],axis:true,showCopyright:false,showNavigation:false});var f=function(x){return 4-x*x;};var fill=b.create('curve',[[],[]],{fillColor:'#d98324',fillOpacity:0.25,strokeOpacity:0});fill.updateDataArray=function(){var xs=[],ys=[],n=60,i,x;for(i=0;i<=n;i++){x=-2+4*i/n;xs.push(x);ys.push(f(x));}xs.push(2);ys.push(0);xs.push(-2);ys.push(0);this.dataX=xs;this.dataY=ys;};b.create('functiongraph',[f,-3,3],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[-2,0],{name:'',size:2,fixed:true,color:'#3a5a9c'});b.create('point',[2,0],{name:'',size:2,fixed:true,color:'#3a5a9c'});b.update();})();</script>

<details><summary>Schritt 1 — Wo schneidet der Graph die x-Achse? (Grenzen finden)</summary>

Die Fläche „mit der \( x \)-Achse" wird von den <b>Nullstellen</b> begrenzt. Wir setzen also
\( f(x) = 0 \):

\[ 4 - x^2 = 0 \;\Longleftrightarrow\; x^2 = 4 \;\Longleftrightarrow\; x = \pm 2. \]

Die Integrationsgrenzen sind damit \( a = -2 \) und \( b = 2 \).

<details><summary>Haltung dahinter: warum erst die Nullstellen?</summary>

Ein bestimmtes Integral braucht immer <b>untere und obere Grenze</b>. Wenn nach der Fläche „mit der
\( x \)-Achse" gefragt ist, sind das genau die Stellen, an denen der Graph die \( x \)-Achse trifft —
sonst wäre gar nicht festgelegt, <i>wie weit</i> wir messen. <b>Typische Falle:</b> einfach von \( 0 \)
bis irgendwo zu integrieren, ohne die Nullstellen zu bestimmen.

</details>
</details>

<details><summary>Schritt 2 — Stammfunktion bilden</summary>

Wir suchen ein \( F \) mit \( F'(x) = 4 - x^2 \). Term für Term mit der Potenzregel für Stammfunktionen
(Exponent um \( 1 \) erhöhen, durch den neuen Exponenten teilen):

\[ F(x) = 4x - \tfrac{1}{3}x^3. \]

<details><summary>Haltung dahinter: Probe durch Ableiten</summary>

Eine Stammfunktion prüfst du <b>immer</b> durch Rückwärts-Ableiten:
\( F'(x) = 4 - \tfrac{1}{3}\cdot 3x^2 = 4 - x^2 = f(x). \) Passt. <b>Typische Falle:</b> das Teilen durch
den neuen Exponenten vergessen, also fälschlich \( x^3 \) statt \( \tfrac{1}{3}x^3 \) schreiben.

</details>
</details>

<details><summary>Schritt 3 — Hauptsatz anwenden und ausrechnen</summary>

Nach dem Hauptsatz gilt \( \displaystyle\int_a^b f(x)\,dx = F(b) - F(a) \):

\[ \int_{-2}^{2} (4 - x^2)\,dx = F(2) - F(-2). \]

Die Werte einzeln, von Hand:

\[ F(2) = 4\cdot 2 - \tfrac{1}{3}\cdot 2^3 = 8 - \tfrac{8}{3} = \tfrac{24 - 8}{3} = \tfrac{16}{3}, \]

\[ F(-2) = 4\cdot(-2) - \tfrac{1}{3}\cdot(-2)^3 = -8 + \tfrac{8}{3} = -\tfrac{16}{3}. \]

Also:

\[ F(2) - F(-2) = \tfrac{16}{3} - \left(-\tfrac{16}{3}\right) = \tfrac{32}{3} \approx 10{,}67. \]

Die eingeschlossene Fläche hat den Inhalt \( \dfrac{32}{3} \) Flächeneinheiten.

<details><summary>Haltung dahinter: Vorzeichen-Falle und Symmetrie-Kontrolle</summary>

Hier ist \( f \) auf \( [-2,2] \) durchgehend \( \ge 0 \) (die Parabel ist nach unten geöffnet, Scheitel
bei \( (0,4) \)), darum sind Integral und Flächeninhalt <b>gleich</b>. Läge der Graph unter der
\( x \)-Achse, wäre das Integral negativ und du müsstest den Betrag nehmen. <b>Schnelle Kontrolle:</b>
\( f \) ist achsensymmetrisch zur \( y \)-Achse, also \( \int_{-2}^{2} = 2\int_{0}^{2} \). Und
\( 2\cdot(F(2)-F(0)) = 2\cdot\tfrac{16}{3} = \tfrac{32}{3} \). Gleiches Ergebnis — gutes Zeichen.

</details>
</details>

## Teil B — Fläche zwischen zwei Graphen <span class="tag tag-ok">AB II</span>

Gegeben sind \( f(x) = 4 - x^2 \) und die Gerade \( g(x) = x + 2 \). Berechne den Inhalt der Fläche, die
die beiden Graphen einschließen.

<div class="jxgbox" id="jxg-flaeche-b" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-flaeche-b',{boundingbox:[-3.4,5.4,2.6,-2.2],axis:true,showCopyright:false,showNavigation:false});var f=function(x){return 4-x*x;};var g=function(x){return x+2;};b.create('functiongraph',[f,-3.2,2.4],{strokeColor:'#3a5a9c',strokeWidth:2.5,name:'f',withLabel:true});b.create('functiongraph',[g,-3.2,2.4],{strokeColor:'#5a8f69',strokeWidth:2.5,name:'g',withLabel:true});b.create('curve',[function(t){return t;},function(t){return g(t);},-2,1],{visible:false});var c=b.create('curve',[[],[]],{fillColor:'#d98324',fillOpacity:0.25,strokeOpacity:0});c.updateDataArray=function(){var xs=[],ys=[],n=60,i,x;for(i=0;i<=n;i++){x=-2+3*i/n;xs.push(x);ys.push(f(x));}for(i=n;i>=0;i--){x=-2+3*i/n;xs.push(x);ys.push(g(x));}this.dataX=xs;this.dataY=ys;};b.update();b.create('point',[-2,0],{name:'',size:2,fixed:true,color:'#444'});b.create('point',[1,3],{name:'',size:2,fixed:true,color:'#444'});})();</script>

<details><summary>Schritt 1 — Schnittstellen bestimmen (die Grenzen)</summary>

Die Fläche wird dort begrenzt, wo sich beide Graphen treffen, also wo \( f(x) = g(x) \):

\[ 4 - x^2 = x + 2 \;\Longleftrightarrow\; -x^2 - x + 2 = 0 \;\Longleftrightarrow\; x^2 + x - 2 = 0. \]

Mit Satz von Vieta (zwei Zahlen mit Produkt \( -2 \) und Summe \( -1 \)) faktorisieren wir rechnerfrei:

\[ x^2 + x - 2 = (x + 2)(x - 1) = 0 \;\Longrightarrow\; x = -2 \ \text{oder}\ x = 1. \]

Die Grenzen sind \( a = -2 \) und \( b = 1 \).

<details><summary>Haltung dahinter: warum gleichsetzen und nicht raten</summary>

Zwei Graphen schließen genau zwischen ihren <b>Schnittstellen</b> eine Fläche ein — vorher und nachher
laufen sie auseinander. Darum ist Gleichsetzen der erste Schritt. <b>Typische Falle:</b> die Gleichung
in der Form \( -x^2 - x + 2 = 0 \) stehen lassen; mit negativem führenden Koeffizienten verrechnet man
sich leicht. Erst mit \( (-1) \) multiplizieren, dann faktorisieren.

</details>
</details>

<details><summary>Schritt 2 — Differenzfunktion: oben minus unten</summary>

Für die Fläche zwischen zwei Graphen integrieren wir die <b>Differenz</b> „obere minus untere
Funktion". Zwischen \( -2 \) und \( 1 \) liegt die Parabel \( f \) <b>über</b> der Geraden \( g \) (prüfe
es mit einem Zwischenwert, z. B. \( x = 0 \): \( f(0) = 4 \), \( g(0) = 2 \), also \( f > g \)). Damit:

\[ d(x) = f(x) - g(x) = (4 - x^2) - (x + 2) = -x^2 - x + 2. \]

<details><summary>Haltung dahinter: Reihenfolge oben/unten und der Betrag</summary>

Welche Funktion oben liegt, entscheidet das Vorzeichen. Integrierst du „oben minus unten", kommt
direkt eine <b>positive</b> Fläche heraus. <b>Typische Falle:</b> die Reihenfolge vertauschen — dann
erhältst du genau das negative Ergebnis. Mit einem einzigen Zwischenwert ist die Reihenfolge sicher
geklärt, ein Skizzieren genügt.

</details>
</details>

<details><summary>Schritt 3 — Integrieren und einsetzen</summary>

Stammfunktion der Differenz \( d(x) = -x^2 - x + 2 \):

\[ D(x) = -\tfrac{1}{3}x^3 - \tfrac{1}{2}x^2 + 2x. \]

Jetzt die Grenzen einsetzen, jeden Wert sauber als Bruch:

\[ D(1) = -\tfrac{1}{3} - \tfrac{1}{2} + 2 = \tfrac{-2 - 3 + 12}{6} = \tfrac{7}{6}, \]

\[ D(-2) = -\tfrac{1}{3}(-8) - \tfrac{1}{2}(4) + 2(-2) = \tfrac{8}{3} - 2 - 4 = \tfrac{8 - 18}{3} = -\tfrac{10}{3}. \]

Differenz:

\[ \int_{-2}^{1} d(x)\,dx = D(1) - D(-2) = \tfrac{7}{6} - \left(-\tfrac{10}{3}\right) = \tfrac{7}{6} + \tfrac{20}{6} = \tfrac{27}{6} = \tfrac{9}{2} = 4{,}5. \]

Die eingeschlossene Fläche hat den Inhalt \( \dfrac{9}{2} = 4{,}5 \) Flächeneinheiten.

<details><summary>Haltung dahinter: gemeinsamer Nenner statt Dezimalbrüche</summary>

Rechnerfrei ist Bruchrechnung dein Freund: Bring alles auf einen gemeinsamen Nenner (\( 6 \) bzw.
\( 3 \)), dann ist das Ergebnis exakt. <b>Typische Falle:</b> mit gerundeten Dezimalzahlen rechnen und
am Ende einen „krummen" Wert erhalten — in der Prüfung ist der saubere Bruch \( \tfrac{9}{2} \) das,
was zählt.

</details>
</details>

## Teil C — Bestand aus einer Änderungsrate <span class="tag tag-ok">AB II</span>

In einen Wassertank fließt Wasser. Die <b>Zuflussrate</b> beträgt \( r(t) = 6 - 2t \) (in Litern pro
Minute) für \( t \in [0;\,3] \) Minuten. Zu Beginn (\( t = 0 \)) sind bereits \( 10 \) Liter im Tank.

<b>a)</b> Wie viel Wasser fließt in den ersten \( 3 \) Minuten <i>insgesamt</i> hinzu?<br>
<b>b)</b> Wie lautet die Bestandsfunktion \( B(t) \), und wie viel Wasser ist nach \( 3 \) Minuten im
Tank?

<details><summary>Schritt 1 — Was bedeutet „Bestand aus Änderungsrate"?</summary>

\( r(t) \) ist eine <b>Rate</b> (Liter <i>pro Minute</i>), also die Ableitung des Bestands. Die
zugeflossene Wassermenge bekommen wir, indem wir die Rate über die Zeit <b>aufintegrieren</b>:

\[ \text{Zufluss in } [0; t] = \int_0^t r(s)\,ds. \]

<details><summary>Haltung dahinter: Rate integrieren ⇒ Menge</summary>

Eine Rate \( \times \) Zeit ergibt eine Menge — das Integral ist die „unendlich feine" Summe genau
dieser kleinen Mengen \( r(s)\,ds \). <b>Typische Falle:</b> die Rate mit dem Bestand verwechseln und
\( r(3) \) als Antwort hinschreiben. \( r(3) = 0 \) ist nur die <i>momentane</i> Zuflussrate am Ende,
nicht die im Tank befindliche Menge.

</details>
</details>

<details><summary>Schritt 2 (a) — Gesamtzufluss in 3 Minuten berechnen</summary>

\[ \int_0^3 (6 - 2t)\,dt = \big[\,6t - t^2\,\big]_0^3 = (6\cdot 3 - 3^2) - 0 = 18 - 9 = 9. \]

In den ersten \( 3 \) Minuten fließen also <b>\( 9 \) Liter</b> hinzu.

<details><summary>Haltung dahinter: Probe über die Fläche</summary>

\( r(t) = 6 - 2t \) ist eine Gerade von \( r(0) = 6 \) bis \( r(3) = 0 \). Die Fläche darunter ist ein
Dreieck mit Grundseite \( 3 \) und Höhe \( 6 \), also \( \tfrac{1}{2}\cdot 3\cdot 6 = 9 \). Gleiches
Ergebnis ohne Stammfunktion — eine starke rechnerfreie Kontrolle. <b>Falle:</b> die Dreiecksformel nur
anwenden, wenn die Rate wirklich linear ist.

</details>
</details>

<details><summary>Schritt 3 (b) — Bestandsfunktion aufstellen und auswerten</summary>

Der Bestand ist der Anfangswert plus alles, was bis zum Zeitpunkt \( t \) hinzugekommen ist:

\[ B(t) = B(0) + \int_0^t (6 - 2s)\,ds = 10 + \big[\,6s - s^2\,\big]_0^t = 10 + 6t - t^2. \]

Einsetzen von \( t = 3 \):

\[ B(3) = 10 + 6\cdot 3 - 3^2 = 10 + 18 - 9 = 19. \]

Nach \( 3 \) Minuten sind <b>\( 19 \) Liter</b> im Tank.

<details><summary>Haltung dahinter: die Integrationskonstante ist der Anfangsbestand</summary>

\( B \) ist eine Stammfunktion von \( r \), und die Konstante legt der Startwert fest: \( B(0) = 10 \).
Genau deshalb erscheint die \( 10 \) als fester Summand. <b>Typische Falle:</b> den Anfangsbestand
vergessen und nur \( 6t - t^2 \) hinschreiben — das wäre der reine Zufluss, nicht der Bestand.

<details><summary>Noch tiefer: Zusammenhang Rate, Zufluss, Bestand</summary>

Es gilt \( B'(t) = r(t) \): die Bestandsfunktion abgeleitet ergibt wieder die Rate
(\( B'(t) = 6 - 2t = r(t) \), Probe bestanden). Weil \( r(t) \ge 0 \) auf ganz \( [0;3] \) ist (Wasser
fließt nur zu, nie ab), <b>wächst</b> der Bestand durchgehend; sein Maximum auf dem Intervall liegt
daher am rechten Rand \( t = 3 \) mit \( 19 \) Litern.

</details>
</details>
</details>

## Wie du diese Aufgabe für die Prüfung nutzt

Das mündliche Prüfungsgespräch dreht sich oft weniger um das Endergebnis als um <b>deine Begründung</b>.
Übe darum, jeden Teil <b>laut zu erklären</b>:

- In Teil A: „Ich brauche die Nullstellen als Grenzen, weil …"
- In Teil B: „Ich integriere oben minus unten, also \( f - g \), weil …"
- In Teil C: „Die Rate integriere ich, um die Menge zu bekommen; den Startwert \( 10 \) addiere ich,
  weil …"

> Selbsttest: Klappe alle Lösungen zu und rechne die drei Teile auf einem leeren Blatt komplett durch.
> Wenn du an einer Stelle hängst, schau <b>nur</b> in den passenden Haltung-Kasten und versuche es
> erneut. Sprich danach eine kurze Sprachnachricht: Welcher Teil ging flüssig, wo hast du
> nachgeschaut?
