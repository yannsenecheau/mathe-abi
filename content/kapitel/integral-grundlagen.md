# Integralrechnung — Grundlagen

In diesem Kapitel geht es um eine einzige große Idee: **Flächen unter und zwischen Graphen messen**.
Du lernst zuerst, was der Wert eines Integrals *geometrisch* bedeutet (mit Vorzeichen!), und danach,
wie du daraus echte Flächeninhalte rechnerfrei bestimmst — auch dann, wenn der Graph mitten im
Intervall die x-Achse kreuzt oder du die Fläche zwischen zwei Kurven brauchst.

Eine Sache vorweg, Léona: In deiner Prüfung rechnest du das alles **von Hand**, ohne Taschenrechner.
Genau darauf ist dieses Kapitel ausgelegt — alle Zahlen sind so gewählt, dass du sie im Kopf bzw. mit
Bruchrechnung sicher erreichst.

<span class="tag tag-ok">Relevanz: Kernthema mündliche Prüfung Basisfach, AB I–II</span>

## Worauf wir aufbauen (der Hauptsatz, ganz kurz)

Das Werkzeug, mit dem wir jedes Integral ausrechnen, ist der **Hauptsatz der Differential- und
Integralrechnung**. Er sagt: Wenn \( F \) eine **Stammfunktion** von \( f \) ist (also \( F'(x)=f(x) \)),
dann gilt

\[ \int_a^b f(x)\,dx = \big[\,F(x)\,\big]_a^b = F(b) - F(a). \]

Mehr brauchst du fürs Rechnen nicht. Wie man Stammfunktionen findet, ist ein eigenes Thema — hier
nutzen wir nur die **Potenzregel für Stammfunktionen**: \( x^n \) wird zu \( \tfrac{1}{n+1}x^{n+1} \).

<details><summary>Potenzregel für Stammfunktionen — kurz nachgewiesen</summary>

Behauptung: Eine Stammfunktion von \( f(x)=x^n \) (mit \( n\neq -1 \)) ist \( F(x)=\tfrac{1}{n+1}x^{n+1} \).

**Probe durch Ableiten** (das ist die Haltung: eine Stammfunktion prüft man immer, indem man sie
*zurück*ableitet und schaut, ob \( f \) herauskommt):
\[ F'(x) = \tfrac{1}{n+1}\cdot (n+1)\, x^{n} = x^{n} = f(x). \quad\checkmark \]

<details><summary>Warum \( n\neq -1 \)?</summary>

Für \( n=-1 \) wäre der Nenner \( n+1 = 0 \) — Division durch null, verboten. Der Fall \( f(x)=\tfrac1x \)
braucht deshalb eine andere Stammfunktion (den Logarithmus) und gehört nicht zum Basisfach-Kern.

<span class="tag tag-warn">Relevanz: \( f(x)=\tfrac1x \) und ihre Stammfunktion offiziell Leistungsfach [97 %] — mit Lehrkraft prüfen</span>

</details>
</details>

## Der orientierte Flächeninhalt — was das Vorzeichen bedeutet

Der Wert eines Integrals \( \int_a^b f(x)\,dx \) ist ein **orientierter** (vorzeichenbehafteter)
Flächeninhalt. Das ist der wichtigste Begriff dieses Kapitels:

- Wo der Graph **oberhalb** der x-Achse liegt (\( f(x)>0 \)), zählt die Fläche **positiv** (\( + \)).
- Wo der Graph **unterhalb** der x-Achse liegt (\( f(x)<0 \)), zählt die Fläche **negativ** (\( - \)).

Das Integral addiert diese vorzeichenbehafteten Stücke. Liegt also gleich viel Fläche ober- wie
unterhalb, kann das Integral sogar \( 0 \) werden, obwohl „Fläche da ist". Genau hier passiert der
häufigste Fehler — merke dir den Unterschied:

> **Integralwert** = orientierte (vorzeichenbehaftete) Bilanz. &nbsp;**Flächeninhalt** = immer \( \geq 0 \).

<details><summary>Haltung: Warum überhaupt mit Vorzeichen? Wozu ist das gut?</summary>

Das Vorzeichen ist kein Schönheitsfehler, sondern die eigentliche Stärke des Integrals. Es erlaubt, mit
Flächen zu *rechnen* wie mit Zahlen — Stücke addieren, abziehen, verschieben. Eine reine „Fläche \(\geq 0\)"
könnte man nicht so flexibel kombinieren. Deshalb ist die Grundgröße der **orientierte** Flächeninhalt,
und den echten Flächeninhalt holen wir uns daraus, indem wir die Vorzeichen bewusst behandeln (s. u.).

<details><summary>Woher kommt das Vorzeichen — Annahme dahinter</summary>

Man stellt sich das Integral als Summe vieler schmaler Rechtecke der Breite \( \Delta x \) und der Höhe
\( f(x) \) vor. Ist \( f(x)<0 \), ist die „Höhe" negativ, das Rechteck zählt also negativ. Beim
Grenzübergang \( \Delta x\to 0 \) bleibt dieses Vorzeichen erhalten. (Diese Summen-Idee ist die
Definition des Integrals; wir verwenden sie hier nur als anschauliche Begründung, nicht zum Rechnen.)

</details>
</details>

### Beispiel zum Orientieren: \( f(x)=x \) über \( [-1,\,2] \) <span class="tag tag-ok">AB I</span>

Schau dir den Graphen an: Die Gerade liegt links von \( 0 \) **unter** der Achse (negativer Beitrag),
rechts von \( 0 \) **über** der Achse (positiver Beitrag).

<div class="jxgbox" id="jxg-orient" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-orient',{boundingbox:[-2.2,2.6,2.8,-1.8],axis:true,showCopyright:false,showNavigation:false});
var f=function(x){return x;};
// Fläche unter der Achse (links, negativ): von (-1,0) entlang Graph bis (0,0)
var xs=[],ys=[]; xs.push(-1);ys.push(0); for(var t=-1;t<=0.0001;t+=0.05){xs.push(t);ys.push(f(t));} xs.push(0);ys.push(0);
b.create('curve',[xs,ys],{fillColor:'#d98324',fillOpacity:0.28,strokeWidth:0,withLabel:false});
// Fläche über der Achse (rechts, positiv): von (0,0) entlang Graph bis (2,0)
var xs2=[],ys2=[]; xs2.push(0);ys2.push(0); for(var u=0;u<=2.0001;u+=0.05){xs2.push(u);ys2.push(f(u));} xs2.push(2);ys2.push(0);
b.create('curve',[xs2,ys2],{fillColor:'#3a5a9c',fillOpacity:0.28,strokeWidth:0,withLabel:false});
b.create('functiongraph',[f,-1.8,2.4],{strokeColor:'#3a5a9c',strokeWidth:2.5});
b.create('text',[-0.95,-0.75,'− (negativ)'],{fontSize:13,color:'#a8651a'});
b.create('text',[1.05,0.55,'+ (positiv)'],{fontSize:13,color:'#27406e'});
})();</script>

Wir rechnen den **orientierten** Wert mit der Stammfunktion \( F(x)=\tfrac12 x^2 \):

\[ \int_{-1}^{2} x\,dx = \Big[\tfrac12 x^2\Big]_{-1}^{2} = \tfrac12\cdot 4 - \tfrac12\cdot 1 = 2 - \tfrac12 = \tfrac32. \]

Das ist die **Bilanz**: Der positive Teil rechts überwiegt den negativen Teil links um \( \tfrac32 \).

<details><summary>Und der echte Flächeninhalt? (hier schon mal als Vorschau)</summary>

Den echten Flächeninhalt bekommen wir, indem wir an der Nullstelle \( x=0 \) **trennen** und die Beträge
addieren:
\[ \int_{-1}^{0} x\,dx = \Big[\tfrac12 x^2\Big]_{-1}^{0} = 0 - \tfrac12 = -\tfrac12, \qquad
   \int_{0}^{2} x\,dx = 2. \]
\[ A = \big|{-\tfrac12}\big| + |2| = \tfrac12 + 2 = \tfrac52. \]

Sieh den Unterschied: orientierte Bilanz \( \tfrac32 \), echte Fläche \( \tfrac52 \). Genau dieses
Trennen üben wir gleich systematisch.

</details>

## Fläche zwischen Graph und x-Achse — der Standardfall

Liegt der Graph im ganzen Intervall **auf einer Seite** der x-Achse, ist es einfach:

- Graph komplett **oberhalb**: Fläche \( = \displaystyle\int_a^b f(x)\,dx \) (Wert ist schon positiv).
- Graph komplett **unterhalb**: Fläche \( = \displaystyle\left|\int_a^b f(x)\,dx\right| = -\int_a^b f(x)\,dx \).

Der entscheidende Schritt — und die typische Falle — kommt, **wenn der Graph die x-Achse im Intervall
kreuzt**. Dann hat das Integral teils positive, teils negative Beiträge, die sich gegenseitig wegkürzen.
Das darf bei einer Flächenaufgabe nicht passieren.

> **Rezept bei Vorzeichenwechsel:** Nullstellen im Intervall bestimmen → an jeder Nullstelle das Integral
> **trennen** → von jedem Teilintegral den **Betrag** nehmen → die Beträge **addieren**.

<details><summary>Haltung: Warum nicht einfach „ein Integral über alles"?</summary>

Weil das Integral die Stücke mit ihrem Vorzeichen *verrechnet*. Ein Teil unter der Achse (negativ) würde
einen Teil über der Achse (positiv) auffressen — du bekämest die *Bilanz*, nicht die *Fläche*. Die Fläche
will aber jedes Stück positiv zählen. Deshalb: erst trennen, dann jedes Stück positiv machen, dann addieren.
Das ist die wichtigste Routine dieses Kapitels.

</details>

### Beispiel mit Vorzeichenwechsel: \( f(x)=x^2-1 \) über \( [0,\,2] \) <span class="tag tag-ok">AB II</span>

Der Graph (eine nach oben geöffnete Parabel, um \( 1 \) nach unten verschoben) hat im Intervall die
Nullstelle \( x=1 \): links davon liegt er **unter** der Achse, rechts davon **über** der Achse.

<div class="jxgbox" id="jxg-vzw" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-vzw',{boundingbox:[-0.6,3.4,2.6,-1.6],axis:true,showCopyright:false,showNavigation:false});
var f=function(x){return x*x-1;};
// Stück 1: [0,1] unter der Achse (negativ -> orange)
var a1=[],o1=[]; a1.push(0);o1.push(0); for(var t=0;t<=1.0001;t+=0.04){a1.push(t);o1.push(f(t));} a1.push(1);o1.push(0);
b.create('curve',[a1,o1],{fillColor:'#d98324',fillOpacity:0.3,strokeWidth:0});
// Stück 2: [1,2] über der Achse (positiv -> blau)
var a2=[],o2=[]; a2.push(1);o2.push(0); for(var u=1;u<=2.0001;u+=0.04){a2.push(u);o2.push(f(u));} a2.push(2);o2.push(0);
b.create('curve',[a2,o2],{fillColor:'#3a5a9c',fillOpacity:0.3,strokeWidth:0});
b.create('functiongraph',[f,-0.4,2.4],{strokeColor:'#3a5a9c',strokeWidth:2.5});
b.create('point',[1,0],{name:'N(1|0)',size:2,fixed:true,color:'#27406e',label:{offset:[6,-14]}});
b.create('text',[0.35,-0.7,'A₁'],{fontSize:15,color:'#a8651a'});
b.create('text',[1.55,0.7,'A₂'],{fontSize:15,color:'#27406e'});
})();</script>

