# Grenzwerte (Limes) & Randverhalten im Zusammenhang

Wenn du in einer Kurvendiskussion das **Randverhalten** bestimmst — „Wohin läuft der Graph ganz links
und ganz rechts?" — dann rechnest du in Wahrheit **Grenzwerte**. Dieses Kapitel macht genau diesen
Zusammenhang sichtbar: Der **Limes** ist das saubere Werkzeug, mit dem sich das anschauliche
„Verhalten an den Rändern" exakt fassen lässt. Es geht hier eine Ebene tiefer als in den übrigen
Kapiteln — wenn du im Prüfungsgespräch nicht nur *was*, sondern auch *warum* sagen kannst, hebt dich
das deutlich. Alles rechnerfrei, wie in der mündlichen Prüfung.

## 1. Was ein Grenzwert ist — die Grundidee <span class="tag tag-ok">AB I–II</span>

Der Grenzwert beantwortet die Frage: **Welchem Wert nähert sich \( f(x) \), wenn \( x \) sich einer
Stelle nähert?** Man schreibt

\[ \lim_{x \to a} f(x) = L \]

und liest: „Der Limes von \( f(x) \) für \( x \) gegen \( a \) ist \( L \)." Gemeint ist: Je näher
\( x \) an \( a \) heranrückt, desto näher liegt \( f(x) \) an \( L \) — und zwar **beliebig** nah.

Bei den meisten Funktionen, mit denen du arbeitest, ist das einfach: Du darfst die Stelle **einsetzen**.

\[ \lim_{x \to 2} x^2 = 2^2 = 4 \]

<details><summary>Haltung dahinter: warum darf man einfach einsetzen?</summary>

Weil \( f(x)=x^2 \) **stetig** ist — der Graph hat keinen Sprung und kein Loch, du kannst ihn „ohne
abzusetzen" zeichnen. Bei einer stetigen Funktion ist der Wert, dem man sich nähert, genau der Wert an
der Stelle selbst. Deshalb ist Einsetzen erlaubt. Ganzrationale Funktionen, \( e^x \), \( \sin \) und
\( \cos \) sind überall stetig — bei ihnen ist die Grenzwertberechnung an einer „normalen" Stelle also
trivial.

<details><summary>Tiefer: das Einsetzen kann scheitern — die spannenden Fälle</summary>

Interessant wird der Grenzwert erst dort, wo Einsetzen **nicht** geht: an einer **Definitionslücke**
(z. B. Nenner null), bei einem **Sprung**, oder „am Rand" für \( x \to \pm\infty \), wo es gar keine
Stelle zum Einsetzen gibt. Genau diese Fälle behandeln die nächsten Abschnitte — und genau dort wohnt
das Randverhalten.

<details><summary>Noch eine Ebene tiefer: was „beliebig nahe" präzise meint</summary>

Mathematisch sauber heißt \( \lim_{x\to a} f(x)=L \): Gibst du mir eine noch so kleine **Toleranz** um
\( L \) vor (ein schmales waagerechtes Band um die Höhe \( L \)), dann finde ich immer eine genügend
kleine Umgebung um \( a \), in der der Graph **vollständig** in diesem Band bleibt. Egal wie eng du das
Band machst — ich kann die Umgebung um \( a \) klein genug wählen. Diese „für-jede-Toleranz-gibt-es-eine
-Umgebung"-Idee ist der Kern des Grenzwertbegriffs; im Basisfach brauchst du sie nicht formal
hinzuschreiben, aber sie erklärt, warum ein Grenzwert etwas anderes ist als ein bloßer Funktionswert.

</details>
</details>
</details>

## 2. Einseitige Grenzwerte <span class="tag tag-ok">AB II</span>

Man kann sich einer Stelle **von rechts** (\( x \to a^{+} \), größere \( x \)) oder **von links**
(\( x \to a^{-} \), kleinere \( x \)) nähern. Stimmen beide Seiten überein, existiert der Grenzwert.
Unterscheiden sie sich, existiert er **nicht**.

Klassisches Beispiel mit einem **Sprung**: \( f(x) = \dfrac{|x|}{x} \). Für \( x>0 \) ist das
\( +1 \), für \( x<0 \) ist es \( -1 \):

\[ \lim_{x \to 0^{+}} \frac{|x|}{x} = +1 \qquad\qquad \lim_{x \to 0^{-}} \frac{|x|}{x} = -1 \]

Die beiden Seiten sind verschieden — bei \( x=0 \) **existiert kein Grenzwert**. Der Graph springt von
\( -1 \) auf \( +1 \).

<details><summary>Haltung: warum die Richtung zählt</summary>

