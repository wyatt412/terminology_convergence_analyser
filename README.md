# Terminology Convergence Analyser
A lightweight, reproducible workflow for analysing competing lexical variants of the same concepts in large corpora.
The project focuses on **variant identification, normalisation, contextual disambiguation**, and **dominance scoring**.

Although the case study uses Arabic, a very lexically abundant language where this analyser comes to its usage, the workflow aims to be **language-agnostic**, and hopefully can be adapted to other languages and domains.

## What does this project does

Given:
- a concept (e.g., "Hashtag")
- a list of candidate variants (surface forms)
- (optional) concordance samples exported a corpus tool

The workflow produces:
- frequency table for each variant
- dominance ratio (share of the most frequent variant)
- a convergence label (strong / medium / weak)
- simple visualisations (variant distribution)

## Workflow (high level)

1. **Variant specification** (concept → variant list)
2. **Corpus querying** (via corpus tool; exports as input)
3. **Normalisation** (merge known surface variations)
4. **Disambiguation (optional)** using concordance filtering rules
5. **Metrics & reporting** (dominance scoring + plots)

## Repository structure

- 'docs/' - diagrams and documentation
- 'data/sample/' - small representative samples
- 'notebooks/' - demo notebooks
- 'src/' - scripts/modules (to be added)

## Data note

This corpus does **not** contain full dumps of certain corpus.
Instead, it uses **small representative samples** (e.g. 100 concordance lines) for demonstrating the workflow. Please note that this is a common practice due to corpus access and licensing constraints.

## Next steps

- Add 'config/terms.yml' to store concept-variant mappings
- Add a demo disambiguation example (e.g., filtering ambiguous variants using simple markers)
- Generate 1-2 plots for variant distributions
