import os, re

ROOT = os.path.expanduser('~/mnt/aeronauticaltrax.com')
SITE = 'https://aeronauticaltrax.com'

PRODUCTS = {
 'aerotrax': dict(
   display='AeroTrax', icon='aerotrax',
   pillars=[
     ('aircraft',  'tracks',  'The aircraft', 'Aircraft maintenance tracking',
      'Hobbs and tach time, airworthiness directives, inspection cycles and component times &mdash; each on its own clock, calendar or hours.'),
     ('parts',     'parts',   'The parts', 'Aircraft parts and traceability',
      '8130-3 tags, approval basis and source traceability, alongside life limits, cycles and the install history behind them.'),
     ('fuel',      'fuel',    'The fuel', 'Aircraft fuel tracking',
      'Uplift, density and the whole invoice &mdash; burn, economy and what a stop actually cost, for pistons and turbines alike.'),
     ('pilot',     'logbook', 'The pilot', 'Pilot logbook and currency',
      'PIC, night, instrument, cross-country and landings, with currency and a flight review date calculated rather than remembered.'),
   ],
   explore_title='Four records, one airplane.',
   explore_lede='Each one is its own problem with its own clock, so each gets its own page rather than a paragraph. Start wherever the question you came with lives.'),
 'nauticaltrax': dict(
   display='NauticalTrax', icon='nauticaltrax',
   pillars=[
     ('vessel',      'tracks',  'The vessel', 'Boat maintenance tracking',
      'Engine hours, calendar dates and the haul-out cycle &mdash; a season that starts and ends, and work that only happens out of the water.'),
     ('sea-service', 'seatime', 'Sea service', 'Sea service and credentials',
      'Days underway recorded per voyage rather than reconstructed years later, totalling toward a Merchant Mariner Credential.'),
   ],
   explore_title='Two records, one boat.',
   explore_lede='The vessel keeps its own time and so do you. Each gets its own page rather than a paragraph.'),
}

def load(product):
    return open(os.path.join(ROOT, product, 'index.html'), encoding='utf-8').read()

def block(src, pat):
    m = re.search(pat, src, re.S); assert m, pat[:50]; return m.group(0)

def meta(src, pat):
    m = re.search(pat, src, re.S); return m.group(1).strip() if m else ''

def section_inner(src, sid):
    m = re.search(r'<section class="section" id="%s">(.*?)</section>' % sid, src, re.S); assert m, sid
    inner = m.group(1)
    i = inner.index('<div class="wrap">') + len('<div class="wrap">')
    return inner[i:inner.rindex('</div>')].strip('\n')

def split_head(inner):
    m = re.search(r'<div class="section-head">(.*?)</div>\s*', inner, re.S)
    head = m.group(1); body = (inner[:m.start()] + inner[m.end():]).strip('\n')
    return (re.search(r'<p class="eyebrow">(.*?)</p>', head, re.S).group(1).strip(),
            re.search(r'<h2>(.*?)</h2>', head, re.S).group(1).strip(),
            re.search(r'<p>(.*?)</p>', head, re.S).group(1).strip(),
            body)

def collapse_tails(body):
    return re.sub(r'<h3 class="eyebrow list-label">(Also on every [^<]*)</h3>\s*(<ul class="shared-list">.*?</ul>)',
        lambda m: '<details class="reveal" open>\n        <summary class="eyebrow">%s</summary>\n        %s\n      </details>' % (m.group(1), m.group(2)),
        body, flags=re.S)

def repath(html, prefix):
    return html.replace('"../', '"' + prefix)

def head(cfg, prefix, title, desc, canonical):
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AeroNauticalTrax">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="icon" href="%sassets/icons/%s-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="%sassets/icons/%s-16.png" sizes="16x16" type="image/png">
<link rel="apple-touch-icon" href="%sassets/icons/%s-180.png">
<link rel="stylesheet" href="%sassets/style.css">
</head>
<body>''' % (title, desc, title, desc, canonical,
             prefix, cfg['icon'], prefix, cfg['icon'], prefix, cfg['icon'], prefix)

def nav(cfg, prefix, here):
    up = '' if here is None else '../'
    out = ['      <a class="opt" href="%s%s/index.html"%s>%s</a>'
           % (up, s, ' aria-current="page"' if here == s else '', label)
           for s, _sid, label, _seo, _b in cfg['pillars']]
    out.append('      <a class="opt" href="%sindex.html#pricing">Pricing</a>' % up)
    out.append('      <a class="opt" href="%ssupport.html">Support</a>' % prefix)
    return '\n'.join(out)

def masthead(cfg, prefix, here=None):
    return '''<header class="masthead">
  <div class="wrap">
    <a class="brand" href="%sindex.html">
      <img class="brand-logo" src="%sassets/brand-instruments.webp" width="73" height="38" alt="" aria-hidden="true" decoding="async">
      <span>
        <span class="brand-name">Aero<span class="wm-a">Nautical</span>Trax</span>
        <span class="brand-sub">%s</span>
      </span>
    </a>
    <nav class="mast-nav" aria-label="Primary">
%s
      <span class="app-status app-status-dev">In development</span>
    </nav>
  </div>
