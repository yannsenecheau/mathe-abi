# Aufgabe: e-Funktion untersuchen

Diese Aufgabe ist im Stil einer mündlichen Prüfung aufgebaut, Léona. Du bekommst eine Funktion und
untersuchst sie rechnerfrei, also komplett per Hand und ohne Taschenrechner — genau so wie in der
Prüfung. Arbeite jede Teilaufgabe erst selbst durch und klappe die Lösung danach auf. Wichtig ist
nicht nur das Ergebnis, sondern dass du laut sagen kannst, **warum** du jeden Schritt gehst.

Gegeben ist die Funktion

\[ f(x) = (x-1)\,e^{x}. \]

<span class="tag tag-ok">Relevanz: e-Funktion, Kernthema Analysis im Basisfach</span>

> **So gehst du an eine Funktionsuntersuchung heran.** Es gibt eine feste Reihenfolge, die fast jede
> mündliche Aufgabe trägt: erst der Definitionsbereich, dann Nullstellen, dann das Verhalten im
> Unendlichen, danach die Ableitung für Extrem- und Wendepunkte. Wenn du diese Reihenfolge im Kopf
> hast, gerätst du nie ins Stocken, weil du immer weißt, was als Nächstes dran ist.

## Teilaufgabe a) Nullstellen bestimmen

<span class="tag tag-ok">AB I — Grundkompetenz</span>

Bestimme alle Nullstellen von \( f \).

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Wir setzen \( f(x) = 0 \):

\[ (x-1)\,e^{x} = 0. \]

Ein Produkt ist genau dann null, wenn einer der Faktoren null ist. Der Faktor \( e^{x} \) wird
**niemals** null. Also bleibt nur \( x - 1 = 0 \), und das ergibt

\[ x = 1. \]

Die einzige Nullstelle liegt bei \( x = 1 \), der Punkt ist \( N(1 \mid 0) \).

<details><summary>Haltung dahinter: Warum ist \( e^{x} \) nie null?</summary>

Die Exponentialfunktion \( e^{x} \) ist für **jedes** \( x \) echt positiv, ihr Wertebereich ist
\( (0; \infty) \). Sie nähert sich für sehr kleine \( x \) der Null nur an, erreicht sie aber nie.
Das ist ein Werkzeug, das du dir merken solltest: In jedem Produkt aus einem Polynom und \( e^{x} \)
liefern **nur die Nullstellen des Polynomteils** die Nullstellen der ganzen Funktion.

<details><summary>Typische Falle</summary>

Verleite dich nicht dazu, „\( e^{x} = 0 \)" zu schreiben und daraus \( x \) berechnen zu wollen — die
Gleichung hat keine Lösung. Wer das übersieht, „findet" oft eine zweite Nullstelle, die es gar nicht
gibt.

</details>
</details>
</details>

## Teilaufgabe b) Verhalten für \( x \to \pm\infty \)

<span class="tag tag-ok">AB II — Standardanforderung</span>

Untersuche, wie sich \( f(x) \) für \( x \to +\infty \) und für \( x \to -\infty \) verhält.

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Für \( x \to +\infty \):** Beide Faktoren wachsen über alle Grenzen. \( (x-1) \to +\infty \) und
\( e^{x} \to +\infty \). Das Produkt strebt also gegen

\[ \lim_{x \to +\infty} (x-1)\,e^{x} = +\infty. \]

**Für \( x \to -\infty \):** Hier kämpfen zwei Effekte gegeneinander. Der Faktor \( (x-1) \) wird sehr
stark negativ, der Faktor \( e^{x} \) wird sehr klein positiv und strebt gegen \( 0 \). Entscheidend
ist: \( e^{x} \) geht **schneller** gegen null, als \( (x-1) \) gegen \(-\infty\) geht. Die
e-Funktion „gewinnt". Damit

\[ \lim_{x \to -\infty} (x-1)\,e^{x} = 0. \]

Weil \( (x-1) \) für sehr kleine \( x \) negativ ist, nähert sich der Graph der Null **von unten** an.
Die \( x \)-Achse ist also eine waagerechte Asymptote auf der linken Seite.

<details><summary>Haltung dahinter: Wer gewinnt, Polynom oder e-Funktion?</summary>

Die Merkregel lautet: **Die Exponentialfunktion schlägt jede Potenz von \( x \).** Für \( x \to -\infty \)
heißt das, \( e^{x} \) drückt das ganze Produkt gegen null, egal wie groß der Polynomfaktor dem Betrag
nach wird. Für \( x \to +\infty \) heißt dieselbe Regel umgekehrt: \( e^{x} \) lässt das Produkt
explodieren. Du musst das in der Prüfung nicht beweisen — es genügt, die Regel zu nennen und richtig
anzuwenden.

<details><summary>Wie sage ich das mündlich sauber?</summary>

