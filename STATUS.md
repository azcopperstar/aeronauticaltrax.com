# Project status — aeronauticaltrax.com

Last updated: **September 5, 2026**

If you are picking this up in a new Claude session, read this file first. It is the
handoff note: what exists, what was decided, and what is still open.

---

## Where things stand

The site is **live** at <https://aeronauticaltrax.com> with HTTPS enforced. It replaced a
GoDaddy Website Builder placeholder that had been sitting on the domain.

| Thing | Value |
|---|---|
| Live URL | https://aeronauticaltrax.com |
| Repo | https://github.com/azcopperstar/aeronauticaltrax.com (public) |
| Hosting | GitHub Pages, deploy from `main` branch, `/ (root)` |
| Domain | Registered at GoDaddy; DNS only — GoDaddy hosting is not used |
| DNS | Four `A` records on `@` → 185.199.108–111.153; `CNAME` on `www` → azcopperstar.github.io |
| HTTPS | Enforced (GitHub-issued certificate) |
| Contact | support@aeronauticaltrax.com (mailbox created Sept 5, 2026) |

### Pages

```
index.html      landing page
privacy.html    privacy policy   <- App Store Privacy Policy URL should point here
support.html    support + FAQ    <- App Store Support URL should point here
terms.html      terms of use
404.html        not-found page
assets/style.css   all styling
CNAME           managed by GitHub, do not edit by hand
```

---

## Still to do

- [ ] **Ship the receipt logic.** The site now promises, in three places, that existing
      $0.99 purchasers are unlocked to the full version for free. That promise is only good
      if the entitlement check actually ships with the free-tier release.
- [ ] **Upload the Mac screenshots.** The eight 2880x1800 shots in
      `screenshots-appstore/mac/` still have nowhere to go — the macOS version 2026.5.21 is
      Ready for Distribution and its media is locked. Upload them with the next macOS
      version, same order as the other platforms.

      iPhone and iPad were uploaded and verified Sept 5, 2026: iPhone 6.9" holds the eight
      in order 01-08, the nine old 6.5" shots were deleted (Apple scales the largest size
      down for every smaller device, so they were redundant), and iPad 13" holds its eight
      in order with the three old ones removed.

      **Gotcha worth remembering:** dragging all eight files in at once uploads them in
      COMPLETION order, not filename order — the first attempt landed as
      03, 07, 02, 08, 01, 06, 04, 05. Drag them in ONE AT A TIME in filename order, or be
      prepared to drag thumbnails around afterwards. Order matters: it is the order buyers
      see, and the first three are what appear on the app installation sheet.
- [ ] **Swap `02-dashboard.png` once the count string is fixed.** The dashboard reads
      "Totals limited to 7 of 3 vehicles" in the iPhone and iPad shots. Shipped as-is by
      choice on Sept 5, 2026.
- [ ] **macOS Support and Marketing URLs.** Still `http://aeronauticaltrax.com` and empty.
      The macOS version 2026.5.21 is Ready for Distribution, so its metadata is locked —
      only Promotional Text is editable. Set these on the next macOS version.
- [ ] **Review the legal pages.** `privacy.html` and `terms.html` are drafts written to match
      what the App Store listing already claims (no data collected, iCloud-only storage).
      Confirm that stays true once in-app purchase receipt checking ships.
- [ ] **Universal links** — add `.well-known/apple-app-site-association`. Needs the Apple
      Team ID and the bundle identifier.
- [ ] **Cancel the GoDaddy Website Builder subscription.** It serves nothing now.

---

### Screenshots — done Sept 5, 2026

All three platforms recaptured in **light** appearance, same eight screens in the same
order everywhere: vehicles, dashboard, fuel logs, service, parts, checklists, travel logs,
trip report.

| Set | Size | Location |
|---|---|---|
| iPhone | 1320x2868 portrait | `screenshots-appstore/iphone/` |
| iPad | 2752x2064 landscape | `screenshots-appstore/ipad/` |
| Mac | 2880x1800 (16:10) | `screenshots-appstore/mac/` |

All RGB with the alpha channel stripped — Apple rejects PNGs carrying transparency.
Raw captures live in `screenshots-raw/`; that folder and `screenshots-appstore/` are both
gitignored, so only the three web images in `assets/shots/` are tracked.

What was learned doing it, so it does not have to be learned again:

- **Simulator status bar.** `xcrun simctl status_bar booted override --time "9:41" ...`
  on ONE line — a line-continuation paste silently no-ops. `booted` fails when several
  simulators are running, so `xcrun simctl shutdown all` first. iPad takes no cellular
  flags.
