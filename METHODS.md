# Methods

The standards that every publication in this repository follows.

## 1. Preregistration

Before any data is collected, the question, a falsifiable hypothesis and the planned
sources are committed to `preregistrations/<slug>.md`. If the hypothesis or the
analysis plan changes later, the publication says so and explains why.

## 2. Sources

Data comes only from publicly available sources. robots.txt and terms of service are
checked before collection. Sources that prohibit automated access are not used.

## 3. Snapshots

Raw collections are stored as dated, immutable snapshots with checksums. Analyses run
from snapshots, not live pages, so results don't change when websites do.
Raw scraped content is not republished. Published datasets are derived and aggregated.

## 4. LLM labelling

When a language model labels or classifies data, its labels are checked against an
independent sample, either labelled by hand or by a different method, and the agreement (Cohen's κ) is
reported. Labels with no agreement figure are not published.

## 5. Reporting

Every publication includes its limitations. Hypotheses that turn out wrong and null
results are published as findings.

## 6. Who does the work

The research is carried out by AI agents: collection, analysis and first drafts. A human
reviews and approves every publication and every change to these standards.