Ein guter Satz für die Prüfung: „Für \( x \to -\infty \) geht die e-Funktion schneller gegen null als
der lineare Faktor betragsmäßig wächst, deshalb geht das Produkt gegen null, und zwar von unten, weil
\( x-1 \) dort negativ ist." Damit zeigst du, dass du den Mechanismus verstanden hast und nicht nur ein
Ergebnis auswendig kannst.

</details>
</details>
</details>

## Teilaufgabe c) Erste Ableitung mit der Produktregel

<span class="tag tag-ok">AB II — Standardanforderung</span>

Bilde \( f'(x) \) rechnerfrei und vereinfache so weit wie möglich.

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Die Funktion ist ein Produkt zweier Faktoren, also nutzen wir die **Produktregel**
\( (u\cdot v)' = u'\,v + u\,v' \). Wir wählen

\[ u(x) = x-1, \quad v(x) = e^{x}, \qquad u'(x) = 1, \quad v'(x) = e^{x}. \]

Eingesetzt:

\[ f'(x) = 1 \cdot e^{x} + (x-1)\cdot e^{x}. \]

Jetzt klammern wir den gemeinsamen Faktor \( e^{x} \) aus:

\[ f'(x) = e^{x}\big(1 + x - 1\big) = e^{x}\cdot x = x\,e^{x}. \]

Die Ableitung ist also

\[ f'(x) = x\,e^{x}. \]

<details><summary>Haltung dahinter: immer ausklammern, bevor du weiterrechnest</summary>

Das Ausklammern von \( e^{x} \) ist kein Schönheitsschritt, sondern macht die nächste Teilaufgabe erst
einfach: Wir brauchen gleich \( f'(x) = 0 \), und ein ausgeklammertes Produkt liest man sofort. Wer die
Summe \( e^{x} + (x-1)e^{x} \) stehen lässt, tut sich beim Nullsetzen unnötig schwer.

<details><summary>Warum ist die Ableitung von \( e^{x} \) wieder \( e^{x} \)?</summary>

Das ist die definierende Eigenschaft der e-Funktion: Sie ist die einzige Funktion, die mit ihrer
eigenen Ableitung übereinstimmt, \( (e^{x})' = e^{x} \). Genau dafür wurde die Zahl \( e \) gewählt.
Diese Eigenschaft ist der Grund, warum sich \( e^{x} \) in jeder Produkt- und Kettenregel so bequem
verhält.

</details>
</details>
</details>

## Teilaufgabe d) Extrempunkt bestimmen und einordnen

<span class="tag tag-ok">AB II — Standardanforderung</span>

Bestimme die Extremstelle von \( f \) und entscheide rechnerfrei, ob es sich um einen Hoch- oder
Tiefpunkt handelt.

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Notwendige Bedingung** \( f'(x) = 0 \):

\[ x\,e^{x} = 0. \]

Wieder ist \( e^{x} \neq 0 \), also bleibt \( x = 0 \) als einziger Kandidat.

**Funktionswert** an der Stelle:

\[ f(0) = (0-1)\cdot e^{0} = (-1)\cdot 1 = -1. \]

**Hinreichende Bedingung** über die zweite Ableitung. Wir leiten \( f'(x) = x\,e^{x} \) noch einmal mit
der Produktregel ab (\( u=x,\ v=e^{x},\ u'=1,\ v'=e^{x} \)):

\[ f''(x) = 1\cdot e^{x} + x\cdot e^{x} = e^{x}(1+x). \]

Einsetzen von \( x = 0 \):

\[ f''(0) = e^{0}\,(1+0) = 1 \cdot 1 = 1 > 0. \]

Weil \( f''(0) > 0 \) ist, ist die Funktion an dieser Stelle linksgekrümmt — es liegt ein
**Tiefpunkt** vor:

\[ T(0 \mid -1). \]

<details><summary>Haltung dahinter: Warum reicht \( f'(x)=0 \) allein nicht?</summary>

\( f'(x) = 0 \) ist nur das **notwendige** Kriterium: An einem Extrempunkt ist die Tangente waagerecht,
aber eine waagerechte Tangente kann auch ein Sattelpunkt sein. Erst die **hinreichende** Bedingung
entscheidet, was wirklich vorliegt. Das Vorzeichen von \( f''(x_0) \) verrät die Krümmung: \( f'' > 0 \)
bedeutet Linkskrümmung und damit Tiefpunkt, \( f'' < 0 \) bedeutet Rechtskrümmung und damit Hochpunkt.

<details><summary>Alternative ohne zweite Ableitung: Vorzeichenwechsel von \( f' \)</summary>

Du kannst auch ohne \( f'' \) argumentieren. In \( f'(x) = x\,e^{x} \) ist \( e^{x} \) immer positiv,
das Vorzeichen kommt also allein vom Faktor \( x \). Für \( x < 0 \) ist \( f'(x) < 0 \) (Funktion
fällt), für \( x > 0 \) ist \( f'(x) > 0 \) (Funktion steigt). Aus „fällt, dann steigt" folgt ein
Tiefpunkt bei \( x = 0 \). Beide Wege sind in der Prüfung gleichwertig — wähle den, der dir sicherer
von der Hand geht.

</details>
</details>
</details>

## Teilaufgabe e) Tangente an der Nullstelle

<span class="tag tag-ok">AB II — Standardanforderung</span>

Bestimme die Gleichung der Tangente an den Graphen von \( f \) im Punkt \( x_{0} = 1 \).

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Eine Tangente ist die Gerade, die den Graphen an einer Stelle berührt und dort dieselbe Steigung hat.
Wir brauchen also zwei Dinge: den **Berührpunkt** und die **Steigung** dort.

**Funktionswert** (Berührpunkt): wir kennen ihn schon aus Teilaufgabe a),

\[ f(1) = (1-1)\,e^{1} = 0. \]

Der Berührpunkt ist \( (1 \mid 0) \), also genau die Nullstelle.

**Steigung** über die Ableitung \( f'(x) = x\,e^{x} \):

\[ f'(1) = 1\cdot e^{1} = e. \]

**Tangentengleichung** über die Punkt-Steigungs-Form \( t(x) = f(x_0) + f'(x_0)\,(x - x_0) \):

\[ t(x) = 0 + e\,(x - 1) = e\,(x-1) = e\,x - e. \]

Die Tangente hat die Steigung \( e \approx 2{,}72 \) und schneidet die \( x \)-Achse genau bei der
Nullstelle \( x = 1 \).

<details><summary>Haltung dahinter: Woher kommt die Tangentenformel?</summary>

Die Punkt-Steigungs-Form einer Geraden ist \( y = m\,(x - x_0) + y_0 \). Für eine Tangente an einen
Funktionsgraphen ist die Steigung \( m = f'(x_0) \) (Ableitung = lokale Steigung) und der Punkt
\( (x_0 \mid f(x_0)) \) liegt auf dem Graphen. Mehr steckt nicht dahinter — du musst dir nur merken,
**welche** zwei Werte du einsetzt: \( f'(x_0) \) als Steigung, \( f(x_0) \) als Höhe.

<details><summary>Typische Falle bei der Tangente</summary>

Vertausche nicht \( f(x_0) \) und \( f'(x_0) \). Als Steigung kommt **immer** die Ableitung
\( f'(x_0) \) hinein, der Funktionswert \( f(x_0) \) liefert nur die Höhe des Berührpunkts. Und lass den
Term \( x_0 \) nicht weg: Es heißt \( (x - x_0) \), hier \( (x-1) \), nicht einfach \( x \).

</details>
</details>
</details>

## Der Graph zur Kontrolle

Hier siehst du \( f \) (blau), den Tiefpunkt \( T(0\mid -1) \), die Nullstelle \( N(1\mid 0) \) und die
Tangente \( t(x)=e(x-1) \) (orange). Prüfe, ob deine Ergebnisse zum Bild passen: Der Graph kommt von
links von unten an die \( x \)-Achse heran, sinkt bis zum Tiefpunkt und steigt dann steil an. Die
orange Gerade berührt den Graphen genau im Punkt \( (1\mid 0) \).

<div class="jxgbox" id="jxg-efunktion" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-efunktion',{boundingbox:[-3,5.5,2,-2.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return (x-1)*Math.exp(x);},-3,1.8],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('functiongraph',[function(x){return Math.E*(x-1);},-3,2],{strokeColor:'#d98324',strokeWidth:2,dash:2});b.create('point',[0,-1],{name:'T',size:2,fixed:true,color:'#3a5a9c',label:{offset:[8,-12]}});b.create('point',[1,0],{name:'N',size:2,fixed:true,color:'#3a5a9c',label:{offset:[6,10]}});})();</script>

## Selbstcheck: Kannst du es mündlich erklären?

Versuche, die Aufgabe einmal **frei und laut** durchzusprechen, ohne auf die Lösungen zu schauen —
genau das wird in der Prüfung von dir verlangt.

- In welcher Reihenfolge untersuchst du die Funktion, und warum gerade so?
- Warum hat \( f \) trotz des Faktors \( (x-1) \) nur **eine** Nullstelle?
- Wie begründest du das Verhalten für \( x \to -\infty \) in einem Satz?
- Welche zwei Werte setzt du in die Tangentenformel ein, und welcher ist die Steigung?

<details><summary>Kurz-Spickzettel der Ergebnisse (erst nach dem eigenen Versuch aufklappen)</summary>

- Nullstelle: \( N(1 \mid 0) \)
- Grenzverhalten: \( x \to +\infty:\ f \to +\infty \); \quad \( x \to -\infty:\ f \to 0^{-} \)
- Ableitung: \( f'(x) = x\,e^{x} \)
- Extrempunkt: Tiefpunkt \( T(0 \mid -1) \) (wegen \( f''(0) = 1 > 0 \))
- Tangente in \( x_0 = 1 \): \( t(x) = e\,(x-1) = e\,x - e \)

</details>