- **Capture straight to the folder:** `xcrun simctl io booted screenshot <path>` for
  simulators, `screencapture -o -w <path>` on the Mac (`-o` drops the window shadow, which
  is what would otherwise introduce transparency).
- **Mac resolution depends on the display.** The external 1080p monitor is 1x and yields
  only 1920x1050, which caps out at Apple's 1440x900. The MacBook's built-in Retina screen
  yields 3420x2146, which downscales cleanly to 2880x1800. Always shoot Mac shots on the
  laptop's own screen.
- **A Mac window capture is never 16:10** — it gets centered on a 16:10 canvas padded with
  the site's `--ground` colour. At 3420x2146 the padding is only 5px a side.
- **Verify before shooting the whole set:** dimensions, brightness (light shots measure
  ~230-245 mean luma; a dark set measures ~37) and eyes on the actual image. Checking only
  one of those three cost two full recaptures of the Mac set.
- **Excluded on purpose:** the What's New / release-notes overlay, which exposed the
  internal build codename.

The landing page `.shots` section was rebuilt at the same time — Mac full-width above two
iPhone shots, each in its own framed container so it reads correctly in both themes.
Web images are WebP: 640px wide for the phones, 1280px for the Mac.

---

### Icons (Sept 6, 2026)

Three app icons drawn from the original photographic icon: the chart is the shared
background, tinted per product (sepia / blue / green), with a brass instrument lying on it
low-right, tilted 19 degrees and foreshortened to 86% so it reads as an object on paper.
VehicleTrax gets a gauge, AeroTrax an attitude indicator, NauticalTrax a ship's compass
(graduated card and lubber line — not a pocket rose).

Generated by a script, not hand-drawn: size, offset, tilt, squash and tints are all
parameters, so the whole family rebuilds in seconds. **That script lives outside this repo**
— ask before assuming it is here.

On the site:

```
assets/icon-*.png, assets/brand-mark.webp        AeroNauticalTrax parent brand (hub +
                                                 shared support/privacy/terms/404)
assets/icons/<app>-mark-128.webp                 hub card icon, 44px
assets/icons/<app>-mark-60.webp                  product page masthead, 30px
assets/icons/<app>-{180,32,16}.png               per-product favicons
```

**Small sizes use a CROP of the instrument, not the shrunken tile.** The full tile at 44px
is a dark square with a speck in it — the same lesson as the original photographic favicon.
Only use the full tile where it renders large.

**The App Store icons are NOT the site's copies.** Those were delivered separately as
`AppIcon.appiconset` folders plus 1024 marketing icons, and have not been installed in any
Xcode target.

**VehicleTrax's site icon now differs from its shipped App Store icon.** The site shows the
new gauge; the App Store still shows the original photograph. Ship the new icon with the
next version, or revert the site — do not leave them apart for long.

---

### Brand logo (Sept 7, 2026)

**The masthead carries the brand lockup on every page (Sept 7, 2026).** `assets/brand-instruments.webp`
(the three instruments cropped out of `logo.webp` at 292x152, displayed 73x38) plus the wordmark
as **live text**, not an image: `Aero<span class="wm-a">Nautical</span>Trax` in Archivo 800 with
`.wm-a` in the accent colour. The product name sits underneath in `.brand-sub` — "AeroTrax",
"NauticalTrax", "VehicleTrax", or empty on the hub and the shared pages.

Why live text and not `logo.webp` itself: at 44px tall the full lockup's wordmark is about 6px
of cap height and turns to mush, and the three instruments blur into one blob. It only becomes
legible around 60px, which would mean a 92px sticky bar on every page. Live text is sharp at any
size and density and costs no height. Do not swap it back for the image.

The shared pages (404, privacy, support, terms) used to show "VehicleTrax" as the brand name — a
leftover from the single-product site. They now show the brand with no product sub-line.

Sizes step down twice: below 900px the mark is 50x26 and the wordmark 0.98rem; below 640px it is
61x32 and 1rem. Without those steps the wider lockup pushes the nav onto a second row on tablets.


`assets/logo.webp` — chart background, the three brass instruments overlapping, wordmark
with "Nautical" in the accent colour. Sits top-left of the hub above the h1, 420px wide
(300px below 560px viewport), framed with the site's border/radius/shadow.

Two things that matter if it is ever regenerated:

