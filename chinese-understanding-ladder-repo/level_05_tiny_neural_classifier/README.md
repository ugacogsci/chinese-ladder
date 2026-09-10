# Level 5 Tiny neural intent classifier

*Small learned network with hand written responses*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

A 3,986-parameter neural network learns to classify Chinese prompts into six intentions, then selects a response template and applies a small name heuristic.

## What this level adds

Some input-output organization now comes from training examples and learned weights rather than a programmer writing every classification branch.

## How it works

Stable hashed character features feed a 192 by 20 hidden layer and a six-way output layer. Gradient descent trains the weights at startup. The final response sentences and name extraction remain explicit code.

## Example interaction

**Input**

> 如果小王把杯子借给阿明，后来阿明把杯子还给美玲，杯子最后在谁那里？

**Output**

> 我把它判断为多步归属问题；下面的名字提取器会尝试给出最后接收者。按最后出现的接收者猜测：美玲。

Reproducible output with the included training data; reported confidence is about 0.978.

## Interact with this level

1. Install NumPy in any Python environment.
2. Run python3 tiny_neural_bot.py --show-class followed by a quoted Chinese prompt.
3. Change a training example, retrain by rerunning the file, and compare the predicted intent.

## Suggested inputs

- `为什么这看起来像理解？`
- `请把理解翻译成英文，并解释它和模仿有什么区别。`
- `谁把地图还给小林？`
- `这是你没见过的新问题。`

## What it still cannot show

- The network learns categories, not the response language itself.
- Confidence measures competition among its six labels, not correctness or understanding.
- The last-name heuristic can answer for the wrong reason.

## Questions to notice

- Does learning from examples matter even when the learned representation is tiny?
- Are opaque weights less syntactic than readable rules?
- Would the same behavior deserve a different judgment if every weight were hand selected?

## Transition to the next level

Level 6 learns character-to-character transition statistics and generates the response text itself, although with only three characters of context.

## Files in this folder

- Runnable code: [`tiny_neural_bot.py`](tiny_neural_bot.py)

## Sources and links

- This level uses only the included teaching artifact.
