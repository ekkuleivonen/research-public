# research-public

Ekku's public research diary. The research happens in the private lab repo, and this repo
receives its output.

- `publications/<slug>/` is created by `lab publish` from `templates/publication/` and holds
  `article.md` (the story, then lab notes and data links at the end) and `explore.py`.
  Replace every `TODO` before the second `lab publish` run, which opens the PR.
- `explore.py` must run on its own: PEP 723 dependencies, pandas (the in-browser export
  needs it), data from public URLs only, no imports from the private `lab` package.
- No secrets, internal hostnames or raw scraped content. Only derived data.
