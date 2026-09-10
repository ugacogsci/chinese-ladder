# Level 6 Character n gram generator

*Locally trained statistical language model*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

A tiny model learns which Chinese character tends to follow each three-character context in an included corpus, then samples continuations.

## What this level adds

The system produces response text from learned sequence statistics rather than choosing a hand-written answer. It can splice familiar fragments into a sentence absent from the corpus.

## How it works

Training counts every next character after a three-character context. Generation repeatedly samples from those counts and backs off to a sentence start when a context has never appeared.

## Example interaction

**Input**

> 小王

**Output**

> 小王先把杯子借给阿明，后来阿明把绿色的地图借给了小林，因为外面正在下雨。

Reproducible with --seed 4. The fluent-looking sentence splices incompatible training fragments.

## Interact with this level

1. Run python3 character_ngram.py --seed 4 followed by a short Chinese prefix.
2. Add --show-model to display context and transition counts.
3. Change the seed, prefix, corpus, or ORDER constant and compare fluency with consistency.

## Suggested inputs

- `小王`
- `理解`
- `系统`
- `语言模型`

## What it still cannot show

- Only the preceding three characters influence the next choice.
- It does not distinguish a question from an instruction.
- Local fluency can coexist with contradictions and accidental recombination.

## Questions to notice

- Does generating a novel string matter if the novelty comes from local recombination?
- At what context length would lookup and generation stop feeling different?
- Is statistical prediction a new kind of mechanism or a very large conditional rule table?

## Transition to the next level

Level 7 keeps next-token generation but replaces the tiny corpus and three-character memory with a published transformer pretrained on a large Chinese corpus.

## Files in this folder

- Runnable code: [`character_ngram.py`](character_ngram.py)

## Sources and links

- This level uses only the included teaching artifact.
