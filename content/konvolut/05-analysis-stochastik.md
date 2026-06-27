# Aufgabe 5 — Analysis & Stochastik

Dies ist eine vollständige mündliche Beispielprüfung aus dem Abitur-Konvolut 2023:
**Teil 1 (Vortrag) aus der Analysis**, **Teil 2 (Gespräch) aus der Stochastik**. Alles ist
**rechnerfrei** zu lösen. Arbeitet die Aufgabe wie eine echte Simulation durch — eine Person trägt
vor, die andere prüft mit dem Lösungsweg und dem [Prüfer-Leitfaden](#prufer-leitfaden-fur-die-abfragende-person)
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

> **Werkzeug zum Nachschlagen:** Die wiederkehrenden Stochastik-Werkzeuge (Wahrscheinlichkeit,
> Erwartungswert, Bernoulli-Kette, Binomialverteilung, Standardabweichung) stehen kompakt im
> [Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html) (Anker u. a. `#erwartungswert`,
> `#bernoulli-kette`, `#binomialverteilung`). Die Analysis-Werkzeuge findest du in den Kapiteln
> [Ableit-Handwerk](kap-ableiten-handwerk.html),
> [Integral-Grundlagen](kap-integral-grundlagen.html),
> [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html) und
> [Funktionsuntersuchung](kap-funktionsuntersuchung.html).

---

## Teil 1 — Vortrag (Analysis): Wachstumsrate einer Pflanze

<div class="aufgabenkasten">

**Die Funktion \( f \) beschreibt für \( t \ge 0 \) die Wachstumsrate einer Pflanze. Die Zeit \( t \)
wird in Tagen, die Wachstumsrate \( f(t) \) in cm pro Tag angegeben. Die Abbildung zeigt einen
Ausschnitt des Graphen von \( f \).**

**a)** Bestimme anhand der Abbildung \( f'(2) \) und \( \displaystyle\int_0^2 f(t)\,dt \).

**b)** Bestimme die ungefähre Höhe der Pflanze nach dem zweiten Tag, wenn die Pflanze zu
Beobachtungsbeginn 20 cm hoch war.

**c)** Die Funktion \( f \) hat den Funktionsterm \( f(t)=8t\cdot e^{-t} \). Für die Ableitung gilt
\( f'(t)=e^{-t}\cdot(8-8t) \). Berechne den Zeitpunkt, zu dem die Wachstumsrate der Pflanze am
stärksten abnimmt.

**d)** \( F \) ist eine Stammfunktion von \( f \). Formuliere eine Fragestellung im Sachzusammenhang,
die auf die Gleichung \( F(t+1)=F(t)+2{,}5 \) führt. Beschreibe, wie man mithilfe der Abbildung eine
Lösung dieser Gleichung ermitteln kann.

</div>

Hier ist der Graph der Wachstumsrate \( f \). Die orange gestrichelte Linie ist die **Tangente** (die
„Anlege-Gerade") bei \( t=2 \); die blau gefüllte Fläche ist das Stück zwischen Graph und \( t \)-Achse
von \( t=0 \) bis \( t=2 \). Spiele mit dem Bild, bevor du die Lösung aufklappst.

<div class="jxgbox" id="jxg-k5-f" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k5-f',{boundingbox:[-0.8,5.5,7.8,-1.6],axis:true,grid:true,showCopyright:false,showNavigation:false});var f=b.create('functiongraph',[function(t){return 8*t*Math.exp(-t);},0,8],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('integral',[[0,2],f],{fillColor:'#3a5a9c',fillOpacity:0.13,withLabel:false,curveLeft:{visible:false,withLabel:false},curveRight:{visible:false,withLabel:false},baseLeft:{visible:false},baseRight:{visible:false}});var g=b.create('glider',[2,0,f],{name:'',size:1,fixed:true,fillColor:'#d98324',strokeColor:'#d98324'});b.create('tangent',[g],{strokeColor:'#d98324',strokeWidth:1.8,dash:2});})();</script>

<figcaption style="font-size:0.9em;color:#5a5346">Reproduzierter Graph von \( f(t)=8t\,e^{-t} \). Im
Originalbild ist das Gitter in <b>halben</b> Kästchen (\( 0{,}5 \times 0{,}5 \)) gezeichnet — ein
kleines Kästchen hat also den Flächeninhalt \( 0{,}5\cdot 0{,}5 = 0{,}25 \). Das brauchst du in a).</figcaption>

### Teilaufgabe a) — \( f'(2) \) und das Integral aus dem Bild ablesen

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Teil 1 — die Steigung \( f'(2) \).** \( f'(2) \) ist die **Steigung des Graphen an der Stelle
\( t=2 \)**. Man legt im Punkt \( (2 \mid f(2)) \) eine Tangente an und liest ihr Steigungsdreieck ab:
Geht man **1 nach rechts**, fällt die Tangente um etwa **1 nach unten**. Die Steigung ist also negativ
und ungefähr