**Schritt 1 — Nullstellen im Intervall finden.** <span class="tag tag-ok">AB I</span>

\[ x^2 - 1 = 0 \;\Longleftrightarrow\; x^2 = 1 \;\Longleftrightarrow\; x = \pm 1. \]
Im Intervall \( [0,2] \) liegt nur \( x=1 \). Dort trennen wir.

<details><summary>Haltung: Warum zuerst die Nullstellen?</summary>

Die Nullstellen sind genau die Stellen, an denen der Graph die Seite wechselt — wo also aus „\(+\)"
ein „\(-\)" wird (oder umgekehrt). Nur dort muss getrennt werden. Findest du sie nicht, übersiehst du
den Vorzeichenwechsel und rechnest die falsche (zu kleine) Fläche. Erst die Nullstellen, dann alles
andere — das ist die feste Reihenfolge.

</details>

**Schritt 2 — Stammfunktion und Teilintegrale.** <span class="tag tag-ok">AB II</span>

Stammfunktion: \( F(x) = \tfrac{1}{3}x^3 - x \) (Potenzregel; \( \int 1\,dx = x \)).

Teilintegral links (\( [0,1] \), erwartet **negativ**, weil unter der Achse):
\[ \int_0^1 (x^2-1)\,dx = \Big[\tfrac{1}{3}x^3 - x\Big]_0^1 = \big(\tfrac13 - 1\big) - 0 = -\tfrac{2}{3}. \]