- **The logo's instruments are ROUND; the icons' are foreshortened to 86%.** The squash
  reads as perspective inside a small app tile and as "skewed" at logo size. Do not reuse
  the icon renders in the logo.
- **No tagline in the on-page logo.** At 420px it renders about 4px tall. A version with
  the tagline exists among the masters for large-format use only.

The `<h1>` is still real text — the logo is an `<img>` with alt text above it, never the
heading itself.

Masters (full-resolution PNG, plus horizontal / stacked / mark-only variants with tagline)
were produced outside this repo and are not tracked here. The script that draws the
instruments also lives outside the repo — ask before assuming either is available.

---

### App Store names (settled Sept 6, 2026)

| App | Name (30 cap) | Subtitle (30 cap) |
|---|---|---|
| Vehicle | `VehicleTrax Complete Logbook` (28) | `Service, fuel, parts and costs` (30) |
| Aero | `AeroTrax Complete Logbook` (25) | `Airframe, engine, pilot time` (28) |
| Nautical | `NauticalTrax Complete Logbook` (29) | `Boat upkeep and sea service` (27) |

**"Complete" was added Sept 7, 2026.** All three still fit the 30-character cap, with one
character to spare on NauticalTrax — any further addition will not fit.

**"Logbook" is the umbrella word on purpose.** A logbook records operations, not just
repairs — voyages, hours, fuel, work done, who was aboard — which is the actual feature
set. It is also domain-native to aviation and marine, where AeroTrax and NauticalTrax
track operator time toward credentials. "Maintenance" was rejected as too narrow;
"Records" as unsearchable and filing-cabinet.

The Subtitle field is ALSO indexed for App Store search, so the domain keywords live
there rather than being crammed into the name.

**Where the verbose name is allowed on the site (decided Sept 7, 2026):** page `<title>`,
`og:title` and both meta descriptions ONLY. Never in mastheads, `<h1>`s, card titles or
body copy — those keep the short product name, which is what the app itself, the home
screen and customers all call it. Store names change; keeping them in three files rather
than dozens is deliberate.

`vehicletrax/whatsnew.html` is generated — its title lives in `tools/build-whatsnew.py`
and must be changed there too.

**Watch this one:** the store name now says "Complete" while the trial caps you at 2
vehicles and 10 records per table. "Complete" describes the product's scope, not the
trial's state, but a buyer can read it the other way. Make sure the subtitle and
description make "free to try" unmistakable.

Two things to remember:

- `CFBundleDisplayName` is a separate field and controls the home-screen icon label,
  which truncates near 12 characters. Keep it at `VehicleTrax` / `AeroTrax` /
  `NauticalTrax` — the longer store name costs nothing where users look daily.
- VehicleTrax is already live as plain `VehicleTrax`. A name change is staged metadata:
  it goes live with the next version release, not on save.

---

### Site structure (restructured Sept 5, 2026)

The domain is the **AeroNauticalTrax** brand hub; each product gets a folder.

```
/                      brand hub — the three apps, shared principles
/vehicletrax/          product page (was / until Sept 5)
/vehicletrax/whatsnew.html   release notes  (generated)
/vehicletrax/changelog.md    release notes  (source, synced from the app)
/aerotrax/             product overview — app in development
/aerotrax/aircraft/    pillar page — maintenance, ADs, inspection cycles, component times
/aerotrax/parts/       pillar page — traceability, approval basis, life limits
/aerotrax/fuel/        pillar page — uplift, density, invoice, burn, tankering
/aerotrax/pilot/       pillar page — flight logbook, currency, certificates
/nauticaltrax/         product overview — app in development
/nauticaltrax/vessel/  pillar page — engine hours, haul-out cycle
/nauticaltrax/sea-service/  pillar page — days underway toward a credential
/support.html          shared across all products
/privacy.html          shared
/terms.html            shared
/assets/               shared styles, icons, screenshots
/tools/                generators
```

**Product pages are split into an overview plus one pillar page each (Sept 7, 2026).**
The overview carries the hero, spec strip, a "What it tracks" card grid linking to each
pillar, the shared-engine list and pricing. Each pillar page carries that pillar's full
depth, and ends with a "Keep reading" row linking the others. The masthead nav is the
pillar list. Reasons: each page targets its own search query instead of one page competing
with itself; depth becomes linkable; and the nav stopped crowding.

