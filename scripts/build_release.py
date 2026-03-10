#!/usr/bin/env python3

from __future__ import annotations

import shutil
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
ADDON_DIR = ROOT / "skin.kodi4seniors"
DIST_DIR = ROOT / "dist"


def addon_version() -> str:
    tree = ElementTree.parse(ADDON_DIR / "addon.xml")
    return tree.getroot().attrib["version"]


def build_zip() -> Path:
    version = addon_version()
    DIST_DIR.mkdir(exist_ok=True)
    archive_base = DIST_DIR / f"skin.kodi4seniors-{version}"
    archive_path = shutil.make_archive(str(archive_base), "zip", ROOT, ADDON_DIR.name)
    return Path(archive_path)


def main() -> None:
    archive = build_zip()
    print(archive)


if __name__ == "__main__":
    main()
