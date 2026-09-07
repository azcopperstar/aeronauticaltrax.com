#!/usr/bin/env python3
"""
Generate whatsnew.html from changelog.md.

    python3 tools/build-whatsnew.py

changelog.md is the same file the app shows as its splash screen, so it stays the
single source for release notes. Re-run this after editing it, then commit both.

Format it expects (blocks separated by a line of dashes):

    Version: 2026.09.02 Build: <codename>      <- Build is stripped from the site
    NOTES / ADDED / FIXED / CHANGED            <- section keywords, bare on a line
    ## Area                                    <- optional grouping inside a section
    - text before a colon: becomes the bold lead, the rest is detail

Empty sections and empty bullets are dropped.
"""
import html
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "vehicletrax" / "changelog.md"
OUT = ROOT / "vehicletrax" / "whatsnew.html"

SECTIONS = ("ADDED", "FIXED", "CHANGED", "NOTES")
SECTION_LABEL = {"ADDED": "Added", "FIXED": "Fixed",
                 "CHANGED": "Changed", "NOTES": "Notes"}


def parse(text):
    blocks, cur = [], None
    for raw in text.splitlines():
        line = raw.rstrip()
        if re.fullmatch(r"-{5,}", line.strip()):
            if cur:
                blocks.append(cur)
            cur = None
            continue
        m = re.match(r"^Version:\s*(.+)$", line)
        if m:
            if cur:
                blocks.append(cur)
            rest = m.group(1)
            build = None
            bm = re.search(r"\bBuild:\s*(\S+)", rest)
            if bm:
                build = bm.group(1)
                rest = rest[:bm.start()].strip()
            cur = {"version": rest.strip(), "build": build,
                   "sections": [], "_sec": None, "_area": None}
            continue
        if cur is None:
            continue
        if line.strip() in SECTIONS:
            cur["_sec"] = {"name": line.strip(), "groups": []}
            cur["sections"].append(cur["_sec"])
            cur["_area"] = None
            continue
        if line.startswith("## ") and cur["_sec"] is not None:
            cur["_area"] = {"area": line[3:].strip(), "items": []}
            cur["_sec"]["groups"].append(cur["_area"])
            continue
        if line.startswith("- ") or line.strip() == "-":
            body = line[2:].strip() if line.startswith("- ") else ""
            if not body or cur["_sec"] is None:
                continue
            if cur["_area"] is None:
                cur["_area"] = {"area": None, "items": []}
                cur["_sec"]["groups"].append(cur["_area"])
            cur["_area"]["items"].append(body)
    if cur:
        blocks.append(cur)

    for b in blocks:
        b.pop("_sec", None)
        b.pop("_area", None)
        b["sections"] = [s for s in b["sections"]
                         if any(g["items"] for g in s["groups"])]
        for s in b["sections"]:
            s["groups"] = [g for g in s["groups"] if g["items"]]
    return [b for b in blocks if b["sections"]]


def count(block, name):
    for s in block["sections"]:
        if s["name"] == name:
            return sum(len(g["items"]) for g in s["groups"])
    return 0


def pretty_version(v):
    return v.replace(".", "-") if re.fullmatch(r"\d{4}\.\d{2}\.\d{2}", v) else v


def bullet(item):
    """`lead: detail` -> bold lead + detail. A trailing colon is just a lead."""
    m = re.match(r"^(.{3,80}?):\s*(.*)$", item)
    if m and m.group(1).count(".") == 0:
        lead, detail = m.group(1).strip(), m.group(2).strip()
        if detail:
            return f'<strong>{html.escape(lead)}</strong> {html.escape(detail)}'
        return f'<strong>{html.escape(lead)}</strong>'
    return html.escape(item)


