# Level 7 UER Chinese GPT 2

*Published transformer base language model*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

A Chinese GPT-2 checkpoint uses twelve transformer layers and broad-corpus pretraining to continue text over a 21,128-token vocabulary.

## What this level adds

Learned attention replaces a fixed three-character context. Many layers build context-sensitive internal vectors, and a much larger corpus supplies broader syntax and vocabulary.

## How it works

The transformer predicts one token at a time from all tokens within its context window. It is a base language model, so a question may be continued rather than answered as a request.

## Example interaction

**Input**

> 理解语言意味着

**Output**

> 理解语言意味着能够把握词语之间的关系……

Illustrative continuation form, not a saved run. Sampling output varies.

## Interact with this level

1. Open the official model card and inspect its files, configuration, and usage example.
2. Run python3 run_model.py followed by a Chinese prefix to download and sample the checkpoint.
3. Try both an unfinished sentence and a direct question. Compare completion with instruction following.

## Suggested inputs

- `中国的首都是`
- `理解语言意味着`
- `请回答这个问题：猫是动物吗？`
- `为什么规则系统像是在理解？`

## What it still cannot show

- Pretraining optimizes continuation, not obedience to user requests.
- It can repeat common associations without reliably following a task.
- Broad linguistic behavior does not establish grounding outside its training text.

## Questions to notice

- Does attention over a longer context differ in kind from the n-gram table?
- Does learning representations across layers make the system less like a rule book?
- Should knowledge acquired from text count as contact with meaning?

## Transition to the next level

Level 8 adds instruction post-training to a small multilingual transformer so that it treats the input as a request and produces a conversational answer.

## Files in this folder

- Runnable code: [`run_model.py`](run_model.py)

## Sources and links

- [Official model card](https://huggingface.co/uer/gpt2-chinese-cluecorpussmall)
- [UER py repository](https://github.com/dbiir/UER-py)
