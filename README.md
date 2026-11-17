# Six-Pack Practice website

Static site for the Six-Pack Practice app.

| Path | What it is |
|---|---|
| `index.html` | Landing page with a live demo of the app on a phone |
| `app/` | The app itself, a standalone copy built from `../six-pack-practice` |
| `privacy.html`, `support.html` | Privacy policy and help page |
| `404.html`, `.nojekyll` | Needed for GitHub Pages |
| `src/` | Page sources, shared header/footer (`partials.py`), and the script that pulls diagrams out of the app |
| `site.css` | Shared styles (same look as the app) |

## Rebuild

```bash
python3 build.py
```

This rebuilds the app, copies it into `app/`, re-extracts the showcase diagrams and regenerates every page. It needs Node.js for the diagram step.

Before publishing, set two values at the top of `build.py`:

- `REPO`: the GitHub `owner/name` of the site's repository. Support and Privacy then link to its issues page.
- `ROOT`: `"/"` for a site at the domain root (for example `name.github.io`), or `"/repo-name/"` for a GitHub project site.

## Preview locally

```bash
python3 -m http.server 8738 --directory six-pack-site
```

Then open http://localhost:8738. A local server is needed; opening the files directly breaks the root-relative links.
