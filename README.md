# Introduction to snapshot (aka golden) testing (in R)

In this presentation, I introduce what is snapshot testing, why is it
necessary, and its implementation in R in `{testthat}` package and its
extensions.

<img src="media/logos_combined.webp" width="70%" alt="Logos Combined" />

In particular, the presentation provides a detailed account of how these
tests are valuable in testing:

- text outputs
- graphical outputs
- Shiny apps
- entire files

Slides can be seen here:
<https://www.indrapatil.com/intro-to-snapshot-testing/>

## Development

This project uses R 4.6.0 or later (declared in `DESCRIPTION`), [Quarto](https://quarto.org/) for rendering slides, and [just](https://github.com/casey/just) as a command runner.

### Prerequisites

```bash
# Install just (macOS)
brew install just
```

### Setup

```bash
just install
```

### Just Commands

```bash
just help     # Show all available commands
just install  # Install R dependencies from DESCRIPTION
just render   # Render slides to HTML
just preview  # Start a live preview with auto-reload
just open     # Alias for preview (live-reload dev server over localhost)
just clean    # Remove generated files and caches
just check    # Check the Quarto and R version setup
just axe      # Preview with an Accessibility Report slide
just          # Install dependencies and start live-reload preview
```

`just axe` enables the opt-in `a11y` profile. It accepts preview options, for example `just axe --no-browser --port 8834`. Inspect slide and scroll views, including all fragments and tab panels. Run `just render` for the production deck, which excludes the audit payload and report.

## Feedback

Feedback and suggestions are welcome in [the issue tracker](https://github.com/IndrajeetPatil/intro-to-snapshot-testing/issues).