„Sich nähern" hat zwei Richtungen. Solange der Graph aus beiden Richtungen auf **dieselbe** Höhe
zuläuft, ist klar, welcher Wert gemeint ist. Laufen die Richtungen auf verschiedene Höhen (Sprung) oder
ins Unendliche, gibt es keinen einzelnen Wert — dann hilft nur die getrennte Betrachtung links/rechts.
Genau diese Trennung brauchst du an Definitionslücken (nächster Abschnitt).

</details>

## 3. Grenzwerte im Unendlichen = Randverhalten <span class="tag tag-ok">AB II</span>

Lässt man \( x \) nicht gegen eine Stelle, sondern **ins Unendliche** laufen, fragt man nach dem
Verhalten „ganz rechts" und „ganz links" — das **Randverhalten**:

\[ \lim_{x \to +\infty} f(x) \qquad\text{und}\qquad \lim_{x \to -\infty} f(x) \]

Das ist exakt der Schritt „Verhalten im Unendlichen" aus der Kurvendiskussion — nur mit dem richtigen
Namen. Die wichtigsten Bausteine:

- **Ganzrationale Funktion (Polynom):** Allein der **Term höchsten Grades** entscheidet. Für
  \( f(x)=2x^3-3x^2+4 \) zählt nur \( 2x^3 \): \( \lim_{x\to+\infty} f(x)=+\infty \),
  \( \lim_{x\to-\infty} f(x)=-\infty \) (ungerader Grad → „über Kreuz").
- **e-Funktion:** \( \lim_{x\to+\infty} e^{x}=+\infty \) und \( \lim_{x\to-\infty} e^{x}=0^{+} \).
- **Sinus/Cosinus:** \( \lim_{x\to\pm\infty}\sin(x) \) **existiert nicht** — der Wert pendelt für immer
  zwischen \( -1 \) und \( 1 \), nähert sich also keiner festen Zahl.

<details><summary>Haltung: warum nur der höchste Grad zählt</summary>

Klammere bei \( 2x^3-3x^2+4 \) den höchsten Term aus:
\( x^3\big(2-\tfrac{3}{x}+\tfrac{4}{x^3}\big) \). Für große \( |x| \) gehen \( \tfrac{3}{x} \) und
\( \tfrac{4}{x^3} \) gegen \( 0 \); in der Klammer bleibt praktisch \( 2 \) übrig. Es bleibt also
\( \approx 2x^3 \) — der Rest ist im Vergleich winzig. Deshalb darfst du beim Randverhalten eines
Polynoms alle kleineren Glieder ignorieren.

</details>

<details><summary>Typische Falle: \( \sin \) und \( \cos \) haben keinen Grenzwert im Unendlichen</summary>

Verlockend ist die Antwort „geht gegen \( 0 \)" oder „bleibt bei \( 1 \)" — beides falsch. Eine
Schwingung kommt **keiner** festen Höhe beliebig nahe, sie wiederholt sich endlos. Die korrekte Aussage
im Prüfungsgespräch lautet: „Der Grenzwert existiert nicht, weil die Funktion beschränkt zwischen
\( -1 \) und \( 1 \) oszilliert."

</details>

## 4. Uneigentliche Grenzwerte & Asymptoten <span class="tag tag-ok">AB II–III</span>

Wenn \( f(x) \) über alle Grenzen wächst, schreibt man \( \lim f(x) = +\infty \) (bzw. \( -\infty \))
und nennt das einen **uneigentlichen Grenzwert** — „uneigentlich", weil \( \infty \) keine Zahl ist,
sondern eine Richtung. Geometrisch erzeugen Grenzwerte die **Asymptoten**:

- **Waagerechte Asymptote** \( y=c \): wenn \( \lim_{x\to+\infty} f(x)=c \) (oder für \( x\to-\infty \)).
  Der Graph schmiegt sich für große \( |x| \) an die Höhe \( c \) an.
- **Senkrechte Asymptote** \( x=a \): wenn \( f(x) \) für \( x\to a \) gegen \( \pm\infty \) läuft (an
  einer Definitionslücke). Beispiel \( \tfrac{1}{x} \): \( \lim_{x\to 0^{+}}\tfrac{1}{x}=+\infty \),
  \( \lim_{x\to 0^{-}}\tfrac{1}{x}=-\infty \). <span class="tag tag-warn">gebrochenrational: offiziell Leistungsfach [97 %] — mit Lehrkraft prüfen</span>

Hier eine Funktion mit **waagerechter Asymptote** \( y=2 \): \( g(x)=2-e^{-x} \). Für \( x\to+\infty \)
geht \( e^{-x}\to 0 \), also \( g(x)\to 2 \) (gestrichelte Linie). Nach links wächst \( e^{-x} \), und
\( g \) fällt ins Negative.

<div class="jxgbox" id="jxg-hasymp" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-hasymp',{boundingbox:[-1.2,3,5.2,-1.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 2;},-1.2,5.2],{strokeColor:'#d98324',strokeWidth:1.5,dash:2});b.create('functiongraph',[function(x){return 2-Math.exp(-x);},-1.2,5],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('text',[3.1,2.25,'y = 2'],{fontSize:13,color:'#d98324'});})();</script>

<details><summary>Haltung: eine Asymptote wird berührt, nie erreicht</summary>

„Asymptote" heißt: Der Abstand zwischen Graph und Gerade wird **beliebig klein**, ohne je \( 0 \) zu
werden. Bei \( g(x)=2-e^{-x} \) ist der Abstand zur Linie \( y=2 \) genau \( e^{-x} \) — das ist für
jedes \( x \) echt positiv, geht aber für \( x\to+\infty \) gegen \( 0 \). Genau das ist die
Grenzwertaussage \( \lim_{x\to+\infty} g(x)=2 \), in Bildsprache übersetzt.

<details><summary>Tiefer: Asymptote als „Grenzgerade" formulieren</summary>

Eine waagerechte Asymptote ist nichts anderes als der Grenzwert im Unendlichen, geometrisch gelesen.
Im Prüfungsgespräch kannst du beides verbinden: „Da \( \lim_{x\to+\infty} g(x)=2 \), nähert sich der
Graph der Geraden \( y=2 \) beliebig an; \( y=2 \) ist also waagerechte Asymptote." Damit zeigst du,
dass Limes und Asymptote dieselbe Sache aus zwei Blickwinkeln sind.

</details>
</details>

## 5. Mit Grenzwerten rechnen — die Grenzwertsätze <span class="tag tag-ok">AB II</span>

Existieren \( \lim f(x)=A \) und \( \lim g(x)=B \), so darf man Grenzwerte **gliedweise** behandeln:

\[ \lim\big(f\pm g\big)=A\pm B,\qquad \lim\big(f\cdot g\big)=A\cdot B,\qquad \lim\frac{f}{g}=\frac{A}{B}\ (B\neq 0) \]

Ein konstanter Faktor bleibt erhalten: \( \lim\big(c\cdot f\big)=c\cdot A \).

\[ \lim_{x\to 3}\frac{x^2+1}{x-1}=\frac{3^2+1}{3-1}=\frac{10}{2}=5 \]

<details><summary>Haltung: erst einsetzen, und nur wenn es „klemmt", genauer hinsehen</summary>

Solange der Nenner an der Stelle nicht \( 0 \) wird, liefern die Grenzwertsätze einfach das Einsetzen —
wie oben \( 5 \). Erst wenn beim Einsetzen etwas Verbotenes entsteht (Nenner \( 0 \), \( \infty\cdot 0 \),
\( \tfrac{\infty}{\infty} \)), musst du umformen, ausklammern oder die Dominanz (nächster Abschnitt)
bemühen. Die Sätze sagen dir also, *wann* du bedenkenlos einsetzen darfst.

</details>

## 6. Dominanz: \( e^{x} \) schlägt jede Potenz <span class="tag tag-ok">AB III</span>

Manche Grenzwerte sehen nach einem „Patt" aus — ein Faktor will nach \( \infty \), der andere nach
\( 0 \). Dann entscheidet, **wer schneller ist**. Die zentrale Regel der Analysis:

> Die e-Funktion wächst (und fällt) schneller als jede Potenz von \( x \).

Daraus folgt das wichtigste Beispiel — es taucht bei fast jeder e-Funktions-Aufgabe auf:

\[ \lim_{x\to+\infty} x\,e^{-x}=0 \]

Zwar wächst \( x \) gegen \( \infty \), aber \( e^{-x} \) **fällt schneller** gegen \( 0 \) — das
Produkt wird winzig. Im Bild: Der Graph steigt kurz an (Maximum bei \( x=1 \), Höhe \( \tfrac{1}{e}\approx 0{,}37 \))
und sinkt dann unaufhaltsam gegen die \( x \)-Achse.

<div class="jxgbox" id="jxg-dom" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-dom',{boundingbox:[-0.4,0.55,6.3,-0.1],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return x*Math.exp(-x);},0,6.2],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[1,1/Math.E],{name:'Max (1|1/e)',size:2,fixed:true,color:'#d98324'});})();</script>

<details><summary>Haltung: woran man die Dominanz erkennt</summary>

Steht ein Produkt aus „Potenz mal e-Term" und läuft \( x \) so, dass der e-Term gegen \( 0 \) geht
(also \( e^{-x} \) für \( x\to+\infty \), oder \( e^{x} \) für \( x\to-\infty \)), dann **gewinnt der
e-Term**: Das ganze Produkt geht gegen \( 0 \). Geht der e-Term gegen \( \infty \), gewinnt er ebenfalls
und das Produkt geht gegen \( \pm\infty \). Merksatz: *„Im Zweifel entscheidet die e-Funktion."*

<details><summary>Tiefer: das zweite Standardbeispiel und die allgemeine Form</summary>

Dieselbe Dominanz, andere Richtung: \( \lim_{x\to-\infty} x^2 e^{x}=0 \). Hier geht \( x^2\to+\infty \),
aber \( e^{x}\to 0 \) (für \( x\to-\infty \)) — und schlägt das \( x^2 \). Allgemein gilt für jede
Potenz \( x^n \): \( \lim_{x\to+\infty} x^{n} e^{-x}=0 \) und \( \lim_{x\to-\infty} x^{n} e^{x}=0 \).
Genau deshalb hat z. B. \( f(x)=x^2 e^{x} \) nach links die waagerechte Asymptote \( y=0 \).

</details>
</details>

## 7. Randverhalten in der Kurvendiskussion — der rote Faden <span class="tag tag-ok">AB II</span>

Jetzt fügt sich alles zusammen. Wenn du in der Kurvendiskussion das **Randverhalten** angibst, führst
du genau diese Grenzwerte aus — und liest daraus die Asymptoten und die Skizze ab. Vollständiges
Beispiel: \( f(x)=(x-1)\,e^{x} \).

- **Nach rechts** (\( x\to+\infty \)): \( (x-1)\to+\infty \) und \( e^{x}\to+\infty \), also
  \( \lim_{x\to+\infty} f(x)=+\infty \) — der Graph läuft oben rechts davon.
- **Nach links** (\( x\to-\infty \)): \( (x-1)\to-\infty \), aber \( e^{x}\to 0 \) und **dominiert**:
  \( \lim_{x\to-\infty} (x-1)e^{x}=0 \). Der Graph schmiegt sich von unten an die \( x \)-Achse an —
  **waagerechte Asymptote \( y=0 \)** nach links.

<details><summary>Haltung: warum das Randverhalten den ersten Strich der Skizze vorgibt</summary>

Bevor du Hoch-, Tief- und Wendepunkte berechnest, weißt du allein aus dem Randverhalten schon, „wo der
Graph herkommt und wohin er geht": links flach aus der \( x \)-Achse heraus (von unten, da das Produkt
nahe \( 0 \) negativ ist), rechts steil nach oben. Dieses Gerüst füllst du dann mit den markanten
Punkten. Im Prüfungsgespräch ist es stark, wenn du das Randverhalten zuerst nennst und die übrige
Analyse darin einordnest.

