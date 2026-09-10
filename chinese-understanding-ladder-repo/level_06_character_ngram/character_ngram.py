#!/usr/bin/env python3
"""A tiny character-level statistical language model.

It learns which Chinese characters tend to follow the previous three characters
in the included corpus. It can produce new sequences, but it has no word model,
facts database, parser, or instruction-following objective.
"""

from __future__ import annotations

import argparse
import random
import re
from collections import Counter, defaultdict


CORPUS = """
昨天，小林把蓝色的地图借给了阿明。阿明说，他今天会仔细看地图。
上周，阿明把绿色的地图还给了小林。小林把地图放进了书包。
今天，小王把黄色的地图送给了小林。小林向小王表示感谢。
美玲把红色的雨伞借给了小林，因为外面正在下雨。
小王先把杯子借给阿明，后来阿明把杯子还给美玲，所以杯子最后在美玲那里。
理解通常涉及把握意义、关系和原因。模仿则强调做出相似的行为或形式。
一个系统可以按照规则移动符号，也可以根据例子学习符号之间的统计关系。
如果输出稳定、流畅而且符合语境，人们可能会觉得这个系统理解了语言。
但是，外在表现是否足以证明理解，正是中文房间思想实验提出的问题。
语言模型根据已有文字预测接下来较可能出现的文字。
统计规律能产生新的句子，却不保证句子真实、合理或者被系统理解。
"""

ORDER = 3
START = "^" * ORDER
STOP = "$"


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text)


def train(text: str) -> dict[str, Counter[str]]:
    table: dict[str, Counter[str]] = defaultdict(Counter)
    for sentence in re.split(r"(?<=[。！？])", normalize(text)):
        if not sentence:
            continue
        padded = START + sentence + STOP
        for index in range(ORDER, len(padded)):
            context = padded[index - ORDER:index]
            table[context][padded[index]] += 1
    return table


MODEL = train(CORPUS)


def choose(counter: Counter[str], rng: random.Random) -> str:
    symbols = list(counter)
    weights = [counter[symbol] for symbol in symbols]
    return rng.choices(symbols, weights=weights, k=1)[0]


def complete(prompt: str, length: int = 80, seed: int = 7) -> str:
    rng = random.Random(seed)
    clean = normalize(prompt)
    generated = clean
    context = (START + clean)[-ORDER:]
    for _ in range(length):
        options = MODEL.get(context)
        if not options:
            # Back off by restarting a sentence, rather than consulting meaning.
            context = START
            options = MODEL[context]
        symbol = choose(options, rng)
        if symbol == STOP:
            break
        generated += symbol
        context = (context + symbol)[-ORDER:]
    return generated


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="*", help="Chinese prefix to continue")
    parser.add_argument("--length", type=int, default=80)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--show-model", action="store_true")
    args = parser.parse_args()
    prompt = "".join(args.prompt) if args.prompt else input("> ")
    print(complete(prompt, args.length, args.seed))
    if args.show_model:
        transitions = sum(len(options) for options in MODEL.values())
        print(f"[order={ORDER}; contexts={len(MODEL)}; transitions={transitions}]")


if __name__ == "__main__":
    main()
