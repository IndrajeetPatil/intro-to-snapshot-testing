# AGENTS.md

Project-level instructions for AI coding agents working on this repository —
Codex, GitHub Copilot (code review and coding agent), and other
`AGENTS.md`-aware tools read this file directly.

## What this is

A single-page [Quarto](https://quarto.org/) presentation rendered to [RevealJS](https://revealjs.com/) slides and deployed as a static site via GitHub Pages.

## Repository layout

```
index.qmd           # All slide content (the only file you usually need to edit)
_quarto.yml          # Quarto project config (output dir, resources list)
_quarto-a11y.yml     # Opt-in profile enabling the axe accessibility checker (`just axe`)
accessibility.html  # Compatibility fixes supplementing the a11y extension
style.css            # Custom RevealJS theme (fonts, colours, component classes)
meta-tags.html       # OpenGraph, Twitter Card, JSON-LD, and analytics tags
justfile             # Command runner (install, render, preview, clean, etc.)
media/               # Images: evidence screenshots, illustrations, social card
llms.txt             # Short machine-readable summary for LLM discovery
llms-full.txt        # Extended machine-readable summary
.well-known/         # Mirrors of llms.txt and llms-full.txt
robots.txt           # Crawl rules
sitemap.xml          # Sitemap for search engines
.editorconfig        # Shared editor/formatting settings
.github/             # CI workflows (reusable, from IndrajeetPatil/workflows) and Dependabot
_extensions/         # Latest a11y extension, installed by `just install` and CI (gitignored)
_site/               # Build output (gitignored)
```

### Language-specific files

Python-based decks also have:

```
pyproject.toml       # Project metadata and dependencies (managed by uv)
uv.lock              # Locked Python dependencies
.python-version      # Python version pin
.venv/               # Python virtualenv (gitignored)
```

R-based decks (including this one) have instead:

```
DESCRIPTION          # R package dependencies, installed with pak
```

Check which set is present to know which language context applies.

## Key conventions

- **Single-file deck.** All slides live in `index.qmd`. There are no partial includes or multi-file splits.
- **Slide syntax.** Slides are separated by `##` headings. Use Quarto's RevealJS dialect: fenced divs (`:::`), columns (`.columns` / `.column`), raw HTML blocks (`{=html}`), and the `{.smaller}` class for dense slides.
- **Inline styling.** Visual design uses inline `style` attributes on fenced divs with a small palette of background colours (e.g. `#e3f2fd`, `#e8f5e9`, `#fff3e0`, `#ffebee`, `#FFFBC1`, `#f8f9fa`). The CSS maps these to the custom theme. Do not change these colour values without updating `style.css`.
- **Image classes.** Images may use semantic classes (e.g. `.hero`, `.artifact`, `.illustration`) that control border, shadow, and rounding in `style.css`. Check the existing CSS before adding new image classes.
  The snapshot-review screenshot uses per-slide `.nostretch` to prevent RevealJS auto-stretch from collapsing it. Verify image sizing in both presentation mode and native `?view=scroll` when changing that slide.
- **Sources.** Every factual claim has a source citation at the bottom of its slide in a small-font centered div. Keep this pattern.
- **Accessibility.** Images must have `fig-alt` text. Raw HTML widgets use `role="img"` and `aria-label`. Keep these.
  Verify with `just axe`, which appends an "Accessibility Report" slide listing axe-core violations. Keep `axe` in
  `_quarto-a11y.yml`, not `index.qmd`, so production builds exclude the audit payload. CLI metadata such as
  `-M axe:true` cannot override this deck's `format:` block. Links inside muted text need a non-colour cue such as an underline.
  Inspect all slides, revealed fragments, and tab panels in both presentation and scroll view; the initial report alone does not exercise every state.
  The `a11y` extension supplies zoom, focus indicators, link underlines, reduced motion,
  slide isolation, and screen-reader announcements. Keep `accessibility.html` for
  code scrolling, menu focus, and vertical-slide semantics.
  `accessibility.html` is a shared fleet-wide file, kept byte-identical to the template by the
  scheduled `Check Template Drift` workflow. It is therefore a superset: it contains every branch
  any deck in the fleet needs. The tab-ordering and arrow-key branch is inert in decks with no
  tabsets, but this deck has a `panel-tabset` (the "Reviewing snapshot changes" slide), so the
  branch is live here. Never delete a branch from this file because it looks unused — change it in
  the template and re-sync, otherwise the drift check fails.
  Keep explicit `aria-label` attributes on repeated slide headings so scroll-view
  landmarks have unique names.
  Disable the extension's slide-menu patch and settings menu as in the reference
  deck: version 0.2.3 introduces ARIA and contrast failures in those components.
- **Icons.** Icons use lightweight HTML spans backed by only the required SVG path data in the custom stylesheet; no icon-font or Quarto icon extension is needed.
  When adding an icon, add only its mask data, preserve the source licence attribution, keep an accessible label where the icon conveys meaning, and render the deck to verify it.
- **Mermaid performance boundary.** Keep Mermaid diagrams as Mermaid source. Do not replace them with pre-rendered SVGs solely to reduce the website bundle.
- **Code execution is ON for this deck.** The YAML front matter sets `execute: eval: true`. Unlike the display-only decks in the fleet, this one genuinely needs computed output: the slides run live `testthat` snapshot examples (including deliberate failures via `error=TRUE`), build a `ggplot2` figure, and pull screenshots in with `knitr::include_graphics()`. Setting `eval: false` blanks those slides. The R packages in `DESCRIPTION` are runtime dependencies, not just engine satisfaction.
- **Compute engine.** Python decks declare `jupyter: python3` in the front matter; this R deck uses Quarto's default `knitr` engine.

## Commands

All commands use [just](https://github.com/casey/just). The recipes are the same across decks; only the dependency backend differs:

```bash
just install   # Install language dependencies and the latest a11y extension
just sync      # Alias for install
just update    # Update language dependencies
just render    # Render index.qmd to _site/
just preview   # Live-reload dev server
just open      # Alias for preview (live-reload dev server over localhost)
just clean     # Remove build artifacts
just check     # Verify Quarto setup
just axe       # Preview with the axe accessibility checker enabled
```

This deck renders with Quarto. R dependencies are declared in `DESCRIPTION` and installed with `pak`; CI installs them with `r-lib/actions/setup-r-dependencies`. Slides live in `index.qmd`.

## Editing slides

When modifying `index.qmd`:

1. Follow the existing card/column layout patterns visible in neighbouring slides.
2. Preserve the source-citation div at the bottom of each slide.
3. Use the established background-colour palette for info cards rather than inventing new colours.
4. Keep `fig-alt` on every image and `aria-label` on HTML widgets.
5. Run `just render` (or `just preview`) to verify changes compile without errors.

## Editing styles

`style.css` defines CSS custom properties under `:root` and component classes for complex HTML widgets. The variable names and widget classes vary per deck. When adding a new widget, follow the naming and structure patterns already present in the file.

## SEO and discoverability files

- `meta-tags.html` contains OpenGraph, Twitter Card, JSON-LD structured data, and Google Analytics. Update it when the title, description, or social card image changes.
- `llms.txt` and `llms-full.txt` are machine-readable summaries following the llms.txt convention. Update them when the deck content changes significantly.
- `sitemap.xml` and `robots.txt` are static and rarely need changes.

## CI/CD

- The GitHub Actions workflow in `.github/workflows/` renders the deck and deploys to GitHub Pages on push to `main`. It calls a reusable workflow from `IndrajeetPatil/workflows` (Python and R decks use different workflow files). Do not inline the workflow.
- Two scheduled companion workflows also call reusable workflows from `IndrajeetPatil/workflows`: `check-link-rot.yaml` (weekly, Sunday 00:00 UTC) verifies the deck's external links, and `check-template-drift.yaml` (weekly, Monday 06:00 UTC) reports divergence from the shared presentation template.
- **Reference the first-party reusable workflow as `@main`.** This intentionally receives upstream fixes immediately, including stable Quarto builds and removal of the unused FontAwesome installation. Do not pin it to a commit SHA.
- Install the latest a11y extension directly from upstream with
  `quarto add mcanouil/quarto-revealjs-a11y --no-prompt` in both `justfile` and CI.
  This extension is trusted; do not add version pins, vendoring, or checksum checks.
- Dependabot keeps GitHub Actions dependencies up to date weekly. Python decks also have Dependabot configured for `uv`; R decks do not use Dependabot for R packages.

## What not to do

- Do not add new top-level files without a clear reason; the project intentionally has a flat structure.
- Do not split `index.qmd` into multiple files.
- Do not change the Quarto theme from `simple` or the output format from `revealjs`.
- Do not disable code execution (`eval: false`) on this deck; see the execution note above.
- Do not commit `_site/`, `_extensions/`, `index.html`, or `.quarto/` (all gitignored). For Python decks, `.venv/` is also gitignored.
- Do not modify the reusable CI workflow inline; it lives in a separate repository.
