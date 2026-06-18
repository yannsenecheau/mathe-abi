# Prüfungssimulation 2 (Analysis) — Integral & Bestand

So läuft deine mündliche Prüfung ab: Du bekommst eine Aufgabe, hast eine kurze
Vorbereitungszeit, und hältst dann einen kleinen <b>Vortrag</b> (Prüfungsteil 1). Danach stellt die
Lehrkraft dir <b>Rückfragen</b> und schaut, ob du auch über den Tellerrand denkst (Prüfungsteil 2,
das <b>Gespräch</b>). Diese zweite Simulation hat denselben Aufbau wie die erste, aber den
Schwerpunkt <b>Integralrechnung und Bestand</b> — also: von einer <em>Änderungsrate</em> auf den
<em>Bestand</em> schließen.

Arbeite sie ehrgeizig durch: erst selbst rechnen (von Hand, kein Taschenrechner — das ist auch in der
echten Prüfung so), dann die aufklappbaren Lösungen vergleichen. Die <b>Haltung</b> hinter jedem
Schritt steht jeweils im Detailkasten — die ist in der mündlichen Prüfung mindestens so wichtig wie
das Ergebnis.

<div class="meta-row">
  <span>Schwerpunkt: Integral &amp; Bestand</span>
  <span>rechnerfrei</span>
  <span>Vortrag + Gespräch + Erwartungshorizont</span>
  <span>ca. 10 Min Vorbereitung</span>
</div>

## Die Ausgangssituation (lies das zuerst)

In einen Wassertank fließt Wasser zu. Die <b>Zuflussrate</b> wird durch die Funktion

\[ f(t) = -\tfrac14 t^2 + t \]

beschrieben, wobei \( t \) die Zeit in Stunden ist (\( 0 \le t \le 4 \)) und \( f(t) \) die Rate in
<b>Kubikmetern pro Stunde</b> (\( \mathrm{m}^3/\mathrm{h} \)). Zu Beginn (\( t = 0 \)) sind bereits
\( 5\ \mathrm{m}^3 \) Wasser im Tank.

<blockquote>
<b>Wichtig — der gedankliche Kern dieser Aufgabe:</b> \( f(t) \) ist <b>nicht</b> die Wassermenge,
sondern die <b>Geschwindigkeit</b>, mit der die Wassermenge wächst. Den <b>Bestand</b> (also wie viel
Wasser drin ist) bekommst du, indem du die Rate <b>aufsummierst</b> — und das Aufsummieren einer Rate
über die Zeit ist genau das <b>Integral</b>. Dieses eine Bild trägt die ganze Aufgabe.
</blockquote>

<details><summary>Haltung dahinter: Rate ↔ Bestand — woher kommt dieser Zusammenhang?</summary>

