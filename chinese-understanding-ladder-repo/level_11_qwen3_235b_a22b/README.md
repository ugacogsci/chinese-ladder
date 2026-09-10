# Level 11 Qwen3 235B A22B Instruct

*Server scale sparse mixture of experts language model*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

This model expands the sparse instruction-tuned paradigm to 235 billion total parameters and 22 billion active per token.

## What this level adds

The organization remains recognizable while breadth, stored statistical structure, and task performance increase. The level exists to prevent frontier behavior from appearing as one unexplained jump.

## How it works

A transformer routes tokens among many learned experts while maintaining shared attention and residual state. Only a fraction of the stored parameters participates in each token's forward pass.

## Example interaction

**Input**

> 构造一个你能想到的、反对塞尔的最强新思想实验，然后说明什么证据会使它失败。

**Output**

> 可以设想逐步用功能等价的人工部件替换双语者的神经过程，同时保持对话和自我报告。如果有证据表明功能等价虽然保存了行为，却系统地移除了意义所需的因果能力，这个反例就会失败。

Illustrative answer form, not a saved run. It is included to show the intended test, not a benchmark claim.

## Interact with this level

1. Open the official model card and use an offered inference provider or another compatible hosted deployment.
2. Self-host only with appropriate server hardware and deployment expertise.
3. Use the same prompts as Level 10 before adding harder long-form synthesis or counterfactual tasks.

## Suggested inputs

- `创造一个新的中文房间变体，并分析争论双方。`
- `说明这个分析成立所需的假设。`
- `反转其中一个假设，然后更新结论。`
- `在十轮追问中保持一个一致的立场。`

## What it still cannot show

- Server-scale sophistication remains behavioral evidence under one experimental interface.
- The model may produce persuasive but unsupported philosophical arguments.
- The absence of a sharp architectural threshold leaves the attribution question unresolved.

## Questions to notice

- Did your rating rise smoothly or jump despite a mostly quantitative change?
- Does a more coherent self-defense count as evidence, or is it only another output?
- What would this model need besides text to satisfy your criterion?

## Transition to the next level

Level 12 adds native visual input, a one-million-token context, and tool-oriented agentic behavior while greatly scaling the sparse model.

## Files in this folder

- Runnable code: [`run_model.py`](run_model.py)

## Sources and links

- [Official model card](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)
- [Qwen3 repository](https://github.com/QwenLM/Qwen3)