def render(blocks):
    out = []
    for i, b in enumerate(blocks):
        ver = pretty_version(b["version"])
        added, fixed = count(b, "ADDED"), count(b, "FIXED")
        chips = []
        if added:
            chips.append(f'<span class="rel-chip rel-added">{added} added</span>')
        if fixed:
            chips.append(f'<span class="rel-chip rel-fixed">{fixed} fixed</span>')
        latest = ' <span class="rel-chip rel-latest">Latest</span>' if i == 0 else ""
        body = []
        for s in b["sections"]:
            body.append(f'<h3 class="rel-sec">{SECTION_LABEL[s["name"]]}</h3>')
            for g in s["groups"]:
                if g["area"]:
                    body.append(f'<h4 class="rel-area">{html.escape(g["area"])}</h4>')
                body.append("<ul class=\"rel-list\">")
                body += [f"<li>{bullet(it)}</li>" for it in g["items"]]
                body.append("</ul>")
        out.append(
            f'<details class="release"{" open" if i == 0 else ""}>\n'
            f'  <summary><span class="rel-ver">{html.escape(ver)}</span>'
            f'{latest}{"".join(chips)}</summary>\n'
            f'  <div class="rel-body">\n    ' + "\n    ".join(body) +
            "\n  </div>\n</details>"
        )
    return "\n".join(out)


SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>What's new — VehicleTrax Complete Logbook</title>
<meta name="description" content="Release notes for VehicleTrax on iPhone, iPad and Mac — what was added, fixed and changed in each version.">
<meta name="apple-itunes-app" content="app-id=6751254040">
<meta property="og:type" content="website">
<meta property="og:site_name" content="VehicleTrax">
<meta property="og:title" content="What's new — VehicleTrax Complete Logbook">
<meta property="og:description" content="Release notes for VehicleTrax on iPhone, iPad and Mac — what was added, fixed and changed in each version.">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="icon" href="../assets/icons/vehicletrax-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="../assets/icons/vehicletrax-16.png" sizes="16x16" type="image/png">
<link rel="apple-touch-icon" href="../assets/icons/vehicletrax-180.png">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="masthead">
  <div class="wrap">
    <a class="brand-plate" href="../index.html">
      <img class="plate-mark" src="../assets/brand-instruments.webp" width="62" height="32" alt="" aria-hidden="true" decoding="async">
      <span>
        <span class="plate-wm">Aero<span class="wm-a">Nautical</span>Trax</span>
        <span class="plate-sub">VehicleTrax</span>
      </span>
    </a>
    <nav class="mast-nav" aria-label="Primary">
      <a class="opt" href="index.html#tracks">What it tracks</a>
      <a class="opt" href="index.html#pricing">Pricing</a>
      <a class="opt" href="../support.html">Support</a>
      <a class="btn btn-primary" href="https://apps.apple.com/us/app/vehicletrax/id6751254040">App Store</a>
    </nav>
  </div>
</header>
<main>
  <div class="wrap page-head">
    <p class="eyebrow">Release notes</p>
    <h1>What's new in VehicleTrax</h1>
    <p class="updated">The same notes the app shows you after an update. Newest first — open any
    version to read what changed.</p>
  </div>

  <div class="wrap prose">
__RELEASES__
    <p class="rel-foot">Found something broken, or want a feature? Write to
      <a href="mailto:info@aeronauticaltrax.com">info@aeronauticaltrax.com</a> — it reaches
      the developer directly. Requests from owners drive most of what ships.</p>
  </div>
</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <span class="brand-name">VehicleTrax</span>
        <p class="brand-sub">Tucson, Arizona</p>
      </div>
      <nav class="foot-links" aria-label="Footer">
        <a href="../index.html">All apps</a>
        <a href="https://apps.apple.com/us/app/vehicletrax/id6751254040">App Store</a>
        <a href="whatsnew.html">What's new</a>
        <a href="../support.html">Support</a>
        <a href="../privacy.html">Privacy Policy</a>
        <a href="../terms.html">Terms of Use</a>
      </nav>
    </div>
    <p class="foot-legal">
      &copy; 2026 AeroNauticalTrax. All rights reserved. Apple, iPhone, iPad, Mac and iCloud
      are trademarks of Apple Inc.
    </p>
  </div>
</footer>
</body>
</html>
"""

def main():
    blocks = parse(SRC.read_text(encoding="utf-8"))
    OUT.write_text(SHELL.replace("__RELEASES__", render(blocks)), encoding="utf-8")
    print(f"{OUT.parent.name}/{OUT.name}: {len(blocks)} releases")
    for b in blocks:
        print(f"  {pretty_version(b['version']):<12} "
              f"added {count(b,'ADDED'):>3}  fixed {count(b,'FIXED'):>3}  "
              f"changed {count(b,'CHANGED'):>3}  notes {count(b,'NOTES'):>3}"
              + (f"   [build '{b['build']}' stripped]" if b["build"] else ""))

if __name__ == "__main__":
    main()
