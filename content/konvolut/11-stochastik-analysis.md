# Aufgabe 11 — Stochastik & Analysis

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Stochastik**, **Teil 2 (Gespräch) aus der Analysis**. Alles ist
**rechnerfrei** zu lösen. Arbeitet die Aufgabe wie eine echte Simulation durch — eine Person trägt
vor, die andere prüft mit dem Lösungsweg und dem [Prüfer-Leitfaden](#prüfer-leitfaden-für-die-abfragende-person)
am Ende mit.

> **Lesehilfe für die Detailkästen.** Jeder Lösungsschritt hat darunter einen klappbaren Kasten
> **„Haltung dahinter"**. Der erklärt den Schritt **von Grund auf** — so, als hätte man den Stoff
> lange nicht mehr gesehen. Jeder Fachbegriff wird beim ersten Auftauchen in einfachen Worten erklärt.
> Wer nur das Ergebnis braucht, lässt die Kästen zu; wer *verstehen* will, klappt sie auf.

<details><summary><b>Kurzanleitung für die abfragende Person</b> (zuerst lesen)</summary>

Du musst den Stoff **nicht** selbst beherrschen, um diese Aufgabe abzunehmen. So gehst du vor:

- Lass die andere Person nur die **grauen Aufgabenkästen** sehen und **laut erklären**.
- Du hast den **ausgeklappten Lösungsweg** vor dir. Vergleiche nicht Wort für Wort — achte auf die
  **fett markierten Kernschritte** und die **Ergebnisse**.
- Die **„Haltung dahinter"-Kästen** erklären dir jeden Schritt in Alltagssprache. Lies sie ruhig
  selbst mit — danach kannst du die Erklärung der anderen Person einordnen, auch ohne Vorwissen.
- Am Ende findest du den **Prüfer-Leitfaden**: dort steht je Teilaufgabe in einem Satz, *was eine
  gute Antwort enthält* und *welche Rückfrage* du stellen kannst.
- Grüne Markierung = Grundwissen (sollte sicher sitzen), gelbe = anspruchsvoller (Nachfragen ok).

</details>

> **Werkzeug zum Nachschlagen:** Die wiederkehrenden Stochastik-Werkzeuge (Normalverteilung,
> Vierfeldertafel, bedingte Wahrscheinlichkeit, Unabhängigkeit, Baumdiagramm) stehen kompakt im
> [Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html) (Anker u. a.
> `#normalverteilung`, `#erwartungswert`, `#vierfeldertafel`, `#binomialverteilung`,
> `#bernoulli-kette`). Die Analysis-Werkzeuge findest du in den Kapiteln
> [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Funktionsuntersuchung](kap-funktionsuntersuchung.html),
> [Integral-Grundlagen](kap-integral-grundlagen.html),
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html) und
> [Grundfunktionen](kap-grundfunktionen.html).

---

## Teil 1 — Vortrag (Stochastik): Normalverteilung und Vierfeldertafel

<div class="aufgabenkasten">

**Die Körpergröße der erwachsenen Männer in einer Stadt ist normalverteilt.**

**a)** Beschreibe die Eigenschaften einer normalverteilten Zufallsgröße. Gehe dabei auch auf die
Begriffe **Erwartungswert** und **Standardabweichung** ein.

Ein Mitarbeiter einer Fotoagentur geht durch eine Fußgängerzone und spricht Männer an, ob sie an einem
Fotoshooting interessiert sind. Die ideale Körpergröße hierfür liegt zwischen \( 1{,}80\,\text{m} \)
und \( 1{,}90\,\text{m} \). Die folgende Vierfeldertafel zeigt das Ergebnis seiner Befragung:

<table class="vft">
<thead><tr><th></th><th>Ideale Körpergröße</th><th>Keine ideale Körpergröße</th><th>Summe</th></tr></thead>
<tbody>
<tr><th>Interesse am Fotoshooting</th><td>22&nbsp;%</td><td>19&nbsp;%</td><td></td></tr>
<tr><th>Kein Interesse am Fotoshooting</th><td></td><td></td><td></td></tr>
<tr><th>Summe</th><td>37&nbsp;%</td><td></td><td></td></tr>
</tbody>
</table>

**b)** Erläutere die direkt aus dieser Vierfeldertafel ablesbaren Aussagen. Bestimme die
Wahrscheinlichkeit, dass ein Mann Interesse am Fotoshooting hat. Aus einer Gruppe mit Männern der
idealen Körpergröße wird zufällig ein Mann ausgewählt. Berechne die Wahrscheinlichkeit dafür, dass
dieser Mann kein Interesse am Fotoshooting hat.

**c)** Untersuche, ob die Ereignisse \( A \): „Interesse am Fotoshooting" und \( B \): „Ideale
Körpergröße" stochastisch unabhängig sind.

In einer Gruppe von zehn Männern haben vier Männer ideale Körpergröße. Aus dieser Gruppe werden drei
Männer zufällig ausgewählt.

**d)** Begründe, dass die Binomialverteilung für Überlegungen zur Anzahl der ausgewählten Männer mit
idealer Körpergröße nicht geeignet ist. Bestimme die Wahrscheinlichkeit dafür, dass genau zwei der
drei ausgewählten Männer ideale Körpergröße haben.

</div>

### Teilaufgabe a) — Eigenschaften einer normalverteilten Zufallsgröße

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Eine **normalverteilte Zufallsgröße** hat diese Eigenschaften:

- Sie ist eine **stetige** Zufallsgröße: Sie kann **alle reellen Werte in einem Intervall** annehmen
  (jede Körpergröße, auch \( 1{,}8237\ldots\,\text{m} \)), nicht nur einzelne abgezählte Werte.
- Die zugehörigen Wahrscheinlichkeiten lassen sich über **Flächenbetrachtungen an einer Glockenkurve**
  beschreiben: Die Wahrscheinlichkeit, dass der Wert in einem Bereich liegt, ist die **Fläche unter der
  Glockenkurve** über diesem Bereich.
- Diese **Glockenkurve hat ihren Hochpunkt an der Stelle des Erwartungswerts \( \mu \)** und ist
  **achsensymmetrisch zur senkrechten Geraden \( x = \mu \)**.
