# sfillingham.github.io

Personal website for Sean P. Fillingham — Technical AI Governance, Systems Safety for Frontier AI.

Built with [Pelican](https://getpelican.com), a Python static site generator.

## Quick Start

### 1. Install dependencies

```bash
pip install pelican markdown
```

### 2. Local development

```bash
# From the project root:
pelican content --listen --autoreload
```

This builds the site and serves it at `http://localhost:8000`. It auto-rebuilds when you change files.

### 3. Deploy to GitHub Pages

```bash
pelican content -s publishconf.py
```

Then commit and push the `output/` directory contents to your GitHub Pages repo. (See "Deployment" below for the recommended workflow.)

## Project Structure

```
.
├── pelicanconf.py          # Main configuration
├── publishconf.py          # Production overrides (sets SITEURL, enables feeds)
├── content/
│   ├── blog/               # Blog posts (Substack cross-posts go here)
│   │   └── *.md
│   ├── pages/              # Static pages (About, Research)
│   │   ├── about.md
│   │   ├── research.md
│   │   └── home.md         # Landing page (don't edit — edit landing.html template instead)
│   └── images/             # Images referenced in content
├── theme/
│   ├── templates/          # Jinja2 HTML templates
│   │   ├── base.html       # Base layout (nav, footer)
│   │   ├── landing.html    # Home page
│   │   ├── index.html      # Blog listing (/writing/)
│   │   ├── article.html    # Single post
│   │   └── page.html       # Static page (About, Research)
│   └── static/
│       └── css/
│           └── style.css   # All styles
└── output/                 # Generated site (don't edit directly)
```

## Adding a New Blog Post (Substack Cross-Post Workflow)

1. Write and publish on Substack as usual.
2. Save the Markdown version of the post in `content/blog/` with this header:

```markdown
Title: Your Post Title
Date: 2026-04-15
Tags: STAMP, systems-safety, agentic-AI
Summary: A one-sentence description that appears in the post listing.

*This post is cross-posted from [my Substack](https://yoursubstack.substack.com).*

---

Your post content here...
```

3. Rebuild and deploy:

```bash
pelican content -s publishconf.py
# then push to GitHub
```

That's it. The post will appear on your Writing page and on the home page (if it's one of the 3 most recent).

## Editing Pages

- **About page**: Edit `content/pages/about.md`
- **Research page**: Edit `content/pages/research.md`
- **Home page hero text**: Edit `theme/templates/landing.html`
- **Navigation, footer**: Edit `theme/templates/base.html`
- **Styles**: Edit `theme/static/css/style.css`

## Deployment Options

### Option A: Simple (push output to master)

If your repo is `sfillingham.github.io`, GitHub Pages serves from the root of `master`. You can either:

- Build locally, copy output files to root, commit and push
- Or restructure so the Pelican source lives on a `source` branch and output goes to `master`

### Option B: GitHub Actions (recommended)

Create `.github/workflows/deploy.yml` to auto-build on push:

```yaml
name: Deploy
on:
  push:
    branches: [source]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install pelican markdown
      - run: pelican content -s publishconf.py
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./output
          publish_branch: master
```

With this setup: push your source files to a `source` branch, and GitHub Actions automatically builds and deploys to `master`.

## Configuration

Key settings in `pelicanconf.py`:

- `SUBSTACK_URL`: Set this to your actual Substack URL. It's used in templates for subscribe CTAs.
- `SITEURL`: Leave empty for local dev. Set in `publishconf.py` for production.
- `MENUITEMS`: Controls the navigation links.

## Customization

The theme is fully custom and self-contained in `theme/`. Fonts are loaded from Google Fonts (Source Serif 4, DM Sans, JetBrains Mono). Colors and spacing are controlled via CSS variables at the top of `style.css`.
