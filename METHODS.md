# How I do the research

The rules every project here follows.

## 1. I preregister

Before collecting any data, I commit the question, a prediction that could turn out wrong, and
the sources I plan to use to `preregistrations/<slug>.md`. If my prediction or plan changes
later, the publication says what changed and why.

## 2. I only use public data, politely

Data comes from publicly available sources only. Before collecting anything, I check
robots.txt and the terms of service, and I don't use sources that prohibit automated access.

## 3. I snapshot everything

Every raw collection is saved as a dated snapshot with a checksum, and it never changes
afterwards. Analyses run from those snapshots, not from live pages, so results don't shift when
websites do. I don't republish raw scraped content. Published datasets are derived or
aggregated.

## 4. I check the machine's homework

When a language model labels or classifies data, I get an independent set of labels for a
sample, either by hand or by a different method. Then I report how often the two agree
(Cohen's κ). If there's no agreement figure, the labels don't get published.

## 5. I publish the awkward parts

Every publication includes its limitations. Wrong predictions and null results are findings
and get published like any other.

## 6. Who does what

AI agents do much of the work: collecting data, labelling, analysis and first drafts. I choose
the questions, review the work, and approve every publication and every change to these rules.
