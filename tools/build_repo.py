#!/usr/bin/env python3
"""Build the public repo folder from out/ and scripts/.

Site root: the funnel pages (index.html = sales page) + review pages:
  revue.html             hub linking every asset
  annonces.html          Facebook/Instagram post mockups (from the JSON block in out/ads.md)
  emails.html            the emails rendered as mail cards (from out/emails.md)
  scripts/*.html         each Funnel Scripts document (template, variables, filled, final)
  test-aveugle-kit.html  the lead magnet
Docs under funnel/. No dependencies."""
import html, json, pathlib, re, shutil

SRC = pathlib.Path('/home/agentic/webmoderne-fiable')
DST = pathlib.Path('/home/agentic/construire-fiable')


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])', r'<em>\1</em>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+|[\w./-]+\.(?:html|md|yml))\)', r'<a href="\2">\1</a>', s)
    s = re.sub(r'(?<![">])(https?://[^\s<)]+)', r'<a href="\1">\1</a>', s)
    return s


def md_to_html(md):
    out, para, in_code, in_list, table = [], [], False, None, []

    def flush():
        nonlocal para
        if para:
            out.append('<p>' + '<br>'.join(inline(x) for x in para) + '</p>')
            para = []

    def close_list():
        nonlocal in_list
        if in_list:
            out.append('</ol>' if in_list == 'ol' else '</ul>')
            in_list = None

    def close_table():
        nonlocal table
        if table:
            rows = [r for r in table if not re.match(r'^\|[\s:|-]+\|$', r)]
            cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
            h = '<div class="tw"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in cells[0]) + '</tr></thead><tbody>'
            for r in cells[1:]:
                h += '<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>'
            out.append(h + '</tbody></table></div>')
            table = []

    def open_list(kind, tag):
        nonlocal in_list
        if in_list != kind:
            close_list(); out.append(tag); in_list = kind

    for line in md.split('\n'):
        if line.startswith('```'):
            flush(); close_list(); close_table()
            out.append('</pre>' if in_code else '<pre>')
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line)); continue
        if line.strip().startswith('|'):
            flush(); close_list(); table.append(line.strip()); continue
        close_table()
        if not line.strip():
            flush(); close_list(); continue
        if line.strip() == '---':
            flush(); close_list(); out.append('<hr>'); continue
        m = re.match(r'(#{1,4}) (.*)', line)
        if m:
            flush(); close_list()
            lvl = len(m.group(1))
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>'); continue
        m = re.match(r'\s*[-*] \[ \] (.*)', line)
        if m:
            flush(); open_list('check', '<ul class="check">')
            out.append(f'<li>{inline(m.group(1))}</li>'); continue
        m = re.match(r'\s*[-*] (.*)', line)
        if m:
            flush(); open_list('ul', '<ul>')
            out.append(f'<li>{inline(m.group(1))}</li>'); continue
        m = re.match(r'\s*(\d+)\. (.*)', line)
        if m:
            flush(); open_list('ol', '<ol>')
            out.append(f'<li>{inline(m.group(2))}</li>'); continue
        if line.startswith('>'):
            flush(); out.append(f'<blockquote>{inline(line.lstrip("> "))}</blockquote>'); continue
        para.append(line.strip())
    flush(); close_list(); close_table()
    return '\n'.join(out)


