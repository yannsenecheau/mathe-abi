# Funktionsuntersuchung

Eine **Funktionsuntersuchung** (auch „Kurvendiskussion") ist das Herzstück der Analysis-Prüfung.
Du bekommst eine Funktion und sollst ihren Graphen vollständig verstehen, ohne ihn vorher zu
sehen: Wo schneidet er die Achsen? Ist er symmetrisch? Wo steigt und fällt er? Wo sind seine Spitzen?
Wo ändert sich seine Krümmung? Wenn du das beantwortest, kannst du den Graphen am Ende von Hand
skizzieren.

Die **Haltung dahinter:** Du gehst immer dieselbe Checkliste durch — von der gröbsten Information
(Achsenschnitte, Symmetrie, Randverhalten) zur feinsten (Extrem- und Wendestellen). Jeder Schritt
schränkt das mögliche Aussehen des Graphen weiter ein, bis am Ende nur noch eine Form übrig bleibt.

Wir untersuchen das **ganze Kapitel über dieselbe Funktion**, damit du den roten Faden behältst:

\[ f(x) = x^3 - 3x \]

Das ist eine **ganzrationale Funktion** dritten Grades (ein Polynom). Halte dir schon die drei
Ableitungen bereit — fast jeder Schritt braucht eine davon:

\[ f'(x) = 3x^2 - 3, \qquad f''(x) = 6x, \qquad f'''(x) = 6 \]

<details><summary>Wie komme ich rechnerfrei auf diese Ableitungen?</summary>

Du brauchst nur die **Potenzregel**: Der Exponent wandert als Faktor nach vorn, dann wird der Exponent
um \( 1 \) kleiner. Aus \( x^n \) wird \( n\,x^{n-1} \).

- \( x^3 \) wird zu \( 3x^2 \).
- \( -3x = -3x^1 \) wird zu \( -3 \cdot 1 \cdot x^0 = -3 \) (denn \( x^0 = 1 \)).

Zusammen: \( f'(x) = 3x^2 - 3 \). Genauso noch einmal abgeleitet: aus \( 3x^2 \) wird \( 6x \), aus
\( -3 \) (eine Konstante) wird \( 0 \). Also \( f''(x) = 6x \). Und einmal mehr: \( f'''(x) = 6 \).

<details><summary>Haltung dahinter: Warum verschwinden Konstanten beim Ableiten?</summary>

Die Ableitung misst die **Steigung**, also wie stark sich der Funktionswert ändert. Eine Konstante
ändert sich nie — ihr Graph ist eine waagerechte Linie mit Steigung \( 0 \). Darum fällt jede additive
Konstante beim Ableiten weg. Das ist auch der Grund, warum \( f(x) = x^3 - 3x \) und \( x^3 - 3x + 5 \)
dieselbe Ableitung haben: Der Summand \( +5 \) verschiebt den Graphen nur nach oben, ändert aber an
keiner Stelle die Steigung.

</details>
</details>

## Nullstellen & y-Achsenabschnitt

Die ersten beiden Fragen sind die einfachsten und liefern dir sofort konkrete Punkte des Graphen.

**Der y-Achsenabschnitt** ist der Schnittpunkt mit der senkrechten Achse. Dort ist \( x = 0 \), also
setzt du einfach \( 0 \) ein: \( f(0) = 0^3 - 3 \cdot 0 = 0 \). Der Graph geht durch den Ursprung
\( (0 \mid 0) \). <span class="tag tag-ok">AB I</span>

**Die Nullstellen** sind die Schnittpunkte mit der waagerechten Achse. Dort ist \( f(x) = 0 \). Du
löst also die Gleichung \( x^3 - 3x = 0 \). <span class="tag tag-ok">AB II</span>

<details><summary>Wie löse ich \( x^3 - 3x = 0 \) rechnerfrei?</summary>

Der **erste Reflex bei jeder Gleichung „etwas \( = 0 \)" ist: ausklammern**. Hier steckt in beiden
Summanden ein \( x \):

\[ x^3 - 3x = x \,(x^2 - 3) = 0 \]

Jetzt greift der **Satz vom Nullprodukt**: Ein Produkt ist genau dann null, wenn einer der Faktoren
null ist. Also untersuchst du die Faktoren einzeln:

- \( x = 0 \) — das ist schon eine Nullstelle.
- \( x^2 - 3 = 0 \;\Leftrightarrow\; x^2 = 3 \;\Leftrightarrow\; x = \pm\sqrt{3} \approx \pm 1{,}73 \).

Die drei Nullstellen sind also \( x_1 = -\sqrt{3} \), \( x_2 = 0 \), \( x_3 = +\sqrt{3} \).

<details><summary>Haltung dahinter: Warum ausklammern und nicht „durch x teilen"?</summary>

Verlockend wäre, beide Seiten durch \( x \) zu teilen. **Das ist eine klassische Falle:** Damit würdest
du die Nullstelle \( x = 0 \) verlieren, denn durch \( 0 \) darf man nicht teilen. Ausklammern behält
alle Lösungen. Merke: Beim Lösen von Gleichungen wird **faktorisiert, nicht dividiert** — Division
durch einen Term, der null sein könnte, löscht Lösungen aus.

</details>

<details><summary>Warum hat ein Polynom dritten Grades höchstens drei Nullstellen?</summary>

Eine ganzrationale Funktion vom Grad \( n \) hat höchstens \( n \) Nullstellen. Anschaulich: Jede
Nullstelle entspricht einem Linearfaktor \( (x - x_0) \), und mehr als \( n \) solche Faktoren passen
nicht in ein Polynom vom Grad \( n \), ohne den Grad zu sprengen. Hier ist \( n = 3 \), und wir haben
genau drei gefunden — also alle.

</details>
</details>

## Symmetrie

Bevor du dich in Rechnungen stürzt, lohnt ein Blick auf die **Symmetrie**: Sie halbiert oft die Arbeit,
weil du dann nur eine Hälfte des Graphen untersuchen musst und die andere spiegelst.

Es gibt zwei Standardfälle, die du im Abitur prüfst:

- **Achsensymmetrie zur y-Achse**, wenn \( f(-x) = f(x) \) gilt.
- **Punktsymmetrie zum Ursprung**, wenn \( f(-x) = -f(x) \) gilt.

Für unsere Funktion prüfst du \( f(-x) \): <span class="tag tag-ok">AB II</span>

\[ f(-x) = (-x)^3 - 3(-x) = -x^3 + 3x = -\bigl(x^3 - 3x\bigr) = -f(x) \]

Es kommt \( -f(x) \) heraus — also ist \( f \) **punktsymmetrisch zum Ursprung**. Das passt zu dem,
was du oben schon gesehen hast: Die Nullstellen liegen spiegelbildlich bei \( -\sqrt{3} \) und
\( +\sqrt{3} \), und der Graph geht durch den Ursprung.

<details><summary>Die schnelle Abkürzung bei Polynomen (Exponenten-Trick)</summary>

Bei **ganzrationalen Funktionen** musst du nicht jedes Mal \( f(-x) \) ausrechnen. Du schaust nur auf
die **Exponenten**:

- Kommen **nur gerade** Exponenten vor (inkl. der konstanten \( x^0 \))? → achsensymmetrisch zur
  y-Achse. Beispiel: \( x^4 - 2x^2 + 1 \).
- Kommen **nur ungerade** Exponenten vor? → punktsymmetrisch zum Ursprung. Genau unser Fall:
  \( x^3 - 3x \) hat die Exponenten \( 3 \) und \( 1 \), beide ungerade.
- **Gemischt** (gerade *und* ungerade)? → keine der beiden Standardsymmetrien.

<details><summary>Haltung dahinter: Warum funktioniert der Exponenten-Trick?</summary>

Setzt du \( -x \) ein, dreht ein Term genau dann sein Vorzeichen um, wenn sein Exponent ungerade ist
(z. B. \( (-x)^3 = -x^3 \)); bei geradem Exponenten bleibt das Vorzeichen (z. B. \( (-x)^2 = x^2 \)).
Sind **alle** Exponenten ungerade, dreht **jeder** Term sein Vorzeichen — der ganze Term wird zu
\( -f(x) \). Sind alle gerade, bleibt alles gleich, also \( f(-x) = f(x) \). Der Trick ist nur die
abgekürzte Version der ausführlichen Rechnung oben.

</details>
</details>

## Randverhalten (Verhalten im Unendlichen)

Das **Randverhalten** beantwortet die Frage: Wohin läuft der Graph ganz weit links und ganz weit
rechts? Es legt die grobe „Flugbahn" der Kurve fest. <span class="tag tag-ok">AB II</span>

Bei ganzrationalen Funktionen entscheidet allein der **Term mit dem höchsten Exponenten** — hier
\( x^3 \). Für sehr große \( |x| \) wächst \( x^3 \) so schnell, dass der Summand \( -3x \) daneben
keine Rolle mehr spielt. Also verhält sich \( f \) für die Ränder wie \( x^3 \):

\[ \lim_{x \to +\infty} f(x) = +\infty, \qquad \lim_{x \to -\infty} f(x) = -\infty \]

In Worten: Der Graph kommt links unten herein und läuft rechts oben hinaus.

<details><summary>Warum darf ich die kleineren Terme ignorieren?</summary>

Klammere den höchsten Term aus:

\[ f(x) = x^3 - 3x = x^3\left(1 - \frac{3}{x^2}\right) \]

Für \( x \to \pm\infty \) wird \( \frac{3}{x^2} \) beliebig klein, geht also gegen \( 0 \). Die Klammer
strebt damit gegen \( 1 \), und übrig bleibt das Verhalten von \( x^3 \). Das ist die **Haltung
dahinter**: Im Unendlichen dominiert immer der höchste Term, weil er alle anderen überwächst.

<details><summary>Die Merkregel für ganzrationale Funktionen</summary>

Du musst nur auf zwei Dinge schauen: den **Grad** (gerade oder ungerade) und das **Vorzeichen des
Leitkoeffizienten** (Zahl vor dem höchsten Term).

- **Ungerader Grad** (wie hier, Grad \( 3 \), Leitkoeffizient \( +1 \)): Die beiden Enden laufen in
  **entgegengesetzte** Richtungen — links nach \( -\infty \), rechts nach \( +\infty \). Bei negativem
  Leitkoeffizienten genau andersherum.
- **Gerader Grad** (z. B. eine Parabel \( x^2 \)): Beide Enden laufen in **dieselbe** Richtung — bei
  positivem Leitkoeffizienten beide nach \( +\infty \).

Das passt zur Punktsymmetrie: Ein punktsymmetrischer Graph *muss* an den Enden gegenläufig sein.

</details>
</details>

## Extremstellen & Monotonie

Jetzt zur Feinform. **Monotonie** beschreibt, wo der Graph steigt und wo er fällt;
**Extremstellen** sind die Hoch- und Tiefpunkte, an denen er von Steigen auf Fallen umschlägt (oder
umgekehrt). Beides hängt am Vorzeichen der **ersten Ableitung** \( f' \), denn \( f'(x) \) ist die
Steigung des Graphen an der Stelle \( x \):

- \( f'(x) > 0 \): Graph steigt (streng monoton steigend).
- \( f'(x) < 0 \): Graph fällt (streng monoton fallend).
- \( f'(x) = 0 \): waagerechte Tangente — ein Kandidat für eine Extremstelle.

**Schritt 1 — notwendige Bedingung \( f'(x) = 0 \):** <span class="tag tag-ok">AB II</span>

\[ 3x^2 - 3 = 0 \;\Leftrightarrow\; x^2 = 1 \;\Leftrightarrow\; x = \pm 1 \]

Die Kandidaten sind \( x = -1 \) und \( x = +1 \).

**Schritt 2 — hinreichende Bedingung über \( f'' \):** Ist \( f''(x_0) \neq 0 \) an einer Stelle mit
\( f'(x_0) = 0 \), liegt dort wirklich ein Extrempunkt. Dabei gilt: <span class="tag tag-ok">AB II</span>

- \( f''(x_0) > 0 \) → **Tiefpunkt** (Graph ist dort nach oben gekrümmt, „Tal").
- \( f''(x_0) < 0 \) → **Hochpunkt** (Graph ist dort nach unten gekrümmt, „Berg").

Du setzt die Kandidaten in \( f''(x) = 6x \) ein:

- \( f''(-1) = 6 \cdot (-1) = -6 < 0 \) → **Hochpunkt** bei \( x = -1 \).
- \( f''(+1) = 6 \cdot 1 = +6 > 0 \) → **Tiefpunkt** bei \( x = +1 \).

**Schritt 3 — y-Werte (die vollständigen Punkte):** Du setzt die Stellen in das *ursprüngliche*
\( f \) ein, nicht in eine Ableitung:

\[ f(-1) = (-1)^3 - 3(-1) = -1 + 3 = 2, \qquad f(1) = 1^3 - 3 \cdot 1 = 1 - 3 = -2 \]

Ergebnis: **Hochpunkt** \( H(-1 \mid 2) \) und **Tiefpunkt** \( T(1 \mid -2) \). Auch hier siehst du
die Punktsymmetrie: Die beiden Punkte liegen spiegelbildlich zum Ursprung.

<details><summary>Warum reicht \( f'(x)=0 \) allein nicht — und warum hilft \( f'' \)?</summary>

\( f'(x) = 0 \) bedeutet nur „die Tangente ist waagerecht". Das ist bei jedem Hoch- und Tiefpunkt so,
**aber auch** an einem sogenannten Sattelpunkt (waagerechte Tangente ohne Extremum, der Graph steigt
davor und danach weiter). Darum heißt \( f'(x) = 0 \) **notwendig**: Jede Extremstelle erfüllt es, aber
nicht jede Stelle, die es erfüllt, ist eine Extremstelle.

Die **hinreichende** Bedingung \( f''(x_0) \neq 0 \) schließt die Lücke. \( f''(x_0) > 0 \) heißt: Der
Graph ist dort nach oben gekrümmt — eine waagerechte Tangente in einem nach oben gekrümmten Bogen kann
nur am tiefsten Punkt liegen, also Tiefpunkt. Umgekehrt bei \( f''(x_0) < 0 \): Hochpunkt.

<details><summary>Die Eselsbrücke für Hoch-/Tiefpunkt</summary>

\( f'' \) **positiv = Tiefpunkt**, \( f'' \) **negativ = Hochpunkt** — das fühlt sich oft „verkehrt"
an. Merke es dir über die Form: Ein positives \( f'' \) bedeutet eine nach oben geöffnete Kurve (wie
ein lachender Mund \( \smile \), ein Tal → Tiefpunkt), ein negatives \( f'' \) eine nach unten
geöffnete Kurve (wie ein trauriger Mund \( \frown \), ein Berg → Hochpunkt).

</details>

<details><summary>Was tun, wenn auch \( f''(x_0) = 0 \) ist?</summary>

Dann versagt das \( f'' \)-Kriterium, und du weichst auf das **Vorzeichenwechsel-Kriterium von
\( f' \)** aus: Du prüfst, ob \( f' \) links und rechts von \( x_0 \) das Vorzeichen wechselt. Wechsel
von \( + \) nach \( - \) → Hochpunkt; von \( - \) nach \( + \) → Tiefpunkt; **kein** Wechsel → Sattel-
bzw. Terrassenpunkt. In unserem Beispiel tritt dieser Fall nicht auf, weil \( f''(\pm 1) \neq 0 \) ist.

</details>
</details>

**Monotonie-Tabelle.** Mit den beiden Extremstellen ist die Zahlengerade in drei Bereiche geteilt. In
jedem Bereich behält \( f' \) sein Vorzeichen; du musst nur einen Probewert je Bereich einsetzen.
<span class="tag tag-ok">AB II</span>

| Bereich | Probewert | \( f'(\text{Probe}) = 3x^2 - 3 \) | Vorzeichen | Verhalten |
|---|---|---|---|---|
| \( x < -1 \) | \( x = -2 \) | \( 3 \cdot 4 - 3 = 9 \) | \( + \) | steigt |
| \( -1 < x < 1 \) | \( x = 0 \) | \( 0 - 3 = -3 \) | \( - \) | fällt |
| \( x > 1 \) | \( x = 2 \) | \( 3 \cdot 4 - 3 = 9 \) | \( + \) | steigt |

Der Graph steigt also bis zum Hochpunkt \( H(-1\mid 2) \), fällt dann hinab zum Tiefpunkt
\( T(1\mid -2) \) und steigt danach wieder — genau das typische Auf-und-Ab einer Funktion dritten
Grades.

<details><summary>Haltung dahinter: Warum genügt ein einziger Probewert pro Bereich?</summary>

Zwischen zwei benachbarten Nullstellen von \( f' \) kann \( f' \) das Vorzeichen nicht wechseln — ein
Vorzeichenwechsel bräuchte ja eine Nullstelle dazwischen, und die gibt es per Annahme nicht. Also ist
\( f' \) im ganzen Bereich gleich gepolt, und ein einziger Testwert verrät das Vorzeichen für den
gesamten Abschnitt. Das spart dir viel Rechnerei.

</details>

## Wendestellen & Krümmung

Zuletzt die **Krümmung**: Sie sagt, ob sich der Graph nach oben oder nach unten wölbt. Eine
**Wendestelle** ist der Punkt, an dem die Krümmung umschlägt — der Graph wechselt von einer Linkskurve
in eine Rechtskurve oder umgekehrt. Das hängt am Vorzeichen der **zweiten Ableitung** \( f'' \):

- \( f''(x) > 0 \): **konvex** (linksgekrümmt, nach oben gewölbt \( \smile \)).
- \( f''(x) < 0 \): **konkav** (rechtsgekrümmt, nach unten gewölbt \( \frown \)).
- \( f''(x) = 0 \): möglicher Wechsel — Kandidat für eine Wendestelle.

**Schritt 1 — notwendige Bedingung \( f''(x) = 0 \):** <span class="tag tag-ok">AB II</span>

\[ 6x = 0 \;\Leftrightarrow\; x = 0 \]

**Schritt 2 — hinreichende Bedingung über \( f''' \):** Ist \( f'''(x_0) \neq 0 \), liegt dort
tatsächlich eine Wendestelle. Hier ist \( f'''(x) = 6 \), also konstant: \( f'''(0) = 6 \neq 0 \) —
\( x = 0 \) ist **gesichert** eine Wendestelle. <span class="tag tag-ok">AB II</span>

**Schritt 3 — y-Wert:** \( f(0) = 0^3 - 3 \cdot 0 = 0 \). Der **Wendepunkt** ist \( W(0 \mid 0) \) —
er liegt genau im Ursprung, dem Symmetriezentrum.

<details><summary>Warum \( f''=0 \) notwendig, \( f''' \neq 0 \) hinreichend — die Parallele zu den Extremstellen</summary>

Das Muster ist dasselbe wie eine Stufe tiefer bei den Extremstellen, nur um eine Ableitung
verschoben. Ein **Wendepunkt von \( f \)** ist eine **Extremstelle der Steigung \( f' \)**: An der
Wendestelle ist die Steigung am steilsten (oder am flachsten) und kehrt ihre Änderungsrichtung um.

- Eine Extremstelle von \( f' \) verlangt \( (f')'(x) = f''(x) = 0 \) — das ist die notwendige
  Bedingung.
- Dass es wirklich ein Extremum von \( f' \) ist, sichert \( (f')''(x_0) = f'''(x_0) \neq 0 \).

Darum „erbt" die Wendestellen-Rechnung die Logik der Extremstellen-Rechnung — du gehst einfach mit
\( f'' \) und \( f''' \) genauso vor wie vorher mit \( f' \) und \( f'' \).

<details><summary>Haltung dahinter: die typische Falle bei \( f''=0 \)</summary>

\( f''(x_0) = 0 \) allein genügt **nicht** für eine Wendestelle — es ist nur notwendig. Es könnte auch
eine Stelle sein, an der \( f'' \) die Achse nur berührt, ohne das Vorzeichen zu wechseln (dann keine
Wende). Erst der Nachweis \( f'''(x_0) \neq 0 \) (oder ein Vorzeichenwechsel von \( f'' \)) macht die
Wendestelle sicher. Behaupte nie eine Wendestelle, ohne die hinreichende Bedingung gezeigt zu haben.

</details>
</details>

**Krümmungsverhalten.** Da \( f''(x) = 6x \) nur bei \( x = 0 \) das Vorzeichen wechselt, gibt es zwei
Krümmungsbereiche: <span class="tag tag-ok">AB II</span>

- Für \( x < 0 \): \( f''(x) = 6x < 0 \) → **konkav** (rechtsgekrümmt). Dazu passt der Hochpunkt bei
  \( x = -1 \), der in einem nach unten gewölbten Bogen liegt.
- Für \( x > 0 \): \( f''(x) = 6x > 0 \) → **konvex** (linksgekrümmt). Dazu passt der Tiefpunkt bei
  \( x = +1 \) im nach oben gewölbten Bogen.

## Synthese — den Graphen zeichnen

Jetzt setzt du alle Puzzleteile zu einem Bild zusammen. Die **Haltung dahinter:** Du brauchst den
Graphen nicht zu „erraten" — wenn du die markanten Punkte einträgst und das Randverhalten beachtest,
ergibt sich die Form fast von selbst.

So gehst du in der Prüfung beim Skizzieren vor:

1. **Koordinatensystem** mit passender Skalierung zeichnen (hier reicht \( x \) von etwa \( -3 \) bis
   \( 3 \), \( y \) von \( -4 \) bis \( 4 \)).
2. **Markante Punkte eintragen:** Nullstellen \( (-\sqrt{3}\mid 0) \), \( (0\mid 0) \),
   \( (\sqrt{3}\mid 0) \); Hochpunkt \( H(-1\mid 2) \); Tiefpunkt \( T(1\mid -2) \); Wendepunkt
   \( W(0\mid 0) \).
3. **Randverhalten andeuten:** links unten herein (\( \to -\infty \)), rechts oben hinaus
   (\( \to +\infty \)).
4. **Verbinden, passend zur Monotonie und Krümmung:** steigend bis \( H \), fallend bis \( T \), dann
   wieder steigend; links vom Wendepunkt rechtsgekrümmt, rechts davon linksgekrümmt.

So sieht das Ergebnis aus (die markanten Punkte sind eingezeichnet):

<div class="jxgbox" id="jxg-funktionsuntersuchung" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-funktionsuntersuchung',{boundingbox:[-3,4,3,-4],axis:true,showCopyright:false,showNavigation:false,keepaspectratio:false});b.create('functiongraph',[function(x){return x*x*x-3*x;},-2.6,2.6],{strokeColor:'#3a5a9c',strokeWidth:2.5,name:'f',withLabel:false});b.create('point',[-1,2],{name:'H(-1|2)',size:3,fixed:true,color:'#d98324',label:{offset:[8,8]}});b.create('point',[1,-2],{name:'T(1|-2)',size:3,fixed:true,color:'#d98324',label:{offset:[8,-16]}});b.create('point',[0,0],{name:'W(0|0)',size:3,fixed:true,color:'#2f7d4f',label:{offset:[8,10]}});b.create('point',[Math.sqrt(3),0],{name:'',size:2,fixed:true,color:'#29335c',fillOpacity:0.6});b.create('point',[-Math.sqrt(3),0],{name:'',size:2,fixed:true,color:'#29335c',fillOpacity:0.6});})();</script>

<details><summary>Die vollständige Steckbrief-Tabelle (zum Abhaken in der Prüfung)</summary>

| Untersuchung | Ergebnis für \( f(x) = x^3 - 3x \) |
|---|---|
| y-Achsenabschnitt | \( f(0) = 0 \), Punkt \( (0\mid 0) \) |
| Nullstellen | \( x = -\sqrt{3},\; 0,\; +\sqrt{3} \) |
| Symmetrie | punktsymmetrisch zum Ursprung (nur ungerade Exponenten) |
| Randverhalten | \( x\to-\infty:\, f\to-\infty \); \( x\to+\infty:\, f\to+\infty \) |
| Extremstellen | Hochpunkt \( H(-1\mid 2) \), Tiefpunkt \( T(1\mid -2) \) |
| Monotonie | steigt für \( x<-1 \), fällt für \( -1<x<1 \), steigt für \( x>1 \) |
| Wendestelle | Wendepunkt \( W(0\mid 0) \) |
| Krümmung | konkav für \( x<0 \), konvex für \( x>0 \) |

Diese acht Zeilen sind die komplette Funktionsuntersuchung. Wenn du sie für eine beliebige
ganzrationale Funktion füllen kannst, beherrschst du die Kurvendiskussion.

</details>

<details><summary>Mündlich erklärt: Wie würdest du der Prüferin den Graphen in drei Sätzen beschreiben?</summary>

Übe diese Zusammenfassung laut — genau so etwas wird im Prüfungsgespräch verlangt:

„Der Graph von \( f(x) = x^3 - 3x \) ist punktsymmetrisch zum Ursprung. Er kommt von links unten,
steigt zum Hochpunkt \( H(-1\mid 2) \), fällt durch den Ursprung — der zugleich Wendepunkt ist — hinab
zum Tiefpunkt \( T(1\mid -2) \) und steigt dann nach rechts oben weg. Die Nullstellen liegen bei
\( -\sqrt{3} \), \( 0 \) und \( +\sqrt{3} \)."

Wenn du das frei und sicher sagen kannst, ohne abzulesen, hast du das Kapitel verstanden.

</details>

## Zur Prüfungsrelevanz

Die Funktionsuntersuchung an **ganzrationalen Funktionen** (Polynomen) ist Kernstoff des Basisfachs und
mit hoher Wahrscheinlichkeit prüfungsrelevant. <span class="tag tag-ok">Kernstoff Basisfach</span>

Dieselbe Schrittfolge wendest du später auch auf andere Funktionstypen an. Achtung bei zwei davon:

- Die Funktion \( f(x) = \tfrac{1}{x} \) (gebrochenrationale Funktion) ist
  <span class="tag tag-warn">offiziell Leistungsfach, Basisfach unsicher [97 %] — mit Lehrkraft
  prüfen</span>
- Die **Wurzelfunktion** \( f(x) = \sqrt{x} \) ist im Basisfach
  <span class="tag tag-warn">nicht eigenständig ausgewiesen, Basisfach unsicher [80 %] — mit Lehrkraft
  prüfen</span>

Für beide gilt: Falls sie in deiner Prüfung vorkommen, läuft die Untersuchung nach demselben Schema —
nur dass du zusätzlich auf den **Definitionsbereich** achten musst (bei \( \tfrac{1}{x} \) ist
\( x = 0 \) verboten, bei \( \sqrt{x} \) sind negative \( x \) verboten). Kläre den genauen Umfang
sicherheitshalber mit deiner Lehrkraft.
