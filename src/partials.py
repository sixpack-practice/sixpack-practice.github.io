LOGO='<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="18" style="fill:var(--ink)"/><circle cx="20" cy="20" r="12.5" fill="none" style="stroke:var(--paper)" stroke-width="1.2"/><path d="M20 4 L23 20 L20 36 L17 20Z" style="fill:var(--paper)"/><path d="M20 4 L23 20 L17 20Z" style="fill:var(--accent)"/><path d="M4 20 L20 17.5 L36 20 L20 22.5Z" style="fill:var(--paper)" opacity=".55"/></svg>'
FAV="data:image/svg+xml,"+"%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Ccircle cx='20' cy='20' r='18' fill='%230F2433'/%3E%3Cpath d='M20 4 L23 20 L20 36 L17 20Z' fill='%23F2F6F8'/%3E%3Cpath d='M20 4 L23 20 L17 20Z' fill='%23D2470F'/%3E%3C/svg%3E"
def head(title, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#0F2433">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="{{{{ROOT}}}}site.css">
</head>
<body>
'''
DEFS='''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<marker id="ah-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10z" style="fill:var(--ink)"/></marker>
<marker id="ah-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10z" style="fill:var(--accent)"/></marker>
<marker id="ah-chart" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10z" style="fill:var(--chart)"/></marker>
<marker id="ah-muted" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10z" style="fill:var(--muted)"/></marker>
<filter id="glow" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="5"/></filter>
<linearGradient id="nightsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#030810"/><stop offset="1" stop-color="#0c1f30"/></linearGradient>
<linearGradient id="daysky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bcd9ea"/><stop offset="1" stop-color="#e9f3f8"/></linearGradient>
</defs></svg>
'''
def header(home=True):
    p = '' if home else 'index.html'
    return f'''<header class="top"><div class="wrap">
<a class="brand" href="{{{{ROOT}}}}index.html" aria-label="Six-Pack Practice home">{LOGO}<b>Six-Pack Practice</b></a>
<nav aria-label="Sections"><a href="{p}#features">Features</a><a href="{p}#how">How it works</a><a href="{p}#faq">FAQ</a></nav>
<a class="btn primary" href="{{{{ROOT}}}}app/">Open the app</a>
</div></header>
'''
FOOTER='''<footer><div class="wrap">
<div class="links"><a href="{{ROOT}}app/">Open the app</a><a href="{{ROOT}}support.html">Support</a><a href="{{ROOT}}privacy.html">Privacy</a></div>
<p>Six-Pack Practice is an independent study aid for the U.S. Coast Guard OUPV (six-pack) Near Coastal exam. It is not made by, approved by or affiliated with the U.S. Coast Guard. Practice questions are original study items, not official exam questions, and using this app does not replace a USCG-approved course.</p>
<p>© 2026 Six-Pack Practice</p>
</div></footer>
'''
