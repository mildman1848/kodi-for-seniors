# kodi-for-seniors

Seniorenfreundlicher Kodi-Skin mit Fokus auf:

- Live-TV mit gut lesbarem TV-Guide
- schnelle Einstiege in oeffentlich-rechtliche Mediatheken
- moeglichst geringer Bedienkomplexitaet im Alltag
- einmaliger Einrichtung durch eine technisch versierte Person

## Struktur

- `skin.kodi4seniors/`: Kodi-Skin-Addon
- `skin.kodi4seniors/1080i/`: Skin-Window- und Include-Definitionen
- `skin.kodi4seniors/resources/lib/focus_handler.py`: initialisiert den Home-Fokus und synchronisiert aktive Kachel-Properties
- `skin.kodi4seniors/resources/media/`: Home-Vorschauen und Fokusgrafiken
- `scripts/build_release.py`: erzeugt das Release-ZIP
- `scripts/publish_to_repo.py`: aktualisiert die Kodi-Repo unter `mildman1848.github.io`
- `.github/workflows/release-publish.yml`: publiziert nach einem GitHub-Release in die Kodi-Repo
- `docs/setup-playbook.md`: Checkliste fuer die einmalige Einrichtung

## Repository-Hygiene

Das Repo enthaelt ausserdem:

- `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`
- Issue- und PR-Templates unter `.github/`
- `Dependabot`, `CI`, `CodeQL`, `Security`, `Greetings` und `Stale` Workflows
- Prettier-, Git- und Editor-Konfiguration fuer konsistente Aenderungen

## Setup-Idee

Der Skin reduziert die Startseite auf genau vier grosse Kacheln:

- Fernsehen
- Mediatheken
- Bibliothek
- Einstellung

Die technisch versierte Person richtet einmalig ein:

1. PVR-Backend und EPG
2. gewuenschte Mediathek-Add-ons
3. Netzwerk, Audio und Fernbedienung
4. diesen Skin als Standardskin

Danach bleibt die alltaegliche Bedienung auf wenige grosse Schaltflaechen begrenzt.
