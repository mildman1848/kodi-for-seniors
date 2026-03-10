#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
ADDON_DIR = ROOT / "skin.kodi4seniors"
DIST_DIR = ROOT / "dist"


def read_version() -> str:
    tree = ElementTree.parse(ADDON_DIR / "addon.xml")
    return tree.getroot().attrib["version"]


def build_zip(version: str) -> Path:
    DIST_DIR.mkdir(exist_ok=True)
    archive_base = DIST_DIR / f"skin.kodi4seniors-{version}"
    archive_path = shutil.make_archive(str(archive_base), "zip", ROOT, ADDON_DIR.name)
    return Path(archive_path)


def write_index(target_dir: Path, version: str) -> None:
    html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>skin.kodi4seniors</title>
  </head>
  <body>
    <h1>skin.kodi4seniors</h1>
    <p>Senior-friendly Kodi skin focused on Live TV, EPG and broadcaster catch-up services.</p>
    <ul>
      <li><a href="addon.xml">addon.xml</a></li>
      <li><a href="skin.kodi4seniors-{version}.zip">skin.kodi4seniors-{version}.zip</a></li>
    </ul>
  </body>
</html>
"""
    (target_dir / "index.html").write_text(html, encoding="utf-8")


def update_addons_xml(repo_root: Path) -> None:
    addon_files = sorted(repo_root.glob("repo/*/addon.xml"))
    addon_map = {}
    for addon_file in addon_files:
        root = ElementTree.parse(addon_file).getroot()
        addon_map[root.attrib["id"]] = root

    ordered_ids = []
    current_root = None
    try:
        git_xml = subprocess.run(
            ["git", "show", "HEAD:repo/addons.xml"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        current_root = ElementTree.fromstring(git_xml)
    except (subprocess.CalledProcessError, FileNotFoundError, ElementTree.ParseError):
        existing_addons_xml = repo_root / "repo" / "addons.xml"
        if existing_addons_xml.exists():
            current_root = ElementTree.parse(existing_addons_xml).getroot()

    if current_root is not None:
        for addon in current_root.findall("addon"):
            addon_id = addon.attrib.get("id")
            if addon_id in addon_map and addon_id not in ordered_ids:
                ordered_ids.append(addon_id)

    for addon_id in sorted(addon_map):
        if addon_id not in ordered_ids:
            ordered_ids.append(addon_id)

    addons = ElementTree.Element("addons")
    for addon_id in ordered_ids:
        addons.append(addon_map[addon_id])

    ElementTree.indent(addons, space="  ")

    xml_body = ElementTree.tostring(addons, encoding="unicode")
    xml_text = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n" + xml_body + "\n"
    addons_xml = repo_root / "repo" / "addons.xml"
    addons_xml.write_text(xml_text, encoding="utf-8")
    md5 = hashlib.md5(xml_text.encode("utf-8")).hexdigest()
    (repo_root / "repo" / "addons.xml.md5").write_text(md5, encoding="utf-8")


def publish(publish_repo: Path) -> Path:
    version = read_version()
    archive = build_zip(version)
    target_dir = publish_repo / "repo" / "skin.kodi4seniors"
    if target_dir.exists():
        shutil.rmtree(target_dir)
    shutil.copytree(ADDON_DIR, target_dir)
    shutil.copy2(archive, target_dir / archive.name)
    write_index(target_dir, version)
    update_addons_xml(publish_repo)
    return target_dir / archive.name


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish-repo", required=True, type=Path)
    args = parser.parse_args()
    archive = publish(args.publish_repo.resolve())
    print(archive)


if __name__ == "__main__":
    main()
