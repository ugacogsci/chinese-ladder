# Level 3 Deterministic symbolic engine

*Hand written parser and rule based question answering program*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

A short Python program recognizes several Chinese templates, looks up event tuples, answers who questions, accepts one paraphrase family, and tracks ownership across two transfers.

## What this level adds

The people and paper packet become executable software. The program also composes a result from two stated transfers rather than consulting only one stored event.

## How it works

Regular expressions bind named roles such as actor, object, and recipient. Tuples store events. Explicit branches select yes or no, missing actor, missing recipient, or transfer-chain behavior. The entire accepted language is visible in one file.

## Example interaction

**Input**

> 如果小王把杯子借给阿明，后来阿明把杯子还给美玲，杯子最后在谁那里？

**Output**

> 杯子最后在美玲那里。

Reproducible output from symbolic_engine.py.

## Interact with this level

1. Run python3 symbolic_engine.py followed by a quoted Chinese prompt.
2. Add --trace to display the matched rule and intermediate owner states.
3. Edit one event tuple or grammar alternative and observe exactly which inputs change.

## Suggested inputs

- `昨天小林是不是把蓝色地图借给阿明了？`
- `上周，谁把绿色的地图还给了小林？`
- `如果小王把杯子借给阿明，后来阿明把杯子还给美玲，杯子最后在谁那里？`
- `请解释为什么美玲有杯子。`

## What it still cannot show

- Every accepted construction and reasoning step is hand written.
- It rejects unfamiliar synonyms and word order even when a person understands them.
- The two-step rule does not generalize to arbitrary stories.

## Questions to notice

- Does speed or replacement of people by software affect attribution?
- Is composing two explicit rules importantly different from table lookup?
- Could the program's complete transparency count against it?

## Transition to the next level

Level 4 removes the requirement for an exact grammar match. It chooses an answer by graded similarity to stored examples.

## Files in this folder

- Runnable code: [`symbolic_engine.py`](symbolic_engine.py)

## Sources and links

- This level uses only the included teaching artifact.
