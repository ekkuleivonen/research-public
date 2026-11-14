# How I write

This is my research diary, published. Each piece should read like a trip I took through some
data, the kind of thing people send to a friend, and the friend actually reads it. I'm going for
**infotainment with a dry sense of humour**: rigorous underneath, enjoyable on top, and clear to
anyone who's curious, whether they write code or not.

When these goals pull against each other, they rank in this order:

1. **True.** Nothing gets exaggerated for a better story or a better joke.
2. **Clear.** A reader with no technical background follows every step.
3. **Enjoyable.** They want to keep reading.
4. **Funny.** It's a bonus, never at the expense of 1–3.

## Voice: my diary

- **Write as me (Ekku), in the first person singular.** "I wondered", "I expected", "I was
  wrong". Never "we", never "the authors", never the passive voice to dodge who did something.
- **The AI agents are characters, not ghostwriters.** I pick the questions, check the work and
  sign off on every publication. The agents do much of the legwork, and the text says so in
  passing: "I asked my agent to read 12,408 rental ads. It did, without complaint, which is
  more than I'd have managed." Never claim I personally did something an agent did.
- **It's a trace, not a press release.** Show the path: what made me curious, what I guessed,
  what I tried, what broke, what I changed my mind about. The dead ends belong in the story.
  They're often the most honest and the funniest parts.
- **Use the diary's natural tone:** candid, a little wry, thinking out loud. Confident about the
  data, modest about myself.

## Who I'm writing for

Picture a clever friend from a different field. They're curious and smart, they're happy to
think, and they have no patience for jargon. If they'd have to stop and look something up,
the sentence has failed. Technical readers aren't left out. They get `methods.md` and
`explore.py`, so the article itself doesn't have to show its working.

## Shape of an article

- **TL;DR first.** Before the diary starts, give the finding in a sentence or two, including
  when it's "no, and here's the interesting part". Suspense is for novels.
- **Then open with what made me wonder**, made concrete. Start from a situation the reader
  recognises, not from the dataset. "Every flat listing in Helsinki says 'close to transport'.
  I started to suspect this was aspirational."
- **Follow the trail in order:** the hunch, my prediction (as preregistered), getting the data,
  what went wrong, what I found. Dated entries or a looser narrative both work. Pick whatever
  suits the story.
- **One idea per section, one point per chart.** If a section needs two charts to make one
  point, the point isn't clear yet.
- **Chart titles state the finding**, not the variables: "Listings get vaguer as rent goes up",
  not "Description length vs. monthly rent".
- **Say plainly whether I was right.** My preregistered prediction gets a clear verdict.
  Being wrong is a fine result and usually a better story.
- **End with what I still don't know.** The limitations are part of the diary, not a
  disclaimer. Write them with the same care, and the same personality, as the rest.

## Plain language

- Use the everyday word: "about a quarter", not "approximately 24.7%". "Tends to", not
  "is positively correlated with". "I checked a sample by hand", not "validated against a
  gold-standard annotation set".
- When a technical idea really matters, explain what it *does* the first time it comes up,
  in a clause rather than a footnote. Name it once and move on.
  "I graded 200 of the same ads myself and measured how often my agent and I agreed, beyond
  what chance alone would give (statisticians call this kappa; ours was 0.81, which is good)."
- Give numbers something familiar to compare against: "1 in 4", "roughly the population of
  Tampere", "twice as often as".
- Say uncertainty plainly: "probably", "I can't tell from this data", "this could also be
  explained by…". Don't hide it in confidence intervals the reader can't parse. The exact
  figures go in `methods.md`.
- Use short sentences and active voice.

## Humour

The humour is dry: deadpan, understated, and mostly found in the facts themselves.

**Fair game:** the data, my methodology, and occasionally me. **Off limits:** everyone else.
That includes the people in the data, other researchers, the sources and any particular group or place.

- **Let the data deliver the punchline.** State an absurd finding flatly and let it land.
  "Of the 4,000 listings that mentioned a 'cosy' bedroom, the median size was 7 m². Cosy is
  doing a lot of work."
- **Make fun of the method.** "My first scraper confidently collected 3,000 copies of a cookie
  banner." "The model labelled a parking space as 'a charming studio'. In fairness, so did the ad."
- **Make fun of me, sparingly.** "I predicted a strong effect. The data predicted I'd be
  writing this paragraph." Once or twice per piece is plenty. Self-deprecation that never
  stops turns into fishing for sympathy.
- **Understate, don't exaggerate.** "This was not the result I expected" beats "Mind = blown 🤯".
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

## The other files

The same voice runs through everything public: `article.md`, `methods.md`, `data.md`,
`explore.py` and the preregistrations.

- **`methods.md`** is the technical page of my lab notebook. It's still first person and still
  readable, but this is where the exact figures, choices and dead ends go in full. The jokes
  get rarer here. Precision comes first.
- **`explore.py`** opens with a short "here's what you can poke at" note from me, uses
  plain-language labels for every control, and has one sentence above each output saying what
  it shows. Readers should be able to play without reading the article first.

## Before and after

> **Before:** We scraped 12,408 rental listings and applied an LLM-based classifier to extract
> amenity mentions, achieving κ = 0.81 against human annotations. Results indicate a
> statistically significant positive association between listing price and description length
> (ρ = 0.34, p < 0.001).
>
> **After:** I asked my agent to read 12,408 rental ads, then checked its homework by grading
> 200 of them myself. We agreed most of the time, and the disagreements were mostly my fault.
> The pricier the flat, the longer the ad, though only loosely. I'd predicted a much stronger
> link. At the top end, the adjectives appear to be included in the rent.

## Checklist before publishing

- [ ] Is it in my voice throughout, first person singular, reading like a diary rather than a report?
- [ ] Is it clear where an agent did the work rather than me?
- [ ] Could a non-technical reader explain the main finding after one read?
- [ ] Is every technical term either gone or explained where it first appears?
- [ ] Does every chart title state a finding?
- [ ] Is every number in the article traceable to the notebook or `methods.md`?
- [ ] Is every joke aimed at the data, the method or me, and none at anyone else?
- [ ] Does any joke make a result sound bigger, smaller or more certain than it is?
- [ ] Does the article say plainly whether my preregistered prediction held?
- [ ] Are the limitations written as carefully as the findings?
