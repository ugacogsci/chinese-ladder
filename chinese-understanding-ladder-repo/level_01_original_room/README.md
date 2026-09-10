# Level 1 Original finite state room

*Embodied deterministic finite state transducer*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

Four to nine people execute local state instructions over Chinese characters. The room recognizes a narrow question form and appends a canned classification answer.

## What this level adds

This establishes the baseline case: correct Chinese input and output can arise even when the people moving the symbols do not understand Chinese.

## How it works

A pointer moves over a character tape. State owners Q0 through Q9 compare shapes, move the pointer, write characters, and pass the tape to another state. The accepted vocabulary divides a few nouns into animals, fruits, and furniture.

## Example interaction

**Input**

> 猫是动物吗。

**Output**

> 是的猫是动物。

Reproduced from the activity handout.

## Interact with this level

1. Open original_activity.docx and print or distribute its state pages.
2. Give each participant one state, or have one person execute every state in sequence.
3. Place the pointer as shown and use one sample input at a time.
4. Do not translate, repair, or reinterpret any symbol while the machine is running.

## Suggested inputs

- `猫是动物吗。`
- `床是水果吗。`
- `杏是水果吗。`
- `灯 灯 灯。`

## What it still cannot show

- It accepts one rigid surface form and a very small vocabulary.
- Its categories and outputs are written directly into the rules.
- A valid Chinese variation can be rejected merely because its character layout differs.

## Questions to notice

- Could any participant infer the room's task from one local instruction?
- Would your judgment change if one person executed all states alone?
- Are you judging the operators, the complete rule system, or the room plus its designer?

## Transition to the next level

Level 2 keeps the same explicit-rule idea but adds registers, several question forms, role binding, a private event memory, and twenty distributed operators.

## Files in this folder

- Activity handout: [original_activity.docx](original_activity.docx)

## Sources and links

- [Searle Chinese Room paper](https://rintintin.colorado.edu/~vancecd/phil201/Searle.pdf)
