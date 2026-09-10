# Level 2 Twenty person macro machine

*Distributed symbolic machine with registers and lookup tables*

## Main question

**At which point, if any, would you attribute some understanding of Chinese to the system?**

## What this level is

Twenty participants parse structured Chinese questions, store six roles, consult a distributed event record, and construct yes or no and who answers.

## What this level adds

The baseline gains more states, explicit memory, private tables, multiple syntactic modes, more vocabulary, and output assembled from copied input roles.

## How it works

States Q0 through Q11 parse the input into time, actor, color, object, action, and recipient registers. Q12 routes to one of three private event tables. Q16 selects success or failure, and Q17 through Q19 write the answer or a format error.

## Example interaction

**Input**

> 昨天，小林把蓝色的地图借给了阿明吗？

**Output**

> 是的，昨天，小林把蓝色的地图借给了阿明。

Deterministic answer encoded by the supplied event table.

## Interact with this level

1. Open twenty_person_activity.docx and read the facilitator overview.
2. Give one private state card to each of twenty participants and keep the answer key hidden.
3. Prepare a fresh machine packet and one supplied input strip for each run.
4. Follow the route log without conversational repair or semantic hints.

## Suggested inputs

- `昨天，小林把蓝色的地图借给了阿明吗？`
- `上周，谁把绿色的地图还给了小林？`
- `今天，小王把黄色的地图送给了谁？`
- `昨天，小林把蓝色地图借给了阿明吗？`

## What it still cannot show

- Word boundaries, grammatical slots, and the event schema are supplied in advance.
- The room cannot generalize beyond its finite vocabulary and templates.
- A natural omission of the particle de is deliberately rejected by the formal grammar.

## Questions to notice

- Does distributed memory change anything philosophically, or only practically?
- Does the whole room know more than any operator?
- How much competence belongs to the designer's choice of representation?

## Transition to the next level

Level 3 implements a related symbolic system as ordinary software and adds an explicit paraphrase rule plus a two-transfer state calculation.

## Files in this folder

- Activity handout: [twenty_person_activity.docx](twenty_person_activity.docx)

## Sources and links

- [Searle Chinese Room paper](https://rintintin.colorado.edu/~vancecd/phil201/Searle.pdf)
