# Prüfungssimulation 1 (Analysis)

Diese Simulation läuft im echten Format deiner mündlichen Prüfung, Léona: erst eine zusammenhängende
**Vortragsaufgabe** (etwa 10 Minuten, die du in der Vorbereitungszeit durcharbeitest und dann frei
präsentierst), danach ein **Prüfungsgespräch** mit Impulsfragen. Alles ist **rechnerfrei** zu lösen —
genau wie in beiden Teilen deiner Prüfung. Arbeite zuerst selbst, bevor du die Lösungswege aufklappst.

> So nutzt du die Seite: Decke die Lösungen zu, sprich deinen Vortrag **laut** durch (am besten als
> Sprachnachricht an Papa), und vergleiche erst danach mit dem Erwartungshorizont. Lautes Sprechen ist
> die halbe Prüfung.

## Vortragsaufgabe (~10 Min, zusammenhängend)

Gegeben ist die Funktion

\[ f(x) = \tfrac{1}{4}x^3 - \tfrac{3}{4}x. \]

Bearbeite die folgenden Teilaufgaben **zusammenhängend** und erkläre dabei laut, *was* du tust und
*warum*. Das laute Begründen ist in der mündlichen Prüfung genauso wichtig wie das Ergebnis.

**a)** <span class="tag tag-ok">AB I</span> Untersuche \( f \) auf Symmetrie und bestimme die
Nullstellen.

**b)** <span class="tag tag-ok">AB I</span> Bestimme die erste und zweite Ableitung von \( f \).

**c)** <span class="tag tag-warn">AB II</span> Bestimme die Hoch- und Tiefpunkte des Graphen und weise
ihre Art nach.

**d)** <span class="tag tag-warn">AB II</span> Bestimme den Wendepunkt und begründe, warum dort wirklich
eine Wendestelle vorliegt.

**e)** <span class="tag tag-warn">AB II</span> Berechne den Wert \( \displaystyle\int_0^2 f(x)\,dx \) und
deute das Vorzeichen des Ergebnisses geometrisch.

### Erwartungshorizont a) — Symmetrie und Nullstellen

<details><summary>Lösungsweg a) aufklappen</summary>

**Symmetrie.** In \( f(x) = \tfrac14 x^3 - \tfrac34 x \) kommen nur **ungerade** Potenzen von \( x \)
vor. Damit gilt \( f(-x) = -f(x) \), der Graph ist **punktsymmetrisch zum Ursprung**.

<details><summary>Haltung dahinter: warum reicht der Blick auf die Potenzen?</summary>

Ich prüfe Symmetrie zuerst, weil sie mir Arbeit spart: Eine Punktsymmetrie zum Ursprung halbiert die
Untersuchung — was ich rechts von der \( y \)-Achse finde (z. B. einen Tiefpunkt), hat links sein
gespiegeltes Gegenstück (einen Hochpunkt). Die **typische Falle** ist, Symmetrie zu „raten". Sauber ist
das Argument über die Definition: Ersetze ich \( x \) durch \( -x \), wird \( (-x)^3 = -x^3 \) und
\( (-x) = -x \), also \( f(-x) = -\tfrac14 x^3 + \tfrac34 x = -f(x) \) — das **ist** Punktsymmetrie zum
Ursprung. Nur ungerade Exponenten \( \Rightarrow \) punktsymmetrisch; nur gerade \( \Rightarrow \)
achsensymmetrisch zur \( y \)-Achse.

</details>

**Nullstellen.** Setze \( f(x) = 0 \):

\[ \tfrac14 x^3 - \tfrac34 x = \tfrac14 x\,(x^2 - 3) = 0. \]

Ein Produkt ist null, wenn ein Faktor null ist: \( x = 0 \) oder \( x^2 = 3 \), also
\( x = 0,\ x = \sqrt{3},\ x = -\sqrt{3} \).

<details><summary>Haltung dahinter: erst ausklammern, dann Satz vom Nullprodukt</summary>

