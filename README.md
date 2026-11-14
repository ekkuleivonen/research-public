# research-public

Independent research on publicly available data, carried out by AI agents under human
editorial review.

Every project follows the same protocol (see [METHODS.md](METHODS.md)), and every
write-up follows the same house style (see [STYLE.md](STYLE.md)):

1. **Preregistered.** The question and hypothesis are committed to
   [`preregistrations/`](preregistrations/) *before* any data is collected. The commit
   timestamp is the proof.
2. **Reproducible.** Raw data is captured as dated, immutable snapshots. Derived datasets
   are published with each piece of research.
3. **Honest.** Limitations, failed hypotheses and null results are published too.
4. **Reviewed.** A human approves every publication before it goes live.

## Publications

| Date | Title | Question |
|------|-------|----------|
| _none yet_ | | |

Each publication folder contains:

- `article.md`: the write-up
- `explore.py`: an interactive [marimo](https://marimo.io) notebook. Run it with
  `uvx marimo edit --sandbox explore.py`, or open the in-browser version linked from the article.
- `methods.md`: hypothesis, decisions, dead ends and validation figures
- `data.md`: dataset descriptions and download links
- `CITATION.cff`: how to cite it

## Licence

Code (`*.py`) is under the [MIT licence](LICENSE). Writing and published datasets are under
[CC BY 4.0](LICENSE-CONTENT.md) unless a dataset's `data.md` says otherwise, for example
when an upstream licence applies.
