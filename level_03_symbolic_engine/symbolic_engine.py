#!/usr/bin/env python3
"""A deterministic Chinese question-answering engine.

Every accepted form, vocabulary item, database row, and reasoning rule is visible
in this file. It adds compositional parsing, paraphrase rules, and a tiny amount
of multi-step state tracking to the twenty-person room.
"""

from __future__ import annotations

import argparse
import re


PEOPLE = "小林|小王|阿明|美玲"
TIMES = "上周|昨天|今天"
COLORS = "红色|蓝色|绿色|黄色"
OBJECTS = "书包|雨伞|杯子|地图"
VERBS = "送给|借给|还给"

EVENTS = {
    ("上周", "小林", "红色", "书包", "送给", "小王"),
    ("上周", "小王", "蓝色", "雨伞", "借给", "美玲"),
    ("上周", "阿明", "绿色", "地图", "还给", "小林"),
    ("上周", "美玲", "黄色", "杯子", "送给", "阿明"),
    ("昨天", "小林", "蓝色", "地图", "借给", "阿明"),
    ("昨天", "小王", "绿色", "杯子", "还给", "美玲"),
    ("昨天", "阿明", "黄色", "书包", "送给", "小王"),
    ("昨天", "美玲", "红色", "雨伞", "借给", "小林"),
    ("今天", "小林", "绿色", "雨伞", "还给", "美玲"),
    ("今天", "小王", "黄色", "地图", "送给", "小林"),
    ("今天", "阿明", "红色", "杯子", "借给", "美玲"),
    ("今天", "美玲", "蓝色", "书包", "还给", "阿明"),
}

YES_NO = re.compile(
    rf"^(?P<time>{TIMES})[，,]?(?P<actor>{PEOPLE})"
    rf"(?:是不是)?把(?P<color>{COLORS})的?(?P<object>{OBJECTS})"
    rf"(?P<verb>{VERBS})了?(?P<recipient>{PEOPLE})(?:吗|了)?[？?]?$"
)
WH_ACTOR = re.compile(
    rf"^(?P<time>{TIMES})[，,]?谁把(?P<color>{COLORS})的?(?P<object>{OBJECTS})"
    rf"(?P<verb>{VERBS})了?(?P<recipient>{PEOPLE})[？?]?$"
)
WH_RECIPIENT = re.compile(
    rf"^(?P<time>{TIMES})[，,]?(?P<actor>{PEOPLE})把(?P<color>{COLORS})的?"
    rf"(?P<object>{OBJECTS})(?P<verb>{VERBS})了?谁[？?]?$"
)
CHAIN = re.compile(
    rf"^如果(?P<a>{PEOPLE})把(?P<object>{OBJECTS})借给(?P<b>{PEOPLE})[，,]"
    rf"后来(?P=b)把(?P=object)还给(?P<c>{PEOPLE})[，,](?P=object)最后在谁那里[？?]?$"
)


def event_sentence(event: tuple[str, ...]) -> str:
    time, actor, color, obj, verb, recipient = event
    return f"{time}，{actor}把{color}的{obj}{verb}了{recipient}。"


def answer(text: str, trace: bool = False) -> str:
    text = re.sub(r"\s+", "", text.strip())
    steps: list[str] = []

    if match := CHAIN.fullmatch(text):
        steps.extend(["matched CHAIN rule", f"owner after first transfer = {match['b']}",
                      f"owner after second transfer = {match['c']}"])
        result = f"{match['object']}最后在{match['c']}那里。"
    elif match := WH_ACTOR.fullmatch(text):
        steps.append("matched WH_ACTOR rule")
        key = (match["time"], match["color"], match["object"], match["verb"], match["recipient"])
        hits = [e for e in EVENTS if (e[0], e[2], e[3], e[4], e[5]) == key]
        result = event_sentence(hits[0]) if len(hits) == 1 else "记录中没有唯一答案。"
    elif match := WH_RECIPIENT.fullmatch(text):
        steps.append("matched WH_RECIPIENT rule")
        key = (match["time"], match["actor"], match["color"], match["object"], match["verb"])
        hits = [e for e in EVENTS if e[:5] == key]
        result = event_sentence(hits[0]) if len(hits) == 1 else "记录中没有唯一答案。"
    elif match := YES_NO.fullmatch(text):
        steps.append("matched YES_NO or paraphrase rule")
        event = tuple(match[name] for name in ("time", "actor", "color", "object", "verb", "recipient"))
        result = "是的，" + event_sentence(event).replace("，", "", 1) if event in EVENTS else "不是。记录中没有这件事。"
    else:
        steps.append("no grammar rule matched")
        result = "输入超出这个程序的规则范围。"

    if trace:
        return "\n".join(f"TRACE {step}" for step in steps) + "\n" + result
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="*")
    parser.add_argument("--trace", action="store_true")
    args = parser.parse_args()
    if args.text:
        print(answer("".join(args.text), args.trace))
        return
    print("Level 3 symbolic engine. Enter Chinese; Ctrl-D exits.")
    try:
        while True:
            print(answer(input("> "), args.trace))
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == "__main__":
    main()

