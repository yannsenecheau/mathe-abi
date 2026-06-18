# Aufgabe: Graphenpaar f und g

Das ist eine typische mündliche Prüfungsaufgabe zur <b>Analysis</b>. Sie testet, ob du einen
Graphen <b>lesen</b>, sicher <b>per Hand ableiten</b> und über <b>Verschiebung und Symmetrie</b>
argumentieren kannst — und das alles <b>rechnerfrei</b>. Genau das brauchst du im Gespräch.

Gegeben ist die Funktion
\[ f(x) = \tfrac{1}{4}x^4 - 2x^2 . \]
Die Abbildung zeigt den Graphen von \( f \) (<span style="color:#c0392b;font-weight:600">rot</span>)
und einen zweiten Graphen \( g \) (<span style="color:#2d6cb3;font-weight:600">blau</span>), der durch
Verschiebung aus \( f \) entsteht.

<div class="jxgbox" id="jxg-graphenpaar" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-graphenpaar',{boundingbox:[-4,6,10,-6],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 0.25*x*x*x*x-2*x*x;},-3.2,3.2],{strokeColor:'#c0392b',strokeWidth:2.5,name:'f',withLabel:true});b.create('functiongraph',[function(x){return 0.25*(x-6)*(x-6)*(x-6)*(x-6)-2*(x-6)*(x-6);},2.8,9.2],{strokeColor:'#2d6cb3',strokeWidth:2.5,name:'g',withLabel:true});b.create('point',[2,-4],{name:'Tiefpunkt',size:2,fixed:true,color:'#c0392b',label:{offset:[6,-12]}});b.create('point',[-2,-4],{name:'',size:2,fixed:true,color:'#c0392b'});})();</script>

> So gehst du eine solche Aufgabe an: <b>erst lesen, dann rechnen, dann begründen.</b> Sage in der
> Prüfung jeden Schritt laut mit — die Prüfenden bewerten deinen <b>Gedankengang</b>, nicht nur das
> Ergebnis.

<span class="tag tag-warn">Relevanz: Die Aufgabe nutzt eine Funktion vierten Grades. Die Techniken
(Ableiten per Potenzregel, Graph lesen, Verschiebung, Symmetrie) sind voll Basisfach-relevant; der
hohe Funktionsgrad ist im Basisfach eher selten — die <b>Methode</b> ist das Lernziel. Mit Lehrkraft
prüfen.</span>

## a) Zwei markante Eigenschaften benennen <span class="tag tag-ok">AB I</span>

Schon ohne Rechnung kannst du aus dem roten Graphen zwei sichere Aussagen über \( f \) ablesen:

1. <b>Symmetrie zur \( y \)-Achse</b> (\( f \) ist eine gerade Funktion): Der Graph links und rechts
   der \( y \)-Achse ist spiegelbildlich.
2. <b>Zwei Tiefpunkte und ein Hochpunkt</b> dazwischen: Bei \( T_1(-2\mid -4) \) und
   \( T_2(2\mid -4) \) liegt jeweils ein Tiefpunkt, bei \( H(0\mid 0) \) ein Hochpunkt (lokales
   Maximum). Man nennt eine solche Form <b>„W-Form"</b>.

<details><summary>Haltung: Woran erkenne ich die Achsensymmetrie — und warum stimmt sie hier?</summary>

In der Prüfung darfst du Achsensymmetrie zur \( y \)-Achse behaupten, wenn \( f(-x) = f(x) \) für alle
\( x \) gilt. Das prüfst du am Funktionsterm, nicht am Bild:
\[ f(-x) = \tfrac{1}{4}(-x)^4 - 2(-x)^2 = \tfrac{1}{4}x^4 - 2x^2 = f(x). \]

<details><summary>Warum macht das gerade die geraden Hochzahlen?</summary>

\( (-x)^4 = x^4 \) und \( (-x)^2 = x^2 \), weil eine <b>gerade</b> Anzahl von Minuszeichen sich
aufhebt. Stünde im Term auch eine ungerade Potenz wie \( x^3 \) oder \( x^1 \), wäre die Symmetrie
zerstört. Faustregel: <b>nur gerade Hochzahlen \( \Rightarrow \) achsensymmetrisch zur \( y \)-Achse.</b>

</details>

<b>Typische Falle:</b> „Der Graph sieht symmetrisch aus" ist als Begründung zu wenig. Argumentiere
über den Term \( f(-x)=f(x) \) — das Bild ist nur der Anlass, nicht der Beweis.

</details>

<details><summary>Haltung: Warum darf ich die Tiefpunkte hier auch ohne Rechnung nennen?</summary>

