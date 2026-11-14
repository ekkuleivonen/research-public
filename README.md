# research-public

My research diary: independent digging into publicly available data, published.

I pick the questions, AI agents do much of the legwork (scraping, labelling, number
crunching, first drafts), and I check the work and sign off on everything that goes out. I keep
myself honest like this (details in [METHODS.md](METHODS.md)):

1. **I write my guess down first.** Before collecting any data, I commit the question and my
   prediction to [`preregistrations/`](preregistrations/). The commit timestamp is the proof.
2. **Anyone can rerun it.** Raw data is saved as dated snapshots that never change, and the
   derived datasets are published with each piece.
3. **I publish when I'm wrong.** Wrong predictions, null results and limitations go out too.
4. **I read everything before it ships.** Agents draft, I review and approve.

How I write it up is in [STYLE.md](STYLE.md).

## Publications

| Date | Title | Question |
|------|-------|----------|
| _none yet_ | | |

Each publication folder contains:

- `article.md`: the story
- `explore.py`: an interactive [marimo](https://marimo.io) notebook for poking at the data.
  Run it with `uvx marimo edit --sandbox explore.py`, or open the in-browser version linked
  from the article.
- `methods.md`: my lab notes: the prediction, decisions, dead ends and validation figures
- `data.md`: what's in the datasets and where to download them
- `CITATION.cff`: how to cite it

## Licence

Code (`*.py`) is under the [MIT licence](LICENSE). Writing and published datasets are under
[CC BY 4.0](LICENSE-CONTENT.md) unless a dataset's `data.md` says otherwise, for example
when an upstream licence applies.