REVIEW_CSS = '''
.wide{max-width:980px}
.tw{overflow-x:auto;margin:16px 0}
table{border-collapse:collapse;width:100%;font-size:.88rem}
th,td{border:1px solid rgba(255,255,255,.15);padding:8px 10px;text-align:left;vertical-align:top}
th{background:#090935}
code{background:#000014;padding:1px 5px;border-radius:4px;font-size:.88em}
blockquote{border-left:3px solid rgba(255,255,255,.4);margin:12px 0;padding:4px 14px;color:rgba(255,255,255,.8)}
hr{border:0;border-top:1px solid rgba(255,255,255,.15);margin:28px 0}
h3,h4{margin-top:28px}
.nav{font-size:.9rem;margin-bottom:24px}
.nav a{margin-right:14px}
.fb{background:#fff;color:#050505;border-radius:10px;max-width:500px;margin:20px 0;font:15px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;box-shadow:0 2px 12px rgba(0,0,0,.4);overflow:hidden}
.fb-head{display:flex;gap:10px;align-items:center;padding:12px 14px 6px}
.fb-av{width:40px;height:40px;border-radius:50%;background:#090935;color:#fff;display:grid;place-items:center;font-weight:700}
.fb-name{font-weight:600}.fb-meta{color:#65676b;font-size:.8rem}
.fb-text{padding:4px 14px 12px;white-space:pre-wrap}
.fb-img{aspect-ratio:1.91/1;background:linear-gradient(135deg,#05051a,#090935 60%,#db1a1a);display:grid;place-items:center;color:#fff;font-weight:800;font-size:1.3rem;text-align:center;padding:20px}
.fb-foot{display:flex;justify-content:space-between;align-items:center;gap:10px;background:#f0f2f5;padding:10px 14px}
.fb-url{color:#65676b;font-size:.75rem;text-transform:uppercase}.fb-title{font-weight:700}.fb-desc{color:#65676b;font-size:.85rem}
.fb-btn{background:#e4e6eb;border-radius:6px;padding:8px 12px;font-weight:600;white-space:nowrap}
.tag{display:inline-block;font-size:.75rem;border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:2px 10px;margin:0 6px 6px 0;color:rgba(255,255,255,.8)}
.mail{background:#fff;color:#1a1a1a;border-radius:10px;margin:20px 0;overflow:hidden;font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.mail-head{background:#f3f4f6;padding:14px 18px;border-bottom:1px solid #e5e7eb;font-size:.9rem}
.mail-head b{display:inline-block;min-width:88px;color:#555}
.mail-body{padding:18px}.mail-body a{color:#0b57d0}
.mail-body h2,.mail-body h3,.mail-body strong{color:#1a1a1a}
'''

NAV = ('<p class="nav"><a href="{r}revue.html">← Revue</a><a href="{r}index.html">Page de vente</a>'
       '<a href="{r}annonces.html">Publicités</a><a href="{r}emails.html">E-mails</a>'
       '<a href="{r}scripts/index.html">Scripts</a></p>')


def page(title, body, root='', wide=True):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Construire Fiable</title>
<link rel="stylesheet" href="{root}style.css">
<style>{REVIEW_CSS}</style>
</head>
<body>
<main class="{'wide' if wide else ''}">
{NAV.format(r=root)}
{body}
</main>
</body>
</html>
'''


def build_ads():
    md = (SRC / 'out/ads.md').read_text(encoding='utf-8')
    m = re.search(r'```json\s*(\[.*?\])\s*```', md, re.S)
    ads = json.loads(m.group(1)) if m else []
    cards = []
    for a in ads:
        dest = a.get('destination', '')
        cards.append(f'''
<section>
<h2>{html.escape(str(a.get("id", "")))} · {html.escape(a.get("type", ""))}</h2>
<p><span class="tag">accroche Jim Edwards : {html.escape(a.get("accroche_jim_edwards", ""))}</span><span class="tag">vers : {html.escape(dest.rsplit("/", 1)[-1] or "page de vente")}</span></p>
<div class="fb">
  <div class="fb-head"><div class="fb-av">W</div><div><div class="fb-name">WebModerne</div><div class="fb-meta">Sponsorisé · 🌍</div></div></div>
  <div class="fb-text">{html.escape(a.get("texte_principal", ""))}</div>
  <div class="fb-img">{html.escape(a.get("titre", ""))}</div>
  <div class="fb-foot"><div><div class="fb-url">boucheb615-hue.github.io</div><div class="fb-title">{html.escape(a.get("titre", ""))}</div><div class="fb-desc">{html.escape(a.get("description", ""))}</div></div><div class="fb-btn">{html.escape(a.get("bouton", ""))}</div></div>