Aus der Abbildung liest du die ungefähre Lage ab; die <b>genauen</b> Stellen kommen aus
\( f'(x)=0 \) (siehe Teil c-Box). Für eine mündliche Eigenschafts-Nennung in AB I genügt: „zwei
Tiefpunkte, ein Hochpunkt, achsensymmetrisch". Wenn du Werte angibst, solltest du sie kurz
absichern können — darum lohnt es sich, \( f'(x)=x^3-4x \) im Kopf zu haben (Nullstellen
\( x=0 \) und \( x=\pm 2 \)).

</details>

## b) f(4) und f'(4) bestimmen <span class="tag tag-ok">AB I</span>

<b>Funktionswert.</b> Setze \( x=4 \) ein:
\[ f(4) = \tfrac{1}{4}\cdot 4^4 - 2\cdot 4^2 = \tfrac{1}{4}\cdot 256 - 2\cdot 16 = 64 - 32 = 32 . \]

<details><summary>Haltung: rechnerfrei mit Potenzen umgehen</summary>

\( 4^4 = 4^2\cdot 4^2 = 16\cdot 16 = 256 \). Den Faktor \( \tfrac14 \) ziehst du als Division durch
\( 4 \) durch: \( 256:4 = 64 \). Dann \( 4^2 = 16 \), also \( 2\cdot 16 = 32 \). So bleibt jeder
Zwischenschritt eine kleine Kopfrechnung — genau das ist der Sinn der hilfsmittelfreien Prüfung.

</details>

<b>Ableitung.</b> Zuerst die Ableitungsfunktion bilden, dann \( x=4 \) einsetzen:
\[ f'(x) = \tfrac{1}{4}\cdot 4x^3 - 2\cdot 2x = x^3 - 4x , \qquad
   f'(4) = 4^3 - 4\cdot 4 = 64 - 16 = 48 . \]

<details><summary>Haltung: erst die Ableitungsfunktion, dann einsetzen</summary>

Leite <b>summandenweise</b> mit der Potenzregel ab: aus \( x^n \) wird \( n\,x^{n-1} \).

<details><summary>Schritt für Schritt</summary>

- \( \tfrac14 x^4 \;\to\; \tfrac14\cdot 4\,x^{3} = x^3 \) — der Vorfaktor \( \tfrac14 \) und die
  herabgezogene \( 4 \) kürzen sich zu \( 1 \).
- \( -2x^2 \;\to\; -2\cdot 2\,x^{1} = -4x \).
- Konstante gäbe es hier keine; eine reine Zahl fiele beim Ableiten weg.

Ergebnis: \( f'(x) = x^3 - 4x \).

</details>

<b>Typische Falle:</b> nicht \( x=4 \) schon in \( f \) einsetzen und das Ergebnis ableiten — dann
leitest du eine <b>Zahl</b> ab und bekommst \( 0 \). Erst die <b>Funktion</b> ableiten, dann den Wert
einsetzen.

</details>

Die Steigung des Graphen von \( f \) an der Stelle \( x=4 \) ist also \( 48 \) — der Graph steigt dort
sehr steil an. <span class="tag tag-ok">AB I</span>

## c) Ist f''(0) = 0 wahr oder falsch? <span class="tag tag-ok">AB II</span>

Die Behauptung lautet \( f''(0)=0 \). Wir prüfen sie, indem wir die <b>zweite Ableitung</b> bestimmen
und \( x=0 \) einsetzen:
\[ f'(x) = x^3 - 4x \;\Rightarrow\; f''(x) = 3x^2 - 4 , \qquad f''(0) = 3\cdot 0 - 4 = -4 . \]

Wegen \( f''(0) = -4 \neq 0 \) ist die Behauptung <b>falsch</b>.

<details><summary>Haltung: Was würde f''(0)=0 überhaupt bedeuten — und warum ist es hier nicht so?</summary>

\( f''(x)=0 \) ist das <b>notwendige Kriterium für eine Wendestelle</b> (dort, wo die Krümmung das
Vorzeichen wechselt). Die Behauptung unterstellt also, bei \( x=0 \) liege ein Wendepunkt. Das passt
nicht zum Bild: Bei \( x=0 \) hat \( f \) einen <b>Hochpunkt</b>, keine Wende.

<details><summary>Warum bestätigt f''(0)=-4 den Hochpunkt?</summary>

Bei \( x=0 \) ist \( f'(0) = 0^3 - 4\cdot 0 = 0 \) (waagrechte Tangente, notwendige Bedingung für
einen Extrempunkt erfüllt). Das Vorzeichen von \( f'' \) entscheidet über die Art:
\( f''(0) = -4 < 0 \) bedeutet <b>Linkskrümmung nach unten</b>, also einen <b>Hochpunkt</b>. Genau
das zeigt der rote Graph bei \( (0\mid 0) \).

</details>

<b>Typische Falle:</b> Eine waagrechte Tangente (\( f'(0)=0 \)) mit einer Wendestelle verwechseln.
\( f'=0 \) heißt „Extrem<i>kandidat</i>", \( f''=0 \) heißt „Wende<i>kandidat</i>". Hier liegt der
erste Fall vor.

</details>

<details><summary>Haltung: Wo liegen die echten Wendestellen von f?</summary>

Setze \( f''(x)=0 \): \( 3x^2 - 4 = 0 \Rightarrow x^2 = \tfrac{4}{3} \Rightarrow x = \pm\tfrac{2}{\sqrt3}
\approx \pm 1{,}15 \). Die Wendestellen liegen also <b>zwischen</b> Hochpunkt und Tiefpunkten,
nicht bei \( x=0 \) — das untermauert noch einmal, warum \( f''(0)=0 \) falsch ist.

</details>

## d) Funktionsgleichung von g (Verschiebung) <span class="tag tag-ok">AB II</span>

Der blaue Graph \( g \) hat dieselbe Form wie der rote Graph \( f \), liegt aber weiter rechts: Sein
mittlerer Hochpunkt sitzt bei \( x=6 \) statt bei \( x=0 \). \( g \) entsteht aus \( f \) durch eine
<b>Verschiebung um \( 6 \) nach rechts</b> (in positive \( x \)-Richtung), ohne Stauchung und ohne
vertikale Verschiebung. Damit gilt:
\[ g(x) = f(x-6) = \tfrac{1}{4}(x-6)^4 - 2(x-6)^2 . \]

<details><summary>Haltung: Warum „x − 6" und nicht „x + 6"?</summary>

Eine Verschiebung um \( a \) nach <b>rechts</b> ersetzt im Funktionsterm jedes \( x \) durch
\( x-a \). Das fühlt sich „verkehrt herum" an, ist aber logisch: Damit \( g \) an der Stelle \( x=6 \)
denselben Wert wie \( f \) bei \( 0 \) annimmt, muss das Argument \( x-6 \) zu \( 0 \) werden — also
\( g(6) = f(6-6) = f(0) = 0 \). Stimmt mit dem blauen Hochpunkt überein.

<details><summary>Gegenprobe an den Tiefpunkten</summary>

\( f \) hat Tiefpunkte bei \( x=\pm 2 \). Verschoben um \( 6 \) erwarten wir \( g \)-Tiefpunkte bei
\( x = -2+6 = 4 \) und \( x = 2+6 = 8 \). Tatsächlich: \( g(4) = f(-2) = -4 \) und
\( g(8) = f(2) = -4 \). Passt zum blauen Graphen. <span class="tag tag-ok">AB II</span>

</details>

<b>Typische Falle:</b> das Vorzeichen der Verschiebung vertauschen. Merksatz: <b>„rechts wirkt nach
links"</b> — Verschiebung nach rechts \( \Rightarrow x-a \), nach links \( \Rightarrow x+a \).

</details>

<details><summary>Wie kommst du auf gerade 6 — woher die Verschiebungsweite?</summary>

Lies zwei <b>einander entsprechende</b> markante Punkte ab: der Hochpunkt von \( f \) liegt bei
\( x=0 \), der von \( g \) bei \( x=6 \). Die Differenz \( 6-0 = 6 \) ist die Verschiebungsweite. In
der Prüfung nennst du den Punkt, an dem du die \( 6 \) abgelesen hast — das macht deine Antwort
nachvollziehbar. Ausmultiplizieren musst du \( (x-6)^4 \) <b>nicht</b>; die Form \( f(x-6) \) ist als
Funktionsgleichung vollständig und für Teil e) sogar die nützlichere.

</details>

## e) Integrale: Bedeutung und ∫ von g ohne Stammfunktion <span class="tag tag-ok">AB III</span>

Gegeben ist
\[ \int_{-2}^{2} f(x)\,dx \approx -7{,}47 . \]

<b>Graphische Bedeutung.</b> Das bestimmte Integral ist der <b>orientierte Flächeninhalt</b> zwischen
dem Graphen von \( f \) und der \( x \)-Achse über dem Intervall \( [-2,\,2] \). Auf diesem ganzen
Intervall verläuft der rote Graph <b>unterhalb</b> der \( x \)-Achse — nur im Punkt \( x=0 \) berührt er
sie (dort liegt der Hochpunkt \( (0\mid 0) \)). \( f \) ist nämlich zwischen seinen Nullstellen \( x=0 \)
und \( x=\pm 2\sqrt2 \approx \pm 2{,}83 \) negativ, und \( [-2,\,2] \) liegt ganz in diesem Bereich. Eine
Fläche <b>unterhalb</b> der Achse zählt mit <b>negativem Vorzeichen</b> — deshalb ist der Wert negativ. Der
Betrag \( 7{,}47 \) ist der <b>tatsächliche Flächeninhalt</b> dieser Fläche zwischen Kurve und Achse.

<details><summary>Haltung: Was heißt „orientiert" genau?</summary>

„Orientiert" bedeutet: Flächenstücke <b>über</b> der \( x \)-Achse zählen positiv, Flächenstücke
<b>darunter</b> negativ. Das Integral summiert beides <b>mit Vorzeichen</b>. Hier liegt das ganze
Stück unter der Achse, also ist die Summe rein negativ. Würdest du den reinen Flächeninhalt angeben
wollen, nähmst du den Betrag: \( 7{,}47 \).

<details><summary>Kurzcheck: Liegt f auf [−2, 2] wirklich unter der Achse?</summary>

\( f(x) = \tfrac14 x^4 - 2x^2 = x^2\big(\tfrac14 x^2 - 2\big) \). Der Faktor \( x^2 \ge 0 \). Der
Faktor \( \tfrac14 x^2 - 2 \) ist negativ, solange \( x^2 < 8 \), also für \( |x| < 2\sqrt2\approx
2{,}83 \). Auf \( [-2,2] \) ist das erfüllt — daher \( f(x) \le 0 \) dort, und das Integral ist
negativ. (Auf \( [-2,2] \) ist \( f \) nur an der Stelle \( x=0 \) gleich \( 0 \); die Nullstellen
\( x=\pm 2\sqrt2 \) liegen außerhalb dieses Intervalls.)

</details>

</details>

<b>Zweites Integral ohne Stammfunktion von g.</b> Gesucht ist \( \displaystyle\int_{4}^{8} g(x)\,dx \).
Statt eine Stammfunktion von \( g \) zu suchen, nutzt du, dass \( g \) nur die <b>verschobene</b>
Funktion \( f \) ist:
\[ \int_{4}^{8} g(x)\,dx = \int_{4}^{8} f(x-6)\,dx = \int_{-2}^{2} f(u)\,du \approx -7{,}47 . \]

<details><summary>Haltung: Warum darf ich einfach die Grenzen mitverschieben?</summary>

\( g \) ist gegenüber \( f \) um \( 6 \) nach rechts verschoben. Verschiebt man <b>Funktion und
Integrationsgrenzen um denselben Betrag</b>, bleibt die eingeschlossene Fläche unverändert — sie
liegt nur an einer anderen Stelle der \( x \)-Achse, hat aber exakt dieselbe Form und Größe.

<details><summary>Sauber begründet mit Substitution \( u = x-6 \)</summary>

Setze \( u = x-6 \), dann \( du = dx \). Die Grenzen wandern mit: aus \( x=4 \) wird \( u=4-6=-2 \),
aus \( x=8 \) wird \( u=8-6=2 \). Damit
\[ \int_{4}^{8} f(x-6)\,dx = \int_{-2}^{2} f(u)\,du \approx -7{,}47 . \]
Das ist genau das gegebene Integral aus dem ersten Teil — du musst <b>nichts</b> neu berechnen und
<b>keine</b> Stammfunktion von \( g \) bilden. <span class="tag tag-ok">AB III</span>

</details>

<details><summary>Anschaulich am Bild</summary>

Das Stück der blauen Kurve über \( [4,8] \) ist eine <b>1:1-Kopie</b> des roten Kurvenstücks über
\( [-2,2] \), nur um \( 6 \) nach rechts geschoben. Es schließt mit der \( x \)-Achse dieselbe Fläche
ein und liegt ebenfalls vollständig <b>unterhalb</b> der Achse. Gleiche Fläche, gleiches Vorzeichen
\( \Rightarrow \) gleicher Integralwert \( \approx -7{,}47 \).

</details>

<b>Typische Falle:</b> hier eine waagrechte (vertikale) Verschiebung vermuten und Flächen umrechnen
wollen. Es ist eine reine <b>Rechtsverschiebung</b> — die Fläche ändert sich dabei nicht, nur ihr
Ort. Genau deshalb ist die Stammfunktion überflüssig.

</details>

> <b>Merke für die Prüfung:</b> Wenn ein Integral „ohne Stammfunktion" gefragt ist, suche nach einer
> <b>Struktur</b>: Symmetrie, Verschiebung oder eine bereits bekannte Fläche. Das spart Rechnung und
> zeigt, dass du den Zusammenhang verstanden hast — genau das wird in AB III belohnt.