</details>

→ Vertiefe die Anwendung im Kapitel **Funktionsuntersuchung** (Schritt „Randverhalten") und bei den
Grundfunktionen (Verhalten im Unendlichen je Bausteinfunktion).

## 8. Überblick: typische Grenzwerte auf einen Blick

| Ausdruck | Grenzwert | Merke |
|---|---|---|
| \( \lim\limits_{x\to a} f(x) \), \( f \) stetig | \( f(a) \) | einfach einsetzen |
| \( \lim\limits_{x\to+\infty} x^n \) | \( +\infty \) | Potenz wächst über alle Grenzen |
| \( \lim\limits_{x\to+\infty} e^{x} \) | \( +\infty \) | e-Funktion explodiert |
| \( \lim\limits_{x\to-\infty} e^{x} \) | \( 0^{+} \) | waagerechte Asymptote \( y=0 \) |
| \( \lim\limits_{x\to+\infty} e^{-x} \) | \( 0^{+} \) | fällt gegen die Achse |
| \( \lim\limits_{x\to+\infty} x\,e^{-x} \) | \( 0 \) | e schlägt Potenz |
| \( \lim\limits_{x\to\pm\infty} \sin x \) | existiert nicht | oszilliert zwischen \( -1 \) und \( 1 \) |
| \( \lim\limits_{x\to 0^{\pm}} \tfrac{1}{x} \) | \( \pm\infty \) | senkrechte Asymptote (LF) |

<details><summary>Selbsttest & Prüfungsgespräch: laut erklären</summary>

Decke die mittlere Spalte ab und sprich jeden Grenzwert samt **Begründung** aus — genau so wird im
Gespräch gefragt. Drei Sätze, die sitzen sollten:

- „Bei einer stetigen Funktion ist der Grenzwert der Funktionswert — ich darf einsetzen."
- „\( \sin \) hat keinen Grenzwert im Unendlichen, weil die Funktion beschränkt oszilliert."
- „Bei einem Produkt aus Potenz und e-Term entscheidet die e-Funktion — sie dominiert."

Wer diese drei Begründungen frei sprechen kann, beherrscht den Zusammenhang von Limes und Randverhalten
auf Prüfungsniveau.

</details>