**`tools/split-product-pages.py` performed the migration and is NOT re-runnable as-is.**
It reads a *pre-split* product `index.html` (one page with `#tracks`, `#parts`, … sections),
extracts the hero, spec strip, pillar sections, shared-engine and pricing blocks, and writes
the overview plus every pillar page. Running it again after the split fails with
`AssertionError: tracks`, because the overview it produced no longer contains those sections.
To re-run it you must first restore the pre-split page:
`git show <commit>:aerotrax/index.html > aerotrax/index.html`. Note `git checkout -- <file>`
fails on this machine ("Operation not permitted") because the sandbox cannot unlink; the
`git show >` redirect writes in place and works.

**Day to day, edit the pillar pages directly.** To add a new pillar, copy an existing pillar
page, add it to the `PRODUCTS` config in the tool (for the record), add its card to the
overview's `#explore` grid, add it to the masthead nav on every page of that product, and add
its URL to `sitemap.xml`. Relative-path depth is `../` on an overview and `../../` on a pillar
page — getting this wrong is the easiest way to break the stylesheet link.

**Reference lists use `<details class="reveal" open>`, defaulted OPEN.** Safari still does
not auto-expand `<details>` for find-in-page (Chrome/Edge do since 2022, Firefox since v148
in Feb 2026), and this audience is Apple-heavy. Collapsing by default would hide content from
Cmd-F. Keep them open.

**Footers are per-location, standardised Sept 6, 2026.** Shared pages list the three
products then the shared pages; each product page leads with "All apps" and then only what
belongs to that product. Do not put a VehicleTrax App Store link or its release notes in
the footer of a shared page — that was a leftover from the single-product site.

**`vehicletrax/whatsnew.html` is generated**, footer included. Change a footer there and
`tools/build-whatsnew.py` must change with it, or the next changelog sync reverts it.

`AeroTrax` and `NauticalTrax` have full product pages as of Sept 6, 2026, linked from the
hub and in the sitemap. **Neither app exists yet**, so each page carries three separate
signals: an "In development" chip in the masthead, a "Not yet available" banner across the
top of the page, and a pricing section that states nothing is on sale. The hub cards link
with "What it will do" rather than a download verb. Keep all of that until each app ships —
the site must never imply something is buyable before it is.

Each product page also carries a **"What this is not" disclaimer** under Pricing. Those are
not decoration: the pages make regulatory-adjacent claims (an FAA-style pilot logbook, sea
service toward a Merchant Mariner Credential), so the caveat belongs where the claim is
made, not only in the App Store description. Review that wording before launch.

The two new pages describe features that are planned, not shipped. Before either launches,
re-read them against what the first build actually does and cut anything that did not make
it. The hero panels use plausible sample intervals (transponder/static 24 months, 100-hour,
annual; zincs 6 months, impeller 250 hrs, bottom paint 24 months) — JP should confirm those
are right, since wrong figures lose exactly the readers these pages are for.

When one ships, give it its own `changelog.md` and a generator target alongside
VehicleTrax's.

Legal and support pages are deliberately SHARED. That holds only while all products
collect no data and sync via iCloud. The moment one of them differs, split them per
product before shipping it.

**Paths matter here.** Pages under `/vehicletrax/` reference `../assets/…` and `../support.html`;
the hub uses `assets/…`. Relative links only — absolute paths break the `github.io` test URL.

**Still pointing at the old location:** the App Store Connect Marketing URL is
`https://aeronauticaltrax.com`, which is now the hub rather than the VehicleTrax page. That
still resolves and is defensible, but `https://aeronauticaltrax.com/vehicletrax/` is the
more accurate target. Support and Privacy URLs are unaffected — those pages are shared and
did not move.

---

### Release notes — how they get published

`whatsnew.html` is GENERATED. Never edit it by hand; the next sync overwrites it.

The app keeps the master copy bundled at
`Dropbox/xCode/LandShip/LandShip/0 Main/changelog.md`. After shipping a build:

```sh
cd ~/Sites/aeronauticaltrax.com
python3 tools/sync-changelog.py     # copies + sanitises + rebuilds
```

then commit `changelog.md` and `whatsnew.html` together. The script strips the
`Build: <codename>` marker on the way in and refuses to publish if one survives — this
repo is public, so anything written into `changelog.md` is readable at
`aeronauticaltrax.com/changelog.md` and stays in git history. Hiding a value in the
rendered HTML is NOT the same as it being absent from the file; sanitise on copy.
Do not name the codename anywhere in this repo, including in comments and notes.

