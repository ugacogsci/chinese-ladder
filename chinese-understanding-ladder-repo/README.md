# Chinese Understanding Ladder

This repository turns Searle's Chinese Room into a twelve-level continuum of Chinese input and output systems. It begins with people manually executing a tiny finite-state program and ends with Kimi K3, a frontier multimodal and tool-using model.

The recurring question is:

> **At which point, if any, would you attribute some understanding of Chinese to the system?**

The repository does not treat the final model as an answer key. Each level adds a mechanism or capability in a small enough step to make threshold judgments difficult. A later system can also fail a task that an earlier specialized system handles. The levels are therefore a guided sequence for examining intuitions, not a one-dimensional scientific scale of understanding or consciousness.

## How to use the repository

1. Open each level folder in order.
2. Read the DOCX guide or its matching Markdown page.
3. Try the supplied activity, code, model link, or hosted interface.
4. Give the system one or more common prompts.
5. Rate the claim that the system understands Chinese from 0 to 100 before and after learning how it works.
6. Record what feature changed the rating and where the relevant system boundary lies.

## Levels

| Level | System | Main addition |
|---:|---|---|
| 1 | [Original finite state room](level_01_original_room/README.md) | This establishes the baseline case: correct Chinese input and output can arise even when the people moving the symbols do not understand Chinese. |
| 2 | [Twenty person macro machine](level_02_twenty_person_room/README.md) | The baseline gains more states, explicit memory, private tables, multiple syntactic modes, more vocabulary, and output assembled from copied input roles. |
| 3 | [Deterministic symbolic engine](level_03_symbolic_engine/README.md) | The people and paper packet become executable software. The program also composes a result from two stated transfers rather than consulting only one stored event. |
| 4 | [Approximate retrieval bot](level_04_retrieval_bot/README.md) | Matching becomes graded rather than all or nothing. Unseen wording can succeed when its characters and short character sequences resemble a stored question. |
| 5 | [Tiny neural intent classifier](level_05_tiny_neural_classifier/README.md) | Some input-output organization now comes from training examples and learned weights rather than a programmer writing every classification branch. |
| 6 | [Character n gram generator](level_06_character_ngram/README.md) | A finite-order markov chain. The system produces response text from learned sequence statistics rather than choosing a hand-written answer. It can splice familiar fragments into a sentence absent from the corpus. |
| 7 | [UER Chinese GPT 2](level_07_uer_chinese_gpt2/README.md) | Learned attention replaces a fixed three-character context. Many layers build context-sensitive internal vectors, and a much larger corpus supplies broader syntax and vocabulary. |
| 8 | [Qwen2 5 0 5B Instruct](level_08_qwen25_05b_instruct/README.md) | The system is now trained to treat a user message as something to answer. It can translate, compare concepts, and follow formatting requests without a hand-written intent menu. |
| 9 | [Qwen3 4B Instruct](level_09_qwen3_4b_instruct/README.md) | The mechanism does not change dramatically. The model can preserve and transform more context, represent more patterns, and usually handle more involved instructions. |
| 10 | [Qwen3 30B A3B Instruct](level_10_qwen3_30b_a3b/README.md) | Specialization and routing become explicit parts of the neural architecture. Total learned capacity grows much faster than the computation used for a single token. |
| 11 | [Qwen3 235B A22B Instruct](level_11_qwen3_235b_a22b/README.md) | The organization remains recognizable while breadth, stored statistical structure, and task performance increase. The level exists to prevent frontier behavior from appearing as one unexplained jump. |
| 12 | [Kimi K3](level_12_kimi_k3/README.md) | The final level combines frontier-scale sparse computation with perception-like inputs, very long working context, tool calls, and sustained multi-step action. |

## Common prompts

Use the same prompts whenever a level accepts them. Failure is useful evidence rather than a reason to replace the prompt.

1. `昨天，小林把蓝色的地图借给了阿明吗？`
2. `昨天小林是不是把蓝色地图借给阿明了？`
3. `上周，谁把绿色的地图还给了小林？`
4. `如果小王把杯子借给阿明，后来阿明把杯子还给美玲，杯子最后在谁那里？`
5. `请把“理解”翻译成英文，并解释这个词和“模仿”有什么区别。`
6. `为什么一个只按照规则移动符号的系统可能看起来像是在理解中文？`

The first two test paraphrase invariance. The third tests role binding. The fourth tests multi-step state. The fifth combines translation and conceptual comparison. The sixth asks for an open explanation about the sequence itself.

## Interpretive cautions

- Behavioral range, implementation complexity, parameter count, grounding, and conscious experience are different variables.
- Reveal output before architecture if you want to measure the effect of implementation knowledge.
- Distinguish understanding attributed to a component from understanding attributed to an organized system.
- Disclose sampling, retries, edited transcripts, external retrieval, and tool results.
- Examples for Levels 7 through 12 are clearly labeled illustrative where no saved run was performed. They are prompts and output forms, not benchmark claims.

## Repository contents

Every level folder contains a DOCX guide and a Markdown equivalent. Levels 1 and 2 also include printable activity handouts. Levels 3 through 6 contain transparent teaching programs. Levels 7 through 11 include simple model runners and official model links. Level 12 links to the Kimi platform and includes a minimal API client.

Python environments, model weights, and API keys are intentionally excluded from version control. Large checkpoints require suitable hardware or a hosted provider.

## Sources

Model specifications were checked against official sources on 10 September 2026:

- [UER Chinese GPT 2](https://huggingface.co/uer/gpt2-chinese-cluecorpussmall)
- [Qwen2 5 0 5B Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)
- [Qwen3 4B Instruct](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)
- [Qwen3 30B A3B Instruct](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)
- [Qwen3 235B A22B Instruct](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)
- [Qwen3 repository](https://github.com/QwenLM/Qwen3)
- [Kimi K3 repository](https://github.com/MoonshotAI/Kimi-K3)
- [Kimi K3 model card](https://huggingface.co/moonshotai/Kimi-K3)

## License

No license has been selected. Choose one before inviting reuse or contributions; publishing a repository without a license does not grant general permission to copy or modify its contents.
