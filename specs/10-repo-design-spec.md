# Design-Spec — Mathe-Abi-Lernbuch

> **Strang:** `mathe-abi` · **Datum:** 2026-06-18 · **Status:** Entwurf zur Abnahme
> **Provenance:** DLG-2026-06-17-B61 · DLG-2026-06-18-B62 · DLG-2026-06-18-B63
> **Datenklasse:** public (keine Verschlüsselung) · **Deploy-Ziel:** `mathe.senecheau.com`
> **HARD GATE:** Vor YANNs Abnahme dieses Specs entsteht kein HTML/Code.

Dieser Spec beschreibt **das gesamte System** — das Lernbuch, die unterstützenden Werkzeuge und den
Mechanismus, mit dem das System selbst weiterentwickelt wird. Konkrete Bau-Schritte folgen nach Abnahme
über `writing-plans`.

---

## 0. Warum — didaktischer Charter

**Zweck:** Léona soll in der verbleibenden Zeit ihre Verständnislücken in der Analysis effizient schließen
und in der mündlichen Prüfung sicher auftreten. Das Lernbuch ist ihr persönliches, mitwachsendes
Arbeitsmittel; Agents erweitern es laufend auf Basis ihres tatsächlichen Lernstands.

**Leitplanken (evidenzbasiert, knapp begründet):**

1. **Prüfungsrealismus.** Aufgaben spiegeln das echte mündliche Format (Vortrag + Prüfungsgespräch) und die
   tatsächlichen Anforderungsbereiche. Léona übt, wie sie geprüft wird.
2. **Rechnerfrei.** Die mündliche Prüfung ist in beiden Teilen hilfsmittelfrei [99 %]. Training und
   Beispielrechnungen kommen ohne GTR/Formelsammlung aus; Kopf- und Handrechnung stehen im Vordergrund.
3. **Verstehen vor Auswendiglernen.** Jeder Schritt nennt die **Haltung** dahinter (warum dieser Schritt,
   welches Prinzip) — über aufklappbare Detailkästen, die kaskadiert in die Tiefe gehen (Schritt → Begründung
   → Annahme/Axiom → Herleitung).
4. **Aktives Erinnern + ausgearbeitete Beispiele.** Gestützt auf belegte Lernprinzipien (Retrieval Practice,
   Worked-Example-Effekt, Cognitive-Load-Theorie). Erst geführte Musterlösung, dann zunehmend selbst lösen.
5. **Keine Redundanz.** Jeder Inhalt existiert genau einmal (Konzept-Register) und wird je Kontext in der
   passenden Form gezeigt; an deutlichen Schnitten Querverweis statt Wiederholung.
6. **Konfidenz-Ehrlichkeit.** Prüfungsrelevanz-Aussagen tragen sichtbar Konfidenz + Quelle; was unsicher ist,
   ist als unsicher markiert. Ein dezenter Hinweis macht klar, dass agentischer Output nicht zu 100 %
   verlässlich ist.
7. **Anpassbar an Léonas Feedback.** Startannahmen sind bewusst gesetzt und werden korrigiert, sobald sie mit
   dem Buch arbeitet. Schnelles Feedback fließt schnell zurück (Evolutions-Mechanismus, §13).

**Nicht-Ziele (YAGNI):** keine native App; keine fertig implementierte lokale TTS (nur Stub); keine
Companion-Anbindung; kein Vorab-Rendern aller Audios.

---

## 1. Zielbild & Erfolgskriterien

**Zielbild:** Léona ruft `mathe.senecheau.com` auf (Desktop oder Smartphone), arbeitet Kapitel und Aufgaben
durch, lässt sich Abschnitte vorlesen, hört unterwegs thematische Podcasts und bekommt auf ihren Lernstand
zugeschnittene nächste Schritte (nummerierte Vorschläge).

