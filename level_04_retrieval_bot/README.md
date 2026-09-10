# Level 4 Approximate retrieval bot

*Character n gram TF IDF nearest neighbor system*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

The program measures how similar a new Chinese prompt is to stored examples and returns the answer paired with the nearest example.

## What this level adds

Matching becomes graded rather than all or nothing. Unseen wording can succeed when its characters and short character sequences resemble a stored question.

## How it works

Each question becomes counts of characters and two-character sequences. TF IDF weights rarer features more heavily. Cosine similarity selects the nearest stored prompt, subject to a minimum threshold.

## Example interaction

**Input**

> 昨天小林是否把蓝地图借给阿明？

**Output**

> 是的，昨天小林把蓝色的地图借给了阿明。

Reproducible output. The nearest stored prompt scores about 0.669 with the included data.

## Interact with this level

1. Run python3 retrieval_bot.py followed by a quoted Chinese prompt.
2. Add --show-match to reveal the stored question and cosine similarity score.
3. Add or delete one example pair in EXAMPLES and test the same prompt again.

## Suggested inputs

- `昨天小林是否把蓝地图借给阿明？`
- `理解跟模仿有什么不同？`
- `为什么这个规则机器好像会中文？`
- `如果小王把杯子借给阿明后来阿明还给美玲呢？`

## What it still cannot show

- The chosen answer is copied from a stored pair rather than derived from the prompt.
- Small wording changes can cause a different neighbor to win.
- Similarity does not ensure that roles, negation, or factual relations match.

## Questions to notice

- Is approximate recognition a qualitative change from explicit rules?
- Does a continuous similarity score resemble human categorization more than a branch does?
- If the output is copied, does it matter how flexibly the input was matched?

## Transition to the next level

Level 5 learns the mapping from text features to response category as neural weights instead of calculating a stored neighbor directly.

## Files in this folder

- Runnable code: [`retrieval_bot.py`](retrieval_bot.py)

## Sources and links

- This level uses only the included teaching artifact.