\[ f'(2) \approx -1. \]

**Teil 2 — das Integral \( \displaystyle\int_0^2 f(t)\,dt \).** Das Integral ist der **Flächeninhalt
zwischen dem Graphen und der \( t \)-Achse** von \( t=0 \) bis \( t=2 \) (blaue Fläche). Diese Fläche
**zählt man in Kästchen aus**. Im Originalbild liegen unter dem Kurvenstück etwa \( 19 \) kleine
Kästchen, und jedes Kästchen ist \( 0{,}25 \) groß:

\[ \int_0^2 f(t)\,dt \;\approx\; 19\cdot 0{,}25 \;=\; \frac{19}{4} \;=\; 4{,}75. \]

<details><summary>Haltung dahinter: Was heißt „Ableitung an einer Stelle", und wie liest man eine Steigung ab? (ganz von vorn)</summary>

Ganz langsam, was hier gefragt ist.

**Steigung.** Die **Steigung** sagt, wie steil eine Linie ansteigt oder abfällt. Bei einer Geraden
misst man sie mit einem **Steigungsdreieck**: „Gehe ein Stück nach rechts, schaue, wie viel es dabei
nach oben (oder unten) geht." Steigung \( = \dfrac{\text{Höhenänderung}}{\text{Schritt nach rechts}} \).
Geht es nach unten, ist die Steigung **negativ**.

**Ableitung \( f'(2) \).** Eine krumme Kurve hat an jeder Stelle eine andere Steilheit. Die
**Ableitung** \( f'(2) \) ist genau die Steigung der Kurve **an der einen Stelle \( t=2 \)**. Man
bekommt sie, indem man dort die **Tangente** anlegt — das ist die Gerade, die sich an dieser Stelle
genau an die Kurve „anschmiegt" — und deren Steigung mit dem Steigungsdreieck abliest. Hier fällt die
Kurve bei \( t=2 \), die Tangente geht abwärts, also ist \( f'(2) \) negativ. Ein Schritt nach rechts,
ungefähr ein Schritt nach unten \( \Rightarrow f'(2)\approx -1 \).

**Was bedeutet das im Sachzusammenhang?** \( f \) ist die Wachstums**rate** (wie schnell die Pflanze
gerade wächst, in cm pro Tag). \( f'(2)\approx -1 \) heißt: Am zweiten Tag **nimmt diese
Geschwindigkeit ab** — die Pflanze wächst noch, aber von Tag zu Tag langsamer.

</details>

<details><summary>Haltung dahinter: Was ist ein Integral, und warum ist es eine Fläche? (ganz von vorn)</summary>

Ein **Integral** \( \displaystyle\int_0^2 f(t)\,dt \) ist eine Maschine, die die **Fläche zwischen dem
Graphen und der \( t \)-Achse** zwischen den senkrechten Grenzen \( t=0 \) (links) und \( t=2 \)
(rechts) zusammenrechnet. Man kann es sich als „lauter hauchdünne senkrechte Streifen unter der Kurve,
alle aufaddiert" vorstellen.

Weil hier die ganze Kurve **über** der \( t \)-Achse liegt, ist die Fläche einfach **positiv** — man
muss nicht mit Vorzeichen aufpassen. Man darf sie deshalb direkt **abzählen**.

<details><summary>Kästchenzählen ganz langsam (mit Zahlen)</summary>

Das **Kästchenzählen** geht so: Man schaut, wie viele kleine Gitterquadrate unter dem Kurvenstück
liegen, und multipliziert mit dem Flächeninhalt **eines** Quadrats.

- Wie groß ist ein Kästchen? Im Bild ist das Gitter in Schritten von \( 0{,}5 \) gezeichnet. Ein
  Kästchen ist also \( 0{,}5 \) breit und \( 0{,}5 \) hoch. Sein Flächeninhalt:
  \( 0{,}5 \cdot 0{,}5 = 0{,}25 \). (Halb mal halb ist ein Viertel.)
- Wie viele Kästchen? Volle Kästchen voll zählen, angeschnittene zu ganzen zusammenstückeln. Hier
  kommt man auf etwa \( 19 \) Kästchen.
- Fläche: \( 19 \cdot 0{,}25 \). Rechne \( 19 \cdot 0{,}25 = 19 : 4 = 4{,}75 \). (Mal \( 0{,}25 \) ist
  dasselbe wie geteilt durch \( 4 \).)

Ergebnis: \( \displaystyle\int_0^2 f(t)\,dt \approx 4{,}75 \).

</details>

<details><summary>Typische Falle</summary>

Zwei Stolperstellen:
- **\( f'(2) \) mit \( f(2) \) verwechseln.** \( f(2) \) ist der **Wert** der Kurve bei \( t=2 \)
  (ungefähr \( 2{,}2 \)). \( f'(2) \) ist die **Steigung** dort (ungefähr \( -1 \)). Gefragt ist die
  Steigung.
- **Kästchen mit Flächeninhalt \( 1 \) ansetzen.** Weil das Gitter in Halben gezeichnet ist, hat ein
  kleines Kästchen nur \( 0{,}25 \). Wer mit \( 1 \) rechnet, bekommt das Vierfache heraus.

</details>
</details>
</details>

### Teilaufgabe b) — Höhe der Pflanze nach dem zweiten Tag

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Die Pflanze war zu Beginn \( 20 \) cm hoch. Das Integral aus a) ist der **Höhenzuwachs** in den ersten
zwei Tagen, nämlich \( 4{,}75 \) cm. Höhe nach dem zweiten Tag = Starthöhe + Zuwachs:

\[ 20 + 4{,}75 = 24{,}75. \]

Die Pflanze ist nach dem zweiten Tag **ungefähr \( 24{,}75 \) cm** hoch.

<details><summary>Haltung dahinter: Warum ist die Fläche unter der Rate genau der Zuwachs? (ganz von vorn)</summary>

Der Schlüssel ist der Unterschied zwischen **Geschwindigkeit** und **zurückgelegtem Weg**.

\( f \) ist eine **Rate**: Sie sagt, *wie schnell* die Pflanze gerade wächst — in cm **pro Tag**. Die
gesamte Höhenänderung über einen Zeitraum bekommt man, indem man die Rate über die Zeit aufsummiert,
und genau das tut das Integral.

**Alltagsanalogie Tacho.** Stell dir ein Auto vor. Der Tacho zeigt die **Geschwindigkeit** (km pro
Stunde). Die **gefahrene Strecke** ist nicht der Tachowert selbst, sondern „Geschwindigkeit mal Zeit"
— bzw. die Fläche unter der Geschwindigkeitskurve. Genauso hier: \( f \) ist der „Tacho" des Wachstums
(cm pro Tag), und die **Fläche** unter \( f \) ist die „gefahrene Strecke", also der Höhenzuwachs in cm.

**Die Einheiten zeigen es.** \( f(t) \) hat die Einheit \( \tfrac{\text{cm}}{\text{Tag}} \), die
Zeitspanne hat die Einheit \( \text{Tag} \). Multipliziert man (und ein Integral ist im Kern eine
Multiplikation „Höhe mal Breite"), kürzt sich „Tag" weg und es bleibt **cm** — eine Länge, also eine
Höhe. Deshalb ist \( \int_0^2 f\,dt = 4{,}75 \) ein Zuwachs von \( 4{,}75 \) **cm**.

<details><summary>Ganz langsam (mit Zahlen)</summary>

- Starthöhe: \( 20 \) cm.
- Zuwachs in 2 Tagen (= Fläche aus a)): \( 4{,}75 \) cm.
- Endhöhe: \( 20 + 4{,}75 = 24{,}75 \) cm.

Das „ungefähr" steht da, weil der Zuwachs aus dem **Abzählen** der Kästchen kommt — ein abgelesener,
gerundeter Wert.

</details>

<details><summary>Typische Falle</summary>

\( f(2) \approx 2{,}2 \) ist **nicht** die Höhe — das ist nur die Wachstums*geschwindigkeit* am zweiten
Tag. Auch das „\( +20 \)" darf nicht vergessen werden: Das Integral liefert nur die **Änderung** der
Höhe, nicht die Höhe selbst.

</details>
</details>
</details>

### Teilaufgabe c) — Zeitpunkt der stärksten Abnahme

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Gesucht ist der Zeitpunkt, an dem die Wachstumsrate **am stärksten abnimmt** — also dort, wo der Graph
von \( f \) **am steilsten fällt**. „Am steilsten fallen" heißt: die Steigung \( f' \) ist dort **am
negativsten**, hat also ein **Minimum**. Ein Minimum von \( f' \) findet man, indem man die Ableitung
von \( f' \) — das ist \( f'' \) — null setzt.

**Schritt 1 — \( f'' \) bilden.** Aus \( f'(t)=e^{-t}\,(8-8t) \) wird mit der Produktregel

\[ f''(t) = \underbrace{-e^{-t}}_{(e^{-t})'}\,(8-8t) \;+\; e^{-t}\,\underbrace{(-8)}_{(8-8t)'}
   = e^{-t}\big(-8+8t-8\big) = e^{-t}\,(8t-16) = 8\,(t-2)\,e^{-t}. \]

**Schritt 2 — null setzen.** Ein Produkt ist null, wenn ein Faktor null ist. Da \( e^{-t} \) **nie**
null wird, bleibt nur der Faktor \( (t-2) \):

\[ 8\,(t-2)\,e^{-t} = 0 \;\;\Longrightarrow\;\; t-2 = 0 \;\;\Longrightarrow\;\; t = 2. \]

**Schritt 3 — prüfen, dass es wirklich die stärkste Abnahme ist.** \( f''(t)=8(t-2)e^{-t} \) wechselt
bei \( t=2 \) das Vorzeichen von **minus** (für \( t<2 \)) zu **plus** (für \( t>2 \)). Damit hat
\( f' \) bei \( t=2 \) ein **Minimum** — die Steigung ist dort am negativsten. Also nimmt die
Wachstumsrate **nach \( 2 \) Tagen** am stärksten ab.

<details><summary>Haltung dahinter: „am stärksten abnehmen" — welche Ableitung ist das überhaupt? (ganz von vorn)</summary>

Hier stapeln sich drei Ebenen aufeinander, deshalb der Reihe nach.

- \( f \) selbst ist die **Wachstumsrate** (wie schnell die Pflanze wächst).
- \( f' \) ist die **Steigung von \( f \)** — also wie schnell sich die *Wachstumsrate* ändert. Ist
  \( f'<0 \), so **sinkt** die Rate (die Pflanze verliert an Schwung).
- „Am **stärksten** abnehmen" heißt: dieses Sinken ist am **heftigsten**, die Rate stürzt am
  schnellsten — \( f' \) ist so **negativ** wie nirgends sonst, hat also ein **Minimum**.

Und ein Hoch- oder Tiefpunkt einer Funktion liegt dort, wo **ihre** Ableitung null ist. Die Ableitung
von \( f' \) ist \( f'' \). Deshalb: \( f''(t)=0 \) setzen. Der Punkt, den man findet, heißt
**Wendepunkt** von \( f \) — die Stelle, an der die Kurve von „Linkskurve" auf „Rechtskurve" umschaltet
und genau dazwischen am steilsten ist.

<details><summary>Produkt- und Kettenregel — wozu hier?</summary>

\( f'(t)=e^{-t}\,(8-8t) \) ist ein **Produkt** aus zwei Bausteinen: \( e^{-t} \) und \( (8-8t) \). Die
**Produktregel** sagt, wie man so etwas ableitet: „erster Baustein abgeleitet mal zweiter, plus erster
mal zweiter abgeleitet."

- Ableitung von \( e^{-t} \): Das ist \( -e^{-t} \). (Die **Kettenregel**: außen bleibt \( e^{-t} \)
  stehen, mal innere Ableitung von \( -t \), die \( -1 \) ist — also \( e^{-t}\cdot(-1)=-e^{-t} \).)
- Ableitung von \( (8-8t) \): Das ist \( -8 \) (die \( 8 \) fällt weg, aus \( -8t \) wird \( -8 \)).

Zusammengesetzt: \( f''(t) = (-e^{-t})(8-8t) + e^{-t}(-8) \). Ausmultiplizieren und zusammenfassen
ergibt \( e^{-t}(8t-16) = 8(t-2)e^{-t} \). Ausführlich:
[Ableit-Handwerk](kap-ableiten-handwerk.html).

</details>

<details><summary>Ganz langsam (mit Zahlen): warum ist \( t=2 \) wirklich der steilste Abfall?</summary>

Vergleiche die Steigung \( f' \) an ein paar Stellen — je negativer, desto steiler fällt \( f \):

- \( f'(1) = e^{-1}(8-8\cdot 1) = e^{-1}\cdot 0 = 0 \). Bei \( t=1 \) ist die Steigung null — das ist der
  **Höhepunkt** der Wachstumsrate (die Kurve ist dort oben am Bogen waagerecht).
- \( f'(2) = e^{-2}(8-16) = e^{-2}\cdot(-8) \approx -1{,}08 \).
- \( f'(3) = e^{-3}(8-24) = e^{-3}\cdot(-16) \approx -0{,}80 \).

\( -1{,}08 \) ist negativer als \( -0{,}80 \). Bei \( t=2 \) fällt die Kurve also steiler als bei
\( t=3 \) — und steiler als überall sonst. Das bestätigt \( t=2 \).

</details>

<details><summary>Typische Falle</summary>

„Wachstumsrate **am stärksten ab**nehmend" wird oft mit zwei anderen Stellen verwechselt:
- mit dem **Maximum der Rate** (das ist \( t=1 \), wo \( f \) am höchsten und \( f'=0 \) ist) — da
  wächst die Pflanze am schnellsten, aber die Rate nimmt dort *nicht* ab;
- mit einer **Nullstelle von \( f \)** — da wäre gar kein Wachstum mehr.

Gesucht ist der **Wendepunkt** von \( f \): \( f''=0 \), Vorzeichenwechsel von \( f' \). Das ist \( t=2 \).

</details>
</details>
</details>

### Teilaufgabe d) — Fragestellung formulieren und grafisch lösen

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**Die Fragestellung.** \( F \) ist eine Stammfunktion von \( f \); im Sachzusammenhang ist \( F(t) \)
die **bis zum Zeitpunkt \( t \) angesammelte Höhenzunahme**. Dann ist

\[ F(t+1) - F(t) = \int_t^{t+1} f(\tau)\,d\tau = \text{Zuwachs der Höhe während des Tages von } t
   \text{ bis } t+1. \]

Die Gleichung \( F(t+1)=F(t)+2{,}5 \) sagt also: dieser Zuwachs ist genau \( 2{,}5 \) cm. Eine passende
Frage lautet:

> **„Innerhalb welchen \( 1 \)-Tages-Zeitraums nimmt die Höhe der Pflanze um \( 2{,}5 \) cm zu?"**

**Lösung mithilfe der Abbildung.** \( F(t+1)-F(t) \) ist der **Flächeninhalt** unter dem Graphen von
\( f \) über dem Intervall \( [\,t,\;t+1\,] \). Man legt also einen **senkrechten Streifen der Breite
\( 1 \)** unter die Kurve und **verschiebt** ihn nach rechts, bis die eingeschlossene Fläche genau
\( 2{,}5 \) beträgt (in Kästchen: \( 2{,}5 : 0{,}25 = 10 \) Kästchen). Die **Lage des linken Randes**
dieses Streifens ist eine Lösung der Gleichung.

<div class="jxgbox" id="jxg-k5-d" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-k5-d',{boundingbox:[-0.8,5.5,7.8,-1.6],axis:true,grid:true,showCopyright:false,showNavigation:false});var f=b.create('functiongraph',[function(t){return 8*t*Math.exp(-t);},0,8],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('integral',[[0.2,1.2],f],{fillColor:'#d98324',fillOpacity:0.2,withLabel:false,curveLeft:{visible:false,withLabel:false},curveRight:{visible:false,withLabel:false},baseLeft:{visible:false},baseRight:{visible:false}});})();</script>

<figcaption style="font-size:0.9em;color:#5a5346">Ein Streifen der <b>Breite 1</b> (orange). Man schiebt
ihn waagerecht, bis seine Fläche \( =2{,}5 \) ist; der linke Rand des Streifens ist dann die gesuchte
Lösung \( t \).</figcaption>

<details><summary>Haltung dahinter: Was ist eine Stammfunktion im Sachzusammenhang, und warum ist die Differenz eine Fläche? (ganz von vorn)</summary>

**Stammfunktion.** Eine **Stammfunktion** \( F \) von \( f \) ist „Ableiten rückwärts": Ihre Ableitung
ist wieder \( f \), also \( F'=f \). Wenn \( f \) die Wachstums**rate** ist, dann ist \( F \) die davon
**aufsummierte Größe** — die **angesammelte Höhenzunahme** seit dem Start. Bild: \( f \) sind die
täglichen Einzahlungen aufs Konto, \( F \) ist der **Kontostand**.

**Differenz von Kontoständen.** \( F(t+1) \) ist der Kontostand am Tag \( t+1 \), \( F(t) \) der am Tag
\( t \). Die Differenz \( F(t+1)-F(t) \) ist also genau das, was **in diesem einen Tag dazugekommen**
ist — der Zuwachs zwischen \( t \) und \( t+1 \).

**Warum eine Fläche?** Der **Hauptsatz der Differenzial- und Integralrechnung** verknüpft beides:
\( \displaystyle\int_t^{t+1} f\,d\tau = F(t+1)-F(t) \). Das Integral ist die Fläche unter \( f \). Also
ist der Tageszuwachs gleich der Fläche unter der Ratenkurve über diesem Tag — und Flächen kann man im
Bild **abzählen**. (Mehr dazu: [Stammfunktion & Hauptsatz](kap-stammfunktion-hauptsatz.html).)

<details><summary>Wie genau „verschiebt" man den Streifen — und gibt es mehrere Lösungen?</summary>

Praktisch: Man nimmt ein Rechteck-Fenster der Breite \( 1 \), legt es ganz links unter die Kurve
(\( t=0 \): Fenster \( [0,1] \)) und schiebt es Schritt für Schritt nach rechts. Bei jeder Position
zählt man die eingeschlossenen Kästchen. Gesucht ist die Position mit **\( 10 \) Kästchen** (Fläche
\( 2{,}5 \)).

Beim Wandern passiert Folgendes: Anfangs liegt der Streifen über dem hohen Bogen der Kurve, die Fläche
ist groß; ganz rechts ist die Kurve fast platt, die Fläche winzig. Dazwischen **durchläuft** die Fläche
den Wert \( 2{,}5 \). Weil der Tageszuwachs erst etwas **steigt** (bis der Streifen genau über dem
höchsten Bogen sitzt) und danach **fällt**, wird der Wert \( 2{,}5 \) sogar an **zwei** Positionen
getroffen — beim Hinaufgehen und beim Herunterkommen. Jeder der beiden linken Ränder ist eine gültige
Lösung. Für die mündliche Prüfung genügt das **beschriebene Verfahren**; man muss keinen exakten
Zahlenwert ausrechnen.

</details>
</details>
</details>

<details><summary>Kurz-Spickzettel Teil 1 (erst nach dem eigenen Versuch aufklappen)</summary>

- a) \( f'(2) \approx -1 \); \( \displaystyle\int_0^2 f(t)\,dt \approx 19\cdot 0{,}25 = \tfrac{19}{4} = 4{,}75 \)
- b) Höhe \( = 20 + 4{,}75 = 24{,}75 \) cm
- c) \( f''(t) = 8\,(t-2)\,e^{-t} \); \( f''(t)=0 \Rightarrow t=2 \) (nach \( 2 \) Tagen)
- d) Frage: „In welchem \( 1 \)-Tages-Zeitraum wächst die Pflanze um \( 2{,}5 \) cm?" — Streifen der
  Breite \( 1 \) verschieben, bis die Fläche \( 2{,}5 \) (\(=10\) Kästchen) ist; linker Rand = Lösung.

</details>

---

## Teil 2 — Gespräch (Stochastik): Würfel mit dem Netz 1, 2, 2, 3, 4, 6

<div class="aufgabenkasten">

**Input.** Gegeben ist das Netz eines Würfels. Die sechs Flächen tragen die Augenzahlen
\( 1,\ 2,\ 2,\ 3,\ 4,\ 6 \) (die „\( 2 \)" kommt zweimal vor, eine „\( 5 \)" gibt es nicht).

Im Gespräch denkbare Aspekte:
- **(AB I)** Die Zufallsgröße \( X \) beschreibt die Augenzahl beim einmaligen Würfeln. Bestimme
  \( P(X<4) \) und den Erwartungswert \( E(X) \).
- **(AB II)** Erläutere die Bedeutung des Erwartungswerts. Beurteile, ob das Spiel „Einsatz \( 1\,€ \);
  Gewinn bei Augenzahl \( 2 \): \( 3\,€ \); sonst geht der Einsatz verloren" fair ist. Bestimme die
  Wahrscheinlichkeit beim zweimaligen Würfeln für die Augensumme \( 8 \). Beschreibe ein
  Zufallsexperiment mit diesem Würfel, das eine Bernoulli-Kette darstellt.
- **(AB III)** Beurteile die Aussage „Der Erwartungswert einer Zufallsgröße ist der Wert, der am
  wahrscheinlichsten ist." Beurteile außerdem: Beim \( 100 \)-maligen Würfeln fallen sechs Sechser —
  „Ich zweifle, dass der Würfel fair ist."

</div>

> **Vorab, in einem Satz, eine Annahme für die ganze Aufgabe:** Wir gehen von einem **fairen Würfel**
> (Laplace-Würfel) aus — der Körper ist ein gleichmäßiger Würfel, sodass **jede der sechs Flächen mit
> Wahrscheinlichkeit \( \tfrac16 \)** oben landet. Wichtig ist nur die *Fläche*, nicht die *Zahl*
> darauf. Weil zwei Flächen eine „\( 2 \)" zeigen, ist \( P(X=2)=\tfrac{2}{6} \). (Im letzten Aspekt
> wird genau diese Fairness-Annahme dann hinterfragt.) Alle Grundbegriffe stehen kompakt im
> [Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html).

So sieht das Würfelnetz aus (saubere Nachzeichnung), daneben die daraus folgende Verteilung von \( X \):

<div class="graph-row">
<figure>
<svg viewBox="0 0 320 320" role="img" aria-label="Würfelnetz mit den Augenzahlen 1, 2, 2, 3, 4 und 6" style="width:100%;max-width:280px;height:auto;background:#fbf7ef;border-radius:8px">
  <g fill="#3a5a9c" fill-opacity="0.06" stroke="#3a5a9c" stroke-width="1.8">
    <rect x="120" y="40" width="60" height="60"/>
    <rect x="60"  y="100" width="60" height="60"/>
    <rect x="120" y="100" width="60" height="60"/>
    <rect x="180" y="100" width="60" height="60"/>
    <rect x="120" y="160" width="60" height="60"/>
    <rect x="120" y="220" width="60" height="60"/>
  </g>
  <g font-size="30" fill="#26324a" text-anchor="middle" font-family="Georgia, serif">
    <text x="150" y="80">1</text>
    <text x="90"  y="140">2</text>
    <text x="150" y="140">2</text>
    <text x="210" y="140">3</text>
    <text x="150" y="200">4</text>
    <text x="150" y="260">6</text>
  </g>
</svg>
<figcaption>Würfelnetz: Flächen \( 1, 2, 2, 3, 4, 6 \).</figcaption>
</figure>
<figure>
<svg viewBox="0 0 480 300" role="img" aria-label="Wahrscheinlichkeitsverteilung der Augenzahl X mit Erwartungswert 3" style="width:100%;max-width:480px;height:auto;background:#fbf7ef;border-radius:8px">
  <line x1="55" y1="245" x2="455" y2="245" stroke="#7a7163" stroke-width="1.5"/>
  <line x1="55" y1="245" x2="55" y2="40" stroke="#7a7163" stroke-width="1.5"/>
  <text x="48" y="189" font-size="12" fill="#7a7163" text-anchor="end">1/6</text>
  <text x="48" y="129" font-size="12" fill="#7a7163" text-anchor="end">2/6</text>
  <line x1="51" y1="185" x2="55" y2="185" stroke="#7a7163"/>
  <line x1="51" y1="125" x2="55" y2="125" stroke="#7a7163"/>
  <g stroke="#3a5a9c" stroke-width="1.5">
    <rect x="80"  y="185" width="44" height="60"  fill="#3a5a9c" fill-opacity="0.12"/>
    <rect x="145" y="125" width="44" height="120" fill="#d98324" fill-opacity="0.24"/>
    <rect x="210" y="185" width="44" height="60"  fill="#3a5a9c" fill-opacity="0.12"/>
    <rect x="275" y="185" width="44" height="60"  fill="#3a5a9c" fill-opacity="0.12"/>
    <rect x="340" y="244" width="44" height="1"   fill="#3a5a9c" fill-opacity="0.12"/>
    <rect x="405" y="185" width="44" height="60"  fill="#3a5a9c" fill-opacity="0.12"/>
  </g>
  <g font-size="14" fill="#26324a" text-anchor="middle">
    <text x="102" y="263">1</text>
    <text x="167" y="263">2</text>
    <text x="232" y="263">3</text>
    <text x="297" y="263">4</text>
    <text x="362" y="263">5</text>
    <text x="427" y="263">6</text>
  </g>
  <text x="255" y="287" font-size="12" fill="#7a7163" text-anchor="middle">Augenzahl x</text>
  <line x1="232" y1="40" x2="232" y2="245" stroke="#b03a2e" stroke-width="1.6" stroke-dasharray="4 3"/>
  <text x="238" y="52" font-size="12" fill="#b03a2e">E(X) = 3 (Schwerpunkt)</text>
  <text x="167" y="116" font-size="11" fill="#a05a10" text-anchor="middle">am häufigsten</text>
</svg>
<figcaption>Verteilung von \( X \): Die „\( 2 \)" ist mit \( \tfrac{2}{6} \) am wahrscheinlichsten
(höchster Balken bei \( 2 \)), der Erwartungswert \( E(X)=3 \) ist der Schwerpunkt (rote Linie) — die
beiden Stellen sind verschieden. Bei \( 5 \) gibt es keinen Balken.</figcaption>
</figure>
</div>

### AB I — \( P(X<4) \) und Erwartungswert

<span class="tag tag-ok">AB I — Grundkompetenz</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

Zuerst die **Verteilung** von \( X \) (jede Fläche \( \tfrac16 \), die „\( 2 \)" zweimal):

\[ P(X{=}1)=\tfrac16,\quad P(X{=}2)=\tfrac26,\quad P(X{=}3)=\tfrac16,\quad P(X{=}4)=\tfrac16,\quad
   P(X{=}6)=\tfrac16,\quad P(X{=}5)=0. \]

**\( P(X<4) \).** „Kleiner als \( 4 \)" meint die Augenzahlen \( 1, 2, 3 \). Diese
Wahrscheinlichkeiten addieren sich:

\[ P(X<4) = P(X{=}1)+P(X{=}2)+P(X{=}3) = \tfrac16+\tfrac26+\tfrac16 = \tfrac46 = \tfrac23 \approx 0{,}67. \]

**Erwartungswert \( E(X) \).** Jeden Wert mit seiner Wahrscheinlichkeit multiplizieren und alles
aufaddieren — das ist hier dasselbe wie „alle sechs Flächenzahlen mitteln":

\[ E(X) = \frac{1+2+2+3+4+6}{6} = \frac{18}{6} = 3. \]

<details><summary>Haltung dahinter: Was ist eine Zufallsgröße, eine Wahrscheinlichkeit, ein Erwartungswert? (ganz von vorn)</summary>

**Zufallsgröße \( X \).** Eine **Zufallsgröße** ist eine Zahl, die vom Zufall abhängt. Hier ist \( X \)
die Augenzahl, die nach **einem** Wurf oben liegt. Vor dem Wurf weiß man sie nicht — man kennt aber die
**Wahrscheinlichkeiten** der möglichen Werte.

**Wahrscheinlichkeit.** Eine **Wahrscheinlichkeit** ist ein Maß zwischen \( 0 \) (unmöglich) und
\( 1 \) (sicher) dafür, wie oft etwas „auf lange Sicht" eintritt. Bei einem fairen Würfel hat jede der
\( 6 \) Flächen die Wahrscheinlichkeit \( \tfrac16 \). Weil zwei Flächen die „\( 2 \)" zeigen, ist die
Augenzahl \( 2 \) **doppelt so wahrscheinlich**: \( P(X{=}2)=\tfrac{2}{6} \). Die „\( 5 \)" steht auf
keiner Fläche, also \( P(X{=}5)=0 \).

**\( P(X<4) \).** Das Zeichen „\( < \)" heißt **echt kleiner**. \( X<4 \) trifft auf \( 1, 2, 3 \) zu —
die \( 4 \) **nicht** (dafür bräuchte es „\( \le \)"). Mehrere getrennte Möglichkeiten, von denen eine
eintreten soll, **addiert** man.

**Erwartungswert.** Der **Erwartungswert** \( E(X) \) ist der **Durchschnittswert auf lange Sicht** —
was im Mittel pro Wurf herauskommt, wenn man sehr oft würfelt. Man berechnet ihn als „**Wert mal
Wahrscheinlichkeit**, aufsummiert". Häufige Werte zählen stärker. (Werkzeug:
[Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html#erwartungswert).)

<details><summary>Ganz langsam (mit Zahlen)</summary>

\[ E(X) = 1\cdot\tfrac16 + 2\cdot\tfrac26 + 3\cdot\tfrac16 + 4\cdot\tfrac16 + 6\cdot\tfrac16. \]

Zähler einzeln: \( 1\cdot 1=1 \); \( 2\cdot 2=4 \) (weil die \( 2 \) doppelt zählt); \( 3\cdot 1=3 \);
\( 4\cdot 1=4 \); \( 6\cdot 1=6 \). Summe der Zähler: \( 1+4+3+4+6 = 18 \). Geteilt durch \( 6 \):
\( \tfrac{18}{6}=3 \). Also \( E(X)=3 \).

</details>

<details><summary>Typische Falle</summary>

- **\( P(X<4) \) zu groß**, weil man die \( 4 \) mitnimmt. „\( <4 \)" schließt die \( 4 \) **aus**.
- **Die doppelte \( 2 \) übersehen.** Wer mit nur „einer \( 2 \)" rechnet, bekommt bei \( P(X<4) \) und
  bei \( E(X) \) zu kleine Werte.
- **Falsch gemittelt:** Den Durchschnitt der *verschiedenen* Zahlen \( \tfrac{1+2+3+4+6}{5}=3{,}2 \) zu
  nehmen, ist falsch — die \( 2 \) ist wahrscheinlicher und muss doppelt eingehen. Richtig:
  über alle **sechs Flächen** mitteln \( \Rightarrow 3 \).

</details>
</details>
</details>

### AB II — Bedeutung des Erwartungswerts, faires Spiel, Augensumme 8, Bernoulli-Kette

<span class="tag tag-warn">AB II — Standardanforderung</span>

<details><summary>Lösung Schritt für Schritt anzeigen</summary>

**(1) Bedeutung des Erwartungswerts.** \( E(X)=3 \) heißt: Würfelt man **sehr oft** mit diesem Würfel
und bildet den Mittelwert aller geworfenen Augenzahlen, so pendelt sich dieser Mittelwert bei
**ungefähr \( 3 \)** ein. Der Erwartungswert ist also der **langfristige Durchschnitt pro Wurf** und
zugleich der **Schwerpunkt** (Balancepunkt) der Verteilung.

**(2) Ist das Spiel fair?** Regel: Einsatz \( 1\,€ \) (immer bezahlt); bei Augenzahl \( 2 \) bekommt man
\( 3\,€ \) ausgezahlt, sonst ist der Einsatz weg. Wir betrachten den **Reingewinn** \( G \) (Auszahlung
minus Einsatz):

- Augenzahl \( 2 \) (Wahrscheinlichkeit \( \tfrac26=\tfrac13 \)): Auszahlung \( 3\,€ \), also Reingewinn
  \( 3-1 = +2\,€ \).
- sonst (Wahrscheinlichkeit \( \tfrac46=\tfrac23 \)): Einsatz verloren, Reingewinn \( -1\,€ \).

\[ E(G) = \tfrac13\cdot(+2) + \tfrac23\cdot(-1) = \tfrac{2}{3} - \tfrac{2}{3} = 0. \]

Der erwartete Reingewinn ist \( 0\,€ \) — das Spiel ist **fair**.

**(3) Augensumme \( 8 \) beim zweimaligen Würfeln.** Beide Würfe sind **unabhängig**. Gesucht sind alle
Wege, wie die beiden Augenzahlen zusammen \( 8 \) ergeben: \( 2{+}6 \), \( 6{+}2 \) und \( 4{+}4 \).
Wahrscheinlichkeiten der einzelnen Würfe einsetzen (mit \( P(2)=\tfrac26 \), \( P(6)=\tfrac16 \),
\( P(4)=\tfrac16 \)):

\[ P(\text{Summe }8) = \underbrace{\tfrac26\cdot\tfrac16}_{2,\ \text{dann}\ 6}
   + \underbrace{\tfrac16\cdot\tfrac26}_{6,\ \text{dann}\ 2}
   + \underbrace{\tfrac16\cdot\tfrac16}_{4,\ \text{dann}\ 4}
   = \tfrac{2}{36}+\tfrac{2}{36}+\tfrac{1}{36} = \tfrac{5}{36} \approx 0{,}14. \]

**(4) Ein Zufallsexperiment, das eine Bernoulli-Kette ist.** Zum Beispiel: **Würfle den Würfel
\( 10 \)-mal und notiere jedes Mal nur, ob eine „\( 2 \)" fällt (Treffer) oder nicht (Niete).** Jeder
Wurf hat genau zwei Ausgänge, die Treffer-Wahrscheinlichkeit ist immer \( p=\tfrac13 \), und die Würfe
beeinflussen sich nicht. Das ist eine **Bernoulli-Kette** der Länge \( 10 \); die Trefferzahl ist
\( B(10;\,\tfrac13) \)-verteilt.

<details><summary>Haltung dahinter: Was heißt „Bedeutung" des Erwartungswerts wirklich?</summary>

Der Erwartungswert ist **kein** Versprechen für den einzelnen Wurf. \( E(X)=3 \) bedeutet **nicht**,
dass man „meistens eine \( 3 \) würfelt". Es ist ein **Durchschnitt über sehr viele Würfe**: Trägt man
nach jedem Wurf den bisherigen Mittelwert auf, so nähert er sich mit wachsender Wurfzahl der \( 3 \).
Bild: der **Schwerpunkt** der Balken — die Stelle, an der die Verteilung „im Gleichgewicht" wäre, wenn
die Balken Gewichte auf einem Brett wären.

</details>

<details><summary>Haltung dahinter: Was bedeutet „faires Spiel", und warum der Reingewinn? (ganz von vorn)</summary>

**Fair** heißt: Auf lange Sicht gewinnt **keine Seite** im Mittel — der erwartete Reingewinn der
spielenden Person ist \( 0 \). Ist er positiv, lohnt sich das Spiel für die spielende Person; ist er
negativ, verliert sie im Schnitt.

Wichtig ist, den **Reingewinn** zu betrachten, nicht die Auszahlung allein. Der Einsatz von \( 1\,€ \)
wird **in jedem** Fall bezahlt. Gewinnt man, bekommt man \( 3\,€ \) zurück — der Reingewinn ist also
\( 3-1=+2\,€ \), nicht \( +3\,€ \). Verliert man, ist der Einsatz weg: \( -1\,€ \).

<details><summary>Ganz langsam (mit Zahlen)</summary>

- Wahrscheinlichkeit für „\( 2 \)": Es gibt **zwei** Flächen mit \( 2 \), also \( \tfrac26=\tfrac13 \).
- Reingewinn dabei: \( +2\,€ \).
- Wahrscheinlichkeit für „keine \( 2 \)": \( 1-\tfrac13 = \tfrac23 \). Reingewinn: \( -1\,€ \).
- \( E(G) = \tfrac13\cdot 2 + \tfrac23\cdot(-1) = \tfrac{2}{3} - \tfrac{2}{3} = 0 \).

Genau null — das Spiel ist fair. (Hinweis zur Lesart: „Gewinn \( 3\,€ \)" ist hier als **Auszahlung**
von \( 3\,€ \) verstanden. Dass exakt \( 0 \) herauskommt, bestätigt diese Lesart — die Zahlen sind
ersichtlich so gewählt.)

</details>
</details>

<details><summary>Haltung dahinter: Augensumme — warum mal, warum die zwei Reihenfolgen? (ganz von vorn)</summary>

**Augensumme** ist die Summe der beiden geworfenen Zahlen. Damit \( 8 \) herauskommt, müssen die beiden
Würfe zusammenpassen.

**Unabhängigkeit → multiplizieren.** Die zwei Würfe beeinflussen sich nicht. Für „erst dies, **dann**
das" multipliziert man die Einzelwahrscheinlichkeiten — wie ein zweistufiger Baum, bei dem man die
Wahrscheinlichkeiten entlang des Astes malnimmt.

**Verschiedene Möglichkeiten → addieren.** Es gibt mehrere Wege zur \( 8 \), und sie schließen sich
gegenseitig aus. Verschiedene Wege werden **addiert**. Welche Wege gibt es?

- \( 2 \) und \( 6 \): einmal „erst \( 2 \), dann \( 6 \)", einmal „erst \( 6 \), dann \( 2 \)" — das
  sind **zwei** verschiedene Reihenfolgen.
- \( 4 \) und \( 4 \): nur **eine** Möglichkeit (beide Würfe \( 4 \)).

\( 5{+}3 \) oder \( 7{+}1 \) gehen nicht (eine \( 5 \) oder \( 7 \) gibt es nicht), \( 6{+}2 \) ist
schon gezählt.

<details><summary>Ganz langsam (mit Zahlen)</summary>

\[ \tfrac26\cdot\tfrac16 = \tfrac{2}{36};\qquad \tfrac16\cdot\tfrac26 = \tfrac{2}{36};\qquad
   \tfrac16\cdot\tfrac16 = \tfrac{1}{36}. \]

Summe: \( \tfrac{2}{36}+\tfrac{2}{36}+\tfrac{1}{36} = \tfrac{5}{36} \approx 0{,}14 \).

Gleicher Weg „von Hand": Beim zweimaligen Würfeln gibt es \( 6\cdot 6 = 36 \) gleich wahrscheinliche
Flächen-Paare. Günstig sind \( (2{,}6),(2{,}6),(6{,}2),(6{,}2),(4{,}4) \) — die zwei \( 2 \)-Flächen
erzeugen die Doppelungen, macht \( 5 \) günstige von \( 36 \): \( \tfrac{5}{36} \).

</details>

<details><summary>Typische Falle</summary>

- **Nur eine Reihenfolge** zählen (\( 2{+}6 \) ohne \( 6{+}2 \)) — dann fehlt die Hälfte.
- **Die doppelte \( 2 \) vergessen** — \( P(2) \) ist \( \tfrac26 \), nicht \( \tfrac16 \).
- **Mit einer „\( 5 \)" rechnen** (\( 5{+}3 \)) — die gibt es auf diesem Würfel nicht.

</details>
</details>

<details><summary>Haltung dahinter: Was macht etwas zu einer „Bernoulli-Kette"? (ganz von vorn)</summary>

Ein **Bernoulli-Versuch** ist ein Zufallsversuch mit **genau zwei** Ausgängen, die man **Treffer** und
**Niete** nennt, mit einer festen Treffer-Wahrscheinlichkeit \( p \). Eine **Bernoulli-Kette** ist
derselbe Versuch **mehrfach hintereinander**, wobei

- die Wiederholungen **unabhängig** sind (eine beeinflusst die nächste nicht) und
- \( p \) **bei jedem Mal gleich** bleibt.

Unser Würfel hat eigentlich sechs Ausgänge — für eine Bernoulli-Kette muss man ihn auf **zwei** Ausgänge
„eindampfen", indem man die Würfe in zwei Gruppen einteilt. Beispiele:

- Treffer = „eine \( 2 \)", Niete = „keine \( 2 \)" \( \Rightarrow p=\tfrac13 \).
- Treffer = „gerade Zahl" (\( 2, 2, 4, 6 \)), Niete = „ungerade" (\( 1, 3 \)) \( \Rightarrow p=\tfrac46=\tfrac23 \).
- Treffer = „eine \( 6 \)", Niete = „keine \( 6 \)" \( \Rightarrow p=\tfrac16 \).

Würfelt man dann \( n \)-mal und zählt die Treffer, ist man bei einer Bernoulli-Kette (Trefferzahl
binomialverteilt). (Mehr: [Werkzeugkasten Stochastik](konv-91-werkzeugkasten-stochastik.html#bernoulli-kette).)

</details>
</details>

### AB III — zwei Aussagen beurteilen

<span class="tag tag-warn">AB III — vertiefte Vernetzung</span>

<details><summary>Lösung / Beurteilung anzeigen</summary>

**Aussage 1: „Der Erwartungswert ist der Wert, der am wahrscheinlichsten ist."** Diese Aussage ist
**falsch**. Der Erwartungswert ist der **langfristige Durchschnitt**, nicht der häufigste Wert (das
wäre der **Modus**). Gegenbeispiel mit unserem Würfel: Der wahrscheinlichste Wert ist die **\( 2 \)**
(mit \( \tfrac26 \) der höchste Balken), der Erwartungswert ist aber \( E(X)=3 \), und ausgerechnet
\( P(X{=}3)=\tfrac16 \) ist klein. Erwartungswert und „wahrscheinlichster Wert" sind hier also
**verschieden** — die Aussage stimmt nicht.

**Aussage 2: „Sechs Sechser bei \( 100 \) Würfen — ich zweifle an der Fairness."** Diese Skepsis ist
**berechtigt**. Bei einem fairen Würfel zeigt genau eine Fläche die \( 6 \), also \( p=\tfrac16 \). Die
Anzahl \( Y \) der Sechser bei \( 100 \) Würfen ist \( B(100;\,\tfrac16) \)-verteilt mit

\[ \mu = n\,p = 100\cdot\tfrac16 \approx 16{,}7, \qquad
   \sigma = \sqrt{n\,p\,(1-p)} = \sqrt{100\cdot\tfrac16\cdot\tfrac56} = \sqrt{\tfrac{500}{36}} \approx 3{,}7. \]

Erwartet wären also rund \( 17 \) Sechser. Beobachtet wurden nur **\( 6 \)** — das liegt weit darunter.
Mit der **\( 2\sigma \)-Regel** (etwa \( 95\,\% \) der Werte liegen in \( [\mu-2\sigma;\ \mu+2\sigma] \)):

\[ [\,\mu-2\sigma;\ \mu+2\sigma\,] \approx [\,16{,}7 - 7{,}5;\ 16{,}7 + 7{,}5\,] = [\,9{,}2;\ 24{,}1\,]. \]

\( 6 \) liegt **außerhalb** dieses Bereichs (sogar fast \( 3\sigma \) unter dem Erwartungswert). Ein so
kleiner Wert ist für einen fairen Würfel **sehr unwahrscheinlich**. Der Zweifel an der Fairness ist
damit statistisch gut begründet — wobei ein seltenes Ergebnis kein **Beweis** ist, sondern ein
**starker Hinweis**.

<div class="jxgbox" id="jxg-k5-binom" style="width:100%;max-width:520px;aspect-ratio:3/2"></div>
<script>(function(){var m=100/6,s=Math.sqrt(500/36);var dn=function(x){return 1/(s*Math.sqrt(2*Math.PI))*Math.exp(-((x-m)*(x-m))/(2*s*s));};var b=JXG.JSXGraph.initBoard('jxg-k5-binom',{boundingbox:[-2,0.14,36,-0.028],axis:true,showCopyright:false,showNavigation:false});var c=b.create('functiongraph',[dn,0,36],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('integral',[[m-2*s,m+2*s],c],{fillColor:'#3a8a5a',fillOpacity:0.12,withLabel:false,curveLeft:{visible:false,withLabel:false},curveRight:{visible:false,withLabel:false},baseLeft:{visible:false},baseRight:{visible:false}});b.create('segment',[[m,0],[m,dn(m)]],{strokeColor:'#3a5a9c',strokeWidth:1.4,dash:2});b.create('segment',[[m-2*s,0],[m-2*s,dn(m-2*s)]],{strokeColor:'#3a8a5a',strokeWidth:1.4,dash:3});b.create('segment',[[m+2*s,0],[m+2*s,dn(m+2*s)]],{strokeColor:'#3a8a5a',strokeWidth:1.4,dash:3});b.create('segment',[[6,0],[6,0.106]],{strokeColor:'#b03a2e',strokeWidth:2.4});b.create('text',[6.4,0.126,'beobachtet: 6'],{fontSize:12,strokeColor:'#b03a2e'});b.create('text',[17.4,0.118,'μ ≈ 16,7'],{fontSize:12,strokeColor:'#26324a'});b.create('text',[9.4,0.055,'μ−2σ ≈ 9,2'],{fontSize:11,strokeColor:'#3a8a5a'});b.create('text',[24.4,0.055,'μ+2σ ≈ 24,1'],{fontSize:11,strokeColor:'#3a8a5a'});})();</script>

<figcaption style="font-size:0.9em;color:#5a5346">Anzahl der Sechser bei \( 100 \) Würfen, angenähert
durch eine Glockenkurve (Erwartungswert \( \mu\approx 16{,}7 \)). Der grüne Bereich ist
\( [\mu-2\sigma;\ \mu+2\sigma] \) — dort liegen rund \( 95\,\% \) der Werte. Die Beobachtung \( 6 \)
(rot) liegt klar links davon.</figcaption>

<details><summary>Haltung dahinter: Erwartungswert vs. wahrscheinlichster Wert — der Unterschied</summary>

Zwei verschiedene „typische Werte" einer Verteilung:
- **Modus** = der **häufigste** Wert (der höchste Balken). Hier: die \( 2 \).
- **Erwartungswert** = der **Durchschnitt** auf lange Sicht (der Schwerpunkt). Hier: \( 3 \).

Die beiden müssen nicht zusammenfallen. Noch deutlicher beim normalen Würfel \( 1\)–\(6 \): Dort sind
alle Werte gleich häufig (es gibt keinen einzelnen „wahrscheinlichsten"), aber
\( E(X)=\tfrac{1+2+3+4+5+6}{6}=3{,}5 \) — und eine „\( 3{,}5 \)" kann man **gar nicht würfeln**. Ein
Erwartungswert muss also nicht einmal ein **möglicher** Wert sein. Das widerlegt die Aussage endgültig.

</details>

<details><summary>Haltung dahinter: Erwartung, Streuung und die \( 2\sigma \)-Regel (ganz von vorn)</summary>

**Erwartete Trefferzahl.** Bei \( 100 \) Würfen und \( p=\tfrac16 \) erwartet man im Mittel
\( 100\cdot\tfrac16\approx 16{,}7 \) Sechser. Das ist die „normale" Größenordnung.

**Streuung \( \sigma \).** Natürlich kommt selten **exakt** \( 16{,}7 \) heraus — die Trefferzahl
schwankt um diesen Wert. Wie stark sie typischerweise schwankt, misst die **Standardabweichung**
\( \sigma=\sqrt{n\,p\,(1-p)} \). Hier \( \sigma=\sqrt{100\cdot\tfrac16\cdot\tfrac56}=\sqrt{\tfrac{500}{36}}\approx 3{,}7 \).
Eine Abweichung von ein, zwei \( \sigma \) ist normal.

**\( 2\sigma \)-Regel.** Als Faustregel liegen rund \( 95\,\% \) aller Ergebnisse im Bereich
\( \mu\pm 2\sigma \), hier \( [\,9{,}2;\ 24{,}1\,] \). Werte **außerhalb** sind selten (zusammen rund
\( 5\,\% \)). \( 6 \) liegt außerhalb — und zwar deutlich. Für einen fairen Würfel wäre „nur \( 6 \)
Sechser" also ein ungewöhnlich seltenes Ergebnis; deshalb ist der Zweifel an der Fairness berechtigt.

<details><summary>Ganz langsam (mit Zahlen)</summary>

- \( \mu = 100\cdot\tfrac16 = \tfrac{100}{6} \approx 16{,}67 \).
- \( n\,p\,(1-p) = 100\cdot\tfrac16\cdot\tfrac56 = \tfrac{500}{36} \approx 13{,}9 \), also
  \( \sigma=\sqrt{13{,}9}\approx 3{,}7 \).
- \( 2\sigma \approx 7{,}5 \); Bereich \( [16{,}7-7{,}5;\ 16{,}7+7{,}5] = [9{,}2;\ 24{,}1] \).
- Abstand der Beobachtung: \( 16{,}7-6 = 10{,}7 \), das sind \( \tfrac{10{,}7}{3{,}7}\approx 2{,}9 \)
  Standardabweichungen unter dem Erwartungswert. So weit weg ist selten.

</details>

<details><summary>Typische Falle</summary>

- **„Jede Abweichung von \( 16{,}7 \) bedeutet unfair."** Falsch — die Trefferzahl schwankt von Natur
  aus um \( \sigma\approx 3{,}7 \). Erst eine Abweichung **deutlich über \( 2\sigma \)** ist
  auffällig.
- **„Damit ist bewiesen, dass der Würfel unfair ist."** Auch falsch — es ist ein **starker Hinweis**,
  keine Gewissheit. Seltene Ergebnisse kommen auch bei fairen Würfeln vor, nur eben selten.

</details>
</details>
</details>

---

## Prüfer-Leitfaden (für die abfragende Person)

Hier steht je Teilaufgabe, **was eine gute Antwort enthält** und **welche Rückfrage** du stellen
kannst. Du musst nichts selbst rechnen — achte auf die genannten Stichworte.

<details><summary>Leitfaden Teil 1 (Analysis) aufklappen</summary>

- **a) Ablesen.** Erwartet: \( f'(2) \) als **Steigung** über eine Tangente \( \approx -1 \); das
  Integral als **Fläche** über **Kästchenzählen** \( \approx 19\cdot 0{,}25 = 4{,}75 \). *Rückfrage:*
  „Was ist der Unterschied zwischen \( f(2) \) und \( f'(2) \)?" *Rote Flagge:* Kästchen mit
  Flächeninhalt \( 1 \) gezählt (statt \( 0{,}25 \)).
- **b) Höhe.** Erwartet: Das Integral ist der **Zuwachs** in cm; Höhe \( = 20 + 4{,}75 = 24{,}75 \) cm.
  *Rückfrage:* „Warum darf man die Fläche unter der Rate einfach zur Starthöhe addieren?" (Antwort:
  Rate mal Zeit ergibt Länge — Tacho/Strecke.)
- **c) Stärkste Abnahme.** Erwartet: \( f''(t)=8(t-2)e^{-t} \), Ansatz \( f''=0 \Rightarrow t=2 \), kurz
  begründet als **Wendepunkt / Minimum von \( f' \)**. *Rote Flagge:* \( f'=0 \) gesetzt (das liefert
  \( t=1 \), das Maximum der Rate). *Rückfrage:* „Welche Ableitung beschreibt, wie stark die Rate
  *fällt*?"
- **d) Fragestellung + Grafik.** Erwartet: sinnvolle Frage wie „In welchem \( 1 \)-Tages-Zeitraum
  wächst die Pflanze um \( 2{,}5 \) cm?"; grafisch ein **Streifen der Breite \( 1 \)**, verschoben bis
  die Fläche \( 2{,}5 \) ist, **linker Rand = Lösung**. *Hinweis für dich:* Ein **beschriebenes
  Verfahren** ist hier die volle Antwort; einen exakten Zahlenwert braucht es nicht.

</details>

<details><summary>Leitfaden Teil 2 (Stochastik) aufklappen</summary>

- **\( P(X<4) \), \( E(X) \).** Erwartet: \( P(X<4)=\tfrac46=\tfrac23 \) (Werte \( 1, 2, 3 \), die
  \( 2 \) doppelt); \( E(X)=\tfrac{1+2+2+3+4+6}{6}=3 \). *Rückfrage:* „Warum zählt die \( 2 \)
  doppelt?" *Rote Flagge:* die \( 4 \) bei \( P(X<4) \) mitgenommen.
- **Bedeutung \( E \) / faires Spiel.** Erwartet: \( E(X) \) = **langfristiger Durchschnitt**; Spiel
  über **erwarteten Reingewinn** \( E(G)=\tfrac13\cdot 2 + \tfrac23\cdot(-1) = 0 \Rightarrow \) **fair**.
  *Rückfrage:* „Wie hoch ist der Reingewinn, wenn man gewinnt — \( 3\,€ \) oder \( 2\,€ \)?" (Antwort:
  \( 2\,€ \), der Einsatz ist schon bezahlt.)
- **Augensumme \( 8 \).** Erwartet: \( 2{+}6,\ 6{+}2,\ 4{+}4 \); \( P=\tfrac{5}{36} \). *Rote Flagge:*
  nur eine Reihenfolge gezählt oder \( P(2)=\tfrac16 \) angesetzt. *Rückfrage:* „Wie viele Möglichkeiten
  gibt es, mit zwei Würfen auf \( 8 \) zu kommen?"
- **Bernoulli-Kette.** Erwartet: Versuch auf **zwei Ausgänge** reduziert (z. B. „\( 2 \) / keine
  \( 2 \)"), \( n \)-mal **unabhängig** mit **festem \( p \)**. *Rückfrage:* „Was ist hier der Treffer,
  und wie groß ist \( p \)?"
- **AB III, Aussage 1.** Erwartet: **falsch** — Erwartungswert (\( 3 \)) ist nicht der häufigste Wert
  (\( 2 \)); ein E-Wert muss nicht einmal vorkommen können. *Rückfrage:* „Welche Augenzahl ist am
  wahrscheinlichsten — und wie groß ist \( E(X) \)?"
- **AB III, Aussage 2.** Erwartet: erwartete Sechser \( \approx 17 \), \( \sigma\approx 3{,}7 \),
  \( 6 \) liegt **außerhalb** \( [\,9{,}2;\ 24{,}1\,] \Rightarrow \) Zweifel **berechtigt** (Hinweis, kein
  Beweis). *Rückfrage:* „Wie viele Sechser würde man bei einem fairen Würfel erwarten?"

</details>

## Selbstcheck: Kannst du es mündlich erklären?

Sprich diese Punkte einmal **frei und laut** durch, ohne in die Lösung zu schauen:

- Wie liest du \( f'(2) \) und das Integral \( \int_0^2 f\,dt \) aus dem Bild ab — und was misst jedes
  von beiden im Sachzusammenhang?
- Warum ist die Fläche unter der Wachstumsrate genau der Höhenzuwachs der Pflanze?
- Welche Ableitung setzt du null, um die **stärkste Abnahme** der Wachstumsrate zu finden, und warum?
- Warum zählt die Augenzahl \( 2 \) bei diesem Würfel doppelt, und wie wirkt sich das auf \( E(X) \) aus?
- Woran erkennst du, dass das Spiel fair ist — und warum ist der Gewinnfall \( +2\,€ \) und nicht \( +3\,€ \)?
- Warum sind sechs Sechser bei \( 100 \) Würfen ein guter Grund, an der Fairness zu zweifeln?