</div>
</section>''')
    intro = ('<h1>Les publicités Facebook et Instagram</h1>'
             f'<p class="muted">{len(ads)} annonces, présentées comme dans le fil. L\'image est un visuel provisoire '
             '(à produire). Le script Funnel Scripts et la notation des accroches sont dans '
             '<a href="scripts/05-publicites.html">le document de script</a>.</p>')
    (DST / 'annonces.html').write_text(page('Publicités', intro + '\n'.join(cards)), encoding='utf-8')
    return len(ads)


def build_emails():
    md = (SRC / 'out/emails.md').read_text(encoding='utf-8')
    parts = re.split(r'\n(?=## )', md)
    head, mails = parts[0], parts[1:]
    cards = []
    for p in mails:
        lines = p.strip().split('\n')
        title = lines[0].lstrip('# ').strip()
        meta, body = {}, []
        for ln in lines[1:]:
            mm = re.match(r'\*\*(Envoi|Objet|Préheader)\W*\*\*\s*(.*)', ln)
            if mm and not body:
                meta[mm.group(1)] = mm.group(2).strip()
            elif ln.strip() == '---' or (not body and not ln.strip()):
                continue
            else:
                body.append(ln)
        cards.append(f'''
<section>
<h2>{inline(title)}</h2>
<div class="mail">
  <div class="mail-head"><div><b>De</b> Karnon Koné (WebModerne)</div><div><b>Objet</b> <strong>{inline(meta.get("Objet", ""))}</strong></div><div><b>Préheader</b> {inline(meta.get("Préheader", ""))}</div><div><b>Envoi</b> {inline(meta.get("Envoi", ""))}</div></div>
  <div class="mail-body">{md_to_html(chr(10).join(body))}</div>
</div>
</section>''')
    intro = ('<h1>Les e-mails</h1>' + md_to_html(re.sub(r'^# .*\n', '', head)) +
             '<p class="muted">Le script Funnel Scripts de chaque séquence est dans '
             '<a href="scripts/04-emails.html">le document de script</a>.</p>')
    (DST / 'emails.html').write_text(page('E-mails', intro + '\n'.join(cards)), encoding='utf-8')
    return len(mails)


def build_scripts():
    (DST / 'scripts').mkdir(exist_ok=True)
    items = []
    for f in sorted((SRC / 'scripts').glob('*.md')):
        md = f.read_text(encoding='utf-8')
        m = re.search(r'^# (.+)', md, re.M)
        title = m.group(1) if m else f.stem
        body = md_to_html(md)
        body = re.sub(r'href="([\w-]+\.html)"',
                      lambda m: f'href="../{m.group(1)}"' if (SRC / 'out/landing' / m.group(1)).exists()
                      or m.group(1) in ('revue.html', 'annonces.html', 'emails.html', 'test-aveugle-kit.html')
                      else m.group(0), body)
        (DST / 'scripts' / (f.stem + '.html')).write_text(page(title, body, root='../'), encoding='utf-8')
        if f.stem != 'CONSIGNES':
            items.append((f.stem, title))
    lis = ''.join(f'<li><a href="{s}.html">{html.escape(t)}</a></li>' for s, t in items)
    body = ('<h1>Les scripts Funnel Scripts</h1><p>Chaque document montre le gabarit d\'origine avec ses '
            '<code>{variables}</code>, les variables remplies depuis le brief, la version remplie brute, puis la '
            f'version finale réécrite selon Jim Edwards.</p><ol>{lis}</ol>'
            '<p class="muted"><a href="CONSIGNES.html">Consignes données aux rédacteurs</a></p>')
    (DST / 'scripts' / 'index.html').write_text(page('Scripts', body, root='../'), encoding='utf-8')
    return len(items)


def build_hub(n_ads, n_mails, n_scripts):
    gh = 'https://github.com/boucheb615-hue/construire-fiable/blob/main/funnel'
    body = f'''<h1>Construire Fiable · revue du tunnel</h1>