Wenn \( B(t) \) der Bestand (die Wassermenge) zur Zeit \( t \) ist, dann ist die Zuflussrate genau die
<b>momentane Änderung</b> des Bestands, also \( B'(t) = f(t) \). Der Bestand \( B \) ist damit eine
<b>Stammfunktion</b> der Rate \( f \). Genau hier verzahnen sich Ableitung und Integral.

<details><summary>… und wie der Hauptsatz daraus die Mengenformel macht</summary>

Aus \( B'(t) = f(t) \) folgt mit dem <b>Hauptsatz der Differential- und Integralrechnung</b>: die in
einem Zeitraum \( [a;b] \) <em>hinzugekommene</em> Menge ist

\[ B(b) - B(a) = \int_a^b f(t)\,dt . \]

Der Bestand am Ende ist dann <b>Anfangsbestand plus Zuflussmenge</b>. Diese Trennung — „Startwert" und
„aufintegrierte Änderung" — solltest du im Vortrag aussprechen, das ist der prüfungsrelevante Kern.

</details>
</details>

## Prüfungsteil 1: Dein Vortrag <span class="tag tag-ok">AB I–II</span>

Bereite die folgenden drei Punkte so vor, dass du sie <b>frei und mit Begründung</b> vortragen kannst.
Sprich beim Üben laut — genau wie in der Prüfung.

<b>(a)</b> Bestimme die <b>Nullstellen</b> der Rate \( f \) und sage, was sie im Sachzusammenhang
bedeuten. <span class="tag tag-ok">AB I</span>

<b>(b)</b> Zu welchem Zeitpunkt ist die Zuflussrate am <b>größten</b>, und wie groß ist sie dann?
<span class="tag tag-ok">AB II</span>

<b>(c)</b> Wie viel Wasser fließt <b>insgesamt</b> in den vier Stunden zu, und wie viel ist am Ende
(\( t = 4 \)) im Tank? <span class="tag tag-ok">AB II</span>

<details><summary>Lösung (a): Nullstellen und ihre Bedeutung</summary>

Setze die Rate gleich null und klammere \( t \) aus — das ist immer der erste Griff bei einem Polynom
ohne konstantes Glied:

\[ -\tfrac14 t^2 + t = 0 \quad\Longleftrightarrow\quad t\left(-\tfrac14 t + 1\right) = 0 . \]

Ein Produkt ist null, wenn ein Faktor null ist (<b>Satz vom Nullprodukt</b>):

\[ t = 0 \qquad\text{oder}\qquad -\tfrac14 t + 1 = 0 \;\Rightarrow\; t = 4 . \]

Also \( t_1 = 0 \) und \( t_2 = 4 \). <b>Bedeutung im Sachzusammenhang:</b> zu Beginn (\( t=0 \)) und
am Ende des betrachteten Zeitraums (\( t=4 \)) ist die Zuflussrate \( 0\ \mathrm{m}^3/\mathrm{h} \) —
in genau diesen Momenten fließt gerade kein Wasser zu.

<details><summary>Haltung dahinter: warum ausklammern statt p-q-Formel?</summary>

Sobald jeder Summand ein \( t \) enthält (kein konstantes Glied), ist <b>Ausklammern</b> der schnellste
und sicherste Weg — gerade rechnerfrei. Die p-q-Formel wäre Overkill und fehleranfällig. Faustregel:
<em>erst auf einen einfachen Faktor schauen, dann zur Formel greifen.</em> Eine der Nullstellen ist
hier sofort \( t=0 \), weil \( f \) keinen konstanten Anteil hat.

</details>
</details>

<details><summary>Lösung (b): Zeitpunkt und Wert der größten Rate</summary>

Gesucht ist das Maximum von \( f \). Notwendige Bedingung für eine Extremstelle: die Ableitung ist
null.

\[ f'(t) = -\tfrac12 t + 1 \stackrel{!}{=} 0 \quad\Longrightarrow\quad t = 2 . \]

Hinreichend prüfen über die zweite Ableitung: \( f''(t) = -\tfrac12 < 0 \) für alle \( t \), also ist
\( t=2 \) eine <b>Maximumstelle</b> (Rechtskrümmung). Der größte Wert ist

\[ f(2) = -\tfrac14\cdot 4 + 2 = -1 + 2 = 1 . \]

<b>Antwort:</b> Nach \( 2 \) Stunden ist die Zuflussrate am größten, nämlich \( 1\ \mathrm{m}^3/\mathrm{h} \).

<details><summary>Haltung dahinter: notwendig vs. hinreichend — nie verwechseln</summary>

\( f'(t)=0 \) ist nur ein <b>Verdacht</b> (notwendige Bedingung) — dort <em>könnte</em> ein Extremum
liegen. Die Entscheidung, ob Hoch- oder Tiefpunkt, liefert ein <b>hinreichendes</b> Kriterium: hier
\( f''(2) < 0 \) ⇒ Hochpunkt. <b>Typische Falle:</b> nur \( f'=0 \) lösen und das Vorzeichen von
\( f'' \) vergessen. In der Prüfung immer beide Schritte aussprechen.

<details><summary>Alternative ohne f'': das Vorzeichen von f' beobachten</summary>

Statt \( f'' \) kannst du auch das <b>Vorzeichen von \( f' \)</b> um die Stelle prüfen: für \( t<2 \)
ist \( f'(t) = -\tfrac12 t + 1 > 0 \) (Rate steigt), für \( t>2 \) ist \( f'(t) < 0 \) (Rate fällt).
Wechsel von <b>+ nach −</b> ⇒ Hochpunkt. Beide Wege sind gleichwertig; der \( f'' \)-Weg ist meist
schneller.

</details>
</details>
</details>

<details><summary>Lösung (c): Gesamtzuflussmenge und Endbestand</summary>

Die <b>insgesamt zugeflossene Menge</b> ist die Rate über den ganzen Zeitraum aufintegriert. Zuerst
eine Stammfunktion bilden (Potenzregel rückwärts: Exponent um \( 1 \) erhöhen, durch den neuen
Exponenten teilen):

\[ F(t) = -\tfrac14\cdot\tfrac{t^3}{3} + \tfrac{t^2}{2} = -\tfrac{1}{12}t^3 + \tfrac12 t^2 . \]

Jetzt der Hauptsatz — Stammfunktion oben minus Stammfunktion unten:

\[ \int_0^4 f(t)\,dt = \Big[\, -\tfrac{1}{12}t^3 + \tfrac12 t^2 \,\Big]_0^4
   = \left(-\tfrac{1}{12}\cdot 64 + \tfrac12\cdot 16\right) - 0 . \]

Schrittweise rechnen, das ist rechnerfrei gut machbar:

\[ -\tfrac{64}{12} + 8 = -\tfrac{16}{3} + \tfrac{24}{3} = \tfrac{8}{3} . \]

Es fließen also \( \tfrac{8}{3}\ \mathrm{m}^3 \approx 2{,}67\ \mathrm{m}^3 \) zu. Der <b>Endbestand</b>
ist Anfangsbestand plus Zufluss:

\[ B(4) = 5 + \tfrac{8}{3} = \tfrac{15}{3} + \tfrac{8}{3} = \tfrac{23}{3} \approx 7{,}67\ \mathrm{m}^3 . \]

<details><summary>Haltung dahinter: warum F(0)=0 hier mühelos ist und wie man Brüche bändigt</summary>

Weil \( F(t) \) nur Potenzen von \( t \) ohne konstantes Glied enthält, ist \( F(0)=0 \) — die untere
Grenze fällt weg. <b>Bruch-Strategie rechnerfrei:</b> alles auf den gemeinsamen Nenner \( 3 \) bringen
(\( 8 = \tfrac{24}{3} \), \( 5 = \tfrac{15}{3} \)), dann nur noch Zähler addieren. Wer das diszipliniert
macht, vermeidet die häufigsten Flüchtigkeitsfehler.

<details><summary>Annahme dahinter: warum darf hier „Bestand = Start + Integral" gerechnet werden?</summary>

Das gilt, weil die Rate auf \( [0;4] \) <b>nicht negativ</b> ist (\( f(t)\ge 0 \), siehe Graph): es
fließt nur zu, nie ab. Dann ist das Integral gleich der tatsächlich hinzugekommenen Wassermenge. Bei
einer Rate mit <em>negativen</em> Abschnitten (Abfluss) zählt das Integral die Bilanz aus Zu- und
Abfluss — das ist genau das Thema im Gespräch unten.

</details>
</details>
</details>

### Der Graph der Zuflussrate (zur Anschauung)

Die <b>schraffierte Fläche</b> unter der Kurve ist die in den vier Stunden zugeflossene Wassermenge
\( \int_0^4 f\,dt = \tfrac{8}{3} \). Der markierte Punkt ist das Maximum der Rate bei \( (2 \mid 1) \).

<div class="jxgbox" id="jxg-sim2-rate" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-sim2-rate',{boundingbox:[-0.6,1.5,4.7,-0.5],axis:true,showCopyright:false,showNavigation:false});var f=function(x){return -0.25*x*x+x;};var c=b.create('functiongraph',[f,0,4],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('integral',[[0,4],c],{fillColor:'#d98324',fillOpacity:0.25,withLabel:false,curveLeft:{visible:false},curveRight:{visible:false},baseLeft:{visible:false},baseRight:{visible:false},label:{visible:false}});b.create('point',[2,1],{name:'Hochpunkt (2|1)',size:2,fixed:true,color:'#d98324',label:{offset:[6,8]}});})();</script>

<details><summary>Wie du diesen Graphen in der Prüfung in einem Satz beschreibst</summary>

„Die Zuflussrate startet bei \( 0 \), steigt bis zum Maximum \( 1\ \mathrm{m}^3/\mathrm{h} \) nach
\( 2 \) Stunden und fällt dann symmetrisch wieder auf \( 0 \) ab; die Fläche unter der Kurve ist die
gesamte zugeflossene Wassermenge." Solche <b>Verbindung von Graph und Sachzusammenhang</b> bringt im
mündlichen Teil viele Punkte.

</details>

## Prüfungsteil 2: Das Gespräch (Rückfragen) <span class="tag tag-ok">AB II–III</span>

Im Gespräch wird tiefer gebohrt. Versuche bei jeder Frage zuerst eine eigene Antwort, bevor du
aufklappst.

<b>(d)</b> Wie groß war die <b>durchschnittliche</b> Zuflussrate in den vier Stunden?
<span class="tag tag-ok">AB II</span>

<b>(e)</b> Ab Stunde \( 0 \) öffnet sich zusätzlich ein <b>Abfluss</b> mit der Rate
\( g(t) = \tfrac12 t \). In welchem Zeitraum <b>steigt</b> der Wasserstand trotzdem noch, und um wie
viel netto in dieser Phase? <span class="tag tag-warn">AB III</span>

<b>(f)</b> Begriffsfrage: Worin unterscheidet sich das <b>Integral</b> \( \int_0^4 f\,dt \) vom
<b>Wert</b> \( f(4) \)? Erkläre an diesem Beispiel. <span class="tag tag-ok">AB II</span>

<details><summary>Lösung (d): Durchschnittliche Rate (Mittelwert eines Integrals)</summary>

Der <b>Mittelwert</b> einer Funktion über \( [a;b] \) ist das Integral geteilt durch die Länge des
Intervalls:

\[ \bar f = \frac{1}{b-a}\int_a^b f(t)\,dt = \frac{1}{4-0}\cdot\tfrac{8}{3} = \tfrac{8}{12} = \tfrac{2}{3} . \]

Die durchschnittliche Zuflussrate war also \( \tfrac{2}{3}\ \mathrm{m}^3/\mathrm{h} \approx
0{,}67\ \mathrm{m}^3/\mathrm{h} \).

<details><summary>Haltung dahinter: was der Mittelwert anschaulich bedeutet</summary>

Der Mittelwert \( \tfrac23 \) ist die Höhe eines <b>Rechtecks</b> über \( [0;4] \), das dieselbe Fläche
(also dieselbe Wassermenge) hat wie die Kurve: \( \tfrac23 \cdot 4 = \tfrac{8}{3} \). Du „verteilst" den
schwankenden Zufluss gedanklich gleichmäßig über die Zeit. Den Term \( \tfrac{8}{3} \) aus Teil (c)
darfst du hier <b>wiederverwenden</b> — in der Prüfung ruhig sagen: „Ich nutze das Ergebnis von vorhin."

</details>
</details>

<details><summary>Lösung (e): Netto-Zuwachs bei zusätzlichem Abfluss</summary>

Jetzt fließt zu mit \( f(t) \) und ab mit \( g(t) = \tfrac12 t \). Die <b>Netto-Änderungsrate</b> des
Bestands ist die Differenz:

\[ n(t) = f(t) - g(t) = \left(-\tfrac14 t^2 + t\right) - \tfrac12 t = -\tfrac14 t^2 + \tfrac12 t . \]

Der Wasserstand <b>steigt</b>, solange \( n(t) > 0 \). Nullstellen von \( n \) durch Ausklammern:

\[ -\tfrac14 t^2 + \tfrac12 t = t\left(-\tfrac14 t + \tfrac12\right) = 0 \;\Rightarrow\; t = 0
   \ \text{oder}\ t = 2 . \]

Zwischen \( 0 \) und \( 2 \) ist \( n(t) > 0 \) (z. B. \( n(1) = -\tfrac14 + \tfrac12 = \tfrac14 > 0 \)),
danach negativ. <b>Der Wasserstand steigt also im Zeitraum \( 0 \le t \le 2 \).</b> Der Netto-Zuwachs
in dieser Phase ist das Integral von \( n \):

\[ \int_0^2 n(t)\,dt = \Big[\, -\tfrac{1}{12}t^3 + \tfrac14 t^2 \,\Big]_0^2
   = -\tfrac{1}{12}\cdot 8 + \tfrac14\cdot 4 = -\tfrac{2}{3} + 1 = \tfrac{1}{3} . \]

In den ersten zwei Stunden kommt also netto \( \tfrac13\ \mathrm{m}^3 \approx 0{,}33\ \mathrm{m}^3 \)
hinzu.

<details><summary>Haltung dahinter: Differenz der Raten — und warum hier ein Vorzeichenwechsel lauert</summary>

Bei zwei gleichzeitig wirkenden Raten ist die <b>Bilanzrate</b> die Differenz \( n=f-g \). Steigen/Fallen
des Bestands hängt am <b>Vorzeichen von \( n \)</b>, nicht von \( f \) allein. <b>Typische Falle:</b>
einfach \( \int_0^4 n\,dt \) bilden — dann mischen sich Steig- und Fallphase und die Frage „in welchem
Zeitraum steigt es?" bleibt unbeantwortet. Erst die Nullstelle \( t=2 \) (der Umschaltpunkt) finden,
dann gezielt über \( [0;2] \) integrieren.

<details><summary>Geometrisch: das ist die Fläche zwischen den beiden Kurven f und g auf [0;2]</summary>

Weil auf \( [0;2] \) gilt \( f(t) \ge g(t) \), ist \( \int_0^2 (f-g)\,dt \) genau der <b>Flächeninhalt
zwischen den beiden Kurven</b> in diesem Bereich — die Standardformel „obere minus untere Funktion,
dann integrieren". Das verbindet das Sachthema „Bestand" mit dem rein geometrischen „Fläche zwischen
Graphen". Der AB-III-Charakter steckt im Erkennen dieser Verbindung.

</details>
</details>
</details>

<details><summary>Lösung (f): Integral vs. Funktionswert — der entscheidende Begriffsunterschied</summary>

Beides sind völlig verschiedene Dinge, auch in der Einheit:

- \( f(4) = -\tfrac14\cdot 16 + 4 = -4 + 4 = 0 \) ist die <b>Rate</b> zum Zeitpunkt \( t=4 \), also wie
  schnell gerade Wasser zufließt: hier \( 0\ \mathrm{m}^3/\mathrm{h} \). Das ist ein <b>Momentanwert</b>.
- \( \int_0^4 f\,dt = \tfrac{8}{3} \) ist die über vier Stunden <b>aufsummierte Menge</b>, also wie viel
  Wasser insgesamt dazugekommen ist: \( \tfrac{8}{3}\ \mathrm{m}^3 \). Das ist eine <b>Menge</b>.

Kurz: \( f(4) \) ist eine <b>Geschwindigkeit</b> (m³ pro Stunde), das Integral eine <b>Menge</b> (m³).
Dass \( f(4)=0 \) ist und der Tank trotzdem voller ist als am Anfang, zeigt es deutlich: gerade kein
Zufluss mehr, aber vorher ist viel zusammengekommen.

<details><summary>Haltung dahinter: warum diese Frage so gern gestellt wird</summary>

Das Verwechseln von <b>Bestand, Änderungsrate und aufintegrierter Änderung</b> ist der häufigste
konzeptionelle Fehler im Abitur. Wer den Unterschied an einem Sachbeispiel mit Einheiten erklären kann
(m³ vs. m³/h), zeigt echtes Verständnis — das ist genau die Sorte AB-II-Begründung, die im mündlichen
Teil zählt.

</details>
</details>

## Erwartungshorizont (so bewertet die Lehrkraft)

Diese Übersicht zeigt dir, <b>worauf es ankommt</b> — nicht nur das Ergebnis, sondern die Begründung.
Hak nach dem Üben ungeschönt ab, was du frei sprechen konntest.

<div class="table-wrap">

| Teil | Erwartete Leistung | Ergebnis | AB |
|---|---|---|---|
| (a) | Ausklammern, Satz vom Nullprodukt, <b>Deutung</b> der Nullstellen im Sachkontext | \( t=0,\ t=4 \) | I |
| (b) | \( f'=0 \), hinreichende Prüfung (\( f''<0 \)), Wert angeben | \( t=2,\ f(2)=1 \) | II |
| (c) | Stammfunktion, Hauptsatz, Trennung Startwert + Zuflussmenge | \( \tfrac{8}{3} \); \( B(4)=\tfrac{23}{3} \) | II |
| (d) | Mittelwertformel \( \tfrac{1}{b-a}\int \), Ergebnis aus (c) wiederverwenden | \( \tfrac{2}{3} \) | II |
| (e) | Netto-Rate \( f-g \), Umschalt-Nullstelle, gezielt integrieren | steigt auf \( [0;2] \); \( +\tfrac{1}{3} \) | III |
| (f) | Rate (Momentanwert) vs. Integral (Menge), mit Einheiten erklären | \( f(4)=0 \) vs. \( \tfrac{8}{3}\,\mathrm{m}^3 \) | II |

</div>

<blockquote>
<b>Dein Selbstcheck:</b> Konntest du bei <b>(c)</b> klar sagen, <em>warum</em> du integrierst (Rate →
Menge) und bei <b>(f)</b> den Unterschied in <em>Einheiten</em> benennen? Wenn ja, sitzt der Kern der
Integralrechnung fürs mündliche Basisfach. Wo es noch hakt: nimm es laut auf einer Sprachnachricht auf
— daraus baut das Lernbuch dir die passende Übung.
</blockquote>

<details><summary>Hinweis zum Prüfungsstatus dieser Aufgabe</summary>

Der Schwerpunkt <b>Integral- und Bestandsrechnung</b> ist Kernstoff der Analysis und für das Basisfach
gesichert relevant <span class="tag tag-ok">gesichert</span>. Teil <b>(e)</b> (Differenz zweier Raten,
Fläche zwischen Kurven mit Sachdeutung) liegt vom Anspruch im Bereich <b>AB III</b> und ist im Basisfach
eher am oberen Rand <span class="tag tag-warn">Anspruch AB III — im Basisfach selten in dieser Tiefe; mit
Lehrkraft prüfen</span>. Übe es trotzdem: das Denken in <em>Netto-Raten</em> festigt das Verständnis für
(c) und (f).

</details>
