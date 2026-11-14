# AGENTS.md — research-public

This repository is the **public archive**. Don't do research here. That happens in the
private lab repo.

- Changes arrive only through the lab's `lab prereg` (direct commit) and `lab publish`
  (pull request). Don't edit `preregistrations/` after they are committed.
- Publications follow `templates/publication/`. Every `TODO` must be replaced before
  a publication PR.
- `explore.py` must run on its own: PEP 723 inline dependencies, data loaded only from
  public URLs, no imports from the private `lab` package.
- `methods.md` is a condensed version of the project's log. Keep the hypothesis, decisions,
  dead ends and validation figures.
- Never include secrets, internal hostnames or raw scraped content.
