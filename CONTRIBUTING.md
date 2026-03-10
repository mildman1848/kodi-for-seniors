# Contributing to kodi-for-seniors

## Before opening a pull request

- Keep changes focused and directly related to the Kodi skin or its release automation.
- Follow the PR template.
- Link the related issue when applicable with `closes #<number>`.
- Update `README.md`, `CHANGELOG.md` or setup docs when behavior changes.
- If you touch publishing logic, verify both the source repo and the GitHub Pages repo flow.

## Files of interest

| File                                    | Purpose                                              |
| --------------------------------------- | ---------------------------------------------------- |
| `skin.kodi4seniors/`                    | Kodi skin addon payload                              |
| `skin.kodi4seniors/xml/`                | Skin window and include definitions                  |
| `scripts/build_release.py`              | Builds the addon ZIP                                 |
| `scripts/publish_to_repo.py`            | Publishes the addon into the Kodi repository repo    |
| `.github/workflows/release-publish.yml` | Cross-repo release publishing                        |
| `docs/setup-playbook.md`                | One-time setup checklist for the technical installer |

## Local validation

- `python3 -m py_compile scripts/build_release.py scripts/publish_to_repo.py`
- `xmllint --noout skin.kodi4seniors/addon.xml skin.kodi4seniors/xml/*.xml`
- `python3 scripts/build_release.py`
- `python3 scripts/publish_to_repo.py --publish-repo /path/to/mildman1848.github.io`