Bevor ich „irgendeine" Lösungsformel ansetze, klammere ich den gemeinsamen Faktor \( x \) aus. Das ist
der rechnerfreie Standardweg bei ganzrationalen Funktionen ohne konstantes Glied: Eine Nullstelle ist
sofort \( x = 0 \), der Rest ist nur noch eine **quadratische** (hier sogar reine) Gleichung. Die
**typische Falle** ist, durch \( x \) zu teilen — dann verliert man die Nullstelle \( x = 0 \). Deshalb
nie dividieren, sondern ausklammern und den **Satz vom Nullprodukt** anwenden.

</details>
</details>

### Erwartungshorizont b) — Ableitungen

<details><summary>Lösungsweg b) aufklappen</summary>

Mit der **Potenzregel** \( (x^n)' = n\,x^{n-1} \), Faktor- und Summenregel:

\[ f'(x) = \tfrac14 \cdot 3x^2 - \tfrac34 = \tfrac34 x^2 - \tfrac34 = \tfrac34\,(x^2 - 1), \]
\[ f''(x) = \tfrac34 \cdot 2x = \tfrac32 x. \]

<details><summary>Haltung dahinter: gleich ausklammern lohnt sich</summary>

Ich schreibe \( f'(x) = \tfrac34(x^2-1) \) bewusst in der ausgeklammerten Form. Der Vorfaktor
\( \tfrac34 \) ist nie null, also entscheidet allein \( x^2 - 1 = 0 \) über die Nullstellen von
\( f' \) — das macht die nächste Teilaufgabe rechnerfrei. Wer den Vorfaktor mitschleppt, rechnet
unnötig kompliziert.

</details>
</details>

### Erwartungshorizont c) — Hoch- und Tiefpunkte

<details><summary>Lösungsweg c) aufklappen</summary>

**Schritt 1 — notwendige Bedingung \( f'(x) = 0 \).** Aus \( \tfrac34(x^2-1) = 0 \) folgt
\( x^2 = 1 \), also \( x = -1 \) oder \( x = 1 \). Das sind die **Kandidaten** für Extremstellen.

**Schritt 2 — hinreichende Bedingung über \( f'' \).** Setze die Kandidaten in
\( f''(x) = \tfrac32 x \) ein:

\[ f''(-1) = -\tfrac32 < 0 \;\Rightarrow\; \text{Hochpunkt}, \qquad
   f''(1) = \tfrac32 > 0 \;\Rightarrow\; \text{Tiefpunkt}. \]

**Schritt 3 — \( y \)-Werte über \( f \).**

\[ f(-1) = \tfrac14(-1) - \tfrac34(-1) = -\tfrac14 + \tfrac34 = \tfrac12, \qquad
   f(1) = \tfrac14 - \tfrac34 = -\tfrac12. \]

Ergebnis: **Hochpunkt** \( H\!\left(-1 \,\middle|\, \tfrac12\right) \), **Tiefpunkt**
\( T\!\left(1 \,\middle|\, -\tfrac12\right) \). Das passt zur Punktsymmetrie aus a): \( T \) ist die
Spiegelung von \( H \) am Ursprung.

<details><summary>Haltung dahinter: notwendig vs. hinreichend — warum zwei Schritte?</summary>

\( f'(x) = 0 \) ist nur **notwendig**: An einer Extremstelle ist die Tangente waagerecht, aber eine
waagerechte Tangente allein garantiert kein Extremum (siehe den Sattelpunkt-Einwand im
Prüfungsgespräch). Erst die **hinreichende** Bedingung sichert die Art ab. Ich nehme hier das
\( f'' \)-Kriterium, weil \( f''(x) = \tfrac32 x \) so einfach ist, dass das Einsetzen rechnerfrei
gelingt: Vorzeichen von \( f'' \) negativ \( \Rightarrow \) Linkskrümmung von oben, also Maximum;
positiv \( \Rightarrow \) Minimum.

<details><summary>Alternative: Vorzeichenwechsel von \( f' \) (falls \( f''=0 \) wäre)</summary>

Wäre an einem Kandidaten \( f'' = 0 \), liefert das \( f'' \)-Kriterium keine Aussage. Dann prüfe ich
den **Vorzeichenwechsel** von \( f' \): \( + \to - \) bedeutet Hochpunkt, \( - \to + \) Tiefpunkt, **kein**
Wechsel bedeutet Sattelpunkt. Dieses Kriterium funktioniert immer und ist die sichere Rückfallebene.

</details>
</details>
</details>

### Erwartungshorizont d) — Wendepunkt

<details><summary>Lösungsweg d) aufklappen</summary>

**Notwendige Bedingung \( f''(x) = 0 \):** \( \tfrac32 x = 0 \Rightarrow x = 0 \).

**Hinreichende Bedingung — Krümmungswechsel.** Ich prüfe \( f''' \): aus \( f''(x) = \tfrac32 x \) folgt
\( f'''(x) = \tfrac32 \neq 0 \). Da die dritte Ableitung an der Stelle \( x=0 \) ungleich null ist,
**wechselt** die Krümmung dort tatsächlich — es liegt eine Wendestelle vor.

**\( y \)-Wert:** \( f(0) = 0 \). Also **Wendepunkt** \( W(0 \mid 0) \) — wegen der Punktsymmetrie genau
das Symmetriezentrum.

<details><summary>Haltung dahinter: was ist ein Wendepunkt anschaulich?</summary>

Ein Wendepunkt ist die Stelle, an der der Graph von einer **Rechts-** in eine **Linkskrümmung**
(oder umgekehrt) wechselt — anschaulich der Punkt, an dem du beim Autofahren das Lenkrad von „nach rechts
eingeschlagen" auf „nach links eingeschlagen" drehst. Mathematisch ist das ein Vorzeichenwechsel von
\( f'' \). Die **typische Falle** ist, bei \( f''(x_0) = 0 \) sofort „Wendepunkt" zu sagen — das ist nur
notwendig. Den Wechsel muss man nachweisen, hier über \( f'''(0) \neq 0 \).

</details>
</details>

### Erwartungshorizont e) — Integral und geometrische Deutung

<details><summary>Lösungsweg e) aufklappen</summary>

**Stammfunktion** über die Potenzregel \( \int x^n\,dx = \tfrac{1}{n+1}x^{n+1} \):

\[ F(x) = \tfrac14 \cdot \tfrac14 x^4 - \tfrac34 \cdot \tfrac12 x^2 = \tfrac{1}{16}x^4 - \tfrac38 x^2. \]

**Hauptsatz** \( \int_a^b f = F(b) - F(a) \):

\[ \int_0^2 f(x)\,dx = F(2) - F(0) = \left(\tfrac{1}{16}\cdot 16 - \tfrac38 \cdot 4\right) - 0
   = 1 - \tfrac{3}{2} = -\tfrac12. \]

**Geometrische Deutung.** Das Ergebnis \( -\tfrac12 \) ist negativ, weil der Graph auf dem größten Teil
des Intervalls \( [0,\,2] \) **unterhalb** der \( x \)-Achse liegt (zwischen \( x=0 \) und \( x=\sqrt3
\approx 1{,}73 \)). Das Integral misst den **orientierten** Flächeninhalt: Flächen unter der Achse zählen
negativ. Über \( [\sqrt3,\,2] \) liegt der Graph wieder oberhalb und liefert einen kleinen positiven
Beitrag, der den negativen aber nicht ausgleicht — in der Summe bleibt es negativ.

<details><summary>Haltung dahinter: orientierter Flächeninhalt vs. „echte" Fläche</summary>

Die **typische Falle** ist, das Integral mit dem Flächeninhalt gleichzusetzen. Das Integral ist der
**orientierte** Flächeninhalt: Was unter der \( x \)-Achse liegt, geht negativ ein. Wäre nach dem
*tatsächlichen* Flächeninhalt zwischen Graph und Achse gefragt, müsste ich an den Nullstellen
**aufteilen** und die Beträge addieren: \( A = \left|\int_0^{\sqrt3} f\right| + \int_{\sqrt3}^{2} f \).
Genau diesen Unterschied fragen Prüfende gern als Rückfrage ab.

<details><summary>Annahme/Voraussetzung: warum darf ich den Hauptsatz anwenden?</summary>

Der Hauptsatz der Differential- und Integralrechnung setzt voraus, dass \( f \) auf \( [0,2] \)
**stetig** ist. Ganzrationale Funktionen (Polynome) sind auf ganz \( \mathbb{R} \) stetig und sogar
beliebig oft differenzierbar — die Voraussetzung ist also automatisch erfüllt, und ich darf das Integral
über die Differenz der Stammfunktion an den Rändern berechnen.

</details>
</details>
</details>

### Der Graph zu \( f \)

So sieht der Graph aus — mit Hochpunkt, Tiefpunkt, Wendepunkt und den drei Nullstellen. Vergleiche ihn
mit deinen Ergebnissen.

<div class="jxgbox" id="jxg-sim1-f" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-sim1-f',{boundingbox:[-2.6,1.4,2.6,-1.4],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 0.25*x*x*x-0.75*x;},-2.4,2.4],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[-1,0.5],{name:'H',size:2,fixed:true,color:'#d98324'});b.create('point',[1,-0.5],{name:'T',size:2,fixed:true,color:'#d98324'});b.create('point',[0,0],{name:'W',size:2,fixed:true,color:'#3a8a5a'});})();</script>

## Prüfungsgespräch (Impulsfragen, Musterantworten, Rückfragen)

Im zweiten Teil stellt die Lehrkraft kurze Impulse. Erwartet wird **freies, begründetes Sprechen** —
keine langen Rechnungen. Übe, jede Antwort in zwei, drei Sätzen klar auf den Punkt zu bringen.

### Impuls 1 <span class="tag tag-ok">AB I</span>

> „Sie haben \( f'(x) = 0 \) gesetzt, um die Extremstellen zu finden. Warum reicht das allein nicht?"

<details><summary>Musterantwort</summary>

„\( f'(x) = 0 \) ist nur die **notwendige** Bedingung — sie sagt, dass die Tangente waagerecht ist. Das
gilt aber auch an einem **Sattelpunkt**, an dem gar kein Extremum vorliegt. Deshalb brauche ich zusätzlich
eine **hinreichende** Bedingung, etwa das Vorzeichen von \( f'' \) oder den Vorzeichenwechsel von
\( f' \), um die Art des Punktes wirklich abzusichern."

<details><summary>Mögliche Rückfrage der Prüfenden</summary>

> „Nennen Sie ein konkretes Beispiel für eine waagerechte Tangente ohne Extremum."

Antwort: \( g(x) = x^3 \) bei \( x = 0 \). Dort ist \( g'(0) = 0 \), aber die Funktion ist streng
steigend — es liegt ein **Sattelpunkt** vor, kein Hoch- oder Tiefpunkt.

</details>
</details>

### Impuls 2 <span class="tag tag-ok">AB I</span>

> „Was sagt Ihnen die Punktsymmetrie über Hoch- und Tiefpunkt, ohne dass Sie beide einzeln ausrechnen?"

<details><summary>Musterantwort</summary>

„Bei Punktsymmetrie zum Ursprung wird jeder Punkt \( (x \mid y) \) auf \( (-x \mid -y) \) gespiegelt. Ein
Hochpunkt links der \( y \)-Achse hat also zwingend einen gespiegelten **Tiefpunkt** rechts davon — mit
entgegengesetzten Koordinaten. Hätte ich nur \( T(1 \mid -\tfrac12) \) berechnet, wüsste ich sofort, dass
der Hochpunkt bei \( (-1 \mid \tfrac12) \) liegt."

</details>

### Impuls 3 <span class="tag tag-warn">AB II</span>

> „Sie haben \( \int_0^2 f\,dx = -\tfrac12 \) erhalten. Ein Flächeninhalt kann doch nicht negativ sein —
> wie passt das zusammen?"

<details><summary>Musterantwort</summary>

„Das Integral ist nicht der Flächeninhalt, sondern der **orientierte** Flächeninhalt. Flächenstücke
**unterhalb** der \( x \)-Achse gehen negativ ein. Zwischen \( 0 \) und \( \sqrt{3} \) verläuft der Graph
unter der Achse, deshalb überwiegt der negative Anteil, und das Integral wird negativ. Den *tatsächlichen*
Flächeninhalt bekäme ich, indem ich an der Nullstelle \( \sqrt{3} \) aufteile und die **Beträge** der
Teilintegrale addiere."

<details><summary>Mögliche Rückfrage der Prüfenden</summary>

> „Wie würden Sie diesen tatsächlichen Flächeninhalt ansetzen — nur den Ansatz, nicht ausrechnen?"

Antwort: \( \displaystyle A = \left| \int_0^{\sqrt3} f(x)\,dx \right| + \int_{\sqrt3}^{2} f(x)\,dx \) —
also die Beträge der Teilstücke addieren, mit der Nullstelle \( \sqrt{3} \) als Trennstelle.

</details>
</details>

### Impuls 4 <span class="tag tag-warn">AB III</span>

> „Begründen Sie ohne Rechnung, warum \( f \) genau **drei** Nullstellen hat und nicht mehr."

<details><summary>Musterantwort</summary>

„\( f \) ist ein Polynom **dritten Grades**, hat also **höchstens drei** Nullstellen. Aus der
Faktorisierung \( \tfrac14 x(x^2-3) \) lese ich drei verschiedene reelle Nullstellen ab:
\( 0,\ \sqrt3,\ -\sqrt3 \). Anschaulich passt das zur Form: Der Graph kommt von unten links, steigt zum
Hochpunkt, fällt durch den Wendepunkt zum Tiefpunkt und steigt wieder — er kreuzt die \( x \)-Achse genau
dreimal."

<details><summary>Haltung dahinter: Grad begrenzt die Nullstellenzahl</summary>

Der **Fundamentalsatz der Algebra** liefert die obere Schranke: Ein Polynom vom Grad \( n \) hat höchstens
\( n \) reelle Nullstellen. Diese Schranke mit der konkreten Faktorisierung und der Kurvenform zu
verbinden, ist typisch AB III — es verlangt das **Vernetzen** mehrerer Konzepte statt eines Rechenschritts.

</details>
</details>

### Impuls 5 <span class="tag tag-warn">AB II</span>

> „Bestimmen Sie die Steigung des Graphen im Wendepunkt und sagen Sie, was sie bedeutet."

<details><summary>Musterantwort</summary>

„Die Steigung im Wendepunkt ist \( f'(0) = \tfrac34(0^2 - 1) = -\tfrac34 \). Sie ist negativ, der Graph
**fällt** dort. Der Wendepunkt ist außerdem die Stelle mit der **stärksten Steigungsänderung** in diesem
Bereich — die Tangente dort heißt **Wendetangente** und ist die am steilsten fallende Tangente zwischen
Hoch- und Tiefpunkt."

</details>

## Relevanz dieser Simulation

<span class="tag tag-ok">AB I/II klar im Kanon</span> Die Vortragsaufgabe deckt den Kern des Basisfachs
ab: Symmetrie, Nullstellen, Ableitungen, Extrem- und Wendepunkte, bestimmtes Integral mit geometrischer
Deutung. Das ist Standardstoff der Analysis und prüfungsrelevant.

<span class="tag tag-warn">AB III nur als Bonus</span> Impuls 4 (Anzahl der Nullstellen über den Grad)
ist bewusst AB III. Im **Basisfach** liegt der Schwerpunkt auf AB I/II; AB-III-Fragen kommen seltener und
eher als vertiefende Rückfrage. Nimm sie als Übung mit, aber lass dich davon nicht verunsichern — der
sichere Umgang mit AB I/II trägt die Prüfung.
