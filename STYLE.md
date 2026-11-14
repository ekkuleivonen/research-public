# How we write

Our publications should be the kind of thing people send to a friend, and the friend actually
reads it. We aim for **infotainment with a dry sense of humour**: rigorous underneath, enjoyable
on top, and clear to anyone who's curious, whether they write code or not.

When these goals pull against each other, they rank in this order:

1. **True.** Nothing gets exaggerated for a better story or a better joke.
2. **Clear.** A reader with no technical background follows every step.
3. **Enjoyable.** They want to keep reading.
4. **Funny.** It's a bonus, never at the expense of 1–3.

## Who we're writing for

Picture a clever friend from a different field. They're curious and smart, they're happy to
think, and they have no patience for jargon. If they'd have to stop and look something up,
the sentence has failed. Technical readers aren't left out. They get `methods.md` and
`explore.py`, so the article itself doesn't have to show its working.

## Shape of an article

- **Open with the question, made concrete.** Start from a situation the reader recognises, not from the dataset.
  "Every flat listing says 'close to transport'. We measured how close."
- **Give the answer early.** The TL;DR states the finding plainly, including when it's
  "no, and here's the interesting part". Suspense is for novels.
- **One idea per section, one point per chart.** If a section needs two charts to make one
  point, the point isn't clear yet.
- **Chart titles state the finding**, not the variables: "Listings get vaguer as rent goes up",
  not "Description length vs. monthly rent".
- **End with what we still don't know.** The limitations section is part of the story, not a
  disclaimer. Write it with the same care, and the same personality, as the rest.

## Plain language

- Use the everyday word: "about a quarter", not "approximately 24.7%". "Tends to", not
  "is positively correlated with". "We checked a sample by hand", not "we validated against a
  gold-standard annotation set".
- When a technical idea really matters, explain what it *does* the first time it comes up,
  in a clause rather than a footnote. Name it once and move on.
  "We had a second labeller grade 200 of the same posts and measured how often they agreed,
  beyond what chance alone would give (statisticians call this kappa; ours was 0.81, which is good)."
- Give numbers something familiar to compare against: "1 in 4", "roughly the population of
  Tampere", "twice as often as".
- Say uncertainty plainly: "probably", "we can't tell from this data", "this could also be
  explained by…". Don't hide it in confidence intervals the reader can't parse. The exact
  figures go in `methods.md`.
- Use short sentences and active voice. Write "we" for the research, and say plainly in
  `methods.md` that AI agents did the work.

## Humour

The humour is dry: deadpan, understated, and mostly found in the facts themselves.

- **Let the data deliver the punchline.** State an absurd finding flatly and let it land.
  "Of the 4,000 listings that mentioned a 'cosy' bedroom, the median size was 7 m². Cosy is
  doing a lot of work."
- **Understate, don't exaggerate.** "This was not the result we expected" beats "Mind = blown 🤯".
- **Be self-deprecating about our own methods and mistakes**, not about other people.
  "Our first scraper confidently collected 3,000 copies of a cookie banner."
- **Never punch at the people in the data.** Landlords, posters and survey respondents are
  the subject, not the butt of the joke. Groups, places and individuals in the data are off
  limits.
- **Leave serious topics alone.** If the subject touches on harm, health, money trouble or
  grief, drop the jokes and keep only the warmth.
- **A joke never replaces a finding.** If you delete the joke, the paragraph must still say
  what it needs to. If a joke makes a result sound bigger, smaller or more certain than it
  is, cut it.
- One good line beats five okay ones. If you're unsure whether something is funny, it isn't. Cut it.

## Charts

- Show one message per chart. Label the lines and bars directly rather than using a legend
  where possible, and keep a sentence of interpretation next to every chart.
- Use units people know, and axis labels in words, not column names.
- Use the shared theme (`lab.style` in the lab, the same palette in `explore.py`).
- Reach for interactivity only when exploring *is* the point. That's what `explore.py` is for.

## The explore notebook

`explore.py` follows the same voice. Open with a short "here's what you can poke at" guide,
use plain-language labels for every control, and keep one prose sentence above each output
explaining what it shows. Readers should be able to play without reading the article first.

## Before and after

> **Before:** We scraped 12,408 rental listings and applied an LLM-based classifier to extract
> amenity mentions, achieving κ = 0.81 against human annotations. Results indicate a
> statistically significant positive association between listing price and description length
> (ρ = 0.34, p < 0.001).
>
> **After:** We read 12,408 rental ads, or rather, a language model did, and we checked its
> homework by grading 200 of the same ads ourselves. We agreed most of the time. The pricier
> the flat, the longer the ad, though only loosely: at the top end, the adjectives appear to be
> included in the rent.

## Checklist before publishing

- [ ] Could a non-technical reader explain the main finding after one read?
- [ ] Is every technical term either gone or explained where it first appears?
- [ ] Does every chart title state a finding?
- [ ] Is every number in the article traceable to the notebook or `methods.md`?
- [ ] Does any joke punch at people in the data, or make a result sound more certain than it is?
- [ ] Does the article say plainly whether the preregistered hypothesis held?
- [ ] Are the limitations written as carefully as the findings?
