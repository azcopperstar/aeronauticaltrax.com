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
- [ ] **Upload the screenshots.** All three sets are built and sitting in
      `screenshots-appstore/`; nothing has been uploaded to App Store Connect yet.
      iPhone 6.9" is empty on the listing and 6.5" still holds 9 old shots (some are
      camera-roll `IMG_99xx.jpeg` files) — delete those once 6.9" is filled, since Apple
      scales the largest size down for every smaller device. iPad 13" holds 3 old shots to
      replace. The Mac slot is locked until the next macOS version.
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
  internal build name "FlightTest".

The landing page `.shots` section was rebuilt at the same time — Mac full-width above two
iPhone shots, each in its own framed container so it reads correctly in both themes.
Web images are WebP: 640px wide for the phones, 1280px for the Mac.

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
  tokens; never define a color only inside a media query.
- **It is a TRIAL, not a free tier** (corrected Sept 5, 2026 — an earlier draft had this
  wrong). The trial is a free download limited to **2 vehicles, 10 records per table, and
  PDF reports that display on screen but cannot be exported**. It does not expire. The
  $19.99 one-time purchase removes all three limits. Written this way in the pricing
  section, two FAQ answers and `terms.html`; keep those in step.
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
