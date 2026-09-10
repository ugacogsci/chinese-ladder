# Level 9 Qwen3 4B Instruct

*Medium dense instruction tuned language model*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

A four-billion-parameter dense model extends the same general approach with more learned capacity, thirty-six layers, and a 262,144-token context.

## What this level adds

The mechanism does not change dramatically. The model can preserve and transform more context, represent more patterns, and usually handle more involved instructions.

## How it works

Every token passes through the same dense transformer layers. Attention relates tokens across the context, and post-training shapes the model for conversational tasks.

## Example interaction

**Input**

> 解释为什么一个只按规则移动符号的系统可能看起来理解中文，并给出一个反对这种说法的理由。

**Output**

> 它可能稳定地把输入映射到合适输出，因此外部观察者会看到类似理解的行为。反对者会说，这种行为也许只展示了形式操作，并没有说明系统把符号与意义联系起来。

Illustrative answer form, not a saved run. Actual generations vary.

## Interact with this level

1. Open the official model card and choose an offered inference provider, or use the included runner.
2. Run python3 run_model.py followed by a Chinese request.
3. Give it a multi-paragraph story, ask role-binding questions, then introduce a counterfactual change.

## Suggested inputs

- `依次回答仓库首页中的六个共同问题。`
- `用不超过一百五十个汉字解释对塞尔最有力的系统回复。`
- `现在反驳你刚才的答案。`
- `创造一个意义相同但表面字符很少重叠的改写。`

## What it still cannot show

- More capacity can improve performance without creating a visible conceptual boundary.
- Long context is available memory, not guaranteed faithful use of every detail.
- The model remains vulnerable to hallucination, framing, and adversarial phrasing.

## Questions to notice

- If the only obvious change is degree, why might your attribution still move sharply?
- Does preserving roles across a long story provide evidence of a world model?
- Would a smaller model with external memory deserve the same rating?

## Transition to the next level

Level 10 changes the internal scaling pattern. A learned router sends each token through a small subset of many specialized feed-forward experts.

## Files in this folder

- Runnable code: [`run_model.py`](run_model.py)

## Sources and links

- [Official model card](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)
- [Qwen3 repository](https://github.com/QwenLM/Qwen3)