- Die **Wendepunkte** liegen genau bei \( x_1 = \mu - \sigma \) und \( x_2 = \mu + \sigma \) (also „eine
  Standardabweichung links und rechts vom Mittelwert").
- **Je größer die Standardabweichung \( \sigma \) ist, umso flacher und breiter wird die Glockenkurve**
  (umso stärker streuen die Werte); je kleiner \( \sigma \), umso schmaler und höher.

<figure>
<div class="jxgbox" id="jxg-k11-glocke" style="width:100%;max-width:520px;aspect-ratio:2/1"></div>
<figcaption>Glockenkurve (Normalverteilung): Hochpunkt und Symmetrieachse bei \( x=\mu \), Wendepunkte (grün) bei \( \mu-\sigma \) und \( \mu+\sigma \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k11-glocke',{boundingbox:[-4.2,1.2,4.2,-0.35],axis:false,showCopyright:false,showNavigation:false});b.create('axis',[[0,0],[1,0]],{ticks:{visible:false},lastArrow:{size:6}});b.create('functiongraph',[function(x){return Math.exp(-x*x/2);},-4,4],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('segment',[[0,0],[0,1]],{dash:2,strokeColor:'#d98324',strokeWidth:1.5});b.create('text',[0.15,1.08,'Symmetrieachse x = μ'],{fontSize:12,color:'#d98324'});b.create('point',[0,0],{name:'μ',size:1,fixed:true,fillColor:'#d98324',strokeColor:'#d98324',label:{offset:[4,-14],fontSize:13}});var hw=Math.exp(-0.5);b.create('point',[-1,hw],{name:'μ−σ',size:2,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',label:{offset:[-48,2],fontSize:12}});b.create('point',[1,hw],{name:'μ+σ',size:2,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a',label:{offset:[8,2],fontSize:12}});})();</script>

<details><summary>Haltung dahinter: Was ist eine „normalverteilte Zufallsgröße"? (ganz von vorn)</summary>

Wir bauen das Wort von hinten auf.

**Zufallsgröße.** Eine **Zufallsgröße** (oder Zufallsvariable) ist eine Zahl, deren Wert vom Zufall
abhängt — hier: „die Körpergröße eines zufällig herausgegriffenen Mannes". Vor dem Messen weiß man
den Wert nicht, aber man kann sagen, wie **wahrscheinlich** welche Werte sind.

**Stetig gegenüber diskret.** Manche Größen springen in festen Stufen — ein Würfel zeigt nur
\( 1,2,3,4,5,6 \), nie \( 3{,}7 \). So etwas heißt **diskret** (abzählbar). Eine Körpergröße dagegen
kann **jeden** Zwischenwert annehmen: \( 1{,}80\,\text{m} \), \( 1{,}803\,\text{m} \),
\( 1{,}8031\,\text{m} \) … Eine Größe, die so ein ganzes Intervall lückenlos füllt, heißt **stetig**.
Genau das ist die Körpergröße.

**Glockenkurve.** Trägt man auf, wie häufig welche Werte vorkommen, ergibt sich bei sehr vielen
natürlichen Größen (Körpergröße, Schuhgröße, Messfehler) eine **symmetrische Glockenform**: In der
Mitte (beim Durchschnitt) ist der Berg am höchsten, nach beiden Seiten fällt er gleichmäßig ab. Diese
Kurve heißt **Glockenkurve** oder **Gauß-Kurve**. Anschaulich: Die allermeisten Männer sind ungefähr
durchschnittlich groß, sehr kleine und sehr große sind selten — deshalb der Berg in der Mitte und die
dünnen „Schwänze" außen.

**Fläche = Wahrscheinlichkeit.** Bei einer stetigen Größe liest man Wahrscheinlichkeiten als **Fläche
unter der Kurve** ab. „Wie wahrscheinlich ist eine Größe zwischen \( 1{,}80 \) und \( 1{,}90\,\text{m} \)?"
= „Wie groß ist die Fläche unter der Glocke über diesem Streifen?" Die **gesamte** Fläche unter der
Glocke ist immer \( 1 \) (\( =100\,\% \)), denn irgendeinen Wert hat jeder Mann.

<details><summary>Erwartungswert \( \mu \) und Standardabweichung \( \sigma \) — die zwei Stellschrauben</summary>

Eine Normalverteilung wird durch genau **zwei** Zahlen vollständig festgelegt:

- **Erwartungswert \( \mu \)** (sprich „mü"): der **Mittelwert/Durchschnitt** — der Wert, um den herum
  alles zentriert ist. Er sagt, **wo** der Berg steht. Anschaulich der „Schwerpunkt" der Verteilung:
  Würde man die Glockenfläche aus Pappe ausschneiden, balancierte sie genau bei \( x=\mu \). Deshalb
  liegt dort der **Hochpunkt**, und deshalb ist die Kurve **spiegelsymmetrisch** zur senkrechten
  Geraden \( x=\mu \) (links wie rechts gleich viel).

- **Standardabweichung \( \sigma \)** (sprich „sigma"): die **typische Streuung** — wie weit die Werte
  im Schnitt vom Mittelwert abweichen. Sie sagt, **wie breit** der Berg ist. Kleines \( \sigma \) =
  alle dicht beieinander = **schmale, hohe** Glocke; großes \( \sigma \) = stark streuend = **breite,
  flache** Glocke. (Die Höhe muss mitsinken, weil die Gesamtfläche immer \( 1 \) bleibt — wird die
  Glocke breiter, muss sie flacher werden.)

**Die Wendepunkte verraten \( \sigma \).** Ein **Wendepunkt** ist die Stelle, an der die Kurve von einer
Rechtskurve in eine Linkskurve übergeht — wo das Gefälle aufhört, steiler zu werden, und anfängt,
flacher zu werden. Bei der Glocke liegen diese beiden Stellen exakt eine Standardabweichung neben dem
Gipfel: bei \( \mu-\sigma \) und \( \mu+\sigma \). Man kann \( \sigma \) also direkt an der Kurve
ablesen: Abstand vom Gipfel bis zum Wendepunkt.

</details>

<details><summary>Typische Falle: bei stetigen Größen ist „genau ein Wert" unmöglich</summary>

Bei einer stetigen Zufallsgröße ist die Wahrscheinlichkeit für **einen einzelnen, exakten** Wert immer
\( 0 \): \( P(X = 1{,}80\,\text{m}) = 0 \). Grund: Ein einzelner Punkt hat keine Fläche, und
Wahrscheinlichkeit ist hier Fläche. Sinnvoll fragt man immer nach einem **Bereich** („zwischen
\( 1{,}80 \) und \( 1{,}90\,\text{m} \)"). Deshalb ist es auch egal, ob man „kleiner" oder „kleiner
gleich" schreibt — die Grenze selbst trägt nichts bei.

</details>
</details>
</details>

### Teilaufgabe b) — Ablesbare Aussagen, \( P(A) \) und bedingte Wahrscheinlichkeit

<span class="tag tag-ok">AB I / AB II</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Direkt aus der Tafel ablesbare Aussagen** (jede Zelle ist eine Prozentangabe der **gesamten**
Befragten):

- **\( 37\,\% \)** der angesprochenen Männer haben die **ideale Körpergröße** (untere Spaltensumme).
- **\( 22\,\% \)** haben die ideale Körpergröße **und** sind am Fotoshooting interessiert.
- **\( 19\,\% \)** haben **keine** ideale Körpergröße **und** sind am Fotoshooting interessiert.

**Wahrscheinlichkeit für Interesse, \( P(A) \).** Man addiert die ganze Zeile „Interesse":

\[ P(A) = 22\,\% + 19\,\% = 41\,\%. \]

**Aus den idealgroßen Männern einen ziehen — Wahrscheinlichkeit „kein Interesse".** Gesucht ist die
**bedingte** Wahrscheinlichkeit \( P_B(\overline A) \): „kein Interesse \( (\overline A) \), **unter der
Bedingung** ideale Größe \( (B) \)". Man bleibt in der Spalte \( B \) und teilt den passenden Anteil
durch die Spaltensumme:

\[ P_B(\overline A) = \frac{P(\overline A \cap B)}{P(B)} = \frac{37\,\% - 22\,\%}{37\,\%}
   = \frac{15}{37} \approx 40{,}5\,\%. \]

Dabei ist \( P(\overline A \cap B) = 37\,\% - 22\,\% = 15\,\% \) (Spalte \( B \) ergibt \( 37\,\% \),
davon entfallen \( 22\,\% \) auf „Interesse", der Rest auf „kein Interesse"). Die vollständig
ausgefüllte Tafel:

<table class="vft">
<thead><tr><th></th><th>Ideale Größe \( B \)</th><th>Keine ideale Größe \( \overline B \)</th><th>Summe</th></tr></thead>
<tbody>
<tr><th>Interesse \( A \)</th><td>22&nbsp;%</td><td>19&nbsp;%</td><td><b>41&nbsp;%</b></td></tr>
<tr><th>Kein Interesse \( \overline A \)</th><td><b>15&nbsp;%</b></td><td><b>44&nbsp;%</b></td><td><b>59&nbsp;%</b></td></tr>
<tr><th>Summe</th><td>37&nbsp;%</td><td><b>63&nbsp;%</b></td><td><b>100&nbsp;%</b></td></tr>
</tbody>
</table>

<details><summary>Haltung dahinter: Wie liest man eine Vierfeldertafel? (ganz von vorn)</summary>

Eine **Vierfeldertafel** sortiert eine Gruppe nach **zwei** Ja/Nein-Merkmalen gleichzeitig — hier
„Interesse: ja/nein" und „ideale Größe: ja/nein". Daraus entstehen vier Kästchen (Felder), eines für
jede Kombination:

- oben links: **beides ja** — ideal **und** interessiert,
- oben rechts: nicht ideal, aber interessiert,
- unten links: ideal, aber nicht interessiert,
- unten rechts: weder noch.

**Die Zahlen sind Anteile an allen Befragten.** „\( 22\,\% \)" heißt: \( 22 \) von je \( 100 \)
Angesprochenen sind ideal **und** interessiert. Dieses „und" ist mathematisch der **Schnitt**
\( A \cap B \) — beide Bedingungen treffen zusammen zu.

**Ränder = Summen.** Addiert man eine ganze **Zeile**, bekommt man die Wahrscheinlichkeit nur für das
Zeilenmerkmal (z. B. „Interesse insgesamt" \( =41\,\% \), egal welche Größe). Addiert man eine
**Spalte**, bekommt man das Spaltenmerkmal („ideale Größe insgesamt" \( =37\,\% \)). Diese Randwerte
heißen **Randwahrscheinlichkeiten**. Und alle vier Felder zusammen ergeben \( 100\,\% \) — jeder
Befragte sitzt in genau einem Feld. Daraus füllt man fehlende Felder per Subtraktion auf (Zeile/Spalte
muss aufgehen).

<details><summary>Bedingte Wahrscheinlichkeit ganz langsam: „nur unter den Idealen schauen"</summary>

„**Aus einer Gruppe mit Männern der idealen Körpergröße** wird zufällig einer ausgewählt" — dieser
Halbsatz schaltet den Blick um: Es zählen **nicht mehr alle** Befragten, sondern **nur noch die
idealgroßen**. Diese Teilgruppe ist der neue \( 100\,\% \)-Bezug. Das ist eine **bedingte
Wahrscheinlichkeit**, geschrieben \( P_B(\overline A) \): „Wahrscheinlichkeit für \( \overline A \),
**gegeben** \( B \)".

Bild: Du legst auf die Tafel eine Schablone, die alles außer der Spalte \( B \) (ideale Größe)
abdeckt. Übrig bleiben \( 37\,\% \) — und **das** sind jetzt deine \( 100\,\% \). Davon haben
\( 15\,\% \) kein Interesse. Der Anteil ist also

\[ \frac{15\,\%}{37\,\%} = \frac{15}{37} = 0{,}4054\ldots \approx 40{,}5\,\%. \]

Ziffernweise: \( 15 \) geteilt durch \( 37 \). \( 37 \) passt nicht in \( 15 \) → \( 0,\ldots \).
\( 150 : 37 = 4 \) Rest \( 2 \) (denn \( 4\cdot 37 = 148 \)). \( 20 \to 200 : 37 = 5 \) Rest \( 15 \)
(\( 5\cdot 37 = 185 \)). Also \( 0{,}405\ldots \approx 40{,}5\,\% \).

</details>

<details><summary>Typische Falle: durch die Teilgesamtheit teilen, nicht durch 100&nbsp;%</summary>

Der häufigste Fehler: \( P_B(\overline A) \) mit \( P(\overline A \cap B) = 15\,\% \) zu verwechseln.
Die \( 15\,\% \) sind der Anteil an **allen** Befragten — die Frage will aber den Anteil **innerhalb
der Idealgroßen**. Deshalb muss man durch \( 37\,\% \) (die Teilgesamtheit) teilen, nicht durch
\( 100\,\% \). Faustregel: „Aus der Gruppe X wird gezogen" → durch \( P(X) \) teilen.

</details>
</details>
</details>

### Teilaufgabe c) — Stochastische Unabhängigkeit

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Zwei Ereignisse \( A \) und \( B \) heißen **stochastisch unabhängig**, wenn

\[ P(A \cap B) = P(A) \cdot P(B). \]

Man prüft, ob die Gleichung mit den Zahlen der Tafel **aufgeht**:

\[ P(A) = 41\,\%, \qquad P(B) = 37\,\%, \qquad P(A \cap B) = 22\,\%. \]
\[ P(A)\cdot P(B) = 41\,\% \cdot 37\,\% = 15{,}17\,\% \;\neq\; 22\,\% = P(A\cap B). \]

Die beiden Seiten sind **verschieden**, also sind die Ereignisse **nicht** stochastisch unabhängig.

<details><summary>Haltung dahinter: Was heißt „unabhängig", und warum dieser Test?</summary>

**Unabhängig** bedeutet anschaulich: Das eine Merkmal verrät **nichts** über das andere. Wüsste man,
dass ein Mann ideal groß ist, und änderte das **nichts** an der Wahrscheinlichkeit, dass er
interessiert ist, wären die Merkmale unabhängig. Sobald das Wissen über das eine die Chance fürs
andere verschiebt, sind sie **abhängig**.

**Warum gerade \( P(A)\cdot P(B) \)?** Wenn zwei Dinge völlig nichts miteinander zu tun haben,
multiplizieren sich ihre Anteile. Stell dir \( 41\,\% \) Interessierte und \( 37\,\% \) Idealgroße vor,
**zufällig gemischt** ohne Zusammenhang: Dann wären unter den Interessierten genauso oft Idealgroße wie
in der Gesamtheit, nämlich \( 37\,\% \) — und der gemeinsame Anteil wäre
\( 41\,\% \cdot 37\,\% = 15{,}17\,\% \). Die Tafel zeigt aber **\( 22\,\% \)** ideal-und-interessiert,
deutlich mehr als die \( 15{,}17\,\% \) eines reinen Zufallsmischens. Idealgröße und Interesse treten
also **häufiger zusammen** auf, als der Zufall allein erklären würde → es gibt einen Zusammenhang →
abhängig.

<details><summary>… ganz langsam (mit Zahlen): \( 41\,\% \cdot 37\,\% \)</summary>

Prozent in Dezimalzahlen: \( 41\,\% = 0{,}41 \), \( 37\,\% = 0{,}37 \). Multiplizieren wie ohne Komma:
\( 41 \cdot 37 \). Rechne \( 41 \cdot 37 = 41\cdot 30 + 41\cdot 7 = 1230 + 287 = 1517 \). Jetzt die
Kommas: zwei Nachkommastellen plus zwei Nachkommastellen = **vier** Nachkommastellen, also
\( 0{,}41 \cdot 0{,}37 = 0{,}1517 = 15{,}17\,\% \). Und \( 15{,}17\,\% \neq 22\,\% \).

</details>

<details><summary>Typische Falle: „unabhängig" mit „schließt sich aus" verwechseln</summary>

**Unabhängig** (das eine sagt nichts über das andere) ist etwas völlig anderes als **unvereinbar /
disjunkt** (beides kann nicht zugleich eintreten, \( P(A\cap B)=0 \)). Hier gilt \( P(A\cap B)=22\,\% \neq 0 \)
— die Ereignisse treten sehr wohl zusammen auf, sind also nicht disjunkt; getestet wird trotzdem die
**Produktgleichung**, nicht „ist der Schnitt null".

</details>
</details>
</details>

### Teilaufgabe d) — Warum keine Binomialverteilung, und \( P(\text{genau }2) \)

<span class="tag tag-warn">AB II / AB III</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Warum die Binomialverteilung hier nicht passt.** Eine Binomialverteilung verlangt eine
**Bernoulli-Kette**: gleich viele unabhängige Versuche mit **konstanter** Trefferwahrscheinlichkeit
\( p \) — das ist **Ziehen mit Zurücklegen**. Hier wird aus nur **zehn** Männern (vier davon ideal)
**ohne Zurücklegen** gezogen. Mit jedem gezogenen Mann ändert sich die Zusammensetzung der Restgruppe,
also auch die Wahrscheinlichkeit für „ideal" beim nächsten Zug
(\( \tfrac{4}{10}, \tfrac{3}{9}, \ldots \)). Weil \( p \) **nicht konstant** ist und die Grundmenge
klein ist, ist die Binomialverteilung **nicht geeignet**.

**Wahrscheinlichkeit, dass genau zwei der drei Gezogenen ideal sind.** Man arbeitet mit dem
**Baumdiagramm / der Pfadregel** (Ziehen ohne Zurücklegen). Ein passender Pfad ist z. B. „ideal,
ideal, nicht ideal":

\[ \frac{4}{10}\cdot\frac{3}{9}\cdot\frac{6}{8}. \]

Die zwei „ideal" und das eine „nicht ideal" können in **drei** Reihenfolgen auftreten (das „nicht
ideal" kann der 1., 2. oder 3. Zug sein). Alle drei Pfade haben dasselbe Produkt, also:

\[ P(\text{genau }2\text{ ideal}) = 3\cdot\frac{6}{10}\cdot\frac{4}{9}\cdot\frac{3}{8}
   = 3\cdot\frac{72}{720} = 3\cdot 0{,}1 = 0{,}3 = 30\,\%. \]

<figure>
<svg viewBox="0 0 520 250" role="img" aria-label="Die drei günstigen Pfade für genau zwei ideale Männer unter drei Gezogenen" style="width:100%;max-width:540px;height:auto;background:#fbf7ef;border-radius:8px">
  <defs><marker id="k11ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#7a7163"/></marker></defs>
  <text x="70"  y="22" font-size="12" fill="#7a7163" text-anchor="middle">1. Zug</text>
  <text x="220" y="22" font-size="12" fill="#7a7163" text-anchor="middle">2. Zug</text>
  <text x="370" y="22" font-size="12" fill="#7a7163" text-anchor="middle">3. Zug</text>
  <text x="470" y="22" font-size="12" fill="#7a7163" text-anchor="middle">Pfad</text>
  <!-- Reihe 1: I, I, N -->
  <line x1="86"  y1="60" x2="204" y2="60" stroke="#7a7163" stroke-width="1.3" marker-end="url(#k11ar)"/>
  <line x1="236" y1="60" x2="354" y2="60" stroke="#7a7163" stroke-width="1.3" marker-end="url(#k11ar)"/>
  <text x="145" y="52" font-size="12" fill="#26324a" text-anchor="middle">3/9</text>
  <text x="295" y="52" font-size="12" fill="#26324a" text-anchor="middle">6/8</text>
  <circle cx="70"  cy="60" r="15" fill="#fff" stroke="#3a5a9c" stroke-width="2"/><text x="70"  y="65" font-size="14" fill="#3a5a9c" text-anchor="middle">I</text>
  <circle cx="220" cy="60" r="15" fill="#fff" stroke="#3a5a9c" stroke-width="2"/><text x="220" y="65" font-size="14" fill="#3a5a9c" text-anchor="middle">I</text>
  <circle cx="370" cy="60" r="15" fill="#fff" stroke="#d98324" stroke-width="2"/><text x="370" y="65" font-size="14" fill="#d98324" text-anchor="middle">N</text>
  <text x="36" y="52" font-size="11" fill="#7a7163" text-anchor="middle">4/10</text>
  <text x="470" y="65" font-size="12" fill="#26324a" text-anchor="middle">0,1</text>
  <!-- Reihe 2: I, N, I -->
  <line x1="86"  y1="125" x2="204" y2="125" stroke="#7a7163" stroke-width="1.3" marker-end="url(#k11ar)"/>
  <line x1="236" y1="125" x2="354" y2="125" stroke="#7a7163" stroke-width="1.3" marker-end="url(#k11ar)"/>
  <text x="145" y="117" font-size="12" fill="#26324a" text-anchor="middle">6/9</text>
  <text x="295" y="117" font-size="12" fill="#26324a" text-anchor="middle">3/8</text>
  <circle cx="70"  cy="125" r="15" fill="#fff" stroke="#3a5a9c" stroke-width="2"/><text x="70"  y="130" font-size="14" fill="#3a5a9c" text-anchor="middle">I</text>
  <circle cx="220" cy="125" r="15" fill="#fff" stroke="#d98324" stroke-width="2"/><text x="220" y="130" font-size="14" fill="#d98324" text-anchor="middle">N</text>
  <circle cx="370" cy="125" r="15" fill="#fff" stroke="#3a5a9c" stroke-width="2"/><text x="370" y="130" font-size="14" fill="#3a5a9c" text-anchor="middle">I</text>
  <text x="36" y="117" font-size="11" fill="#7a7163" text-anchor="middle">4/10</text>
  <text x="470" y="130" font-size="12" fill="#26324a" text-anchor="middle">0,1</text>
  <!-- Reihe 3: N, I, I -->
  <line x1="86"  y1="190" x2="204" y2="190" stroke="#7a7163" stroke-width="1.3" marker-end="url(#k11ar)"/>
  <line x1="236" y1="190" x2="354" y2="190" stroke="#7a7163" stroke-width="1.3" marker-end="url(#k11ar)"/>
  <text x="145" y="182" font-size="12" fill="#26324a" text-anchor="middle">4/9</text>
  <text x="295" y="182" font-size="12" fill="#26324a" text-anchor="middle">3/8</text>
  <circle cx="70"  cy="190" r="15" fill="#fff" stroke="#d98324" stroke-width="2"/><text x="70"  y="195" font-size="14" fill="#d98324" text-anchor="middle">N</text>
  <circle cx="220" cy="190" r="15" fill="#fff" stroke="#3a5a9c" stroke-width="2"/><text x="220" y="195" font-size="14" fill="#3a5a9c" text-anchor="middle">I</text>
  <circle cx="370" cy="190" r="15" fill="#fff" stroke="#3a5a9c" stroke-width="2"/><text x="370" y="195" font-size="14" fill="#3a5a9c" text-anchor="middle">I</text>
  <text x="36" y="182" font-size="11" fill="#7a7163" text-anchor="middle">6/10</text>
  <text x="470" y="195" font-size="12" fill="#26324a" text-anchor="middle">0,1</text>
  <line x1="430" y1="225" x2="510" y2="225" stroke="#7a7163" stroke-width="1"/>
  <text x="470" y="242" font-size="13" fill="#26324a" text-anchor="middle" font-weight="bold">0,3</text>
  <text x="70" y="232" font-size="11" fill="#7a7163">I = ideale Größe (4 von 10)</text>
  <text x="250" y="232" font-size="11" fill="#7a7163">N = keine ideale Größe (6 von 10)</text>
</svg>
<figcaption>Die drei günstigen Pfade für „genau zwei ideal". Jeder Pfad hat die Wahrscheinlichkeit \( \tfrac{4}{10}\cdot\tfrac{3}{9}\cdot\tfrac{6}{8}=0{,}1 \); zusammen \( 3\cdot 0{,}1 = 0{,}3 \).</figcaption>
</figure>

<details><summary>Haltung dahinter: Bernoulli-Kette, Pfadregel und das „mal 3"</summary>

**Wann ist es eine Binomialverteilung?** Die Binomialverteilung beschreibt eine **Bernoulli-Kette**:
ein Versuch wird **\( n \)-mal unter exakt gleichen Bedingungen wiederholt**, jeder Versuch hat nur
„Treffer/kein Treffer", und die Trefferwahrscheinlichkeit \( p \) bleibt **bei jedem Versuch gleich**.
Das passt zum **Ziehen mit Zurücklegen** (man legt den gezogenen wieder rein, alles bleibt wie vorher)
oder zu sehr großen Mengen, bei denen ein einzelner Zug kaum etwas ändert.

**Warum hier nicht?** Aus zehn Männern (vier ideal) wird **ohne** Zurücklegen gezogen. Vor dem ersten
Zug ist die Idealquote \( \tfrac{4}{10} \). Hat man einen Idealen gezogen, sind nur noch drei von neun
ideal: \( \tfrac{3}{9} \). Die Trefferwahrscheinlichkeit **wandert von Zug zu Zug** — die Bedingung
„konstantes \( p \)" ist verletzt, und außerdem hängen die Züge voneinander ab. Also keine
Binomialverteilung. (Die richtige Verteilung beim Ziehen ohne Zurücklegen heißt **hypergeometrische
Verteilung**; man muss den Namen hier nicht nennen, aber wissen, dass man mit dem Baum rechnet.)

**Pfadregel — entlang multiplizieren.** Ein **Baumdiagramm** zeichnet die Züge nacheinander als Äste.
**Erste Pfadregel:** Entlang eines Pfades **multipliziert** man die Wahrscheinlichkeiten. Für „ideal,
ideal, nicht ideal":

- 1. Zug ideal: \( \tfrac{4}{10} \) (vier Ideale unter zehn).
- 2. Zug ideal: \( \tfrac{3}{9} \) (nur noch drei Ideale unter neun Übrigen).
- 3. Zug nicht ideal: \( \tfrac{6}{8} \) (alle sechs Nicht-Idealen sind noch da, acht Übrige).

Produkt: \( \tfrac{4}{10}\cdot\tfrac{3}{9}\cdot\tfrac{6}{8} = \tfrac{72}{720} = \tfrac{1}{10} = 0{,}1 \).

**Zweite Pfadregel — verschiedene Pfade addieren.** „Genau zwei ideal" passiert nicht nur in der
Reihenfolge (ideal, ideal, nicht), sondern auch (ideal, nicht, ideal) und (nicht, ideal, ideal). Das
sind **drei** günstige Pfade. Jeder hat — egal in welcher Reihenfolge man dieselben Brüche
multipliziert — dasselbe Produkt \( 0{,}1 \). Die drei Pfade **addiert** ergeben

\[ 3\cdot 0{,}1 = 0{,}3 = 30\,\%. \]

<details><summary>… ganz langsam (mit Zahlen): \( \tfrac{4}{10}\cdot\tfrac{3}{9}\cdot\tfrac{6}{8} \)</summary>

Brüche multipliziert man **Zähler mal Zähler, Nenner mal Nenner**:

- Zähler: \( 4\cdot 3\cdot 6 = 12\cdot 6 = 72 \).
- Nenner: \( 10\cdot 9\cdot 8 = 90\cdot 8 = 720 \).

Also \( \tfrac{72}{720} \). Kürzen mit \( 72 \): \( 72:72 = 1 \), \( 720:72 = 10 \), also
\( \tfrac{1}{10} = 0{,}1 \). Mal drei Pfade: \( 3\cdot 0{,}1 = 0{,}3 \). Gegenprobe mit Abzählen
(Kombinationen): „2 aus 4 Idealen" \( \cdot \) „1 aus 6 Nicht-Idealen", geteilt durch „3 aus 10":
\( \dfrac{\binom{4}{2}\binom{6}{1}}{\binom{10}{3}} = \dfrac{6\cdot 6}{120} = \dfrac{36}{120} = 0{,}3 \).
Gleiches Ergebnis.

</details>

<details><summary>Typische Falle: trotzdem mit der Binomialformel rechnen</summary>

Wer hier blind die Binomialformel \( \binom{3}{2}p^2(1-p) \) mit \( p=\tfrac{4}{10}=0{,}4 \) ansetzt,
bekommt \( 3\cdot 0{,}4^2\cdot 0{,}6 = 3\cdot 0{,}16\cdot 0{,}6 = 0{,}288 = 28{,}8\,\% \) — ein
**falsches** Ergebnis. Es weicht von den korrekten \( 30\,\% \) ab, gerade weil sich \( p \) ohne
Zurücklegen verändert. Genau deshalb war in der vorigen Teilaufgabe zu begründen, dass die
Binomialverteilung nicht taugt.

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- a) Stetig (alle Werte im Intervall); Wahrscheinlichkeit = Fläche unter der **Glockenkurve**;
  Hochpunkt und Symmetrieachse bei \( x=\mu \) (**Erwartungswert** = Mittelwert); **Wendepunkte** bei
  \( \mu\pm\sigma \) (**Standardabweichung** = Streuung/Breite); größeres \( \sigma \) → flacher/breiter.
- b) Ablesbar: \( 37\,\% \) ideal, \( 22\,\% \) ideal+interessiert, \( 19\,\% \) nicht ideal+interessiert.
  \( P(A) = 22\,\%+19\,\% = 41\,\% \). \( P_B(\overline A) = \tfrac{37\,\%-22\,\%}{37\,\%} = \tfrac{15}{37} \approx 40{,}5\,\% \).
- c) \( P(A)\cdot P(B) = 41\,\%\cdot 37\,\% = 15{,}17\,\% \neq 22\,\% = P(A\cap B) \) → **nicht** unabhängig.
- d) Ziehen **ohne** Zurücklegen, kleine Menge → \( p \) nicht konstant → keine Binomialverteilung.
  \( P(\text{genau }2) = 3\cdot\tfrac{6}{10}\cdot\tfrac{4}{9}\cdot\tfrac{3}{8} = 30\,\% \).

</details>

---

## Teil 2 — Gespräch (Analysis): Kosten und Einnahmen beim Impfstoff

<div class="aufgabenkasten">

**Input.** Gegeben sind der Graph der Funktion \( K \) mit \( K(x) = (x-2)^3 + 10 \) und der Graph
einer zweiten Funktion \( E \). Die **Kosten** (in \( 1000\ \)Euro) bei der Produktion von \( x \)
Gramm eines Impfstoffs werden durch \( K \) beschrieben. Die **Einnahmen** (in \( 1000\ \)Euro) beim
Verkauf von \( x \) Gramm werden durch \( E \) beschrieben. Im Schaubild ist \( E \) eine Gerade durch
den Ursprung; die von den beiden Graphen eingeschlossene Fläche ist gefärbt.

Im Gespräch denkbare Aspekte: **(AB I)** einen der zwei Graphen \( K \) zuordnen · Funktionsgleichung
von \( E \) · Graph von \( f(x)=x^3 \) skizzieren · Bedeutung eines Wendepunkts an \( K \) erläutern ·
Wendepunkt von \( K \) bestimmen · Produktionsmenge bei \( 15\,000\,€ \) Kosten. **(AB II)**
Zusammenhang von \( K \) und \( f(x)=x^3 \) · Rechenweg für die Tangente an \( K \) parallel zu \( E \)
· Rechenweg für den Inhalt der gefärbten Fläche · Verlauf von \( K \) und \( E \) im Sachzusammenhang ·
Bedeutung von \( K(0) \) und \( E(0) \) · grafisch die Gewinnzone · Gleichung der Gewinnfunktion.
**(AB III)** grafisch die Menge mit dem größten Gewinn · \( K \) auf Monotonie untersuchen · zwei
Aussagen über die Kostenzunahme beurteilen.

</div>

> **Vorab, in einem Satz, worum es geht:** \( x \) zählt **Gramm** produzierten Impfstoff,
> \( K(x) \) und \( E(x) \) messen **Geld in Tausend Euro**. Wo die Einnahmen-Gerade \( E \) über der
> Kosten-Kurve \( K \) liegt, macht man **Gewinn**, sonst **Verlust**. Die Werkzeuge zum Ableiten,
> Untersuchen und Integrieren stehen in [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Funktionsuntersuchung](kap-funktionsuntersuchung.html) und
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).

So liegen die beiden Graphen im Koordinatensystem (Reproduktion des Schaubilds):

<figure>
<div class="jxgbox" id="jxg-k11-ke" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Kostenkurve \( K(x)=(x-2)^3+10 \) (blau) und Einnahmen-Gerade \( E(x)=5x \) (orange). Schnittpunkte bei \( x=2 \) und \( x=2+\sqrt5\approx 4{,}24 \). Die grüne gestrichelte Gerade ist die Tangente an \( K \) parallel zu \( E \) (Stelle des größten Gewinns, grüner Punkt).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k11-ke',{boundingbox:[-0.7,27,5.3,-5],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return Math.pow(x-2,3)+10;},-0.6,5],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('functiongraph',[function(x){return 5*x;},0,5],{strokeColor:'#d98324',strokeWidth:2.5});b.create('functiongraph',[function(x){return 5*x-4.303;},1.7,5],{strokeColor:'#3a8a5a',strokeWidth:1.5,dash:2});b.create('point',[2,10],{name:'',size:2,fixed:true,fillColor:'#26324a',strokeColor:'#26324a'});var r=2+Math.sqrt(5);b.create('point',[r,5*r],{name:'',size:2,fixed:true,fillColor:'#26324a',strokeColor:'#26324a'});var xv=2+Math.sqrt(5/3);b.create('point',[xv,Math.pow(xv-2,3)+10],{name:'',size:3,fixed:true,fillColor:'#3a8a5a',strokeColor:'#3a8a5a'});})();</script>

### AB I — Zuordnung, Gleichung von \( E \), \( f(x)=x^3 \), Wendepunkt, Produktionsmenge

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Zuordnen des Graphen von \( K \).** \( K(x)=(x-2)^3+10 \) ist die **kubische (S-förmige) Kurve**, die
bei \( K(0)=(-2)^3+10 = -8+10 = 2 \) auf der \( y \)-Achse startet und im Punkt \( (2\mid 10) \) ihren
Schwung wechselt. Die **Gerade durch den Ursprung** kann nicht \( K \) sein (denn \( K(0)=2\neq 0 \)),
sie gehört zu \( E \). Also: **die geschwungene Kurve ist \( K \), die Gerade ist \( E \).**

**Funktionsgleichung von \( E \).** \( E \) ist eine Gerade **durch den Ursprung**, hat also die Form
\( E(x)=m\cdot x \) (kein \( y \)-Achsenabschnitt, weil sie durch \( (0\mid 0) \) geht). Die Steigung
\( m \) liest man an einem zweiten Punkt ab: Die Gerade geht durch \( (2\mid 10) \) — denselben Punkt,
in dem auch \( K \) liegt. Also \( m=\tfrac{10}{2}=5 \) und

\[ E(x) = 5x. \]

**Graph von \( f(x)=x^3 \) skizzieren.** Die einfachste kubische Funktion: Sie geht durch den Ursprung,
ist **punktsymmetrisch** zum Ursprung (links unten, rechts oben), hat dort eine **waagerechte Tangente**
(„Sattelpunkt") und steigt nach beiden Seiten immer steiler. Stützpunkte: \( f(1)=1 \), \( f(2)=8 \),
\( f(-1)=-1 \), \( f(-2)=-8 \).

<figure>
<div class="jxgbox" id="jxg-k11-fx3" style="width:100%;max-width:360px;aspect-ratio:1/1"></div>
<figcaption>Grundfunktion \( f(x)=x^3 \): punktsymmetrisch zum Ursprung, Sattelpunkt bei \( (0\mid 0) \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k11-fx3',{boundingbox:[-2.6,9,2.6,-9],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return x*x*x;},-2.1,2.1],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[0,0],{name:'',size:2,fixed:true,fillColor:'#d98324',strokeColor:'#d98324'});})();</script>

**Bedeutung eines Wendepunkts an \( K \) erläutern.** Ein **Wendepunkt** ist die Stelle, an der die
Kurve ihre **Krümmungsrichtung wechselt** — von einer Rechtskurve in eine Linkskurve (oder umgekehrt).
Bei \( K \) ist das der Punkt, ab dem die Kurve aufhört, immer flacher zu steigen, und anfängt, wieder
steiler zu steigen. Genau dort ist die **Steigung am kleinsten** (im Sachzusammenhang: die Kosten
wachsen dort am langsamsten).

**Wendepunkt von \( K \) bestimmen.** Man leitet zweimal ab und setzt die zweite Ableitung null:

\[ K'(x) = 3(x-2)^2, \qquad K''(x) = 6(x-2). \]
\[ K''(x) = 0 \;\Longrightarrow\; 6(x-2)=0 \;\Longrightarrow\; x = 2. \]

Wegen \( K'''(x)=6\neq 0 \) ist es wirklich ein Wendepunkt. Der \( y \)-Wert:
\( K(2) = (2-2)^3+10 = 10 \). Also **Wendepunkt \( W(2\mid 10) \)**. (Man sieht das auch direkt: \( K \)
entsteht aus \( x^3 \), dessen Wendepunkt im Ursprung liegt, durch Verschieben um \( 2 \) nach rechts
und \( 10 \) nach oben — der Wendepunkt wandert mit nach \( (2\mid 10) \).)

**Produktionsmenge bei \( 15\,000\,€ \) Kosten.** Kosten in Tausend Euro: \( 15\,000\,€ \) entspricht
\( K(x)=15 \). Lösen:

\[ (x-2)^3 + 10 = 15 \;\Longrightarrow\; (x-2)^3 = 5 \;\Longrightarrow\; x-2 = \sqrt[3]{5}
   \;\Longrightarrow\; x = 2 + \sqrt[3]{5} \approx 3{,}71. \]

Bei Kosten von \( 15\,000\,€ \) werden also rund **\( 3{,}71 \) Gramm** produziert.

<details><summary>Haltung dahinter: „Gerade durch den Ursprung" und das Ablesen der Steigung</summary>

Eine **Gerade** hat die Form \( y = m x + b \). Dabei ist \( b \) der **\( y \)-Achsenabschnitt** (wo
sie die senkrechte Achse schneidet) und \( m \) die **Steigung** (wie viel sie pro Schritt nach rechts
nach oben geht). „Durch den **Ursprung**" heißt: Sie schneidet die \( y \)-Achse bei \( 0 \), also
\( b=0 \), und es bleibt \( y=mx \).

Die **Steigung** \( m \) bekommt man aus **einem** weiteren Punkt: „Höhenunterschied geteilt durch
Schrittweite nach rechts". Von \( (0\mid 0) \) nach \( (2\mid 10) \) sind das \( 10 \) hoch auf \( 2 \)
nach rechts: \( m = \tfrac{10}{2} = 5 \). Probe an einem dritten Punkt: \( E(4) = 5\cdot 4 = 20 \) —
passt zum Schaubild (die Gerade trifft bei \( x=4 \) die Höhe \( 20 \)).

<details><summary>Warum ist \( (x-2)^3+10 \) ein „verschobenes \( x^3 \)"? (mit Zahlen)</summary>

Es gibt zwei einfache Eingriffe an einer Funktion:

- **\( x \) durch \( (x-2) \) ersetzen** verschiebt den Graphen um \( 2 \) **nach rechts**. (Klingt
  verkehrt herum, ist aber so: Damit der Wert herauskommt, den \( x^3 \) bei \( 0 \) hatte, muss man
  jetzt \( x=2 \) einsetzen — der ganze Graph rückt nach rechts.)
- **\( +10 \) dahinter** schiebt alles um \( 10 \) **nach oben**.

Aus dem Sattelpunkt \( (0\mid 0) \) von \( x^3 \) wird so der Wendepunkt \( (2\mid 10) \) von \( K \).
Daher kennt man die Form sofort, ohne viel zu rechnen.

</details>

<details><summary>Die dritte Wurzel ganz langsam: \( (x-2)^3 = 5 \)</summary>

Die Gleichung \( (x-2)^3 = 5 \) fragt: „Welche Zahl, dreimal mit sich selbst multipliziert, ergibt
\( 5 \)?" Das holt die **dritte Wurzel** \( \sqrt[3]{\;} \) zurück — sie macht das „hoch 3" rückgängig,
so wie die normale Wurzel das „hoch 2" rückgängig macht. Also \( x-2 = \sqrt[3]{5} \). Weil
\( 1{,}7^3 = 4{,}913 \) und \( 1{,}71^3 \approx 5{,}00 \), ist \( \sqrt[3]{5}\approx 1{,}71 \), und
\( x \approx 2 + 1{,}71 = 3{,}71 \). In der hilfsmittelfreien Prüfung genügt die exakte Form
\( x = 2+\sqrt[3]{5} \); die Kommazahl ist Nebensache.

</details>
</details>
</details>

### AB II — Zusammenhang mit \( x^3 \), Tangente, Fläche, Verlauf, Gewinnfunktion

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Zusammenhang von \( K \) und \( f(x)=x^3 \).** \( K \) entsteht aus \( f \) durch **Verschieben**:
\( 2 \) Einheiten **nach rechts** (wegen \( (x-2) \) statt \( x \)) und \( 10 \) Einheiten **nach oben**
(wegen \( +10 \)). Form und Krümmung sind identisch, nur die Lage ist verschoben:

\[ K(x) = f(x-2) + 10. \]

**Rechenweg für die Tangente an \( K \) parallel zu \( E \).** „Parallel zu \( E \)" heißt **gleiche
Steigung wie \( E \)**, und \( E \) hat die Steigung \( 5 \). Man setzt die Ableitung von \( K \) gleich
\( 5 \):

\[ K'(x) = 3(x-2)^2 = 5 \;\Longrightarrow\; (x-2)^2 = \tfrac{5}{3} \;\Longrightarrow\;
   x = 2 \pm \sqrt{\tfrac{5}{3}} = 2 \pm \tfrac{\sqrt{15}}{3}. \]

Das ergibt zwei Berührstellen \( x \approx 0{,}71 \) und \( x \approx 3{,}29 \). Den \( y \)-Wert
bekommt man durch Einsetzen in \( K \), die Tangentengleichung dann aus Punkt und Steigung \( 5 \) per
\( y = K(x_0) + 5\,(x-x_0) \). Für die später gefragte **größte-Gewinn-Stelle** ist die rechte
Berührstelle \( x = 2+\tfrac{\sqrt{15}}{3} \approx 3{,}29 \) maßgeblich (im Schaubild die grüne
Tangente).

**Rechenweg für den Inhalt der gefärbten Fläche.** Die Fläche liegt zwischen den Graphen von \( K \)
und \( E \). Vorgehen:

1. **Schnittstellen bestimmen** (Grenzen): \( K(x)=E(x) \). Mit \( u=x-2 \) wird das einfach:
   \( (x-2)^3+10 = 5x \Rightarrow u^3+10 = 5(u+2) = 5u+10 \Rightarrow u^3 = 5u \Rightarrow u(u^2-5)=0 \).
   Also \( u=0 \) oder \( u=\pm\sqrt5 \), d. h. \( x=2 \), \( x=2+\sqrt5\approx 4{,}24 \) (und
   \( x=2-\sqrt5<0 \), außerhalb).
2. **Pro Abschnitt feststellen, wer oben liegt:** auf \( [0;2] \) liegt \( K \) über \( E \), auf
   \( [2;\,2+\sqrt5] \) liegt \( E \) über \( K \).
3. **Differenz (oben \( - \) unten) integrieren und die Beträge addieren.**

\[ A = \underbrace{\int_0^{2}\big(K(x)-E(x)\big)\,dx}_{K \text{ oben}}
     + \underbrace{\int_{2}^{2+\sqrt5}\big(E(x)-K(x)\big)\,dx}_{E \text{ oben}}. \]

Mit \( K(x)-E(x) = u^3-5u \) (wieder \( u=x-2 \)) und der Stammfunktion \( \tfrac{u^4}{4}-\tfrac{5u^2}{2} \)
ergibt sich der erste Teil zu \( 6 \) und der zweite zu \( \tfrac{25}{4}=6{,}25 \), zusammen

\[ A = 6 + \tfrac{25}{4} = \tfrac{49}{4} = 12{,}25. \]

(Der Aspekt verlangt nur das **Erläutern des Rechenwegs**; die Schnittstellen plus der Integralausdruck
sind die volle Antwort. Die ausgerechneten Werte sind zur Kontrolle ergänzt. Liest man die Färbung nur
als die vollständig von beiden Graphen eingeschlossene „Linse" zwischen \( x=2 \) und \( x=2+\sqrt5 \),
ist der Inhalt \( \tfrac{25}{4}=6{,}25 \); der Teil von \( x=0 \) bis \( x=2 \) wird links von der
\( y \)-Achse begrenzt und steuert \( 6 \) bei.)

**Verlauf von \( K \) und \( E \) im Sachzusammenhang.** Für kleine Mengen liegen die **Kosten über den
Einnahmen** (\( K>E \)) → Verlust. Bei \( x=2\,\text{g} \) schneiden sich beide bei
\( 10\,(=10\,000\,€) \) → **Gewinnschwelle** (Kosten = Einnahmen). Zwischen \( x=2 \) und
\( x=2+\sqrt5\approx 4{,}24 \) liegen die **Einnahmen über den Kosten** (\( E>K \)) → Gewinn. Ab
\( x\approx 4{,}24\,\text{g} \) überholen die kubisch wachsenden Kosten die Einnahmen wieder → erneut
Verlust.

**Bedeutung von \( K(0) \) und \( E(0) \).** \( K(0)=2 \): Schon **ohne** Produktion (\( 0 \) Gramm)
entstehen **Fixkosten** von \( 2\,(=2\,000\,€) \). \( E(0)=0 \): Ohne verkauften Impfstoff gibt es
**keine Einnahmen**.

**Grafisch die Gewinnzone.** Gewinn entsteht, wo die **Gerade \( E \) über der Kurve \( K \)** liegt —
im Schaubild der Bereich, in dem orange über blau verläuft: für \( 2 < x < 2+\sqrt5 \), also rund
**zwischen \( 2 \) und \( 4{,}24 \) Gramm**.

**Gleichung der Gewinnfunktion.** Gewinn \( = \) Einnahmen \( - \) Kosten:

\[ G(x) = E(x) - K(x) = 5x - \big((x-2)^3 + 10\big) = -(x-2)^3 + 5x - 10. \]

Ausmultipliziert: \( G(x) = -x^3 + 6x^2 - 7x - 2 \). (Probe: \( G(2) = -8+24-14-2 = 0 \) — an der
Gewinnschwelle ist der Gewinn null. ✓)

<figure>
<div class="jxgbox" id="jxg-k11-gewinn" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<figcaption>Gewinnfunktion \( G(x)=5x-(x-2)^3-10 \). Nullstellen (Gewinnschwellen) bei \( x=2 \) und \( x\approx 4{,}24 \); dazwischen ist \( G>0 \) (Gewinn). Größter Gewinn am orangen Hochpunkt bei \( x\approx 3{,}29 \).</figcaption>
</figure>

<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k11-gewinn',{boundingbox:[-0.7,6,5.3,-13],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return 5*x-Math.pow(x-2,3)-10;},-0.4,5],{strokeColor:'#3a8a5a',strokeWidth:2.5});b.create('point',[2,0],{name:'',size:2,fixed:true,fillColor:'#26324a',strokeColor:'#26324a'});var r=2+Math.sqrt(5);b.create('point',[r,0],{name:'',size:2,fixed:true,fillColor:'#26324a',strokeColor:'#26324a'});var xv=2+Math.sqrt(5/3);b.create('point',[xv,5*xv-Math.pow(xv-2,3)-10],{name:'',size:3,fixed:true,fillColor:'#d98324',strokeColor:'#d98324'});})();</script>

<details><summary>Haltung dahinter: Tangente, Fläche zwischen zwei Graphen, Gewinnfunktion</summary>

**Tangente und „parallel".** Eine **Tangente** ist die Gerade, die sich an einer Stelle perfekt an die
Kurve **anschmiegt** — sie hat dort genau die **Steigung der Kurve**. Die Steigung einer Kurve an einer
Stelle liefert die **Ableitung** \( K'(x) \). Zwei Geraden sind **parallel**, wenn sie dieselbe Steigung
haben. „Tangente an \( K \) parallel zu \( E \)" heißt deshalb: Finde die Stelle(n), an denen \( K \)
**dieselbe Steigung wie \( E \)** hat — also \( K'(x) = 5 \). Das ist genau die Gleichung oben.

**Warum führt das zum größten Gewinn?** Der senkrechte Abstand zwischen Gerade und Kurve ist die
Differenz \( E(x)-K(x) = G(x) \) — der Gewinn. Dieser Abstand ist dort am größten, wo die Kurve
**genauso steil verläuft wie die Gerade** (dort hört der Abstand auf zu wachsen und beginnt zu
schrumpfen). Mathematisch dasselbe: \( G'(x)=E'(x)-K'(x)=5-K'(x)=0 \Leftrightarrow K'(x)=5 \). Tangente
parallel zu \( E \) und Maximum von \( G \) sind also **dieselbe Bedingung**.

**Fläche zwischen zwei Graphen.** Eine Fläche zwischen zwei Kurven berechnet man als Integral der
**Differenz** „obere Funktion minus untere Funktion". Ein Integral misst Fläche **mit Vorzeichen**;
damit jeder Teil **positiv** zählt, trennt man an jeder **Schnittstelle** (dort tauschen oben und unten
die Rollen) und nimmt pro Stück die richtige Reihenfolge (oben \( - \) unten), sodass nichts negativ
wird. Bild vom **Bankkonto**: Fläche über der jeweils anderen Kurve sind Einzahlungen, würde man stur
durchintegrieren, fräßen sich die Stücke gegenseitig auf — deshalb abschnittsweise mit Beträgen.

**Gewinnfunktion.** Die **Gewinnfunktion** \( G \) ist schlicht „Einnahmen minus Kosten",
\( G(x)=E(x)-K(x) \). Wo \( G>0 \), übersteigen die Einnahmen die Kosten (Gewinn); wo \( G=0 \), ist
die Gewinnschwelle; wo \( G<0 \), Verlust. Deshalb sind die **Nullstellen von \( G \)** genau die
**Schnittpunkte von \( K \) und \( E \)**.

<details><summary>… ganz langsam (mit Zahlen): \( G \) ausmultiplizieren und \( K=E \) lösen</summary>

\( (x-2)^3 \) ausmultipliziert: \( (x-2)^3 = x^3 - 3\cdot x^2\cdot 2 + 3\cdot x\cdot 4 - 8
= x^3 - 6x^2 + 12x - 8 \). Damit

\[ G(x) = 5x - (x^3-6x^2+12x-8) - 10 = 5x - x^3 + 6x^2 - 12x + 8 - 10 = -x^3 + 6x^2 - 7x - 2. \]

Die Schnittstellen werden mit dem Trick \( u=x-2 \) bequem: \( K=E \) wird zu \( u^3 = 5u \), also
\( u^3 - 5u = 0 \), ausklammern \( u(u^2-5)=0 \). Ein Produkt ist null, wenn ein Faktor null ist:
\( u=0 \) (→ \( x=2 \)) oder \( u^2=5 \), d. h. \( u=\pm\sqrt5 \) (→ \( x=2+\sqrt5\approx 4{,}24 \) und
\( x=2-\sqrt5\approx -0{,}24 \), Letzteres ohne Sachbezug, da negative Menge).

</details>

<details><summary>Typische Falle: bei der Fläche nicht an den Schnittstellen trennen</summary>

Wer \( \int_0^{2+\sqrt5}(K-E)\,dx \) in **einem** Stück bildet, bekommt nur den „Kontostand": Der Teil,
in dem \( E \) oben liegt, zieht den anderen ab. Das ist **nicht** der Flächeninhalt. Man muss an der
Schnittstelle \( x=2 \) trennen und mit der jeweils richtigen Differenz (Beträge) rechnen.

</details>
</details>
</details>

### AB III — Größter Gewinn, Monotonie, Aussagen beurteilen

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Verfahren anzeigen</summary>

**Grafisch die Produktionsmenge mit dem größten Gewinn.** Der Gewinn \( G(x)=E(x)-K(x) \) ist der
**senkrechte Abstand** zwischen Gerade und Kurve. Er ist dort am größten, wo \( K \) **dieselbe Steigung
wie \( E \)** hat (Tangente an \( K \) parallel zu \( E \)). Rechnerisch \( G'(x)=0 \):

\[ G'(x) = 5 - 3(x-2)^2 = 0 \;\Longrightarrow\; (x-2)^2 = \tfrac{5}{3}
   \;\Longrightarrow\; x = 2 + \sqrt{\tfrac{5}{3}} = 2 + \tfrac{\sqrt{15}}{3} \approx 3{,}29. \]

(Die Lösung \( x=2-\sqrt{5/3}\approx 0{,}71 \) liegt im Verlustbereich und scheidet aus;
\( G''(x)=-6(x-2)<0 \) für \( x>2 \) bestätigt das Maximum.) Der größte Gewinn beträgt
\( G(3{,}29) = \tfrac{10\sqrt{15}}{9} \approx 4{,}30 \), also rund **\( 4\,300\,€ \) bei etwa
\( 3{,}29 \) Gramm** Produktion. Grafisch: dort, wo der Abstand zwischen orange und blau am größten ist.

**\( K \) auf Monotonie untersuchen.** Die Ableitung \( K'(x) = 3(x-2)^2 \) ist ein Quadrat mal eine
positive Zahl, also \( K'(x) \ge 0 \) für **alle** \( x \), mit \( K'(x)=0 \) nur an der einzelnen
Stelle \( x=2 \). Damit ist \( K \) **auf ganz \( \mathbb{R} \) monoton steigend** (streng wachsend,
mit einer waagerechten Tangente bei \( x=2 \), einem **Sattelpunkt**). Bedeutung: Die Kosten **steigen
immer**, wenn man mehr produziert — sie fallen nie. Bei \( x=2 \) wachsen sie nur **am langsamsten**
(die Steigung ist dort momentan null), danach wieder schneller.

**Zwei Aussagen beurteilen.** Beide Aussagen drehen sich um die **Kostenzunahme**, also um die
Steigung \( K'(x) = 3(x-2)^2 \) — die Kosten je zusätzlich produziertem Gramm.

- *„Je größer die Produktionsmenge ist, desto höher sind die Kosten, die die Produktion eines
  zusätzlichen Gramms verursacht."* — **Diese Aussage ist falsch.** Sie behauptet, die Kostenzunahme
  \( K'(x) \) wachse mit \( x \) immer an. Tatsächlich hat \( K'(x)=3(x-2)^2 \) bei \( x=2 \) ein
  **Minimum**: Für \( x<2 \) **sinkt** die Kostenzunahme (bis \( x=2 \)), erst für \( x>2 \) steigt sie.
  Für kleine Mengen wird also jedes zusätzliche Gramm **billiger**, nicht teurer.
- *„Die Zunahme der Kosten wird bis zu einer bestimmten Impfstoffmenge ständig kleiner, ab dieser nimmt
  sie wieder immer mehr zu."* — **Diese Aussage ist richtig.** Die Kostenzunahme \( K'(x) \) fällt bis
  \( x=2 \) (wird ständig kleiner), erreicht dort ihr Minimum und wächst danach wieder. Die „bestimmte
  Menge" ist genau die **Wendepunktstelle \( x=2 \)** von \( K \).

<details><summary>Haltung dahinter: Monotonie, Steigung der Steigung, und die zwei Aussagen</summary>

**Monotonie** beschreibt, ob ein Graph durchgehend **steigt** oder **fällt**. Geprüft wird über das
**Vorzeichen der Ableitung** \( K'(x) \): Ist \( K'(x)>0 \), steigt die Funktion; ist \( K'(x)<0 \),
fällt sie. Hier ist \( K'(x)=3(x-2)^2 \) das **Dreifache eines Quadrats** — ein Quadrat ist nie negativ.
Also \( K'(x)\ge 0 \) überall: \( K \) steigt immer. Nur bei \( x=2 \) ist \( K'=0 \), die Kurve legt
dort eine waagerechte „Verschnaufpause" ein (Sattelpunkt), steigt aber gleich weiter — kein Hoch- oder
Tiefpunkt.

**„Kostenzunahme" = Ableitung.** „Wie viel kostet das **nächste** Gramm?" ist die **Änderungsrate** der
Kosten, also \( K'(x) \). Wie sich diese Zunahme selbst verändert (wird sie größer oder kleiner?),
verrät die **zweite** Ableitung \( K''(x)=6(x-2) \): Für \( x<2 \) ist \( K''<0 \) → die Zunahme
**schrumpft**; für \( x>2 \) ist \( K''>0 \) → die Zunahme **wächst**. Der Umschaltpunkt ist genau der
**Wendepunkt** \( x=2 \). Das ist der Kern beider Aussagen.

- Aussage 1 vergisst den fallenden Ast vor \( x=2 \) und behauptet pauschal „immer teurer" — das gilt
  erst ab \( x=2 \), also **nicht allgemein** → falsch.
- Aussage 2 beschreibt genau dieses Verhalten „erst kleiner werdend, dann wieder größer werdend" mit dem
  Wendepunkt als Wendemarke → richtig.

So hängen Wendepunkt (AB I), Tangente parallel zu \( E \) (AB II) und diese Beurteilung (AB III) am
selben Punkt \( x=2 \) bzw. an derselben Bedingung über \( K' \) zusammen.

<details><summary>… ganz langsam (mit Zahlen): warum jedes Gramm vor \( x=2 \) billiger wird</summary>

Vergleiche die Kostenzunahme an drei Stellen über \( K'(x)=3(x-2)^2 \):

- bei \( x=0 \): \( K'(0) = 3\cdot(-2)^2 = 3\cdot 4 = 12 \),
- bei \( x=1 \): \( K'(1) = 3\cdot(-1)^2 = 3\cdot 1 = 3 \),
- bei \( x=2 \): \( K'(2) = 3\cdot 0^2 = 0 \),
- bei \( x=3 \): \( K'(3) = 3\cdot 1^2 = 3 \),
- bei \( x=4 \): \( K'(4) = 3\cdot 2^2 = 12 \).

Von \( 12 \) über \( 3 \) auf \( 0 \) **fällt** die Kostenzunahme bis \( x=2 \) — das nächste Gramm wird
immer billiger. Danach von \( 0 \) über \( 3 \) auf \( 12 \) **steigt** sie wieder. Genau das sagt
Aussage 2 (richtig) und widerlegt Aussage 1 (die „immer teurer" behauptet).

</details>
</details>

<details><summary>Kurz-Spickzettel Teil 2 (erst nach dem eigenen Versuch aufklappen)</summary>

- **Zuordnung/E:** \( K \) = geschwungene Kurve (\( K(0)=2 \)), \( E \) = Ursprungsgerade
  \( E(x)=5x \) (durch \( (2\mid 10) \)).
- **\( f(x)=x^3 \):** Ursprung, punktsymmetrisch, Sattelpunkt bei \( 0 \).
- **Wendepunkt \( K \):** \( K''=6(x-2)=0 \Rightarrow W(2\mid 10) \).
- **\( 15\,000\,€ \):** \( K(x)=15 \Rightarrow x=2+\sqrt[3]{5}\approx 3{,}71 \) Gramm.
- **Zusammenhang:** \( K(x)=f(x-2)+10 \) (2 rechts, 10 hoch).
- **Tangente \( \parallel E \):** \( K'(x)=5 \Rightarrow x=2\pm\tfrac{\sqrt{15}}{3} \) (\( \approx 0{,}71;\ 3{,}29 \)).
- **Fläche:** Schnittstellen \( x=2,\ 2+\sqrt5 \); \( A=\int_0^2(K-E)+\int_2^{2+\sqrt5}(E-K)=6+\tfrac{25}{4}=\tfrac{49}{4} \) (Linse allein \( \tfrac{25}{4} \)).
- **Verlauf:** \( K>E \) klein → Verlust; Schnitt \( x=2 \) = Gewinnschwelle; \( E>K \) bis \( \approx 4{,}24 \) = Gewinn; danach Verlust.
- **\( K(0)=2 \):** Fixkosten \( 2\,000\,€ \); **\( E(0)=0 \):** keine Einnahmen.
- **Gewinnzone:** \( 2<x<2+\sqrt5 \) (orange über blau).
- **Gewinnfunktion:** \( G(x)=5x-(x-2)^3-10=-x^3+6x^2-7x-2 \).
- **Größter Gewinn:** \( x=2+\tfrac{\sqrt{15}}{3}\approx 3{,}29 \), \( G_{\max}=\tfrac{10\sqrt{15}}{9}\approx 4{,}30 \) (\( \approx 4\,300\,€ \)).
- **Monotonie:** \( K'(x)=3(x-2)^2\ge 0 \) → überall steigend (Sattelpunkt bei \( x=2 \)).
- **Aussagen:** 1 falsch (Zunahme fällt erst bis \( x=2 \)), 2 richtig (Wendemarke \( x=2 \)).

</details>
</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Teilaufgabe, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen
kannst. Du musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Stochastik) aufklappen</summary>

- **a) Normalverteilung.** Gut ist jede Antwort, die nennt: **stetig** (alle Werte in einem Intervall),
  Wahrscheinlichkeit = **Fläche unter der Glockenkurve**, **Hochpunkt/Symmetrie bei \( \mu \)**
  (Erwartungswert = Mittelwert), **Wendepunkte bei \( \mu\pm\sigma \)** (Standardabweichung = Streuung),
  größeres \( \sigma \) → flacher/breiter. *Rückfrage:* „Was bedeutet \( \mu \), was \( \sigma \)
  anschaulich?" *Rote Flagge:* Verwechslung mit einem Würfel/abzählbaren Werten (das wäre diskret).
- **b) Ablesen + Wahrscheinlichkeiten.** Erwartet: \( P(A)=22\,\%+19\,\%=41\,\% \) (Zeile addieren) und
  \( P_B(\overline A)=\tfrac{15}{37}\approx 40{,}5\,\% \) — Betonung: **durch \( 37\,\% \) teilen**, weil
  „aus den Idealgroßen" gezogen wird. *Rückfrage:* „Warum teilst du durch \( 37\,\% \) und nicht durch
  \( 100\,\% \)?" *Rote Flagge:* Antwort \( 15\,\% \) (Schnitt statt bedingter Wahrscheinlichkeit).
- **c) Unabhängigkeit.** Erwartet: Test \( P(A)\cdot P(B)=41\,\%\cdot 37\,\%=15{,}17\,\% \) mit
  \( P(A\cap B)=22\,\% \) vergleichen → ungleich → **nicht unabhängig**. *Rückfrage:* „Was würde
  \( 15{,}17\,\% \) bedeuten, wenn die Merkmale nichts miteinander zu tun hätten?" *Rote Flagge:*
  „unabhängig, weil \( P(A\cap B)\neq 0 \)" (verwechselt mit unvereinbar).
- **d) Keine Binomialverteilung + \( 30\,\% \).** Erwartet: Begründung **Ziehen ohne Zurücklegen / kleine
  Menge → \( p \) nicht konstant**; Rechnung über den Baum \( 3\cdot\tfrac{6}{10}\cdot\tfrac{4}{9}\cdot\tfrac{3}{8}=30\,\% \).
  *Rückfrage:* „Wie ändert sich die Wahrscheinlichkeit für ‚ideal' vom ersten zum zweiten Zug?" *Rote
  Flagge:* Rechnen mit \( B(3;0{,}4) \) (ergäbe falsche \( 28{,}8\,\% \)).

</details>

<details><summary>Leitfaden Teil 2 (Analysis) aufklappen</summary>

- **AB I.** Erwartet: \( K \) = geschwungene Kurve (Begründung \( K(0)=2 \)), \( E(x)=5x \) (Ursprung +
  Punkt \( (2\mid 10) \)); \( f(x)=x^3 \) punktsymmetrisch mit Sattelpunkt; Wendepunkt **\( W(2\mid 10) \)**
  über \( K''=0 \); bei \( 15\,000\,€ \): \( x=2+\sqrt[3]{5}\approx 3{,}71\,\text{g} \). *Rückfrage:*
  „Woran erkennst du, dass die Gerade nicht \( K \) sein kann?" (Antwort: \( K(0)=2\neq 0 \).)
- **AB II.** Erwartet: \( K \) = \( x^3 \) **um 2 rechts, 10 hoch verschoben**; Tangente \( \parallel E \)
  über \( K'(x)=5 \); Fläche über **Schnittstellen + Differenzintegral** (an \( x=2 \) trennen);
  Verlauf = **Verlust/Gewinnschwelle/Gewinn/Verlust**; \( K(0)=2 \) Fixkosten, \( E(0)=0 \) keine
  Einnahmen; Gewinnzone = wo \( E \) über \( K \); \( G(x)=5x-(x-2)^3-10 \). *Rückfrage:* „Warum trennst
  du die Fläche an der Schnittstelle?" *Rote Flagge:* ein einziges Integral ohne Trennen.
- **AB III.** Erwartet: größter Gewinn = **Tangente \( \parallel E \) / \( G'=0 \)** bei \( x\approx 3{,}29 \);
  \( K \) **überall steigend** (\( K'=3(x-2)^2\ge 0 \), Sattelpunkt bei \( 2 \)); **Aussage 1 falsch,
  Aussage 2 richtig**, beide am Wendepunkt \( x=2 \) erklärt. *Rückfrage:* „Wo wächst die Kostenzunahme
  am langsamsten — und was hat das mit dem Wendepunkt zu tun?" *Hinweis für dich:* Hier zählt **sauberes
  Erklären** mehr als der exakte Zahlenwert.

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Was unterscheidet eine stetige (normalverteilte) Größe von einem Würfelwurf, und wo stecken \( \mu \)
  und \( \sigma \) in der Glockenkurve?
- Warum teilst du bei „aus den Idealgroßen wird einer gezogen" durch \( 37\,\% \) und nicht durch
  \( 100\,\% \)?
- Mit welcher Gleichung prüfst du Unabhängigkeit, und was sagt dir das Ergebnis hier?
- Warum ist beim Ziehen ohne Zurücklegen die Binomialverteilung ungeeignet, und wie kommst du auf die
  \( 30\,\% \)?
- Wie findest du die Stelle des größten Gewinns — und warum ist das dieselbe wie „Tangente an \( K \)
  parallel zu \( E \)"?
- Warum ist \( K \) überall steigend, und an welcher Stelle wachsen die Kosten am langsamsten?
