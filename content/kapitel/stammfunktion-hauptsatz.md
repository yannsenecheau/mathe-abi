# Stammfunktion & Hauptsatz

Léona, dieses Kapitel dreht das Ableiten um: Statt von einer Funktion zur Steigung zu gehen, suchst du
jetzt die Funktion, deren Steigung du schon kennst. Das ist die <b>Stammfunktion</b>. Daraus folgt der
<b>Hauptsatz</b> — das Werkzeug, mit dem aus einer Änderungsrate ein Bestand und aus einer Funktion eine
Fläche wird. Alles hier rechnest du von Hand. Geh es ruhig durch, ein Schritt nach dem anderen.

## Was eine Stammfunktion ist

Eine Funktion \( F \) heißt <b>Stammfunktion</b> von \( f \), wenn das Ableiten von \( F \) genau \( f \)
zurückgibt:

\[ F'(x) = f(x). \]

Du machst also das Ableiten <em>rückwärts</em>. Wenn du \( f(x) = 2x \) siehst, fragst du: „Welche Funktion
hat als Ableitung \( 2x \)?" — Antwort: \( F(x) = x^2 \), denn \( (x^2)' = 2x \). <span class="tag tag-ok">AB I</span>

<details><summary>Haltung: Warum gibt es nie nur <em>eine</em> Stammfunktion?</summary>

Eine Konstante fällt beim Ableiten weg: \( (x^2 + 5)' = 2x \) und \( (x^2 - 1)' = 2x \) — beide haben dieselbe
Ableitung. Deshalb hat jedes \( f \) <b>unendlich viele</b> Stammfunktionen, die sich nur um eine Konstante
\( C \) unterscheiden:

\[ F(x) = x^2 + C. \]

<details><summary>Tiefer: Woher weiß man, dass es <em>genau</em> nur die Konstante ist?</summary>

Hätten zwei Stammfunktionen \( F_1, F_2 \) dieselbe Ableitung \( f \), dann hat ihre Differenz
\( D = F_1 - F_2 \) überall die Ableitung \( D' = f - f = 0 \). Eine Funktion mit überall verschwindender
Steigung ändert sich nicht — sie ist konstant. Also \( F_1 - F_2 = C \). Das ist die Begründung dafür, dass
das „\( +C \)" wirklich alle Möglichkeiten erfasst.

</details>
</details>

<blockquote>
<b>Typische Falle.</b> In der mündlichen Prüfung vergisst man gern das „\( +C \)". Bei einer
<b>unbestimmten</b> Stammfunktion gehört es dazu. Sobald du aber mit dem Hauptsatz ein <em>bestimmtes</em>
Integral \( \int_a^b \) ausrechnest, kürzt sich \( C \) wieder weg (siehe unten) — dort darfst du es weglassen.
</blockquote>

## Die Regeln zum Rückwärts-Ableiten

Du brauchst nur wenige Regeln. Jede ist das Spiegelbild einer Ableitungsregel — prüfe sie immer durch
<b>Wiederableiten</b>. <span class="tag tag-ok">AB I</span>

| Regel | Stammfunktion von \( f(x) \) | Probe \( F'(x) \) |
|---|---|---|
| Potenz | \( f(x)=x^n \Rightarrow F(x)=\dfrac{1}{n+1}x^{n+1} \) (für \( n\neq -1 \)) | \( \dfrac{n+1}{n+1}x^{n}=x^n \) |
| Faktor | \( f(x)=c\cdot g(x) \Rightarrow F(x)=c\cdot G(x) \) | \( c\cdot G'(x)=c\,g(x) \) |
| Summe | \( f=g+h \Rightarrow F=G+H \) | \( G'+H'=g+h \) |
| Konstante | \( f(x)=c \Rightarrow F(x)=c\,x \) | \( (c\,x)'=c \) |

<details><summary>Haltung: Warum funktioniert die Potenzregel — und warum gerade \( n+1 \)?</summary>

Beim Ableiten von \( x^{m} \) kommt der Exponent nach vorne und sinkt um 1: \( (x^m)' = m\,x^{m-1} \). Rückwärts
musst du den Exponenten also um 1 <em>erhöhen</em> und durch den neuen Exponenten <em>teilen</em>, um den Faktor
wieder loszuwerden. Aus \( x^n \) wird \( x^{n+1} \), und das Teilen durch \( n+1 \) macht die Probe glatt:

\[ \left(\tfrac{1}{n+1}x^{n+1}\right)' = \tfrac{1}{n+1}\cdot (n+1)\, x^{n} = x^{n}. \]

<details><summary>Warum ist \( n=-1 \) verboten?</summary>

Bei \( n=-1 \) stünde im Nenner \( n+1 = 0 \) — das ist nicht definiert. Die Stammfunktion von
\( \tfrac{1}{x} \) ist \( \ln|x| \) und gehört zur Funktion \( f(x)=\tfrac1x \).
<span class="tag tag-warn">Relevanz: \( \tfrac1x \) offiziell Leistungsfach, im Basisfach unsicher [97 %] — mit Lehrkraft prüfen</span>

</details>
</details>

<details><summary>Beispiel komplett rechnen: \( f(x)=4x^3-6x+5 \)</summary>

Geh Summand für Summand vor (Summen- und Faktorregel). Erhöhe je den Exponenten um 1 und teile durch den
neuen Exponenten:

\[ F(x) = 4\cdot\tfrac{1}{4}x^{4} \;-\; 6\cdot\tfrac{1}{2}x^{2} \;+\; 5x \;+\; C = x^{4} - 3x^{2} + 5x + C. \]

<b>Probe</b> (immer machen!): \( F'(x) = 4x^3 - 6x + 5 = f(x) \). Passt. <span class="tag tag-ok">AB I</span>

</details>

### Lineare Substitution (innere lineare Funktion)

Steht im Inneren nicht nur \( x \), sondern \( ax+b \) (linear), gilt: erst die äußere Stammfunktion bilden,
dann durch die innere Steigung \( a \) teilen.

\[ \text{Ist } F'=f, \text{ dann hat } f(ax+b) \text{ die Stammfunktion } \tfrac{1}{a}\,F(ax+b). \]

<details><summary>Haltung: Woher kommt der Faktor \( \tfrac1a \)? (Kettenregel rückwärts)</summary>

Leitest du \( F(ax+b) \) ab, liefert die Kettenregel einen Extrafaktor \( a \) (die Ableitung der inneren
Funktion):

\[ \frac{d}{dx}\,F(ax+b) = F'(ax+b)\cdot a = a\cdot f(ax+b). \]

Dieser unerwünschte Faktor \( a \) muss wieder weg — deshalb steht beim Aufleiten ein \( \tfrac1a \) davor.
Das funktioniert nur, weil die innere Steigung <em>konstant</em> ist (lineare innere Funktion); bei einer
nichtlinearen inneren Funktion reicht ein Vorfaktor nicht.

<details><summary>Beispiel: \( f(x)=(2x+1)^3 \)</summary>

Äußere Stammfunktion von \( u^3 \) ist \( \tfrac14 u^4 \). Innere Steigung \( a=2 \), also Faktor \( \tfrac12 \):

\[ F(x) = \tfrac12\cdot\tfrac14 (2x+1)^4 = \tfrac18 (2x+1)^4 + C. \]

<b>Probe:</b> \( F'(x) = \tfrac18\cdot 4(2x+1)^3\cdot 2 = (2x+1)^3 = f(x). \) Passt. <span class="tag tag-ok">AB II</span>

</details>
</details>

## Der Hauptsatz — und was er bedeutet

Der <b>Hauptsatz der Differential- und Integralrechnung</b> verbindet Stammfunktion und Integral. Kennst du
<em>eine</em> Stammfunktion \( F \) von \( f \), so ist das bestimmte Integral einfach die Differenz der
Randwerte:

\[ \int_a^b f(x)\,dx = F(b) - F(a). \]

Schreibweise mit eckiger Klammer: \( \big[\,F(x)\,\big]_a^b = F(b)-F(a) \).

<details><summary>Haltung: Warum darf \( C \) hier weggelassen werden?</summary>

Setzt du \( F(x)+C \) ein, hebt es sich auf:

\[ \big(F(b)+C\big) - \big(F(a)+C\big) = F(b)-F(a). \]

Die Konstante kürzt sich raus — deshalb nimmst du beim bestimmten Integral irgendeine bequeme Stammfunktion
(meist die ohne \( C \)). <span class="tag tag-ok">AB I</span>

</details>

### Anwendung 1: Bestandsänderung aus einer Rate

Ist \( f \) eine <b>Änderungsrate</b> (z. B. Zufluss pro Minute, Geschwindigkeit pro Sekunde), dann ist
\( \int_a^b f\,dx \) die <b>Gesamtänderung des Bestands</b> zwischen \( a \) und \( b \). Das ist die Brücke
von „wie schnell ändert es sich" zu „wie viel hat sich insgesamt geändert".

<details><summary>Beispiel rechnen: Zuflussrate \( f(t)=3t^2-2 \) (in Liter/Minute)</summary>

Gesucht: Wie viel Wasser kommt zwischen Minute \( t=1 \) und \( t=2 \) hinzu? Das ist \( \int_1^2 (3t^2-2)\,dt \).

<b>Schritt 1 — Stammfunktion:</b> \( F(t) = t^3 - 2t \). (Probe: \( F'(t)=3t^2-2 \). Passt.)

<b>Schritt 2 — Hauptsatz, Randwerte einsetzen:</b>

\[ \int_1^2 (3t^2-2)\,dt = \big[\,t^3-2t\,\big]_1^2 = \big(2^3-2\cdot2\big) - \big(1^3-2\cdot1\big) = (8-4)-(1-2) = 4-(-1) = 5. \]

Es kommen also \( 5 \) Liter hinzu. <span class="tag tag-ok">AB II</span>

<details><summary>Falle: Vorzeichen beim unteren Randwert</summary>

Der häufigste Fehler ist das Vorzeichen bei \( -F(a) \). Hier ist \( F(1) = 1-2 = -1 \), und
\( F(2)-F(1) = 4 - (-1) = +5 \) — das Minus vor einer negativen Zahl wird zum Plus. Setze die Randwerte
darum immer <b>geklammert</b> ein und ziehe erst danach zusammen.

</details>
</details>

### Anwendung 2: Orientierte Fläche

Geometrisch ist \( \int_a^b f\,dx \) die <b>orientierte Fläche</b> zwischen dem Graphen von \( f \) und der
\( x \)-Achse: Flächenstücke <em>oberhalb</em> der Achse zählen positiv, Stücke <em>unterhalb</em> negativ.

<blockquote>
<b>Wichtig fürs Abi.</b> „Orientierte Fläche" und „tatsächlicher Flächeninhalt" sind nicht dasselbe. Liegt
ein Teil des Graphen unter der Achse, musst du für den <em>echten</em> Inhalt zuerst die Nullstellen suchen,
abschnittweise integrieren und die Beträge addieren — sonst löschen sich positive und negative Anteile aus.
</blockquote>

<details><summary>Haltung: Warum kann ein Integral <em>null</em> sein, obwohl Fläche da ist?</summary>

Bei einer punktsymmetrischen Funktion wie \( f(x)=x^3 \) über \( [-1,1] \) ist die Fläche links unten genauso
groß wie rechts oben, nur mit umgekehrtem Vorzeichen:

\[ \int_{-1}^{1} x^3\,dx = \Big[\tfrac14 x^4\Big]_{-1}^{1} = \tfrac14 - \tfrac14 = 0. \]

Das Integral ist null, obwohl unter dem Graphen sichtbar Fläche liegt — die orientierten Anteile heben sich auf.
Für den echten Flächeninhalt rechnest du \( 2\cdot\int_0^1 x^3\,dx = 2\cdot\tfrac14 = \tfrac12 \). <span class="tag tag-ok">AB II</span>

</details>

## Zusammenhang der Graphen: \( F \), \( f \), \( f' \)

Drei Funktionen, eine Kette: \( F \xrightarrow{\text{ableiten}} f \xrightarrow{\text{ableiten}} f' \). Jeder
Pfeil ist „ableiten", jeder Pfeil rückwärts ist „aufleiten". Daraus liest du die Graphen ineinander, ohne zu
rechnen. <span class="tag tag-ok">AB II</span>

| Am Graphen von \( f \) … | … sagt die Ableitung \( f' \) | … sagt die Stammfunktion \( F \) |
|---|---|---|
| \( f \) hat Hoch-/Tiefpunkt (waagerechte Tangente) | \( f' \) hat dort eine <b>Nullstelle</b> | \( F \) hat dort einen <b>Wendepunkt</b> |
| \( f \) steigt | \( f' > 0 \) (oberhalb der Achse) | \( F \) ist <b>linksgekrümmt</b> |
| \( f \) fällt | \( f' < 0 \) (unterhalb der Achse) | \( F \) ist <b>rechtsgekrümmt</b> |
| \( f \) hat Wendepunkt (steilste/flachste Stelle) | \( f' \) hat dort einen Hoch-/Tiefpunkt | — |

<details><summary>Haltung: Vom Graphen von \( f' \) auf \( f \) schließen — die Leserichtung</summary>

In der Prüfung bekommst du oft nur den Graphen der Ableitung \( f' \) und sollst Aussagen über \( f \) treffen.
Lies dann <b>Vorzeichen</b> und <b>Nullstellen</b> von \( f' \):

- Wo \( f' \) <em>oberhalb</em> der Achse liegt (\( f'>0 \)), <b>steigt</b> \( f \).
- Wo \( f' \) <em>unterhalb</em> liegt (\( f'<0 \)), <b>fällt</b> \( f \).
- Wo \( f' \) die Achse mit Vorzeichenwechsel <b>schneidet</b>, hat \( f \) eine Extremstelle: von \( + \) nach
  \( - \) ein Hochpunkt, von \( - \) nach \( + \) ein Tiefpunkt.
- Wo \( f' \) selbst einen Extrempunkt hat, hat \( f \) einen <b>Wendepunkt</b>.

<details><summary>Falle: Funktionswert von \( f' \) ist nicht der Funktionswert von \( f \)</summary>

\( f'(x_0) \) ist die <em>Steigung</em> von \( f \) an der Stelle \( x_0 \), nicht der Höhenwert von \( f \).
Aus dem Graphen von \( f' \) bekommst du die <b>Form</b> von \( f \) (steigen/fallen/Krümmung), aber nicht die
absolute Höhe — dafür fehlt eine Information (genau das „\( +C \)" der Stammfunktion).

</details>
</details>

### Ein Beispiel zum Mitlesen

Nimm \( f(x) = \tfrac13 x^3 - x \). Dann ist die Ableitung \( f'(x) = x^2 - 1 \) und eine Stammfunktion
\( F(x) = \tfrac{1}{12}x^4 - \tfrac12 x^2 \). Schau im Diagramm, wie die drei zusammenhängen:

<div class="jxgbox" id="jxg-Ffstrich" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-Ffstrich',{boundingbox:[-2.6,4.0,2.6,-2.6],axis:true,showCopyright:false,showNavigation:false});
var F=b.create('functiongraph',[function(x){return x*x*x*x/12 - x*x/2;},-2.5,2.5],{strokeColor:'#c98a3a',strokeWidth:2,dash:2});
var f=b.create('functiongraph',[function(x){return x*x*x/3 - x;},-2.5,2.5],{strokeColor:'#3a5a9c',strokeWidth:2.5});
var fs=b.create('functiongraph',[function(x){return x*x - 1;},-2.5,2.5],{strokeColor:'#d98324',strokeWidth:2});
b.create('point',[-1,2/3],{name:'HP von f',size:2,fixed:true,color:'#3a5a9c',label:{offset:[-58,6]}});
b.create('point',[1,-2/3],{name:'TP von f',size:2,fixed:true,color:'#3a5a9c',label:{offset:[6,-12]}});
b.create('point',[-1,0],{name:'',size:2,fixed:true,color:'#d98324'});
b.create('point',[1,0],{name:'',size:2,fixed:true,color:'#d98324'});
})();</script>

<p class="muted">Blau: \( f \) · Orange: \( f'=x^2-1 \) · Gestrichelt: \( F \). Achte auf die Stellen
\( x=-1 \) und \( x=1 \): Dort schneidet \( f' \) (orange) die \( x \)-Achse — und genau dort hat \( f \)
(blau) seinen Hoch- bzw. Tiefpunkt.</p>

<details><summary>Lies es am Graphen ab (selbst prüfen)</summary>

- Links von \( x=-1 \) liegt \( f' \) (orange) <em>oberhalb</em> der Achse → \( f \) (blau) <b>steigt</b> dort.
- Zwischen \( x=-1 \) und \( x=1 \) liegt \( f' \) <em>unterhalb</em> der Achse → \( f \) <b>fällt</b> dort.
- Bei \( x=-1 \): \( f' \) wechselt von \( + \) nach \( - \) → \( f \) hat den <b>Hochpunkt</b> \( \left(-1,\tfrac23\right) \).
- Bei \( x=1 \): \( f' \) wechselt von \( - \) nach \( + \) → \( f \) hat den <b>Tiefpunkt</b> \( \left(1,-\tfrac23\right) \).

<details><summary>Probe der Werte (rechnerfrei)</summary>

\( f(-1) = \tfrac13(-1)^3 - (-1) = -\tfrac13 + 1 = \tfrac23 \) und \( f(1) = \tfrac13\cdot 1^3 - 1 = -\tfrac23 \). Die
markierten Punkte stimmen. Und \( f'(\pm1) = (\pm1)^2 - 1 = 0 \) — waagerechte Tangenten an genau diesen Stellen.

</details>
</details>

## In drei Sätzen für die Prüfung

Wenn du im Prüfungsgespräch das Wesentliche sagen sollst, reicht das hier — frei und in eigenen Worten:

- Eine <b>Stammfunktion</b> \( F \) ist eine Funktion mit \( F'=f \); sie entsteht durch Ableiten rückwärts und
  ist nur bis auf eine Konstante \( +C \) bestimmt.
- Der <b>Hauptsatz</b> sagt \( \int_a^b f = F(b)-F(a) \): das Integral ist die Differenz der Stammfunktion an
  den Rändern — als Bestandsänderung gelesen oder als orientierte Fläche.
- Die Kette \( F \to f \to f' \) ist „ableiten"; eine <b>Nullstelle von \( f' \)</b> mit Vorzeichenwechsel
  bedeutet eine <b>Extremstelle von \( f \)</b>.
