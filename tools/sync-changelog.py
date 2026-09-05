#!/usr/bin/env python3
"""
Copy the app's changelog into the site repo, sanitised, and rebuild whatsnew.html.

    python3 tools/sync-changelog.py                  # default source path
    python3 tools/sync-changelog.py /path/to/changelog.md

Run this after shipping a build, then commit changelog.md and whatsnew.html together.

WHY THE SANITISE STEP MATTERS: this repo is public. Whatever lands in changelog.md is
readable at aeronauticaltrax.com/changelog.md and stays in git history forever. The
generated HTML hiding a value is not the same as the value being absent from the file,
so internal markers are stripped here, on the way in.
"""
import re
import sys
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_SRC = pathlib.Path(
    "/Users/xcodedev/Library/CloudStorage/Dropbox/xCode/LandShip/LandShip"
    "/0 Main/changelog.md"
)
DST = ROOT / "changelog.md"


def sanitise(text):
    """Strip internal-only markers. Returns (clean_text, [removed descriptions])."""
    removed = []

    def strip_build(m):
        removed.append(f"line {text[:m.start()].count(chr(10)) + 1}: "
                       f"Build: {m.group(1)}")
        return ""
    clean = re.sub(r"\s+Build:\s*(\S+)", strip_build, text)
    return clean, removed


def versions(text):
    return re.findall(r"^Version:\s*(\S+)", text, flags=re.M)


def main():
    src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SRC
    if not src.is_file():
        sys.exit(f"Source changelog not found: {src}")

    raw = src.read_text(encoding="utf-8")
    clean, removed = sanitise(raw)

    before = versions(DST.read_text(encoding="utf-8")) if DST.exists() else []
    after = versions(clean)
    new = [v for v in after if v not in before]

    unchanged = DST.exists() and DST.read_text(encoding="utf-8") == clean
    DST.write_text(clean, encoding="utf-8")

    print(f"source : {src}")
    print(f"target : {DST.relative_to(ROOT)}"
          + ("  (no change)" if unchanged else "  (updated)"))
    if removed:
        print("stripped before publishing:")
        for r in removed:
            print(f"  - {r}")
    else:
        print("stripped before publishing: nothing found")
    print(f"versions: {len(after)}"
          + (f"   NEW: {', '.join(new)}" if new else "   (no new versions)"))

    if re.search(r"\bBuild:", clean):
        sys.exit("REFUSING TO PUBLISH — a Build: marker survived the strip.")

    print()
    subprocess.run([sys.executable, str(ROOT / "tools" / "build-whatsnew.py")],
                   check=True)


if __name__ == "__main__":
    main()
