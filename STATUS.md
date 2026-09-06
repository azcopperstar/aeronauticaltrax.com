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

### App Store names (settled Sept 6, 2026)

| App | Name (30 cap) | Subtitle (30 cap) |
|---|---|---|
| Vehicle | `VehicleTrax Logbook` (19) | `Service, fuel, parts and costs` (30) |
| Aero | `AeroTrax Logbook` (16) | `Airframe, engine, pilot time` (28) |
| Nautical | `NauticalTrax Logbook` (20) | `Boat upkeep and sea service` (27) |

**"Logbook" is the umbrella word on purpose.** A logbook records operations, not just
repairs — voyages, hours, fuel, work done, who was aboard — which is the actual feature
set. It is also domain-native to aviation and marine, where AeroTrax and NauticalTrax
track operator time toward credentials. "Maintenance" was rejected as too narrow;
"Records" as unsearchable and filing-cabinet.

The Subtitle field is ALSO indexed for App Store search, so the domain keywords live
there rather than being crammed into the name.

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
/vehicletrax/          the VehicleTrax product page (was / until Sept 5)
/vehicletrax/whatsnew.html   VehicleTrax release notes  (generated)
/vehicletrax/changelog.md    VehicleTrax release notes  (source, synced from the app)
/support.html          shared across all products
/privacy.html          shared
/terms.html            shared
/assets/               shared styles, icons, screenshots
/tools/                generators
```

`AeroTrax` (small aircraft) and `NauticalTrax` (small/mid-size boats) are named on the hub
and marked **In development**, with no download or purchase links and an explicit "Not yet
available" line on each card. They stay that way until the apps are real — the site should
never imply something is buyable before it is. When one ships, give it `/aerotrax/` with
its own `changelog.md`, and add a generator target alongside VehicleTrax's.

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
