# Beispielseite (Pipeline-Test)

Diese Seite ist ein technischer Beweis für die Content-Pipeline: Sie zeigt eine Inline-Formel, eine
abgesetzte Formel und einen interaktiven Funktionsgraphen. Sie wird in der Test-Phase wieder entfernt.

## Formeln

Die Standardparabel ist \( f(x) = x^2 \). Ihre Ableitung ist \( f'(x) = 2x \), die Steigung im Punkt
\( x_0 \) ist also \( 2x_0 \).

Der orientierte Flächeninhalt unter der Parabel zwischen \( 0 \) und \( 1 \) ist:

\[ \int_0^1 x^2 \,dx = \left[ \tfrac{1}{3}x^3 \right]_0^1 = \tfrac{1}{3} \]

<details><summary>Warum ergibt das genau ein Drittel?</summary>

Wir suchen eine Stammfunktion \( F \) mit \( F'(x) = x^2 \). Nach der Potenzregel für Stammfunktionen ist
\( F(x) = \tfrac{1}{3}x^3 \), denn \( F'(x) = 3 \cdot \tfrac{1}{3} x^2 = x^2 \).

<details><summary>Haltung dahinter: Hauptsatz</summary>

Der Hauptsatz der Differential- und Integralrechnung erlaubt, das Integral über die Differenz der
Stammfunktion an den Rändern zu berechnen: \( \int_a^b f = F(b) - F(a) \). Hier: \( F(1) - F(0) =
\tfrac{1}{3} - 0 = \tfrac{1}{3} \).

</details>
</details>

## Graph

<div class="jxgbox" id="jxg-beispiel" style="width:100%;max-width:520px;aspect-ratio:1/1"></div>
<script>(function(){var b=JXG.JSXGraph.initBoard('jxg-beispiel',{boundingbox:[-2.4,4.2,2.4,-0.6],axis:true,showCopyright:false,showNavigation:false});b.create('functiongraph',[function(x){return x*x;},-2.2,2.2],{strokeColor:'#3a5a9c',strokeWidth:2.5});b.create('point',[1,1],{name:'P',size:2,fixed:true,color:'#d98324'});})();</script>
