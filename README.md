# mathe-abi

Öffentliches HTML-Lernbuch zur Vorbereitung auf die **mündliche Mathe-Abiturprüfung**
(Baden-Württemberg, Basisfach, Schwerpunkt **Analysis**). Datenklasse **public**, kein Passwortschutz.

Live: **https://mathe.senecheau.com** (GitHub Pages, Quelle `main` / `docs`).

## Stand

Aufbauphase. Aktuell veröffentlicht sind die **Spezifikationen** (Startseite):
- `specs/00-bau-charter.md` — wie wir das Lernbuch bauen und weiterentwickeln (Meta-Spec).
- `specs/10-repo-design-spec.md` — was wir bauen (Design-Spec).

Das eigentliche Lernbuch (Kapitel, Beispielaufgaben, interaktive Diagramme) wird hier laufend ergänzt.

## Bauen

```bash
python3 tools/build_site.py   # rendert specs/ -> docs/ (benötigt pandoc)
```

Design-System: `tools/assets/site.css` + `tools/assets/site.js` (klappbare Abschnitte, Sidebar-Navigation,
responsiv Web/Mobil, KaTeX-Skalierung). Keine externen Laufzeit-Abhängigkeiten.

## Provenance

Planung, Dialoge und Lernstand bleiben privat im mywiki-Harness; dieses Repo trägt nur rückverweisende
IDs: DLG-2026-06-17-B61, DLG-2026-06-18-B62/B63, DLG-2026-06-18-Z01.
