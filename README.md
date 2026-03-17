# Matthias Walle Website

Personal academic website for Matthias Walle, focused on bone imaging, biomechanics, AI, and scientific software.

Live site:
[`https://wallematthias.github.io`](https://wallematthias.github.io)

## Local development

This site uses Jekyll and Bundler.

```bash
cd /Users/matthias.walle/Documents/GitHub/website
eval "$(rbenv init - zsh)"
bundle _2.5.6_ install
bundle _2.5.6_ exec jekyll serve
```

Then open:

```text
http://127.0.0.1:4000
```

## Build

```bash
bundle _2.5.6_ exec jekyll build
```

## Deploy

The repository is configured to deploy with GitHub Actions and GitHub Pages.

Typical flow:

1. Commit changes to `main`
2. Push to GitHub
3. GitHub Actions builds the site
4. GitHub Pages deploys the built artifact

In GitHub repository settings, set `Pages` to use `GitHub Actions` as the source.