</header>''' % (prefix, prefix, cfg['display'], nav(cfg, prefix, here))

def devbanner(cfg, prefix):
    return '''  <div class="dev-banner">
    <div class="wrap">
      <span class="dev-tag">Not yet available</span>
      <p>%s is in development. There is nothing to download or buy yet &mdash; this page
      describes what it is being built to do. <a href="%svehicletrax/index.html">VehicleTrax</a>,
      built on the same engine, is shipping today.</p>
    </div>
  </div>''' % (cfg['display'], prefix)

def footer(prefix):
    links = [('index.html','All apps'), ('vehicletrax/index.html','VehicleTrax'),
             ('aerotrax/index.html','AeroTrax'), ('nauticaltrax/index.html','NauticalTrax'),
             ('support.html','Support'), ('privacy.html','Privacy Policy'), ('terms.html','Terms of Use')]
    items = '\n'.join('        <a href="%s%s">%s</a>' % (prefix, h, t) for h, t in links)
    return '''<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <span class="brand-name">AeroNauticalTrax</span>
        <p class="brand-sub">Tucson, Arizona</p>
      </div>
      <nav class="foot-links" aria-label="Footer">
%s
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
''' % items

def card(d, up):
    return '''        <article class="app-card">
          <div class="app-head">
            <div class="app-headtext">
              <h3>%s</h3>
            </div>
          </div>
          <p class="app-for">%s</p>
          <p class="app-desc">%s</p>
          <div class="app-actions">
            <a class="btn btn-ghost" href="%s%s/index.html">See how it works</a>
          </div>
        </article>''' % (d['label'], d['title'], d['blurb'], up, d['slug'])

written = []

for product, cfg in PRODUCTS.items():
    src = load(product)
    HERO   = block(src, r'<section class="hero">.*?</section>')
    SPECS  = block(src, r'<section class="section">\s*<div class="wrap">\s*<dl class="specs">.*?</section>')
    SHARED = block(src, r'<section class="section" id="shared">.*?</section>')
    PRICE  = block(src, r'<section class="section" id="pricing">.*?</section>')
    o_title = meta(src, r'<title>(.*?)</title>')
    o_desc  = meta(src, r'<meta name="description" content="(.*?)">')

    D = {}
    for slug, sid, label, seo, blurb in cfg['pillars']:
        eyebrow, h2, lede, body = split_head(section_inner(src, sid))
        D[slug] = dict(slug=slug, eyebrow=eyebrow, title=h2, lede=lede,
                       body=collapse_tails(body), label=label, seo=seo, blurb=blurb)

    # ---- overview ----
    p = '../'
    cards = '\n\n'.join(card(D[s], '') for s, _, _, _, _ in cfg['pillars'])
    page = '\n'.join([
        head(cfg, p, o_title, o_desc, '%s/%s/' % (SITE, product)),
        masthead(cfg, p),
        '<main id="top">', '',
        devbanner(cfg, p), '',
        repath(HERO, p), '',
        repath(SPECS, p), '',
        '''  <section class="section" id="explore">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">What it tracks</p>
        <h2>%s</h2>
        <p>%s</p>
      </div>
      <div class="apps%s">
%s
      </div>
    </div>
  </section>''' % (cfg['explore_title'], cfg['explore_lede'],
                   '' if len(cfg['pillars']) == 3 else ' apps-4', cards),
        '', repath(SHARED, p), '', repath(PRICE, p), '',
        '</main>', footer(p),
    ])
    dest = os.path.join(ROOT, product, 'index.html')
    open(dest, 'w', encoding='utf-8').write(page); written.append(dest)

    # ---- pillar pages ----
    p = '../../'
    for slug, _sid, _label, _seo, _b in cfg['pillars']:
        d = D[slug]
        others = [s for s, _, _, _, _ in cfg['pillars'] if s != slug]
        keep = '\n\n'.join(card(D[s], '../') for s in others)
        desc = re.sub(r'<[^>]+>', '', d['lede'])
        desc = re.sub(r'\s+', ' ', desc).strip()
        desc = (desc[:157].rsplit(' ', 1)[0] + '…') if len(desc) > 158 else desc
        page = '\n'.join([
            head(cfg, p, '%s &mdash; %s' % (d['seo'], cfg['display']), desc,
                 '%s/%s/%s/' % (SITE, product, slug)),
            masthead(cfg, p, slug),
            '<main id="top">', '',
            devbanner(cfg, p), '',
            '  <div class="wrap page-head">',
            '    <p class="eyebrow">%s</p>' % d['eyebrow'],
            '    <h1>%s</h1>' % d['title'],
            '  </div>', '',
            '  <section class="section">',
            '    <div class="wrap">',
            '      <div class="section-head">',
            '        <p>%s</p>' % d['lede'],
            '      </div>', '',
            '      ' + d['body'],
            '    </div>',
            '  </section>', '',
            '  <section class="section" id="more">',
            '    <div class="wrap">',
            '      <h3 class="eyebrow">Keep reading</h3>',
            '      <div class="apps%s">' % ('' if len(others) == 3 else ' apps-4'),
            keep,
            '      </div>',
            '    </div>',
            '  </section>', '',
            '</main>', footer(p),
        ])
        os.makedirs(os.path.join(ROOT, product, slug), exist_ok=True)
        dest = os.path.join(ROOT, product, slug, 'index.html')
        open(dest, 'w', encoding='utf-8').write(page); written.append(dest)

for w in written:
    print('wrote', os.path.relpath(w, ROOT))