`.nojekyll` is present so GitHub Pages serves `changelog.md` byte-for-byte rather than
letting Jekyll reinterpret it. That keeps the raw URL stable if the app is ever changed
to fetch its release notes from the site instead of a bundled copy — the one-copy end
state. Deferred deliberately (Sept 5, 2026): it adds a network dependency to something
that currently works fully offline, and VehicleTrax users are often out of signal.

---

## Decisions already made (don't relitigate without reason)

- **Waving flag backdrop on the hub only** (added Sept 7, 2026). `index.html` carries a
  `.flagbg` div right after `<body>`: an inline SVG US flag, fixed to the viewport, behind
  everything. It is decorative (`aria-hidden`), so it stays out of the accessibility tree.
  How it is built and why each number is what it is:
  - **Opacity `.085`** on `.flagbg`. Five intensities were rendered side by side before
    picking this one. Anything at or above `.10` puts the canton's hard vertical edge
    through the "Everything on record." headline; below `.06` it stops reading as a flag.
    This is the single knob — change the opacity, nothing else, to tune it.
  - **The canton is pushed to the top-left corner** (`svg` at `168%`, offset `-22% / -26%`)
    with a radial mask fading from `8% 0%`. That keeps the hard blue rectangle out of the
    headline's way and puts the stripes, which are much quieter, across the body copy.
  - **Two animations.** A CSS `flag-sway` transform (12s, cheap — GPU compositing) and an
    SVG `feTurbulence` + `feDisplacementMap` ripple whose `baseFrequency` animates over 12s.
    Both periods match so the loop is seamless. **The turbulence is the expensive one** — it
    recomputes noise every frame across the whole viewport. If battery on a laptop ever
    becomes a complaint, drop the `<animate>` inside `feTurbulence` and keep the sway; that
    loses very little and costs nearly nothing.
  - **`prefers-reduced-motion` disables both** the animation and the filter, leaving a
    crisp static flag. WCAG asks that motion running over five seconds be pausable; this is
    how that is satisfied. Do not remove that block.
  - **Narrow screens get their own rule** (`max-width: 700px`), and it bit once — worth
    understanding before touching it. `preserveAspectRatio="slice"` on a portrait viewport
    zooms the flag until only a grey smudge shows, so under 700px the svg is *fitted*
    instead (`aspect-ratio: 3 / 2; height: auto`). But a fitted flag has a bottom EDGE, and
    the first attempt left the mask ~50% opaque where that edge fell — which rendered as a
    hard-edged rectangular banner across the top of the page, not a backdrop. That is what
    "big flag banner" means if it ever comes back. Two things prevent it now:
      1. the flag is deliberately oversized (`width: 230%`), so its bottom edge sits at
         68-86% of viewport height across every phone size;
      2. the mask reaches fully transparent by ~44% of viewport height, well above it.
    The narrow mask is **radial from the top-left**, not a linear top-to-bottom fade — a
    linear fade leaves the canton's right edge showing as a blue block. Verified at
    390x844, 430x932 and 513x888, light and dark. Change one of these numbers and re-check
    the others.
  - **Content is lifted above it** by `body > header, body > main, body > footer { z-index: 1 }`
    in `style.css`. That rule is global and harmless on pages with no `.flagbg`.
  - **The masthead and the app cards stay opaque**, so the flag never sits under body text
    inside a card — it only shows through the page ground.
  - If it is ever wanted on the product pages too, copy the `.flagbg` div into them; the CSS
    already lives in the shared stylesheet.

- **The domain is the VehicleTrax site.** "AeroNauticalTrax" is the maker name in the
  footer. The old aviation tagline is gone. Revisit only if an aviation product appears.
- **No hero screenshot.** The right side of the hero is a hand-built maintenance panel
  showing real-looking service intervals with green/amber/red status. It demonstrates the
  app's job without needing an image, and it should stay even after screenshots are added.
- **Typography** is Archivo (display) over IBM Plex Sans (body), with IBM Plex Mono for all
  figures — a logbook/instrument feel rather than generic SaaS.
- **Color** is a token system in `assets/style.css`. The green/amber/red accents are the
  app's own maintenance states, not decoration. Light and dark both work off the same
  tokens; never define a color only inside a media query. There are TWO dark blocks — the
  `prefers-color-scheme` media query and `:root[data-theme="dark"]` — and they must be kept
  identical; change one, change both.
- **`--accent` is for fills, `--accent-text` is for type** (added Sept 5, 2026). The vivid
  orange passes contrast as a button background with white on it, but fails as text on the
  light ground, so text uses a deeper tone. Don't collapse them back into one token.