Teilintegral rechts (\( [1,2] \), erwartet **positiv**):
\[ \int_1^2 (x^2-1)\,dx = \Big[\tfrac{1}{3}x^3 - x\Big]_1^2 = \big(\tfrac{8}{3} - 2\big) - \big(\tfrac13 - 1\big) = \tfrac{2}{3} - \big(-\tfrac{2}{3}\big) = \tfrac{4}{3}. \]

<details><summary>Die Bruchrechnung der rechten Grenze Schritt für Schritt</summary>

Oben \( F(2) = \tfrac{1}{3}\cdot 8 - 2 = \tfrac{8}{3} - \tfrac{6}{3} = \tfrac{2}{3} \).
Unten \( F(1) = \tfrac{1}{3} - 1 = \tfrac{1}{3} - \tfrac{3}{3} = -\tfrac{2}{3} \).
Differenz \( F(2)-F(1) = \tfrac{2}{3} - \big(-\tfrac{2}{3}\big) = \tfrac{2}{3} + \tfrac{2}{3} = \tfrac{4}{3} \).
Vorzeichen positiv — passt zur Lage über der Achse. Das ist der Plausibilitäts-Check: Stimmt das
Vorzeichen des Teilintegrals mit der Lage im Bild überein?

</details>

**Schritt 3 — Beträge nehmen und addieren.** <span class="tag tag-ok">AB II</span>

