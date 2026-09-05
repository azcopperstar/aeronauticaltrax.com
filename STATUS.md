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

- [ ] **Screenshots.** The landing page has three empty slots (`.shots` section in
      `index.html`). Need two iPhone portrait captures and one Mac window capture. The
      section is currently three portrait boxes — rebuild it around the real aspect ratios
      once the images exist, since a Mac window is landscape.
- [ ] **Confirm the free vs paid split.** The pricing section currently claims the free tier
      is one vehicle plus maintenance and fuel logs, with everything else behind the $19.99
      unlock. That was a placeholder guess, not JP's actual plan.
- [ ] **Update App Store Connect URLs** — Privacy Policy, Support, and Marketing. The
      listing's privacy URL still points at a GitHub repo path that returns 404.
- [ ] **Review the legal pages.** `privacy.html` and `terms.html` are drafts written to match
      what the App Store listing already claims (no data collected, iCloud-only storage).
      Confirm that stays true once in-app purchase receipt checking ships.
- [ ] **Universal links** — add `.well-known/apple-app-site-association`. Needs the Apple
      Team ID and the bundle identifier.
- [ ] **Cancel the GoDaddy Website Builder subscription.** It serves nothing now.
- [ ] **Decide whether to publish the pricing section before launch.** It currently
      advertises free + $19.99, which is not live yet. The app is $0.99 today.

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
