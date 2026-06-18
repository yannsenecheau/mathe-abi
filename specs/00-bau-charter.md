# Bau-Charter — wie wir dieses Lernbuch bauen und weiterentwickeln

> **Meta-Spezifikation** · Strang `mathe-abi` · Datenklasse **public** · Stand 2026-06-18
> Dies ist die Spezifikation *zu dem, wie wir die Spezifikation und das Repository bauen*. Sie gilt
> gemeinsam mit der [Repo-Design-Spec](design-spec.html). Provenance: DLG-2026-06-17-B61,
> DLG-2026-06-18-B62/B63, DLG-2026-06-18-Z01.

## Zweck dieses Dokuments

Léona bereitet sich auf die mündliche Mathe-Abiturprüfung vor (Baden-Württemberg, Basisfach, Analysis).
Dieses Lernbuch ist ihr persönliches, mitwachsendes Arbeitsmittel. Damit es ohne Zeitverlust weiterwachsen
kann, ist nicht nur das Ergebnis spezifiziert, sondern auch der Mechanismus, mit dem wir es bauen und
ändern — und die Begründungen dahinter, damit jede künftige Variante an der richtigen Stelle andocken kann.

## Leitprinzipien (didaktischer Charter)

- **Prüfungsrealismus.** Aufgaben spiegeln das echte mündliche Format (Vortrag + Prüfungsgespräch) und die
  Anforderungsbereiche AB I/II/III.
- **Rechnerfrei.** Die mündliche Prüfung ist in beiden Teilen hilfsmittelfrei (Konfidenz 99 %); Training und
  Beispiele kommen ohne Taschenrechner aus.
- **Verstehen vor Auswendiglernen.** Jeder Schritt nennt die Haltung dahinter — über klappbare Detailkästen,
  die kaskadiert in die Tiefe gehen (Schritt → Begründung → Annahme/Axiom → Herleitung).
- **Aktives Erinnern + ausgearbeitete Beispiele.** Gestützt auf belegte Lernprinzipien (Retrieval Practice,
  Worked-Example-Effekt, Cognitive-Load-Theorie).
- **Keine Redundanz.** Jeder Inhalt existiert genau einmal; an deutlichen Schnitten Querverweis statt
  Wiederholung.
- **Konfidenz-Transparenz.** Prüfungsrelevanz-Aussagen tragen sichtbar Konfidenz + Quelle. Agentischer Output
  ist nicht zu 100 % verlässlich — das bleibt sichtbar.
- **Anpassbar.** Startannahmen sind bewusst gesetzt und werden korrigiert, sobald Léona mit dem Buch arbeitet.

## Wie Inhalte entstehen

Agents erzeugen Kapitel, Beispielaufgaben und Erläuterungen aus dem Lehrer-Kanon (Screenshots) und dem
lokalen Buchkontext. Jeder erzeugte **Vorschlag** (neue Lektion, Übungsserie, Vertiefung) bekommt eine
**fortlaufende Nummer**. YANN oder Léona sagen „Vorschlag 117 umsetzen", der Agent baut, deployt und
aktualisiert den Lernstand.

## Wie Feedback einfließt

Léona schickt eine WhatsApp-Sprachnachricht → YANN lädt sie herunter → Drag-and-Drop an einen Agent →
Transkription (Parakeet lokal, gehärtet; Cloud-Fallback Deepgram nur bei Bedarf) → der Lernstand wird
antizipiert → daraus entstehen maßgeschneiderte nächste Sequenzen und, bei Verständnisproblemen in
bestimmten Rechen-/Herleitungsarten, dedizierte Remedial-Lektionen. Werkzeuge: `/leona-input`,
`/leona-vorschlag <n>`, `/leona-stand`.

## Wie wir Versionen bauen, deployen und prüfen

1. **Bauen** — statisches HTML (Eleventy, Single-Source), KaTeX für Formeln, JSXGraph für Diagramme.
2. **Testen** — Build fehlerfrei; Links/Konzept-IDs auflösbar; **Formel-Skalierung** automatisch geprüft
   (kein Overflow, Schriftgröße im Soll, unverzerrtes Seitenverhältnis); Playwright-Smoke.
3. **Deployen** — „Deploy das neueste Repository" aktualisiert die Live-Seite; jede Vorversion bleibt
   erhalten (Versionierung + Git-Tags).
4. **Verifizieren** — nach jedem Deploy prüft ein Tool, dass die live ausgelieferte Version die erwartete
   ist (`version.json`-Abgleich); schlägt sonst laut fehl. Gefundene Probleme werden behoben, dann erneut
   deployt und geprüft.

## Wie wir dieses System ändern (Andockpunkte + Folgen)

Diese Charter und die Design-Entscheidungen sind versioniert. Eine Änderung läuft über: neuer Dialogblock
(DLG-…) → Update dieser Spec/Charter → Eintrag im Handoff → Bau → Deploy + Verifikation. So bleibt der volle
Trace erhalten: was kam woher, wann, mit welcher Wirkung. Die **Companion**-Anbindung ist bewusst noch nicht
aktiv; die Schnittstellen bleiben schlank genug für eine spätere Anbindung.

## Design-Entscheidungen (mit Begründung)

- **Look „modernes Schulbuch":** warmes Papier-Off-White, Indigo primär, warmer Amber-Akzent für interaktive
  Elemente. Vertraut-schulisch, hoher Kontrast, nicht templated.
- **Typografie:** lesefreundliche Serife im Fließtext, System-Sans in der Navigation, KaTeX-Font für Mathe.
- **Responsiv ohne UA-Sniffing:** Geräte-Erkennung per CSS (Media-/Container-Queries). Desktop: Kapitelbaum +
  Inhalt + Querverweise. Mobil: einspaltiger Lesemodus, klappbare Abschnitte, große Touch-Ziele.
- **Navigation & Lernpfade:** persistenter Kapitelbaum, Breadcrumb, Voraussetzungs-/Nächster-Schritt-Links,
  Fortschritts-Ampel; zwei Pfade — **Prüfungspfad** (kürzeste Strecke zur Prüfungsreife) und
  **Verstehenspfad** (von Grund auf, mehr Tiefe) — plus Einstieg „Diagnose starten".
- **Klappbare Kaskaden:** Tiefe sichtbar durch Einrückung + Farbverlauf der linken Kante; jede Ebene
  aufklappbar; tastatur- und screenreader-freundlich.
- **Kein Passwortschutz.** Offen erreichbar.

## Tech-Entscheidungen & Exit-Pläne

| Baustein | Wahl | Exit |
|---|---|---|
| Generator | Eleventy (Open Source) | Standard-Markdown/HTML, portabel |
| Formeln | KaTeX, build-time | reine HTML/CSS-Ausgabe, ersetzbar |
| Diagramme | JSXGraph (Open Source) | SVG-Fallback, ersetzbar |
| TTS (Vorlesen) | ElevenLabs (bewusste Premium-Ausnahme) | dünne Schnittstelle, lokaler Stub vorbereitet, Audio als mp3 portabel |
| STT (Voice-Input) | Parakeet lokal | YANN-Standard; Deepgram nur optionaler Fallback |
| Hosting | GitHub Pages → `mathe.senecheau.com` | statisch, überall hostbar |

## Provenance-Modell

Dialoge, Lernstand und Ledger bleiben **privat** in mywiki; dieses public Repo trägt nur rückverweisende
DLG-IDs. So bleibt der Audit-Pfad vollständig, ohne private Inhalte zu zeigen.
