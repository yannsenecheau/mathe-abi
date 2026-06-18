# Handwerk: Ableiten

Ableiten ist das Werkzeug, mit dem du aus einer Funktion \( f \) ihre Steigungsfunktion \( f' \)
machst — die in jedem Punkt sagt, wie steil der Graph dort ist. In der mündlichen Prüfung leitest du
**von Hand** ab, ohne Taschenrechner. Das ist gut so, denn die fünf Regeln auf dieser Seite sind so
gebaut, dass du sie sicher im Kopf anwenden kannst, wenn du das Prinzip dahinter einmal verstanden hast.

Léona, geh die Regeln der Reihe nach durch. Jede hat dieselbe Struktur: **Aussage**, ein **Merksatz**
zum Behalten, und zwei bis drei Beispiele, die du am besten selbst mitrechnest, bevor du die Lösung
aufklappst.

> **Was du am Ende können sollst:** Ein Polynom wie \( f(x) = 2x^3 - 4x + 7 \) im Kopf ableiten, ein
> Produkt wie \( (2x-1)(x^2+3) \) mit der Produktregel angehen, und eine geklammerte Potenz wie
> \( (3x+1)^2 \) mit der linearen Kettenregel — alles ohne Rechner.

## Potenzregel — das Fundament

**Aussage.** Für eine Potenz \( f(x) = x^n \) gilt

\[ f'(x) = n \cdot x^{\,n-1}. \]

Du ziehst den Exponenten als Faktor nach vorn und senkst ihn um eins ab.

**Merksatz:** *Exponent vor, Exponent minus eins.*

<details><summary>Haltung dahinter: Warum gerade „vor und minus eins"?</summary>

Die Ableitung misst, wie schnell sich \( f \) ändert. Bei \( x^n \) wächst der Funktionswert umso
schneller, je größer \( n \) ist — deshalb taucht \( n \) als Faktor auf. Und weil die Steigung selbst
wieder eine (um einen Grad niedrigere) Potenz ist, sinkt der Exponent auf \( n-1 \).

<details><summary>Herleitung am Beispiel \( x^2 \) (Differenzenquotient)</summary>

Die Steigung im Punkt \( x \) ist der Grenzwert des Differenzenquotienten:

\[ f'(x) = \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h}. \]

Der Zähler ist \( (x+h)^2 - x^2 = x^2 + 2xh + h^2 - x^2 = 2xh + h^2 \). Geteilt durch \( h \) bleibt
\( 2x + h \). Lässt man \( h \) gegen \( 0 \) gehen, fällt das \( h \) weg:

\[ f'(x) = 2x. \]

Das passt zur Regel: \( n = 2 \) ergibt \( 2 \cdot x^{1} = 2x \). Genau diese Idee — „Differenzenquotient,
dann \( h \to 0 \)" — steckt hinter jeder Potenz.

</details>
</details>

**Beispiele.**

<details><summary>① \( f(x) = x^4 \) <span class="tag tag-ok">AB I</span></summary>

Exponent \( 4 \) vor, Exponent um eins kleiner:

\[ f'(x) = 4 \cdot x^{4-1} = 4x^3. \]

</details>

<details><summary>② \( f(x) = x \) — der Spezialfall <span class="tag tag-ok">AB I</span></summary>

Schreibe \( x = x^1 \). Dann ist \( f'(x) = 1 \cdot x^{0} = 1 \), denn \( x^0 = 1 \).

**Falle:** Die Ableitung einer reinen Variablen ist \( 1 \), nicht \( 0 \). Und die Ableitung einer
Konstanten wie \( f(x) = 7 \) ist \( 0 \) — eine waagrechte Linie hat überall Steigung null.

</details>

<details><summary>③ Negative und gebrochene Exponenten <span class="tag tag-warn">offiziell Leistungsfach, Basisfach unsicher [80–97 %] — mit Lehrkraft prüfen</span></summary>

Die Regel gilt für **jeden** Exponenten, auch negative und gebrochene. Im Basisfach sind diese Fälle
aber nicht eigenständig im Kanon ausgewiesen — kläre mit deiner Lehrkraft, ob du sie brauchst.

Negativer Exponent (entspricht \( \tfrac{1}{x^2} \), eine Leistungsfach-Funktion, Konfidenz 97 %):

\[ f(x) = x^{-2} \quad\Rightarrow\quad f'(x) = -2 \cdot x^{-3}. \]

Gebrochener Exponent (das ist die Wurzelfunktion \( \sqrt{x} = x^{1/2} \), Basisfach-Status unsicher,
Konfidenz 80 %):

\[ f(x) = x^{1/2} \quad\Rightarrow\quad f'(x) = \tfrac{1}{2} \cdot x^{-1/2}. \]

Das Schema ist immer dasselbe: Exponent vor, Exponent minus eins — egal welcher Art die Zahl ist.

</details>

## Faktorregel — konstante Faktoren bleiben stehen

**Aussage.** Ein konstanter Faktor \( c \) vor der Funktion bleibt beim Ableiten unverändert stehen:

\[ \big( c \cdot f(x) \big)' = c \cdot f'(x). \]

**Merksatz:** *Zahl davor? Lass sie stehen, leite nur den Rest ab.*

<details><summary>Haltung dahinter: Warum darf der Faktor stehen bleiben?</summary>

Ein konstanter Faktor staucht oder streckt den Graphen nur in der Höhe. Wird die Funktion an jeder
Stelle dreimal so hoch, dann ist sie auch überall dreimal so steil — die Steigung skaliert mit demselben
Faktor. Die *Form* der Steigungskurve ändert sich nicht, nur ihre Höhe.

</details>

**Beispiele.**

<details><summary>① \( f(x) = 5x^3 \) <span class="tag tag-ok">AB I</span></summary>

Den Faktor \( 5 \) stehen lassen, \( x^3 \) nach der Potenzregel ableiten (\( \to 3x^2 \)):

\[ f'(x) = 5 \cdot 3x^2 = 15x^2. \]

</details>

<details><summary>② \( f(x) = \tfrac{1}{2}x^4 \) <span class="tag tag-ok">AB I</span></summary>

Faktor \( \tfrac{1}{2} \) bleibt, \( x^4 \to 4x^3 \):

\[ f'(x) = \tfrac{1}{2} \cdot 4x^3 = 2x^3. \]

Die \( 4 \) aus der Potenzregel kürzt sich schön mit dem \( \tfrac{1}{2} \) — solche Brüche, die sich
glatt rechnen, sind in der hilfsmittelfreien Prüfung typisch.

</details>

## Summenregel — Term für Term

**Aussage.** Eine Summe (oder Differenz) wird gliedweise abgeleitet:

\[ \big( f(x) + g(x) \big)' = f'(x) + g'(x). \]

**Merksatz:** *Jeden Summanden einzeln ableiten, dann wieder zusammensetzen.*

<details><summary>Haltung dahinter: Steigungen addieren sich</summary>

Wenn zwei Bewegungen sich überlagern, addieren sich ihre Geschwindigkeiten. Genauso bei Funktionen: Die
Steigung einer Summe ist die Summe der Steigungen. Deshalb darfst du ein Polynom Glied für Glied
ableiten — Faktor- und Summenregel zusammen erledigen jedes Polynom.

</details>

**Beispiele.**

<details><summary>① \( f(x) = x^3 + x^2 \) <span class="tag tag-ok">AB I</span></summary>

Jeden Summanden einzeln: \( x^3 \to 3x^2 \) und \( x^2 \to 2x \). Zusammen:

\[ f'(x) = 3x^2 + 2x. \]

</details>

<details><summary>② Ein vollständiges Polynom: \( f(x) = 2x^3 - 4x + 7 \) <span class="tag tag-ok">AB I–II</span></summary>

Hier wirken alle drei bisherigen Regeln zusammen. Geh von links nach rechts:

- \( 2x^3 \): Faktor \( 2 \) bleibt, \( x^3 \to 3x^2 \), ergibt \( 6x^2 \).
- \( -4x \): Faktor \( -4 \) bleibt, \( x \to 1 \), ergibt \( -4 \).
- \( +7 \): konstanter Summand, Ableitung \( 0 \).

\[ f'(x) = 6x^2 - 4. \]

<details><summary>Falle: Die Konstante verschwindet</summary>

Der Summand \( +7 \) hat keine Steigung (waagrechte Verschiebung des ganzen Graphen) und fällt beim
Ableiten ersatzlos weg. Ein häufiger Flüchtigkeitsfehler ist, die \( 7 \) versehentlich mitzuschleppen.

</details>
</details>

## Produktregel — wenn zwei Funktionen multipliziert werden

**Aussage.** Steht ein Produkt \( f(x) = u(x) \cdot v(x) \) da, gilt

\[ f'(x) = u'(x)\,v(x) + u(x)\,v'(x). \]

**Merksatz:** *Erstes abgeleitet mal zweites, plus erstes mal zweites abgeleitet.*

<details><summary>Haltung dahinter: Warum nicht einfach \( u' \cdot v' \)?</summary>

Ein verbreiteter Fehler ist, ein Produkt faktorweise abzuleiten — das ist **falsch**. Anschaulich: Eine
Rechteckfläche \( u \cdot v \) wächst, wenn die Breite \( u \) wächst (Beitrag \( u' \cdot v \)) **und**
wenn die Höhe \( v \) wächst (Beitrag \( u \cdot v' \)). Beide Beiträge zusammen ergeben die
Änderungsrate — daher die Summe der beiden „Kreuzprodukte".

**Erste-Hilfe-Schema:** Schreib dir vor jeder Produktregel kurz die vier Bausteine hin —
\( u \), \( u' \), \( v \), \( v' \) — dann setzt du nur noch ein. Das verhindert Fehler unter Prüfungsdruck.

</details>

**Beispiele.**

<details><summary>① \( f(x) = x^2 \cdot (x+1) \) <span class="tag tag-ok">AB II</span></summary>

Bausteine bestimmen:

\[ u = x^2,\quad u' = 2x,\qquad v = x+1,\quad v' = 1. \]

In die Regel einsetzen:

\[ f'(x) = u'v + uv' = 2x\,(x+1) + x^2 \cdot 1 = 2x^2 + 2x + x^2 = 3x^2 + 2x. \]

<details><summary>Gegenprobe durch Ausmultiplizieren</summary>

Multiplizierst du zuerst aus, ist \( f(x) = x^3 + x^2 \). Mit Summen- und Potenzregel: \( f'(x) = 3x^2 + 2x \).
Gleiches Ergebnis — die Produktregel ist verlässlich, und das Ausmultiplizieren ist hier die einfache
Gegenprobe. **Haltung:** Bei einem einfachen Produkt, das sich leicht ausmultiplizieren lässt, ist das
oft der schnellere Weg. Die Produktregel brauchst du, wenn das Ausmultiplizieren mühsam oder unmöglich ist.

</details>
</details>

<details><summary>② \( f(x) = (2x-1)(x^2+3) \) <span class="tag tag-ok">AB II</span></summary>

Bausteine:

\[ u = 2x-1,\quad u' = 2,\qquad v = x^2+3,\quad v' = 2x. \]

Einsetzen und zusammenfassen:

\[ f'(x) = 2\,(x^2+3) + (2x-1)\,2x = 2x^2 + 6 + 4x^2 - 2x = 6x^2 - 2x + 6. \]

<details><summary>Gegenprobe</summary>

Ausmultipliziert ist \( f(x) = 2x^3 + 6x - x^2 - 3 \), also \( f(x) = 2x^3 - x^2 + 6x - 3 \). Gliedweise
abgeleitet: \( f'(x) = 6x^2 - 2x + 6 \). Stimmt überein.

</details>
</details>

## Lineare Kettenregel — die innere Funktion ist \( ax + b \)

**Aussage.** Ist die innere Funktion **linear**, also von der Form \( ax + b \), und \( f(x) = g(ax+b) \),
dann gilt

\[ f'(x) = a \cdot g'(ax+b). \]

Du leitest die äußere Funktion ganz normal ab, lässt den inneren Klammerausdruck \( ax+b \) dabei
unangetastet stehen, und multiplizierst am Ende mit der inneren Steigung \( a \).

**Merksatz:** *Außen ableiten, Klammer abschreiben, mal die Zahl vor dem \( x \).*

<details><summary>Haltung dahinter: Was bedeutet „mal \( a \)"?</summary>

Die innere Funktion \( ax+b \) läuft \( a \)-mal so schnell wie \( x \) selbst. Wenn der Eingang \( a \)-mal
schneller voranschreitet, ändert sich auch der Ausgang \( a \)-mal schneller — deshalb der Faktor \( a \).
Das ist der einfache, prüfungsrelevante Spezialfall der Kettenregel, weil die innere Steigung \( a \)
konstant ist.

<details><summary>Warum nur der lineare Fall im Basisfach?</summary>

Die **allgemeine** Kettenregel \( f'(x) = g'(h(x)) \cdot h'(x) \) erlaubt jede innere Funktion \( h(x) \)
(etwa \( h(x) = x^2 \)). Sie gehört zum Leistungsfach. Im Basisfach beschränkt man sich auf die innere
Funktion \( ax+b \), deren Ableitung einfach die Konstante \( a \) ist — daraus wird die handliche Regel
„mal \( a \)".

</details>
</details>

**Beispiele.**

<details><summary>① \( f(x) = (3x+1)^2 \) <span class="tag tag-ok">AB II</span></summary>

Äußere Funktion ist „Quadrat", innere ist \( 3x+1 \) mit \( a = 3 \). Äußere ableiten (\( (\,\cdot\,)^2 \to 2(\,\cdot\,) \)),
Klammer stehen lassen, mal \( a = 3 \):

\[ f'(x) = 3 \cdot 2\,(3x+1) = 6\,(3x+1) = 18x + 6. \]

<details><summary>Gegenprobe durch Ausmultiplizieren</summary>

\( f(x) = (3x+1)^2 = 9x^2 + 6x + 1 \), gliedweise abgeleitet \( f'(x) = 18x + 6 \). Passt.

</details>
</details>

<details><summary>② \( f(x) = (2x-5)^3 \) <span class="tag tag-ok">AB II</span></summary>

Äußere Funktion „hoch drei" (\( (\,\cdot\,)^3 \to 3(\,\cdot\,)^2 \)), innere \( 2x-5 \) mit \( a = 2 \):

\[ f'(x) = 2 \cdot 3\,(2x-5)^2 = 6\,(2x-5)^2. \]

**Haltung:** Du musst die Klammer **nicht** ausmultiplizieren. Bei höheren Potenzen ist die
Klammerschreibweise oft die gewünschte, kompakte Endform.

</details>

<details><summary>③ Achtung beim Vorzeichen: \( f(x) = (1-x)^4 \) <span class="tag tag-warn">AB II–III</span></summary>

Hier ist die innere Funktion \( 1 - x \), also \( a = -1 \) (der Faktor vor dem \( x \) ist negativ!).
Äußere „hoch vier" (\( \to 4(\,\cdot\,)^3 \)), mal \( a = -1 \):

\[ f'(x) = (-1) \cdot 4\,(1-x)^3 = -4\,(1-x)^3. \]

**Falle:** Das Minuszeichen der inneren Funktion wird leicht übersehen. Schau immer genau hin, welche
Zahl vor dem \( x \) steht — und mit welchem Vorzeichen.

</details>

## Abgrenzung — was Leistungsfach ist

Damit du nicht Energie in den falschen Stoff steckst: Zwei verwandte Regeln gehören **nicht** ins
Basisfach-Repertoire.

| Regel | Form | Status |
|---|---|---|
| Allgemeine Kettenregel | \( f'(x) = g'(h(x)) \cdot h'(x) \) mit beliebigem inneren \( h(x) \) | <span class="tag tag-warn">Leistungsfach — mit Lehrkraft prüfen</span> |
| Quotientenregel | \( \left( \dfrac{u}{v} \right)' = \dfrac{u'v - uv'}{v^2} \) | <span class="tag tag-warn">Leistungsfach — mit Lehrkraft prüfen</span> |

<details><summary>Was du im Basisfach stattdessen brauchst</summary>

Für das Basisfach reichen die fünf Regeln dieser Seite: **Potenz-, Faktor-, Summen-, Produkt-** und die
**lineare Kettenregel**. Damit leitest du jedes Polynom und jedes einfache Produkt ab, ebenso geklammerte
Potenzen mit linearer Klammer. Triff im Zweifel die Absprache mit deiner Lehrkraft, welche dieser
Grenzfälle in deiner Prüfung vorkommen können.

</details>

## Bild: Funktion und ihre Steigungsfunktion

Das ganze Handwerk hat ein Ziel: aus \( f \) die Steigungsfunktion \( f' \) zu gewinnen. Hier siehst du
das an \( f(x) = x^3 - 3x \). Mit Faktor- und Summenregel ergibt sich

\[ f'(x) = 3x^2 - 3. \]

Wo \( f' = 0 \) ist (bei \( x = -1 \) und \( x = 1 \)), ist der Graph von \( f \) waagrecht — das sind
genau die Hoch- und Tiefpunkte. Wo \( f' \) negativ ist (zwischen \( -1 \) und \( 1 \)), fällt \( f \);
wo \( f' \) positiv ist, steigt \( f \).

<div class="jxgbox" id="jxg-ableiten-fstrich" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-ableiten-fstrich',{boundingbox:[-2.6,9.5,2.6,-9.5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return x*x*x-3*x;},-2.4,2.4],{strokeColor:'#3a5a9c',strokeWidth:2.5,name:'f',withLabel:false});b.create('functiongraph',[function(x){return 3*x*x-3;},-2.4,2.4],{strokeColor:'#d98324',strokeWidth:2,dash:2,name:'f′',withLabel:false});b.create('point',[-1,2],{name:'Hochpunkt von f',size:2,fixed:true,color:'#29335c',label:{offset:[6,8]}});b.create('point',[1,-2],{name:'Tiefpunkt von f',size:2,fixed:true,color:'#29335c',label:{offset:[6,-14]}});})();</script>

Die blaue Kurve ist \( f \), die gestrichelte orange Kurve ist die Steigungsfunktion \( f' \). Beachte:
An den Nullstellen von \( f' \) liegen die Extrempunkte von \( f \).

<details><summary>Selbsttest: Kannst du das nachvollziehen?</summary>

Decke die Lösung ab und leite \( f(x) = x^3 - 3x \) selbst ab. \( x^3 \to 3x^2 \), \( -3x \to -3 \), also
\( f'(x) = 3x^2 - 3 \). Setze \( f'(x) = 0 \): \( 3x^2 - 3 = 0 \Rightarrow x^2 = 1 \Rightarrow x = \pm 1 \).
Genau dort hat \( f \) die waagrechten Tangenten — vergleiche mit dem Bild.

</details>