\[ A = \Big|{-\tfrac{2}{3}}\Big| + \Big|\tfrac{4}{3}\Big| = \tfrac{2}{3} + \tfrac{4}{3} = \tfrac{6}{3} = 2. \]

Der gesuchte Flächeninhalt ist \( A = 2 \).

<details><summary>Gegenprobe: Was hätte „ein Integral über alles" geliefert — und warum ist das falsch?</summary>

\[ \int_0^2 (x^2-1)\,dx = \Big[\tfrac{1}{3}x^3 - x\Big]_0^2 = \tfrac{8}{3} - 2 = \tfrac{2}{3}. \]
Das ist die **orientierte Bilanz** \( \tfrac23 \) — viel kleiner als die echte Fläche \( 2 \), weil sich
der negative Teil \( -\tfrac23 \) und ein Teil des positiven \( \tfrac43 \) gegenseitig aufgehoben haben
(\( -\tfrac23 + \tfrac43 = \tfrac23 \)). Genau diesen Fehler vermeidest du, indem du an der Nullstelle
trennst und Beträge addierst.

</details>

## Fläche zwischen zwei Graphen

Oft ist nicht die Fläche zur x-Achse gesucht, sondern die **eingeschlossene Fläche zwischen zwei
Kurven**. Die Idee ist dieselbe wie eben — nur misst du die Höhe der Fläche jetzt nicht von der Achse
zur Kurve, sondern **von der unteren zur oberen Kurve**:

