# Level 12 Kimi K3

*Frontier native multimodal agentic sparse model*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

Kimi K3 is an open-weight model with 2.8 trillion total parameters (the largest of any open-weight model, released this summer by Moonshot AI, a Chinese lab based in Beijing), 104 billion active, native image and video input, and a one-million-token context.

## What this level adds

The final level combines frontier-scale sparse computation with perception-like inputs, very long working context, tool calls, and sustained multi-step action.

## How it works

Kimi K3 uses a highly sparse mixture-of-experts architecture with 896 experts and sixteen active, together with Kimi Delta Attention and Attention Residuals. Its deployed interface can coordinate text, visual input, tools, and long interaction histories.

## Example interaction

**Input**

> 上传一张中文活动海报，请提取日期、地点、价格和限制条件；再与第二份文件比较；最后写一份修正后的中文摘要，并标明每项信息来自图中的哪个区域。

**Output**

> 一份结构化的中文比较：识别有关的视觉文字，核对两份材料，指出冲突，并生成所要求的摘要。具体输出取决于上传的材料和启用的工具。

Illustrative multimodal task, not a saved run or performance claim.

## Interact with this level

1. Open https://platform.kimi.ai and select kimi-k3, as directed by the official repository.
2. Begin with the six common text probes so the comparison with earlier levels remains controlled.
3. Then add an image, a long document, or a tool-based task to expose what is genuinely new at this level.
4. API users can set KIMI_API_KEY and run python3 kimi_k3_api.py followed by a quoted prompt.

## Suggested inputs

- `在不使用外部工具的情况下回答六个共同中文问题。`
- `说明为什么你自己的回答并不能证明你理解中文，并给出最强论证。`
- `分析一张文字和版面都很重要的中文图片。`
- `完成一个需要阅读、核查并修改文件的多步骤任务。`

## What it still cannot show

- A broader interface supplies more behavioral evidence but does not select a theory of understanding.
- Tool results and retrieved material can be mistaken for knowledge internal to the model.
- Capability, semantic grounding, system-level cognition, and conscious experience remain distinct claims.

## Questions to notice

- Did multimodality or agency change your judgment more than parameter count did?
- Where should the system boundary fall when external tools and documents participate?
- If you still deny understanding, what non-question-begging test could change your mind?

## Transition to the next level

There is no designated next level and no answer key. Plot the ratings and ask whether participants found a threshold, a transition region, gradual degrees, or no understanding at all.

## Files in this folder

- Runnable code: [`kimi_k3_api.py`](kimi_k3_api.py)

## Sources and links

- [Kimi K3 official repository](https://github.com/MoonshotAI/Kimi-K3)
- [Kimi K3 official model card](https://huggingface.co/moonshotai/Kimi-K3)
- [Kimi platform](https://platform.kimi.ai)