**Erfolgskriterien (überprüfbar):**
- Alle Analysis-Kernthemen des Lehrer-Kanons sind als Kapitel mit Beispielaufgaben + kaskadierten
  Erläuterungen vorhanden, rechnerfrei lösbar dargestellt.
- Mindestens **zwei vollständige Prüfungssimulationen** im echten Format (Vortragsaufgabe + Gesprächsimpuls).
- Lernstand-Graph ist befüllt und steuert die Vorschläge.
- Seite ist auf Smartphone und Desktop mit hoher Usability bedienbar.
- Deployment ist versioniert, historisiert und nach jedem Deploy automatisiert verifiziert.

---

## 2. Prüfungsrahmen (gegroundet, konfidenzgetaggt) — die Randbedingungen für Inhalt

Quellen: KM-Facherlass 2026 (§25.2.3, im PDF-Volltext gegengeprüft), KMK-Bildungsstandards 2012,
Bildungsplan-2016-Leitidee Basisfach, Pfeiffer/Uhl-Abgrenzungstabelle, RP-Tübingen-Basisfach-Konvolut.

| Rahmen | Aussage | Konf. |
|---|---|---|
| Ablauf | ~20 Min Vorbereitung → ~10 Min Vortrag → ~10 Min Prüfungsgespräch | 99 % |
| Struktur | 2 Sachgebiete; **Analysis Pflicht** + (Analyt. Geometrie **oder** Stochastik); Vortrag/Gespräch in verschiedenen Sachgebieten | 99 % |
| Hilfsmittel | **In beiden Teilen hilfsmittelfrei** (Rechner/Formelsammlung nur evtl. in der Vorbereitung) | 99 % |
| Anforderungsbereiche | Schwerpunkt AB II; Basisfach akzentuiert AB I stärker als AB III; „gut" = alle drei AB, „ausreichend" = AB I + ein weiterer | 98 % |
| Schwerpunktthemen | keine thematische Eingrenzung in Mathe; ganzer Bildungsplan 2016 gilt | 98 % |

**Konsequenz für das Lernbuch:** rechnerfrei trainieren; Aufgaben nach AB I/II/III taggen und so mischen, dass
Léona AB I sicher beherrscht und AB II routiniert wird; das mündliche Zwei-Phasen-Format abbilden.

---

## 3. Inhalts-Scope (Analysis-Kanon)

**Kanon = Lehrer-Handout (Bilder 1–2).** Es definiert, was an ihrer Schule drankommt, und ist damit operativ
verbindlich — auch wo es vom allgemeinen Basisfach-Plan abweicht.

**Themenbaum (aus dem Handout):**
- **Funktionsuntersuchung:** Nullstellen/Schnittpunkt y-Achse · Grundsymmetrie · Randverhalten ·
  Extremstellen + Monotonie · Wendestellen + Krümmung → Ziel „Graph zeichnen".
- **Handwerksmittel Analysis:** Gleichungen lösen · Ableitungsregeln (Potenz-, Summen-, Faktor-,
  **Produktregel**, **lineare Kettenregel**) · Grundfunktionen (ganzrational, e-Funktion, trigonometrisch
  sin/cos, Wurzelfunktion*, `f(x)=1/x`*).
- **Integralrechnung:** orientierter Flächeninhalt (graphisch) · Flächenberechnung mit Integralen · Integral
  in Sachzusammenhängen (Textaufgaben) · Aussagen zu Stammfunktion/Ableitungsfunktion beurteilen.
- **Handwerksmittel Integral:** Hauptsatz (anwenden) · Stammfunktionsregeln (Faktor, Summe, Potenz, lineare
  Substitution) · Zusammenhang der Graphen F/f/f′/f″.

**\* Widerspruch zum offiziellen Basisfach-Plan (mit Konfidenz markieren, Lehrkraft verifizieren):**
- `f(x)=1/x` / gebrochenrationale Funktionen sind offiziell **Leistungsfach-only** [97 %].
- Wurzelfunktion ist im Basisfach **nicht eigenständig** ausgewiesen [80 %, Negativbefund].
- Produkt-/lineare Kettenregel, e/sin/cos/ganzrational und alle Integral-Inhalte = sauber Basisfach [95–99 %].

