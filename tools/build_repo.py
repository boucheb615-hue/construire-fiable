#!/usr/bin/env python3
"""Build the public repo folder from out/ : site pages at the root, funnel
documents under funnel/. Renders the lead magnet Markdown to
test-aveugle-kit.html with a tiny converter (no dependencies)."""
import html, pathlib, re, shutil

SRC = pathlib.Path('/home/agentic/webmoderne-fiable')
DST = pathlib.Path('/home/agentic/construire-fiable')


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(https?://[^\s<]+)', r'<a href="\1">\1</a>', s)
    return s


def md_to_html(md):
    out, para, in_code, in_list = [], [], False, None

    def flush():
        nonlocal para
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para = []

    def close_list():
        nonlocal in_list
        if in_list:
            out.append(f'</{in_list}>')
            in_list = None

    for line in md.split('\n'):
        if line.startswith('```'):
            flush(); close_list()
            out.append('</pre>' if in_code else '<pre>')
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        if not line.strip():
            flush(); close_list(); continue
        if line.strip() == '---':
            flush(); close_list(); out.append('<hr style="border-color:rgba(255,255,255,.15)">'); continue
        m = re.match(r'(#{1,3}) (.*)', line)
        if m:
            flush(); close_list()
            lvl = len(m.group(1))
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>')
            continue
        m = re.match(r'- \[ \] (.*)', line)
        if m:
            flush()
            if in_list != 'ul':
                close_list(); out.append('<ul class="check">'); in_list = 'ul'
            out.append(f'<li>{inline(m.group(1))}</li>')
            continue
        m = re.match(r'(\d+)\. (.*)', line)
        if m:
            flush()
            if in_list != 'ol':
                close_list(); out.append('<ol>'); in_list = 'ol'
            out.append(f'<li>{inline(m.group(2))}</li>')
            continue
        para.append(line.strip())
    flush(); close_list()
    return '\n'.join(out)


if DST.exists():
    for p in DST.iterdir():
        if p.name != '.git':
            shutil.rmtree(p) if p.is_dir() else p.unlink()
DST.mkdir(exist_ok=True)
for f in (SRC / 'out/landing').glob('*'):
    shutil.copy(f, DST / f.name)

md = (SRC / 'out/lead-magnet-test-aveugle.md').read_text(encoding='utf-8')
body = md_to_html(md)
(DST / 'test-aveugle-kit.html').write_text(f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Le Test à l'Aveugle · WebModerne</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
{body}
</main>
</body>
</html>
''', encoding='utf-8')

(DST / 'funnel').mkdir()
for rel, name in [('.copy/brief.yml', 'brief.yml'), ('FUNNEL.md', 'FUNNEL.md'), ('out/offer.md', 'offre.md'),
                  ('out/emails.md', 'emails.md'), ('out/ads.md', 'publicites.md'),
                  ('out/lead-magnet-test-aveugle.md', 'aimant-test-aveugle.md'), ('AUDIT.md', 'AUDIT.md')]:
    if (SRC / rel).exists():
        shutil.copy(SRC / rel, DST / 'funnel' / name)
(DST / 'tools').mkdir()
for f in (SRC / 'tools').glob('*.py'):
    if f.name != 'build_repo.py':
        shutil.copy(f, DST / 'tools' / f.name)
shutil.copy(SRC / 'tools/build_repo.py', DST / 'tools/build_repo.py')
if (SRC / 'README.md').exists():
    shutil.copy(SRC / 'README.md', DST / 'README.md')
print('built', sorted(p.name for p in DST.iterdir()))