- **Dark mode was rebalanced Sept 5, 2026** away from near-black. The ground moved
  `#0F1517` -> `#171F22` with surfaces and lines lifted to match, and body text from a grey
  `#A2AFAB` to a muted white `#C5CFCB`. The problem was never too little contrast — headings
  measured 15.4:1, high enough to halate against near-black while the grey body text read
  dim beside them. Body text is now 10.5:1 and muted text 7.8:1. If dark mode ever feels
  hard to read again, check whether contrast is too HIGH before pushing it higher.
- **It is a TRIAL, not a free tier** (corrected Sept 5, 2026 — an earlier draft had this
  wrong). The trial is a free download and does not expire. Exactly three things are
  restricted, confirmed against the shipping implementation Sept 5, 2026:

  1. **2 vehicles**, and **10 records** in every other capped table (Parts, Fuel Log,
     Travel Log, Service Records, Service Items, Systems, Vendors, Improvements,
     Expenditures, Project items, Checklists, Checklist items, Warranties, Scale Tickets,
     Serial Numbers). Settings is exempt and never capped.
  2. **PDF export, print and share** — including the Print button in every report, the
     macOS Cmd-P / right-click / File > Print paths, and the Checklist report's Save As /
     Share. Viewing a report on screen stays free.
  3. **Automatic backups** (Settings > Automatic Backups). Manual backup and restore stay
     free in the trial on purpose, so a trial user is never locked out of their own data —
     which also reads better to App Review.

  Everything else is identical between trial and full. The $19.99 one-time purchase lifts
  all three. Written this way in the pricing section, one FAQ answer and `terms.html`; keep
  those in step, and keep them in step with the app — the site is now making three specific
  promises about what the trial does and does not do.
- **All $0.99 / "introductory price" language is gone from the site** (Sept 5, 2026). The
  trial ships shortly, so the page describes the trial model only rather than hedging about
  what is on sale today. The one place the old paid app is acknowledged is the FAQ answer
  for earlier purchasers, worded as "bought VehicleTrax as a paid app" without a price.
- **App Store Connect URLs were fixed Sept 5, 2026** (app ID 6751254040). Privacy Policy
  URL → `https://aeronauticaltrax.com/privacy.html` (was a GitHub repo path returning 404).
  On the iOS 2026.7.19 version: Support URL → `.../support.html` (was `http://` on the
  apex), Marketing URL → `https://aeronauticaltrax.com` (was empty). All three are staged,
  not live — Apple releases metadata changes with the next app version.
- **Existing $0.99 purchasers get the full version free.** Stated in the FAQ and in
  `terms.html`. Only keep that promise if the receipt logic actually ships.

---

## How to publish a change

1. Edit the files
2. GitHub Desktop → write a short summary → **Commit to main**
3. **Push origin**

GitHub Pages rebuilds in a minute or two. Hard-refresh with **⌘⇧R** — a normal refresh
usually serves the cached old version and looks like a failure.

### Preview locally first

```sh
cd ~/Sites/aeronauticaltrax.com
python3 -m http.server 8000
# http://localhost:8000
```

Use a server, not `open index.html` — file:// URLs behave differently.

---

## Gotchas that already bit once

**`overflow-x: hidden` on `body` silently breaks `position: sticky`.** It makes `body` a
scroll container, so a sticky masthead resolves against that box instead of the viewport and
simply never pins — with no error anywhere. The masthead was made sticky on Sept 7, 2026 and
this had to be changed to `overflow-x: clip`, which still prevents sideways scroll but does
not create a scroll container. Do not change it back to `hidden`.

**A pinned masthead swallows anchor targets.** `html { scroll-padding-top: 5.25rem }` keeps
`#pricing` and friends clear of the ~69px bar. If the header height changes, change that too.


- **Use relative links** (`assets/style.css`, `privacy.html`), never absolute (`/assets/...`).
  Absolute paths break on the `github.io` test URL, where the site sits in a subfolder.
- **`CNAME` is GitHub's file.** It gets created and updated when the custom domain is set in
  Settings → Pages. After changing the domain there, **Pull origin** before you commit
  anything else, or your next push conflicts.
- **Pull before editing** if the repo is cloned in more than one place.
- **Set the commit email in GitHub Desktop → Settings → Git** to
  `28052567+azcopperstar@users.noreply.github.com`. A fresh clone does not inherit it, and
  this is a public repo — the default would expose a personal address.
- **Git left stale `.git/*.lock` files** at one point. If a commit ever fails complaining
  about a lock, delete `.git/index.lock` and try again.
