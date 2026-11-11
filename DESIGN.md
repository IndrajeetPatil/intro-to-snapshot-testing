---
version: alpha
name: Introduction to Snapshot Testing in R
description: >-
  Snapshot and visual regression testing presentation design: clean white
  canvas, high-contrast code diffing, warm line highlights, and testing iconography.
colors:
  primary: "#222222"
  secondary: "#006dad"
  bg-canvas: "#ffffff"
  text: "#222222"
  muted: "#666666"
  code-highlight: "#fff8e1"
  check-green: "#28a745"
  xmark-red: "#dc3545"
typography:
  display:
    fontFamily: News Cycle, Impact, sans-serif
    fontSize: 2.1em
    fontWeight: 700
  heading:
    fontFamily: News Cycle, Impact, sans-serif
    fontSize: 1.4em
    fontWeight: 700
  body:
    fontFamily: News Cycle, sans-serif
    fontSize: 32px
    fontWeight: 400
  mono:
    fontFamily: monospace
rounded:
  sm: 4px
  md: 8px
components:
  page:
    backgroundColor: "{colors.bg-canvas}"
    textColor: "{colors.text}"
  code-highlight:
    backgroundColor: "{colors.code-highlight}"
---

# DESIGN.md

The visual design specification of the Introduction to Snapshot Testing in R presentation deck.

## Overview

The visual design is structured for teaching software verification, snapshot testing, and visual regression workflows in R (`testthat`, `vdiffr`, and `shinytest2`). It uses the RevealJS `simple` theme with a crisp white canvas (`#ffffff`), dark charcoal typography (`#222222`), warm line-level code highlights (`#fff8e1`), and a rich set of testing-focused SVG mask icons.

The presentation format is Quarto RevealJS (`theme: simple`). Custom styles are defined in `style.css` and mirrored in the front matter above.

## Colours

- **Canvas & Typography:**
  - `bg-canvas` (`#ffffff`): Crisp white presentation canvas across all slides.
  - `text` (`#222222`): Standard high-contrast charcoal text.
  - `muted` (`#666666`): Footers and secondary metadata.
- **Code & Testing Accents:**
  - `code-highlight` (`#fff8e1`): Warm highlight background for active code lines, preserving 100% opacity on unhighlighted lines to protect contrast.
  - `check-green` (`#28a745`): Test pass cues and snapshot matches.
  - `xmark-red` (`#dc3545`): Test failure cues, snapshot diffs, and regression warnings.

## Typography

- **Headings & Body:** Default clean sans-serif stack from RevealJS `simple` (`News Cycle`, `Impact`, sans-serif).
- **Code:** Monospace stack for R unit test assertions (`expect_snapshot()`), terminal outputs, and file diffs.

## Layout & Components

- **Title Slide:** Prominently displays the combined ecosystem artwork (`testthat`, `vdiffr`, and `shinytest2` hex logos) using `.absolute` positioning with explicit width/height to ensure stable geometry across standard and scroll views.
- **Callouts:** Standard Quarto callouts (`.callout-important`, `.callout-tip`) used for critical testing warnings (e.g. non-deterministic outputs, platform dependencies).
- **Icons:** SVG mask icons (`.deck-icon`) using Font Awesome Free paths (circle-check, circle-xmark, file-code, flask, equals, arrows-left-right) rendered in `currentColor`.

## Do's and Don'ts

- **Do** retain `theme: simple` in `index.qmd` front matter.
- **Do** preserve the warm `#fff8e1` line-highlight styling for walkthroughs of test assertions and snapshot files.
- **Do** retain accessible SVG masks and `.visually-hidden` headings for untitled visual layouts.
- **Don't** introduce dark backgrounds that diminish the readability of code diffs and snapshot comparisons.
