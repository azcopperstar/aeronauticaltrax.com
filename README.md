# aeronauticaltrax.com

Marketing and support site for **VehicleTrax**, the vehicle maintenance app for iPhone,
iPad and Mac. Plain static HTML — no build step, no dependencies, no framework.

## Structure

```
index.html          landing page
privacy.html        privacy policy  (App Store requires a working URL for this)
support.html        support page + FAQ  (App Store support URL)
terms.html          terms of use / EULA supplement
404.html            not-found page (GitHub Pages serves this automatically)
assets/style.css    all styling, light + dark themes via CSS custom properties
CNAME               custom domain for GitHub Pages
robots.txt          crawler policy
sitemap.xml         page list for search engines
```

## Previewing locally

```sh
cd ~/Sites/aeronauticaltrax.com
python3 -m http.server 8000
# open http://localhost:8000
```

Use a server rather than opening the file directly — the pages link `/assets/style.css`
with a root-relative path, which only resolves over HTTP.

## Deploying

The site is published with **GitHub Pages** from the `main` branch, with the domain
registered at GoDaddy pointing here via DNS.

### One-time setup

1. Create a **public** repository on GitHub named `aeronauticaltrax.com`.
   (GitHub Pages requires a public repo on free accounts.)
2. Connect this folder and push:

   ```sh
   cd ~/Sites/aeronauticaltrax.com
   git remote add origin https://github.com/<username>/aeronauticaltrax.com.git
   git branch -M main
   git push -u origin main
   ```

3. In the repo on GitHub: **Settings → Pages**. Set Source to
   *Deploy from a branch*, branch `main`, folder `/ (root)`. Save.
4. Wait for the first build, then confirm the site loads at
   `https://<username>.github.io/aeronauticaltrax.com/`.
   **Verify it works here before touching DNS.**
5. In **Settings → Pages → Custom domain**, enter `aeronauticaltrax.com` and save.
6. Add the DNS records below at GoDaddy.
7. Once the domain resolves, return to Settings → Pages and tick **Enforce HTTPS**.
   This can take up to 24 hours to become available while the certificate is issued.

### DNS records at GoDaddy

Delete any existing `A` record on `@` (it currently points at the Website Builder site)
and any conflicting `www` record, then add:

| Type  | Name | Value                  |
|-------|------|------------------------|
| A     | @    | 185.199.108.153        |
| A     | @    | 185.199.109.153        |
| A     | @    | 185.199.110.153        |
| A     | @    | 185.199.111.153        |
| AAAA  | @    | 2606:50c0:8000::153    |
| AAAA  | @    | 2606:50c0:8001::153    |
| AAAA  | @    | 2606:50c0:8002::153    |
| AAAA  | @    | 2606:50c0:8003::153    |
| CNAME | www  | `<username>.github.io.` |

The AAAA records are optional but recommended. DNS changes can take up to 24 hours to
propagate, though GoDaddy is usually much faster.

### Publishing a change afterwards

```sh
git add -A && git commit -m "Update copy" && git push
```

GitHub Pages rebuilds within a minute or two.

## Still to do

- [ ] Replace the three screenshot slots on the landing page with real captures
- [ ] Confirm the support email address (currently `support@aeronauticaltrax.com`)
- [ ] Confirm the free vs. paid feature split in the pricing section
- [ ] Update the App Store Connect **Privacy Policy URL** to
      `https://aeronauticaltrax.com/privacy.html` (the current GitHub URL 404s)
- [ ] Update the App Store Connect **Support URL** to
      `https://aeronauticaltrax.com/support.html`
- [ ] Add `.well-known/apple-app-site-association` for universal links
      (needs the Team ID and bundle identifier)
- [ ] Decide whether to publish the free/$19.99 pricing section before launch
