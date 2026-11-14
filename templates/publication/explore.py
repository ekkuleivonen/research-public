# /// script
# requires-python = ">=3.12"
# dependencies = ["marimo", "pandas", "pyarrow", "altair"]
# ///
# Self-contained: loads only public data. Run with `uvx marimo edit --sandbox explore.py`.
# Uses pandas rather than polars so the in-browser (WASM) export works.

import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import altair as alt
    import marimo as mo
    import pandas as pd

    DATA = "TODO: https://<r2-public-url>/{{slug}}/data/<file>.parquet"
    return DATA, alt, mo, pd


@app.cell
def _(mo):
    mo.md(
        """
        # {{title}}

        {{description}}

        TODO: a short note from me on what you can poke at here
        """
    )
    return


@app.cell
def _(DATA, pd):
    df = pd.read_parquet(DATA)
    df
    return (df,)


if __name__ == "__main__":
    app.run()
