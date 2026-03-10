# Changelog

All notable changes to this project will be documented in this file.

## 0.1.5 - 2026-03-10

- Aligned the home screen more closely with the original senior-launcher concept: color-coded sections, two larger primary tiles on top and calmer preview-oriented content blocks.
- Improved the semantic distinction between daily-use areas and the technical settings area.

## 0.1.4 - 2026-03-10

- Reworked the home screen into four large tiles in a 2x2 layout instead of a list-style menu.
- Simplified the supporting text on the start screen so the UI reads more like a calm senior launcher and less like a technical skin fork.

## 0.1.3 - 2026-03-10

- Fixed Linux font loading by shipping lowercase font filenames that match the runtime lookups.
- Restored the global include chain in `Includes.xml` so Estuary-derived windows can resolve shared includes and variables.

## 0.1.2 - 2026-03-10

- Bundled the full skin runtime asset set and base XML windows so the skin can actually render screens and dialogs in Kodi.

## 0.1.1 - 2026-03-10

- Fixed missing base windows and dialog files so the skin can be activated more reliably in Kodi.
- Kept the simplified four-tile home screen for Fernsehen, Mediatheken, Bibliothek and Einstellung.

## 0.1.0 - 2026-03-10

- Added the first installable `skin.kodi4seniors` addon skeleton.
- Added a simplified senior-focused home screen with exactly four tiles: Fernsehen, Mediatheken, Bibliothek and Einstellung.
- Added dedicated PVR channel and EPG guide XML views.
- Added local build and publish scripts for the GitHub Pages Kodi repository.
- Added GitHub repository hygiene files, templates and CI workflows.
