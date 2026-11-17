"""Build the Six-Pack Practice website.
Run: python3 build.py   (re-copies the app from ../six-pack-practice and regenerates pages)
Set REPO below to the GitHub "owner/name" once the site's repository exists, so Support links to its issues page.
"""
import json, os, re, shutil, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(D, 'src'); APP = os.path.join(D, '..', 'six-pack-practice')
sys.path.insert(0, SRC); import partials as P
REPO = "sixpack-practice/sixpack-practice.github.io"   # e.g. "six-pack-practice/six-pack-practice.github.io"
ROOT = "/"  # "/" for a site at the domain root; "/repo-name/" for a GitHub project site

# 1. app: rebuild it, copy the standalone version, extract showcase art
subprocess.run([sys.executable, os.path.join(APP, 'build.py')], check=True, stdout=subprocess.DEVNULL)
os.makedirs(os.path.join(D, 'app'), exist_ok=True)
shutil.copy(os.path.join(APP, 'preview.html'), os.path.join(D, 'app', 'index.html'))
subprocess.run(['node', os.path.join(SRC, 'extract.js'), os.path.join(APP, 'index.html'), os.path.join(SRC, 'art.json')], check=True, stdout=subprocess.DEVNULL)
art = json.load(open(os.path.join(SRC, 'art.json')))

contact = (f'<h2>Contact</h2><p>Report a problem or suggest a fix on <a href="https://github.com/{REPO}/issues">the project\'s GitHub issues page</a>.</p>' if REPO else '')
for name in ['index.html', 'privacy.html', 'support.html', '404.html']:
    s = open(os.path.join(SRC, name)).read()
    s = re.sub(r'\{\{HEAD:(.*?)\|(.*?)\}\}', lambda m: P.head(m.group(1), m.group(2)), s)
    s = s.replace('{{DEFS}}', P.DEFS).replace('{{HEADER}}', P.header(name == 'index.html')).replace('{{FOOTER}}', P.FOOTER)
    s = re.sub(r'\{\{ART:(\w+)\}\}', lambda m: art[m.group(1)], s)
    s = s.replace('{{N_Q}}', str(art['questions'])).replace('{{N_L}}', str(art['lessons'])).replace('{{CONTACT}}', contact)
    s = s.replace('{{ROOT}}', ROOT)
    assert '{{' not in s, (name, s[s.index('{{'):s.index('{{') + 40])
    open(os.path.join(D, name), 'w').write(s)
open(os.path.join(D, '.nojekyll'), 'w').close()
print('built', ', '.join(sorted(f for f in os.listdir(D) if f.endswith('.html'))))