\[ A = \int_a^b \big(\,\text{obere Funktion} - \text{untere Funktion}\,\big)\,dx. \]

Dabei sind \( a \) und \( b \) die **Schnittstellen** der beiden Graphen.

<details><summary>Haltung: Warum „oben minus unten" — und warum darf man die Achse dabei vergessen?</summary>

Stell dir an jeder Stelle \( x \) einen senkrechten Strich von der unteren bis zur oberen Kurve vor. Seine
Länge ist \( \text{oben}(x) - \text{unten}(x) \) — und das ist **immer \( \geq 0 \)**, solange „oben"
wirklich oben liegt. Aufsummiert über alle \( x \) ergibt das die Fläche. Ob beide Kurven über, unter oder
quer zur x-Achse liegen, spielt dabei **keine Rolle**: Eine gemeinsame Verschiebung nach oben/unten
verändert beide gleich und fällt in der Differenz heraus.

<details><summary>Das Wegfallen der Verschiebung — gezeigt</summary>

Verschiebt man beide um denselben Wert \( c \) nach oben, wird aus der Differenz
\[ (\text{oben}+c) - (\text{unten}+c) = \text{oben} - \text{unten}. \]
Das \( +c \) kürzt sich weg. Deshalb darfst du die Achsenlage ignorieren — *solange* sich die Kurven im
Intervall nicht überholen. Tun sie das (zusätzliche Schnittstellen dazwischen), trennst du dort genauso
wie bei den Nullstellen oben.

</details>
</details>

### Beispiel: Fläche zwischen \( g(x)=x \) und \( f(x)=x^2 \) <span class="tag tag-ok">AB II</span>

<div class="jxgbox" id="jxg-zwei" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-zwei',{boundingbox:[-0.4,1.5,1.5,-0.4],axis:true,showCopyright:false,showNavigation:false});
var g=function(x){return x;};        // obere Funktion auf [0,1]
var f=function(x){return x*x;};      // untere Funktion auf [0,1]
// Eingeschlossene Fläche: hin entlang g (oben), zurück entlang f (unten)
var xs=[],ys=[];
for(var t=0;t<=1.0001;t+=0.02){xs.push(t);ys.push(g(t));}
for(var u=1;u>=-0.0001;u-=0.02){xs.push(u);ys.push(f(u));}
b.create('curve',[xs,ys],{fillColor:'#3a5a9c',fillOpacity:0.22,strokeWidth:0});
b.create('functiongraph',[g,-0.3,1.4],{strokeColor:'#27406e',strokeWidth:2.5,name:'g(x)=x',withLabel:true,label:{offset:[-30,8]}});
b.create('functiongraph',[f,-0.3,1.4],{strokeColor:'#d98324',strokeWidth:2.5,name:'f(x)=x²',withLabel:true,label:{offset:[6,-6]}});
b.create('point',[0,0],{name:'',size:1.5,fixed:true,color:'#444'});
b.create('point',[1,1],{name:'S',size:2,fixed:true,color:'#444',label:{offset:[6,-12]}});
})();</script>

**Schritt 1 — Schnittstellen bestimmen.** <span class="tag tag-ok">AB I</span>

Gleichsetzen:
\[ x = x^2 \;\Longleftrightarrow\; x^2 - x = 0 \;\Longleftrightarrow\; x(x-1)=0 \;\Longrightarrow\; x=0 \ \text{oder}\ x=1. \]
Die Integrationsgrenzen sind also \( a=0 \) und \( b=1 \).

<details><summary>Haltung: Warum durch Ausklammern statt mit der p-q-Formel?</summary>

Steht bei einer quadratischen Gleichung kein konstantes Glied (hier \( x^2 - x = 0 \)), ist \( x \) in
jedem Term enthalten — dann **ausklammern**: \( x(x-1)=0 \). Ein Produkt ist null, wenn ein Faktor null
ist (Satz vom Nullprodukt). Das ist rechnerfrei schneller und sicherer als die p-q-Formel. Faustregel:
fehlt das absolute Glied, immer erst ausklammern.

