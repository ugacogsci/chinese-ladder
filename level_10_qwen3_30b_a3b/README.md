# Level 10 Qwen3 30B A3B Instruct

*Sparse mixture of experts instruction model*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

A sparse transformer stores 30.5 billion parameters but activates about 3.3 billion per token. A router selects eight of 128 learned experts.

## What this level adds

Specialization and routing become explicit parts of the neural architecture. Total learned capacity grows much faster than the computation used for a single token.

## How it works

Attention layers share context across the sequence. In mixture-of-experts feed-forward layers, a learned router chooses a small subset of expert networks for each token and combines their outputs.

## Example interaction

**Input**

> 分析中文房间的系统回复、机器人回复和大脑模拟回复，并说明它们分别把理解归因于什么。

**Output**

> 系统回复把理解归因于房间内人员、规则和记忆构成的整体；机器人回复加入感知与行动，把符号与环境联系起来；大脑模拟回复认为，如果因果组织足够接近大脑，就不应仅因实现材料不同而否认理解。

Illustrative answer form, not a saved run. Actual output depends on serving and sampling settings.

## Interact with this level

1. Open the official model card and select an offered hosted inference provider.
2. If suitable hardware is available, run python3 run_model.py --allow-large-download followed by a prompt.
3. Ask one multi-part prompt, then inspect whether the answer preserves every requested distinction.

## Suggested inputs

- `比较对塞尔的三种回复，但不要赞成其中任何一种。`
- `把这个比较改写成三位哲学家的对话。`
- `找出这三种回复共同依赖的一个假设。`
- `把最后的答案译成英文，并保留其中的区别。`

## What it still cannot show

- Expert labels do not correspond neatly to human concepts or jobs.
- Routing explains efficient computation, not whether the routed whole understands.
- Text-only interaction still leaves perceptual grounding largely indirect.

## Questions to notice

- Does a routed population of experts resemble the distributed room more than a dense model does?
- Could understanding belong to the routed whole when no expert sees the entire computation?
- Is sparse activation philosophically relevant or merely an engineering detail?

## Transition to the next level

Level 11 keeps the sparse design but scales it to 235 billion total and 22 billion active parameters, making the transition one of degree again.

## Files in this folder

- Runnable code: [`run_model.py`](run_model.py)

## Sources and links

- [Official model card](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)
- [Qwen3 repository](https://github.com/QwenLM/Qwen3)