<p>Tout le tunnel, dans l'ordre où un prospect le vit. Chaque texte part d'un script Funnel Scripts (gabarit à variables), réécrit selon Jim Edwards. Le tunnel suit le cadre Russell Brunson : aimant à prospects, e-mails, page de vente, option au paiement, offre après achat.</p>
<ol>
<li><a href="annonces.html">Publicités Facebook et Instagram</a> ({n_ads} annonces, en aperçu de fil)</li>
<li><a href="test-aveugle.html">Page d'inscription</a> à l'aimant gratuit</li>
<li><a href="merci.html">Page de remerciement</a> (double opt-in + mention de l'offre)</li>
<li><a href="test-aveugle-kit.html">L'aimant : Le Test à l'Aveugle</a></li>
<li><a href="emails.html">Les e-mails</a> ({n_mails} e-mails : livraison, compte à rebours, confirmation d'achat)</li>
<li><a href="index.html">Page de vente</a> (offre, bonus et leurs valeurs, garantie)</li>
<li><a href="commande.html">Commande</a> avec l'option à 27 € (démo, aucun paiement)</li>
<li><a href="merci-achat.html">Page après achat</a> avec l'offre à 197 €</li>
</ol>
<h2>Les coulisses</h2>
<ul>
<li><a href="scripts/index.html">Les {n_scripts} documents de script</a> : gabarit, variables, version remplie, version finale</li>
<li><a href="{gh}/FUNNEL.md">Le plan du tunnel et l'épine</a> · <a href="{gh}/brief.yml">le brief</a> · <a href="{gh}/AUDIT.md">l'audit à l'aveugle</a></li>
</ul>'''
    (DST / 'revue.html').write_text(page('Revue', body), encoding='utf-8')


if DST.exists():
    for p in DST.iterdir():
        if p.name != '.git':
            shutil.rmtree(p) if p.is_dir() else p.unlink()
DST.mkdir(exist_ok=True)
for f in (SRC / 'out/landing').glob('*'):
    if f.is_file():
        shutil.copy(f, DST / f.name)
kit = md_to_html((SRC / 'out/lead-magnet-test-aveugle.md').read_text(encoding='utf-8'))
(DST / 'test-aveugle-kit.html').write_text(f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Le Test à l'Aveugle · WebModerne</title>
<link rel="stylesheet" href="style.css">
<style>{REVIEW_CSS}</style>
</head>
<body>
<main>
{kit}
</main>
</body>
</html>
''', encoding='utf-8')
n_ads, n_mails, n_scripts = build_ads(), build_emails(), build_scripts()
build_hub(n_ads, n_mails, n_scripts)
(DST / 'funnel').mkdir()
for rel, name in [('.copy/brief.yml', 'brief.yml'), ('FUNNEL.md', 'FUNNEL.md'),
                  ('out/emails.md', 'emails.md'), ('out/ads.md', 'publicites.md'),
                  ('out/lead-magnet-test-aveugle.md', 'aimant-test-aveugle.md'), ('AUDIT.md', 'AUDIT.md')]:
    if (SRC / rel).exists():
        shutil.copy(SRC / rel, DST / 'funnel' / name)
shutil.copytree(SRC / 'scripts', DST / 'funnel' / 'scripts')
(DST / 'tools').mkdir()
for f in (SRC / 'tools').glob('*.py'):
    shutil.copy(f, DST / 'tools' / f.name)
if (SRC / 'README.md').exists():
    shutil.copy(SRC / 'README.md', DST / 'README.md')
print(f'built: {n_ads} ads, {n_mails} emails, {n_scripts} scripts ->', sorted(p.name for p in DST.iterdir()))