</details>

**Schritt 2 — Wer ist oben?** <span class="tag tag-ok">AB II</span>

Auf \( (0,1) \), z. B. bei \( x=\tfrac12 \): \( g(\tfrac12)=\tfrac12 \) und \( f(\tfrac12)=\tfrac14 \).
Wegen \( \tfrac12 > \tfrac14 \) liegt \( g \) **oben**, \( f \) **unten**. Also rechnen wir \( g - f \).

<details><summary>Haltung: die Testeinsetzung — eine Zahl genügt</summary>

Zwischen zwei aufeinanderfolgenden Schnittstellen kann sich die Reihenfolge „oben/unten" nicht ändern
(sonst gäbe es dazwischen eine weitere Schnittstelle). Deshalb reicht **ein** Testpunkt im Inneren, um
zu entscheiden, wer oben liegt. Verlässt du dich nur aufs Bild, ist die Testeinsetzung die saubere
Absicherung — und sie schützt dich vor dem Vorzeichenfehler, falls du „oben" und „unten" vertauschst.

</details>

**Schritt 3 — Integrieren.** <span class="tag tag-ok">AB II</span>

\[ A = \int_0^1 \big(x - x^2\big)\,dx = \Big[\tfrac{1}{2}x^2 - \tfrac{1}{3}x^3\Big]_0^1
     = \Big(\tfrac{1}{2} - \tfrac{1}{3}\Big) - 0. \]

\[ \tfrac{1}{2} - \tfrac{1}{3} = \tfrac{3}{6} - \tfrac{2}{6} = \tfrac{1}{6}. \qquad\Longrightarrow\qquad A = \tfrac{1}{6}. \]

Die eingeschlossene Fläche beträgt \( \tfrac{1}{6} \).

<details><summary>Plausibilitäts-Check: Kann das stimmen?</summary>

Die Fläche liegt im Einheitsquadrat \( [0,1]\times[0,1] \) (Flächeninhalt \( 1 \)) und ist nur die schmale
Sichel zwischen Gerade und Parabel. Ein Ergebnis von \( \tfrac16 \approx 0{,}17 \), also rund ein Sechstel
des Quadrats, ist von der Größenordnung her stimmig. So einen schnellen „passt die Größenordnung?"-Blick
solltest du dir am Ende jeder Flächenaufgabe angewöhnen.

</details>

## Die Schritt-für-Schritt-Routine (zum Auswendig-Vortragen)

Wenn dich die Prüferin nach einer Fläche fragt, hast du immer denselben Fahrplan — sag ihn ruhig laut mit:

1. **Skizze/Lage klären:** Liegt der Graph über oder unter der Achse? (Bzw. bei zwei Graphen: wer ist oben?)
2. **Grenzen finden:** Nullstellen (Fläche zur Achse) bzw. Schnittstellen (zwei Graphen) berechnen.
3. **Trennen, wo es nötig ist:** an jeder Nullstelle/Schnittstelle im Inneren das Integral aufteilen.
4. **Stammfunktion bilden** und die Teilintegrale mit \( F(b)-F(a) \) ausrechnen.
5. **Beträge nehmen** (Fläche zur Achse) bzw. **oben − unten** (zwei Graphen) und **addieren**.
6. **Plausibilität prüfen:** Vorzeichen passt zur Lage, Größenordnung passt zur Skizze.

<details><summary>Die zwei Fallen, die am meisten Punkte kosten</summary>

- **Vorzeichenwechsel übersehen.** „Ein Integral über alles" bei einem Graphen, der die Achse kreuzt,
  liefert die Bilanz, nicht die Fläche. Immer an den Nullstellen trennen und Beträge addieren.
- **„oben − unten" vertauscht.** Bei zwei Graphen führt die falsche Reihenfolge zu einem negativen
  Ergebnis. Eine Fläche ist nie negativ — ein negatives Resultat ist dein Signal, oben/unten zu tauschen
  (oder den Betrag zu nehmen).

</details>
