# AGENTS.md

A single-page [Quarto](https://quarto.org/) presentation rendered to
[RevealJS](https://revealjs.com/) slides and deployed as a static site via
GitHub Pages. The `justfile` lists the commands; `just render` must succeed
before you push. CI renders with `options(warn = 2)`, so any R warning fails
the build.

## Key conventions

- **Single-file deck.** All slides live in `index.qmd`; do not split it.
- **Design specification.** The visual design follows [DESIGN.md](DESIGN.md).
  Respect it when creating or modifying slides, components, styling, colours,
  and typography. Restyle through `style.css`; new widgets follow the naming
  patterns already there.
- **Scroll-view image sizing.** The snapshot-review screenshot uses
  `.nostretch` to stop RevealJS auto-stretch collapsing it. Check its sizing
  in both presentation mode and native `?view=scroll` when changing that
  slide.
- **Sources.** Every factual claim has a source citation at the bottom of its
  slide in a small-font centred div. Keep this pattern.
- **Spelling and punctuation.** Use British spelling in prose (colour, licence,
  catalogue, artefact) and the Oxford comma in lists of three or more. Leave
  code, identifiers, file names, URLs, quotations, and proper names (`license`
  in YAML, `.well-known/api-catalog`) as they are.
- **Spoken notes.** The read-aloud control speaks the `.notes` content. Write
  complete, audience-facing narration; keep staging cues, private reminders,
  and delivery checklists outside these blocks.
- **Accessibility.** Images must have `fig-alt` text; raw HTML widgets use
  `role="img"` and `aria-label`.
- **Icons.** Icons are HTML spans backed by only the required SVG path data in
  `style.css`; no icon font or Quarto icon extension. When adding one, add only
  its mask data, preserve the source licence attribution, and keep an
  accessible label where the icon conveys meaning.
- **Code execution is on.** Keep `execute: eval: true`: slides run live
  `testthat` snapshot examples (including deliberate failures via
  `error=TRUE`), build a `ggplot2` figure, and include screenshots with
  `knitr::include_graphics()`, so disabling it blanks those slides. Declare
  every package a chunk uses in `DESCRIPTION`; `just install` and CI install
  R dependencies from it.
- **Discoverability files.** Update `meta-tags.html` when the title,
  description, or social card changes, and `llms.txt` / `llms-full.txt` (and
  their `.well-known/` mirrors) when the content changes significantly.
- **No new top-level files** without a clear reason; the structure is flat.

## CI/CD

- `.github/workflows/build-presentation.yaml` calls a reusable workflow from
  `IndrajeetPatil/workflows`: pushes to `main` build and deploy to GitHub
  Pages, pull requests build without deploying. Do not inline or modify that
  workflow here.
- Reference reusable workflows as `@main`, never a commit SHA: they are
  first-party, and a pinned SHA goes stale unnoticed.
- `check-link-rot.yaml` checks external links; list false positives in
  `.lycheeignore`.

## Agent skills

Skills live in `.agents/skills/<name>/SKILL.md`. Load one before its task:

| Skill | Load before |
| --- | --- |
| `check-accessibility` | Changing slide markup, styles, widgets, menus or the a11y setup; any accessibility audit |
