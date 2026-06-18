# Grundfunktionen & ihre Ableitungen

Dieses Kapitel ist dein Werkzeugkasten. Fast jede Aufgabe der Analysis besteht aus diesen
wenigen Bausteinen — ganzrationale Funktionen, die e-Funktion, Sinus und Cosinus, dazu zwei
Spezialfälle. Wenn du von jeder Funktion das **Aussehen**, das **Verhalten im Unendlichen** und die
**Ableitung** im Kopf hast, kannst du im Prüfungsgespräch ruhig und sicher argumentieren. Alles hier
rechnest du von Hand — kein Taschenrechner, genau wie in deiner mündlichen Prüfung.

Eine Sache vorweg, die alle Bausteine verbindet: Die **Ableitung** \( f'(x) \) gibt die **Steigung**
des Graphen an der Stelle \( x \) an. Geometrisch ist \( f'(x_0) \) die Steigung der Tangente im
Punkt \( (x_0\mid f(x_0)) \). Diese eine Idee zieht sich durch das ganze Kapitel.

## Die Potenzregel — das Fundament <span class="tag tag-ok">AB I</span>

Bevor wir einzelne Funktionen anschauen, brauchst du eine einzige Regel, aus der sich fast alles
ableitet. Für eine Potenz \( f(x) = x^n \) gilt:

\[ f(x) = x^n \quad\Longrightarrow\quad f'(x) = n\,x^{\,n-1} \]

In Worten: Der Exponent kommt **als Faktor nach vorne**, und der neue Exponent ist um \( 1 \)
**kleiner**.

<details><summary>Haltung dahinter: warum „Exponent runter, dann minus eins"?</summary>

Die Ableitung misst, wie schnell sich \( f \) ändert. Bei \( x^2 \) wächst die Fläche eines Quadrats
mit Seitenlänge \( x \): Vergrößerst du \( x \) ein winziges Stück, kommen an **zwei** Seiten
Streifen dazu — daher der Faktor \( 2 \) in \( f'(x) = 2x \). Bei \( x^3 \) (Volumen eines Würfels)
kommen an **drei** Flächen Schichten dazu — daher \( 3x^2 \). Das Muster „Exponent als Faktor" ist
also kein Trick, sondern beschreibt, an wie vielen „Seiten" das Wachstum gleichzeitig passiert.

<details><summary>Tiefer: Herleitung über den Differenzenquotienten (für \( x^2 \))</summary>

Die Ableitung ist der Grenzwert des Differenzenquotienten:

\[ f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} \]

Für \( f(x) = x^2 \) rechnen wir den Zähler von Hand aus:

\[ (x+h)^2 - x^2 = x^2 + 2xh + h^2 - x^2 = 2xh + h^2 = h\,(2x + h) \]

Geteilt durch \( h \) bleibt \( 2x + h \). Lässt man nun \( h \) gegen \( 0 \) gehen, fällt das
\( h \) weg und es bleibt \( f'(x) = 2x \). Das ist die Potenzregel für \( n = 2 \), von Hand
nachgerechnet.

</details>
</details>

Zwei Helfer, die du ständig brauchst:

- **Faktorregel:** Ein konstanter Faktor bleibt beim Ableiten stehen: \( \big(c\cdot f\big)' = c\cdot f' \).
- **Summenregel:** Eine Summe wird gliedweise abgeleitet: \( \big(f+g\big)' = f' + g' \).

<details><summary>Typische Falle: die Ableitung einer Konstanten</summary>

Eine Konstante wie \( 7 \) hat die Ableitung \( 0 \) — ein waagerechter Graph hat überall die
Steigung \( 0 \). Schreibe \( 7 = 7x^0 \), dann liefert die Potenzregel \( 0\cdot 7x^{-1} = 0 \).
Ebenso: \( (x)' = 1 \), denn \( x = x^1 \) und \( 1\cdot x^0 = 1 \). Diese beiden vergisst man unter
Prüfungsdruck am leichtesten.

</details>

## Ganzrationale Funktionen (Polynome) <span class="tag tag-ok">AB I–II</span>

Eine **ganzrationale Funktion** (Polynom) ist eine Summe von Potenzen von \( x \) mit Zahlfaktoren,
zum Beispiel:

\[ f(x) = 2x^3 - 3x^2 + 4 \]

Der **Grad** ist der höchste vorkommende Exponent (hier \( 3 \)). Den Grad solltest du sofort
erkennen — er bestimmt das grobe Aussehen und das Verhalten im Unendlichen.

### Ableiten — gliedweise mit Potenz-, Faktor- und Summenregel

Wir leiten \( f(x) = 2x^3 - 3x^2 + 4 \) Glied für Glied ab:

\[ f'(x) = 2\cdot 3x^2 \;-\; 3\cdot 2x \;+\; 0 \;=\; 6x^2 - 6x \]

<details><summary>Schritt für Schritt nachvollzogen</summary>

- \( 2x^3 \): Exponent \( 3 \) nach vorne, neuer Exponent \( 2 \): \( 2\cdot 3\,x^{2} = 6x^2 \).
- \( -3x^2 \): \( -3\cdot 2\,x^{1} = -6x \).
- \( +4 \): konstant, Ableitung \( 0 \).

Zusammen: \( f'(x) = 6x^2 - 6x \). Du kannst noch \( 6x \) ausklammern: \( f'(x) = 6x(x-1) \) — diese
faktorisierte Form ist Gold wert, wenn du gleich die Nullstellen von \( f' \) (also Extremstellen von
\( f \)) suchst.

<details><summary>Haltung: warum ist die faktorisierte Form so nützlich?</summary>

Ein Produkt ist genau dann \( 0 \), wenn **einer der Faktoren** \( 0 \) ist (Satz vom Nullprodukt).
Aus \( 6x(x-1)=0 \) liest du sofort \( x=0 \) oder \( x=1 \) ab — ohne Mitternachts-/pq-Formel. Im
hilfsmittelfreien Teil ist Ausklammern fast immer schneller und sicherer als jede Lösungsformel.

</details>
</details>

### Linearfaktordarstellung — Polynome an ihren Nullstellen ablesen

Statt der ausmultiplizierten Form lässt sich ein Polynom oft als **Produkt von Linearfaktoren**
schreiben. Hat \( g \) die Nullstellen \( x_1, x_2, \dots \), so gilt:

\[ g(x) = a\,(x - x_1)(x - x_2)\cdots \]

Beispiel: \( g(x) = (x+1)(x-2) \) hat die Nullstellen \( x_1 = -1 \) und \( x_2 = 2 \).
Ausmultipliziert ist das \( g(x) = x^2 - x - 2 \).

<details><summary>Probe: stimmen die Nullstellen?</summary>

Einsetzen: \( g(-1) = (-1+1)(-1-2) = 0\cdot(-3) = 0 \) ✓ und
\( g(2) = (2+1)(2-2) = 3\cdot 0 = 0 \) ✓. Beide Faktoren werden an „ihrer" Nullstelle zu \( 0 \) und
ziehen das ganze Produkt auf \( 0 \) — das ist der ganze Sinn der Linearfaktorform.

<details><summary>Haltung: Vielfachheit und Verhalten an der Nullstelle</summary>

Kommt ein Faktor mehrfach vor, z. B. \( (x-2)^2 \), spricht man von einer **doppelten Nullstelle**.
Dort **berührt** der Graph die \( x \)-Achse, statt sie zu schneiden (er „dreht um"). Bei einer
einfachen Nullstelle schneidet er hindurch. Diese Unterscheidung hilft beim schnellen Skizzieren
ohne Wertetabelle.

</details>
</details>

Hier siehst du \( g(x) = (x+1)(x-2) = x^2 - x - 2 \) mit seinen beiden Nullstellen:

<div class="jxgbox" id="jxg-poly" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-poly',{boundingbox:[-3,5,4,-3],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return (x+1)*(x-2);},-3,4],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[-1,0],{name:'x_1=-1',size:2,fixed:true,color:'#d98324'});b.create('point',[2,0],{name:'x_2=2',size:2,fixed:true,color:'#d98324'});})();</script>

### Verhalten im Unendlichen <span class="tag tag-ok">AB II</span>

Für sehr große \( |x| \) bestimmt allein der **Term mit dem höchsten Grad** das Verhalten — alle
kleineren Glieder werden im Vergleich winzig. Für \( f(x) = 2x^3 - 3x^2 + 4 \) zählt also nur
\( 2x^3 \):

\[ x \to +\infty:\ f(x) \to +\infty \qquad\qquad x \to -\infty:\ f(x) \to -\infty \]

<details><summary>Haltung: ungerader Grad „über Kreuz", gerader Grad „gleiche Seite"</summary>

Bei **ungeradem** Höchstgrad (wie \( x^3 \)) laufen die beiden Enden in **entgegengesetzte**
Richtungen (eines hoch, eines runter). Bei **geradem** Höchstgrad (wie \( x^2 \) oder \( x^4 \))
laufen beide Enden in **dieselbe** Richtung — bei positivem Leitfaktor beide nach oben. Das
Vorzeichen des Leitfaktors entscheidet, ob es „so herum" oder gespiegelt ist. Mit diesen zwei Regeln
kennst du das Fernverhalten jedes Polynoms in Sekunden.

</details>

## Die e-Funktion <span class="tag tag-ok">AB II</span>

Die **natürliche Exponentialfunktion** \( f(x) = e^x \) (mit der Eulerschen Zahl
\( e \approx 2{,}718 \)) ist der wichtigste „nicht-polynomiale" Baustein der Analysis. Drei Dinge
musst du sicher können.

**1. Sie ist immer positiv.** Für **jedes** \( x \) gilt \( e^x > 0 \). Der Graph liegt vollständig
oberhalb der \( x \)-Achse und hat **keine Nullstelle**.

**2. Verhalten im Unendlichen.**

\[ x \to +\infty:\ e^x \to +\infty \qquad\qquad x \to -\infty:\ e^x \to 0^{+} \]

Nach links nähert sich der Graph der \( x \)-Achse beliebig an, ohne sie je zu erreichen — die
\( x \)-Achse (\( y = 0 \)) ist eine **waagerechte Asymptote**.

**3. Die Ableitung — die berühmteste Eigenschaft:**

\[ f(x) = e^x \quad\Longrightarrow\quad f'(x) = e^x \]

Die e-Funktion ist **ihre eigene Ableitung**. An jeder Stelle ist ihre Steigung gleich ihrem
Funktionswert.

<details><summary>Haltung: was bedeutet „eigene Ableitung" anschaulich?</summary>

Je höher der Graph schon ist, desto steiler steigt er weiter — Wachstum, das sich selbst antreibt.
Im Punkt \( (0\mid 1) \) ist die Steigung genau \( 1 \) (denn \( e^0 = 1 \)); im Punkt
\( (1 \mid e) \) ist sie \( e \approx 2{,}72 \). Diese Selbstbezüglichkeit macht \( e^x \) zum
Modell für alles, was proportional zum eigenen Bestand wächst (Zinsen, Populationen, Zerfall mit
negativem Exponenten).

</details>

<details><summary>Kettenregel: die Ableitung von \( e^{kx} \) <span class="tag tag-ok">AB II–III</span></summary>

In Anwendungen steht im Exponenten oft ein Faktor, z. B. \( f(x) = e^{2x} \) oder \( e^{-0{,}5x} \).
Dann brauchst du die **Kettenregel** „äußere mal innere Ableitung":

\[ f(x) = e^{kx} \quad\Longrightarrow\quad f'(x) = k\,e^{kx} \]

Die äußere Funktion \( e^{(\;)} \) bleibt beim Ableiten stehen, und der innere Faktor \( k \) kommt
als Faktor nach vorne. Beispiel: \( \big(e^{2x}\big)' = 2e^{2x} \); \( \big(e^{-0{,}5x}\big)' =
-0{,}5\,e^{-0{,}5x} \).

<details><summary>Tiefer: warum der innere Faktor?</summary>

Die Kettenregel lautet allgemein \( \big(u(v(x))\big)' = u'(v(x))\cdot v'(x) \). Hier ist
\( u(z)=e^z \) (also \( u'=e^z \)) und \( v(x)=kx \) (also \( v'(x)=k \)). Eingesetzt:
\( e^{kx}\cdot k = k\,e^{kx} \). Die innere Ableitung \( v'(x)=k \) ist der Faktor, der „nach vorne"
wandert.

</details>
</details>

Der Graph von \( f(x)=e^x \): immer positiv, links flach an der Achse, rechts steil steigend. Der
Punkt \( (0\mid 1) \) ist markiert.

<div class="jxgbox" id="jxg-exp" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-exp',{boundingbox:[-3,6,3,-1],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return Math.exp(x);},-3,1.79],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[0,1],{name:'(0|1)',size:2,fixed:true,color:'#d98324'});})();</script>

## Sinus und Cosinus <span class="tag tag-ok">AB II</span>

Die **trigonometrischen Funktionen** \( \sin(x) \) und \( \cos(x) \) beschreiben alles
Periodische — Schwingungen, Wellen, Kreisbewegungen. Im Abitur arbeitest du mit dem **Bogenmaß**
(Winkel in \( \pi \) gemessen, nicht in Grad).

**Periode und Amplitude.** Beide Funktionen wiederholen sich nach einer **Periode** von \( 2\pi \):
\( \sin(x + 2\pi) = \sin(x) \). Ihre Werte liegen stets zwischen \( -1 \) und \( 1 \) — die
**Amplitude** ist \( 1 \). Es gilt \( -1 \le \sin(x) \le 1 \) und ebenso für \( \cos \).

**Die Ableitungen** (unbedingt auswendig):

\[ \big(\sin x\big)' = \cos x \qquad\qquad \big(\cos x\big)' = -\sin x \]

Beachte das **Minuszeichen** beim Ableiten des Cosinus — die häufigste Fehlerquelle.

<details><summary>Haltung: warum ist die Ableitung von \( \sin \) gerade \( \cos \)?</summary>

Die Ableitung ist die Steigung. Schau auf den Sinus: Bei \( x=0 \) steigt er am steilsten
(Steigung \( 1 \)) — und genau dort ist \( \cos(0)=1 \). Am Hochpunkt bei \( x=\tfrac{\pi}{2} \) ist
der Sinus waagerecht (Steigung \( 0 \)) — und \( \cos(\tfrac{\pi}{2})=0 \). Die Steigungswerte des
Sinus durchlaufen also genau die Werte des Cosinus. Beim Cosinus ist es dasselbe Spiel, nur fällt er
bei \( x=0 \), daher das Minus: \( (\cos x)' = -\sin x \).

<details><summary>Tiefer: der „Vierer-Zyklus" beim wiederholten Ableiten</summary>

Leitet man immer weiter ab, dreht sich alles im Kreis:

\[ \sin x \;\xrightarrow{\;'\;}\; \cos x \;\xrightarrow{\;'\;}\; -\sin x \;\xrightarrow{\;'\;}\; -\cos x \;\xrightarrow{\;'\;}\; \sin x \]

Nach **vier** Ableitungen bist du wieder am Anfang. Wer das einmal als Kreis im Kopf hat, vertut sich
beim Vorzeichen nicht mehr.

</details>
</details>

So sehen \( \sin(x) \) (blau) und \( \cos(x) \) (amber) über etwas mehr als eine Periode aus — beide
zwischen \( -1 \) und \( 1 \), gegeneinander verschoben:

<div class="jxgbox" id="jxg-sincos" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-sincos',{boundingbox:[-0.6,1.8,7,-1.8],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return Math.sin(x);},0,6.6],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('functiongraph',[function(x){return Math.cos(x);},0,6.6],{strokeColor:'#d98324',strokeWidth:2.5,dash:2});})();</script>

## Wurzelfunktion <span class="tag tag-warn">Relevanz: offiziell Leistungsfach, im Basisfach nicht eigenständig ausgewiesen [80 %] — mit Lehrkraft prüfen</span>

Die **Wurzelfunktion** \( f(x) = \sqrt{x} \) ist nur für \( x \ge 0 \) definiert (man kann aus
negativen Zahlen keine reelle Quadratwurzel ziehen). Ihr Graph startet im Ursprung und steigt nach
rechts, wird dabei aber **immer flacher**.

Zum Ableiten schreibt man die Wurzel als **Potenz mit gebrochenem Exponenten** und nutzt die
gewohnte Potenzregel:

\[ f(x) = \sqrt{x} = x^{\frac{1}{2}} \quad\Longrightarrow\quad f'(x) = \tfrac{1}{2}\,x^{-\frac{1}{2}} = \frac{1}{2\sqrt{x}} \]

<details><summary>Schritt für Schritt mit der Potenzregel</summary>

Mit \( n = \tfrac{1}{2} \) liefert die Potenzregel \( n\,x^{n-1} = \tfrac{1}{2}\,x^{\frac{1}{2}-1} =
\tfrac{1}{2}\,x^{-\frac{1}{2}} \). Ein negativer Exponent bedeutet „im Nenner", und
\( x^{\frac{1}{2}} = \sqrt{x} \), also:

\[ \tfrac{1}{2}\,x^{-\frac{1}{2}} = \frac{1}{2\,x^{\frac{1}{2}}} = \frac{1}{2\sqrt{x}} \]

<details><summary>Haltung: warum wird der Graph immer flacher?</summary>

Die Steigung ist \( f'(x) = \tfrac{1}{2\sqrt{x}} \). Je größer \( x \), desto größer der Nenner —
also wird der Bruch und damit die Steigung **kleiner**. Bei \( x=1 \) ist die Steigung \( \tfrac12 \),
bei \( x=4 \) nur noch \( \tfrac14 \). Nahe \( x=0 \) dagegen wird der Nenner winzig und die Steigung
riesig: Der Graph startet senkrecht. Genau das siehst du im Diagramm.

</details>
</details>

<div class="jxgbox" id="jxg-sqrt" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-sqrt',{boundingbox:[-1,3.2,8,-1],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return Math.sqrt(x);},0,8],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[1,1],{name:'(1|1)',size:2,fixed:true,color:'#d98324'});})();</script>

## Die Funktion \( f(x)=\tfrac{1}{x} \) <span class="tag tag-warn">Relevanz: offiziell Leistungsfach [97 %] — mit Lehrkraft prüfen</span>

Die Funktion \( f(x) = \dfrac{1}{x} \) heißt **Hyperbel**. Sie ist für **alle** \( x \) außer
\( x = 0 \) definiert (Teilen durch \( 0 \) ist verboten) — bei \( x=0 \) hat sie eine
**Definitionslücke** mit senkrechter Asymptote.

**Verhalten.** Für \( x \to \pm\infty \) nähert sich der Graph der \( x \)-Achse (\( y=0 \) ist
waagerechte Asymptote). Nahe \( x=0 \) schießt er ins Unendliche: von rechts nach \( +\infty \), von
links nach \( -\infty \). Der Graph besteht aus zwei getrennten Ästen.

Zum Ableiten wieder als Potenz schreiben:

\[ f(x) = \frac{1}{x} = x^{-1} \quad\Longrightarrow\quad f'(x) = -1\cdot x^{-2} = -\frac{1}{x^2} \]

<details><summary>Schritt für Schritt mit der Potenzregel</summary>

Mit \( n = -1 \): der Exponent \( -1 \) kommt als Faktor nach vorne, der neue Exponent ist
\( -1 - 1 = -2 \). Also \( f'(x) = -1\cdot x^{-2} = -\dfrac{1}{x^2} \).

<details><summary>Haltung: die Steigung ist überall negativ</summary>

\( x^2 \) ist für jedes \( x \neq 0 \) positiv, also ist \( -\dfrac{1}{x^2} \) **immer negativ**. Das
passt zum Bild: Auf beiden Ästen fällt der Graph. Es gibt deshalb **keinen** Hoch- oder Tiefpunkt —
die Ableitung wird nie \( 0 \).

</details>
</details>

<div class="jxgbox" id="jxg-recip" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-recip',{boundingbox:[-5,5,5,-5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 1/x;},0.2,5],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('functiongraph',[function(x){return 1/x;},-5,-0.2],{strokeColor:'#3a5a9c',strokeWidth:2.5});})();</script>

## Überblick: alle Ableitungen auf einen Blick

Diese Tabelle ist deine Spickzettel-Essenz. Wenn du sie sicher beherrschst, hast du das Fundament
für die gesamte Analysis.

| Funktion \( f(x) \) | Ableitung \( f'(x) \) | merke dir |
|---|---|---|
| \( x^n \) | \( n\,x^{\,n-1} \) | Exponent runter, dann minus eins |
| \( c \) (Konstante) | \( 0 \) | waagerecht = Steigung null |
| \( e^x \) | \( e^x \) | bleibt sich selbst |
| \( e^{kx} \) | \( k\,e^{kx} \) | innerer Faktor \( k \) nach vorne |
| \( \sin x \) | \( \cos x \) | — |
| \( \cos x \) | \( -\sin x \) | Vorsicht: Minus! |
| \( \sqrt{x} = x^{1/2} \) | \( \dfrac{1}{2\sqrt{x}} \) | als Potenz schreiben |
| \( \dfrac{1}{x} = x^{-1} \) | \( -\dfrac{1}{x^2} \) | als Potenz schreiben |

<details><summary>Selbsttest: deck die rechte Spalte ab</summary>

Sprich jede Ableitung laut aus, bevor du nachschaust — so, wie du es der Prüferin erklären würdest.
Achte besonders auf die zwei Stolpersteine: das **Minus** bei \( (\cos x)' = -\sin x \) und der
**innere Faktor** bei \( \big(e^{kx}\big)' = k\,e^{kx} \). Wenn diese beiden sitzen, sitzt der Rest
meist von allein.

</details>