→ **Umgang:** beide Funktionen aufnehmen (Kanon), aber im Kapitel mit Relevanz-Tag „offiziell LF, Basisfach
unsicher [97 %] — mit Lehrkraft prüfen". Lieber leicht überdecken als eine evtl. geprüfte Funktion auslassen.

**Quelle des Inhalts:** Das Schulbuch (vermutl. Lambacher Schweizer) dient **nur lokal** als Agent-Kontext;
im public Repo erscheinen ausschließlich **eigene** Formulierungen, eigene Aufgaben und **Seitenverweise**
(z. B. „vgl. Lehrbuch S. 142") — keine verbatim-Scans/Abbildungen (Urheberrecht).

---

## 4. Lernbuch-Architektur (Repository & Rendering)

**Statische Website, Pages-/Caddy-tauglich, kein Anwendungsserver für die Inhalte.**

| Baustein | Wahl | Begründung |
|---|---|---|
| Generator | **Eleventy (11ty)** | Single-Source: gemeinsame Konzept-Fragmente werden **transkludiert**, nicht kopiert → Redundanzfreiheit strukturell erzwungen. Open Source, schlanker Build. |
| Formeln | **KaTeX** (Build-Zeit-Rendering) | schnell, serverlos, deterministisch. |
| Diagramme | **JSXGraph** | interaktive Funktionsgraphen (Schieberegler, Tangenten, Flächen); in der deutschen Mathedidaktik etabliert; Open Source. Kein Mermaid. |
| Detailkästen | native verschachtelte `<details>`/`<summary>` | kaskadierte Tiefe (Schritt → Begründung → Axiom/Herleitung) ohne Framework, barrierearm, druckbar. |
| Layout-Modi | **eine** Codebasis, zwei adaptive Modi | Desktop: mehrspaltig mit Querverweis-Seitenleiste. Mobil: einspaltiger Lesemodus (große Schrift, Kästen default zugeklappt, fester Vorlese-Button). Single-Source, keine Doppelpflege. |

**Inhaltsmodell (Redundanzfreiheit + Querverweise):**
- **Konzept-Register** (`content/concepts/*.md` mit eindeutiger ID + Metadaten: Titel, AB-Tags,
  Prüfungsrelevanz+Konfidenz+Quelle, `provenance: [DLG-…]`, Voraussetzungen, verwandte IDs).
- Seiten **binden** Konzepte per ID ein (Transklusion); eine Definition steht genau einmal.
- **Querverweis „an deutlichen Schnitten":** Verweise laufen über die Konzept-ID; das Register ist die
  Landkarte (welches Konzept setzt welches voraus, was kommt als Nächstes).

**Seitentypen:** (a) **Themenseite** (Konzept + Haltung + kaskadierte Detailkästen + interaktiver Graph),
(b) **Aufgabenseite** (Beispielaufgabe im Prüfungsformat, §5), (c) **Übersicht/Lernpfad** (Kapitelkarte +
Lernstands-Ampel), (d) **Prüfungssimulation**.

---

## 5. Beispielaufgaben-Modell (prüfungsrealistisch)

Vorlage ist Bild 3 („Analysis Teil 1 – Aufgabe", `f(x)=¼x⁴−2x²`, Teilaufgaben a–e mit Graph).

**Jede Aufgabe enthält:**
- **Aufgabenstellung** im echten Stil, inkl. JSXGraph-Abbildung, Teilaufgaben nach AB I/II/III getaggt.
- **Zwei-Phasen-Bezug:** kennzeichnet, was Vortragsteil (vorbereitet, zusammenhängend) und was
  Gesprächsimpuls (spontan, vertiefend) wäre.
- **Lösungsweg** Schritt für Schritt, **rechnerfrei**.
- **Haltung dahinter** je Schritt (warum so, welches Prinzip, typische Fallen) — als Detailkasten.
- **Kaskadierte Erläuterungen:** Schritt → Begründung → Annahme/Axiom → Herleitung, beliebig tief, jeweils
  als aufklappbarer Unterkasten.
- **Prüfungsgespräch-Antizipation:** mögliche Rückfragen der Prüfenden + knappe Musterantworten.

---

## 6. Lernstand-Modell (K3)

**Maschinenlesbarer Kompetenz-Graph** (YAML, versioniert, agent-gepflegt) — bleibt **privat in mywiki**
(Léonas Lernstand ist nicht public), das Lernbuch liest daraus nur abgeleitete Hinweise.

```yaml
# context/registers/leona-lernstand.yaml (in mywiki, privat)
themen:
  - id: extremstellen
    teilkompetenzen:
      - id: notwendiges-kriterium      # f'(x)=0
        status: wackelig               # sicher | wackelig | luecke | unbekannt
        datum: 2026-06-18
        beleg: DLG-…/Aufgabe-…         # woher das Signal stammt
```

**Diagnose:** Startannahme „alles wackelig/unbekannt"; Gerüst breit-flach bauen. Aus Bild 3 ein erstes
Referenz-Diagnoseset ableiten; sobald Léona greifbar ist, ein ~15-Aufgaben-Set im echten Format zur
Verfeinerung.

**Lernstand aus Dialogen (B62):** Aus transkribierten Antworten Léonas wird ihr Stand antizipiert — wo sie in
bestimmten **Rechen-/Herleitungsarten** Verständnisprobleme zeigt, wird gezielt eine **dedizierte
Remedial-Lektion** vorgeschlagen.

**Nummerierte Vorschläge:** Jeder vom Agenten erzeugte Vorschlag (neue Lektion, Übungsserie,
Vertiefung) bekommt eine fortlaufende **Nummer**. YANN/Léona sagen „Vorschlag 117 umsetzen". Angenommene
Vorschläge werden über Léonas Transkripte zurückverfolgt (was bezog sie sich worauf, was wurde umgesetzt).
Register: `context/registers/leona-vorschlaege.yaml` (privat): `{nr, datum, thema, beschreibung, status:
offen|angenommen|umgesetzt, provenance}`.

---

## 7. Audio — Vorlesen + Podcasts (K4)

**Zwei verschiedene Funktionen, bewusst getrennt:**

**(a) Realtime-Vorlesen (on-demand, sporadisch).**
- Léona klickt an einem Abschnitt „Vorlesen" → **ElevenLabs** streamt in Echtzeit.
- **TTS-Proxy** als kleiner Dienst auf dem Hetzner-Server (hinter Caddy) hält den ElevenLabs-Key (darf nicht
  ins public Frontend) und **cacht** das erzeugte mp3 → jeder Abschnitt verursacht höchstens **einmal**
  Kosten (deckelt YANNs Kostenbedenken aus B62).
- **Dünne Schnittstelle** über TTS-Anbieter (austauschbar); **lokale Variante nur Stub** — nicht
  implementiert/getestet/lauffähig, keine automatisierten Tests dafür (B62).

**(b) Thematische Podcasts (on-demand, vorab generiert).**
- **Kein** Vorab-Rendern aller Inhalte. YANN nennt Bereich + Kontextelemente, der Agent leitet ab, was in die
  Episode kommt, und formuliert **audio-first** (alles im Geiste vorstellbar; keine visuellen Bezüge wie
  „siehe Diagramm oben"). Erzeugt Skript → TTS → mp3-Episode.
- **Aufgeschoben**, bis YANN mehr mit Léona gesprochen hat (welche Themen als Podcast nützen) — kein „ins
  Blaue".
- **Auslieferung aufs iPhone:** RSS-Feed auf `mathe.senecheau.com`; **QR-Code** auf der Seite →
  `podcast://…/feed.xml` (Apple Podcasts abonniert nativ); zusätzlich Web-Player-Fallback. Kein Spotify/Upload.

---

## 8. Voice-Ingestion von Léonas Sprachnachrichten (neu, B62)

**Ablauf:** Léona schickt YANN eine WhatsApp-Sprachnachricht → YANN lädt sie herunter → **Drag-and-Drop** der
Audio-Datei an einen Agent → Transkription → Lernstand-Update + neue nummerierte Vorschläge.

**STT-Verdikt (Q4-Recherche):** **Parakeet TDT 0.6B V3 lokal** als Standard (M5 Max), **gehärtet**:
- **NeMo-Word-Boosting** mit Mathe-Hotword-Liste (Stammfunktion, Wendestelle, Ableitung, Hauptsatz, …) gegen
  das OOV-Problem (Fachvokabular).
- **langid-Nachprüfung** des Transkripts (≠ de → markieren/neu) gegen Sprach-Drift ins Englische bei kurzen,
  spontanen Clips (Parakeet hat kein Deutsch-Locking — belegt).
- Audio nicht künstlich kürzen; **Anglizismen nativ behalten** (nicht filtern).
- **Benannter Cloud-Fallback: Deepgram Nova-3** (einziges mit für Deutsch bestätigtem Keyterm-Boosting) — nur
  falls echte Samples gehäuft OOV/Drift zeigen. Daten sind public → Cloud datenschutzrechtlich unkritisch.
- **Verifikation am ersten echten Sample**, bevor wir uns festlegen.

**Slash-Kommandos (Werkzeuge, B63):**
- `/leona-input` — Drag-and-Drop-Audio → transkribieren → Lernstand aktualisieren → neue nummerierte Vorschläge.
- `/leona-vorschlag <n>` — nummerierten Vorschlag umsetzen.
- `/leona-stand` — aktuellen Kompetenz-Graph anzeigen.

---

## 9. Deployment & serverseitige Versionierung (K5/K6)

**Ziel:** `mathe.senecheau.com` über das bestehende **Caddy/Hetzner-Infra**-Muster (Caddy auf Hetzner,
Route53-DNS, TLS automatisch).

**Subdomain anlegen (4 Schritte, einmalig):** Subdomain ins `DOMAINS`-Array (`das DNS-Setup-Skript der Server-Infra`)
→ Caddyfile-Block `mathe.senecheau.com { root * /srv/mathe … }` → Bind-Mount `- /srv/mathe:/srv/mathe:ro` in
`docker-compose.prod.yml` → rsync + Caddy-Recreate.

**„Deploy das neueste Repository" = Codex-delegiertes Update/Redeploy** (einfacherer Agent), komplettes
Redeployment ist ok.

**Serverseitige Versionierung (neu — existiert für statische Sites noch nicht):**
- Atomare Releases: `/srv/mathe/releases/<UTC-Zeitstempel>/`, Umschaltung per `current`-Symlink.
- Jede Vorversion bleibt erreichbar unter eigener Route `/v/<zeitstempel>/` (Caddy).
- Zusätzlich Git-Deploy-Tag `deploy/JJJJ-MM-TT-HHMM` (wie im bestehenden Deploy-Muster) als Rollback-Anker.
- Rollback = Symlink-Switch.

---

## 10. Testing & Deployment-Verifikation (neu, B62)

**Gesamtlösung automatisiert testen** (YANN testet nicht manuell durch):
- **Inhalt/Build:** Eleventy baut fehlerfrei; KaTeX/JSXGraph rendern; Links/Konzept-IDs auflösbar (kein toter
  Querverweis); keine Redundanz-Duplikate (Konzept genau einmal definiert).
- **Deployment-Verifikation (Tool):** Build schreibt `version.json` (Git-Kurz-SHA + UTC-Zeit + Inhalts-Hash)
  in die Site. Nach dem Deploy lädt ein Tool `https://mathe.senecheau.com/version.json` und prüft Gleichheit
  mit dem gebauten Stand. **„Deploy" schlägt laut fehl**, wenn die live Version nicht die erwartete ist.
- **Playwright-Smoke:** Schlüsselseiten laden, Formeln/Graphen sichtbar, keine Konsolenfehler.
- Beweis-vor-Übergabe: kein Baustein gilt als fertig ohne automatisierten grünen Lauf mit verbatim-Output.

---

## 11. Provenance & Governance (K7)

- **Privat in mywiki:** alle Dialoge (`dialog/`), der Verlauf-Export, Handoff, Lernstand- und
  Vorschlags-Register, Ledger.
- **Public im mathe-abi-Repo/Site:** nur das Lernbuch + je Kapitel/Konzept ein `provenance: [DLG-…]`
  + Deploy-Hash. Sichtbar „kam von X", nie der private Klartext.
- **Provenance-Inhalt:** was kam woher, wann, mit welcher Wirkung — inkl. der gesamten Dialoge (bereits als
  B61–B63 + Verlauf gesichert). Anknüpfung an das mywiki-Hub-Modell (ADR-0009 [Datenklassen-Routing]).
- **Konfidenz-Disziplin** (Bauprinzip): Prüfungsrelevanz-Aussagen tragen „Relevanz: X % (Quelle)"; Nicht-
  Relevantes wird knapp begründet + prozentual markiert; globaler Hinweis auf begrenzte Verlässlichkeit.

---

## 12. Skills (Q5 — Risikobewertung erledigt)

- **Übernehmen, nur als Lesereferenz:** `education-agent-skills` (reines Markdown, studienzitiert:
  Retrieval Practice, Worked-Example-Fading, Cognitive Load). MCP-Server **nicht** installieren;
  CC-BY-SA-Attribution mitführen. Niedriges Risiko nach Review.
- **Selbst bauen (kein seriöses Fertigprodukt am Markt):** `mathe-pruefungsdidaktik` (mit KMK-/BW-
  Operatorenkatalog, AB-Logik, mündlichem Format) und `audio-erklaer-skript` (audio-first formulieren).
  Beide reines Markdown, kein Fremd-Code im Harness.
- **Meiden:** alle externen Audio-/TTS-Skills mit `install.sh`/Git-Hooks/`curl|bash`/Cloud-Upload/eigenem
  Server (Datenexfiltration, Persistenz, beliebige Codeausführung) — siehe Risikobefund im Verlauf.

---

## 13. Evolutions-Mechanismus („Mechanismus zum Ändern des Mechanismus")

Das System ist so vorgebaut, dass es ohne Zeitverlust mitwächst, sobald Léona es nutzt:
- **Erweiterungs-Loop:** Agent erzeugt Inhalt → nummerierte Vorschläge → YANN/Léona nehmen an
  (`/leona-vorschlag <n>`) → Agent baut → Deploy inkl. Verifikation → Lernstand-Update.
- **Feedback-Loop:** Léonas Sprachnachricht → `/leona-input` → Lernstand-Antizipation → maßgeschneiderte
  nächste Sequenzen/Remedial-Lektionen.
- **Selbst-Änderung:** Dieser Spec und der Charter (§0) sind versioniert; Änderungen an Leitplanken laufen
  über einen neuen Dialogblock (DLG-…) + Spec-Update + Eintrag im Handoff. Die Bau-/Deploy-/Test-Mechanik
  ist dokumentiert und reproduzierbar.
- **Companion:** bewusst **nicht** angeschlossen (B62). Schnittstellen bleiben so schlank, dass eine spätere
  Anbindung möglich ist, ohne sie jetzt vorauszusetzen.

---

## 14. Repo-Struktur (public `mathe-abi`)

```
mathe-abi/
  .eleventy.js                 # Build-Konfiguration
  src/
    content/
      concepts/                # Konzept-Register (eine Definition je ID)
      kapitel/                 # Themenseiten
      aufgaben/                # Beispielaufgaben (Prüfungsformat)
      simulationen/            # Prüfungssimulationen
    _includes/                 # Layouts (Desktop/Mobil), Detailkasten-Komponente
    assets/                    # KaTeX/JSXGraph (vendored), CSS (schulisches Design), Audio-Cache-Verweise
    podcast/feed.xml           # RSS (wenn Podcasts existieren)
  tools/
    build.js · deploy.sh · verify_deploy.py · version.json (generiert)
  tests/                       # Build-/Link-/Smoke-Tests (Playwright)
  README.md                    # inkl. Provenance-Hinweis (DLG-IDs) + Exit-Plan
```
GitHub-gesichert (public), keine Verschlüsselung. TTS-Proxy lebt in `die Server-Infra` (nicht im public Repo,
wegen Key).

---

## 15. Tool-Auswahl & Exit-Pläne (Open-Source-first-Konformität)

| Tool | Klasse | Exit-Plan |
|---|---|---|
| Eleventy, KaTeX, JSXGraph | Open Source | Standardformate (Markdown/HTML/SVG); ersetzbar, Inhalt bleibt portabel. |
| ElevenLabs (TTS) | **Premium (bewusste Ausnahme, mit YANN abgestimmt)** | hinter dünner Schnittstelle gekapselt; lokaler Stub vorbereitet; Audio gecacht (portabel als mp3). |
| Parakeet (STT) | Open Source, lokal | YANN-Standard; Deepgram nur als optionaler Fallback. |
| Caddy/Route53/Hetzner | bestehende Infra | gleiches Muster wie bestehende Server-Infra; Site ist statisch und überall hostbar. |

---

## 16. Annahmen & offene Punkte

- **Annahme:** „Grundstufe" = Basisfach/grundlegendes Niveau (Gymnasium). Falls Leistungsfach: Scope ändert
  sich (1∕x, allgemeine Kettenregel etc. dazu).
- **Offen:** genauer Prüfungstermin (29.6.–9.7.); zweites Sachgebiet; 1∕x-/Wurzelfunktion-Relevanz mit
  Lehrkraft verifizieren; Podcast-Themenbereiche (nach mehr Léona-Input); erstes Voice-Sample für Parakeet.

---

## 17. Bau-Reihenfolge (Grobschnitt — Details über `writing-plans`)

1. Gerüst: Repo + Eleventy + Stack + zwei Layout-Modi + schulisches Design; `version.json` + Deploy-/Verify-
   Skripte; Subdomain `mathe.senecheau.com` live; Deployment-Verifikation grün.
2. Inhalt Welle 1: Funktionsuntersuchung (Kanon Bild 1/2) + Beispielaufgabe (Bild 3) als Format-Referenz,
   inkl. kaskadierter Detailkästen + JSXGraph.
3. Lernstand-Graph + nummerierte Vorschläge + `/leona-*`-Kommandos + Voice-Ingestion (Parakeet, gehärtet).
4. Realtime-TTS-Proxy (ElevenLabs, gecacht) + Vorlese-Button.
5. Inhalt Welle 2: Integralrechnung + restliche Themen; zwei Prüfungssimulationen.
6. Podcasts (sobald Themen mit Léona geklärt) + RSS/QR.
7. Skills `mathe-pruefungsdidaktik` + `audio-erklaer-skript`.

---

## 18. Selbst-Review (vor Abnahme)

- Platzhalter/TODO: keine offenen.
- Konsistenz: Architektur (§4) deckt alle Funktionsanforderungen (§5–§10) ab; Provenance (§11) konsistent mit
  Datenklasse public + privat in mywiki.
- Scope: fokussiert auf ein implementierbares System; Léonas Lernstand-Daten bewusst privat.
- Mehrdeutigkeit: „zwei Versionen" als zwei Layout-Modi einer Codebasis festgelegt (nicht zwei Repos).
