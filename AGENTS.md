# research-public

The public archive of finished research. The research itself happens in the private lab repo.
This repo receives its output.

## How changes arrive

- `lab prereg` commits files to `preregistrations/`. They are the timestamped proof that a
  hypothesis came before the data, so never edit them afterwards. Add a dated note to the
  publication's `methods.md` instead.
- `lab publish` scaffolds `publications/<slug>/` from `templates/publication/`, and a second
  run opens the PR. Replace every `TODO` before that second run.

## Publication files

- `article.md`: the write-up for everyone. Keep the technical detail in `methods.md`.
- `methods.md`: a condensed version of the project's log. Keep the hypothesis, any changes
  since preregistration, exclusions with counts, validation figures and dead ends.
- `data.md`: a table per published file. Note any upstream licence that overrides CC BY 4.0.
- `explore.py`: runs on its own with PEP 723 dependencies. It uses pandas, not polars,
  because the in-browser export needs it, and it loads data only from public URLs.
  Don't import the private `lab` package.
- Raw scraped content, secrets and internal hostnames never belong here, only derived data.

## Writing style

All prose, including notebook text, follows the house style:

@STYLE.md
