#!/usr/bin/env python3
"""A character n-gram TF-IDF retrieval bot written with the standard library.

The response is not derived from logical rules. The program measures similarity
to stored examples and returns the answer paired with the nearest example.
"""

from __future__ import annotations

import argparse
import math
import re
from collections import Counter


EXAMPLES = [
    ("你好", "你好！很高兴见到你。"),
    ("你是谁", "我是一个按相似度检索答案的程序。"),
    ("昨天小林把蓝色的地图借给了阿明吗", "是的，昨天小林把蓝色的地图借给了阿明。"),
    ("昨天小林是不是把蓝色地图借给阿明了", "是的，昨天小林把蓝色的地图借给了阿明。"),
    ("上周谁把绿色的地图还给了小林", "上周，阿明把绿色的地图还给了小林。"),
    ("今天小王把黄色地图送给谁了", "今天，小王把黄色的地图送给了小林。"),
    ("理解是什么意思", "“理解”通常指把握某件事的意义、关系或原因。"),
    ("模仿是什么意思", "“模仿”是按照已有行为或形式做出相似表现。"),
    ("理解和模仿有什么区别", "模仿强调表现相似；理解还涉及意义、关系或理由。"),
    ("把理解翻译成英文", "“理解”常译为 understanding 或 comprehend。"),
    ("为什么天空是蓝色的", "阳光在大气中散射时，较短的蓝光更容易进入我们的视线。"),
    ("为什么规则系统看起来像懂中文", "稳定的规则、记忆和输出结构可以产生与理解相似的外在行为。"),
    ("如果小林把书给小王后来小王把书给美玲书在谁那里", "书最后在美玲那里。"),
    ("如果阿明把杯子借给小林后来小林把杯子还给小王杯子在谁那里", "杯子最后在小王那里。"),
]


def normalize(text: str) -> str:
    return re.sub(r"[\s，。！？、,.!?“”\"']+", "", text.lower())


def features(text: str) -> Counter[str]:
    text = normalize(text)
    feats = Counter(text)
    feats.update(text[i:i + 2] for i in range(len(text) - 1))
    return feats


DOCS = [features(q) for q, _ in EXAMPLES]
DF = Counter(term for doc in DOCS for term in doc)
N = len(DOCS)


def vector(doc: Counter[str]) -> dict[str, float]:
    return {term: (1 + math.log(count)) * (math.log((N + 1) / (DF[term] + 1)) + 1)
            for term, count in doc.items()}


VECTORS = [vector(doc) for doc in DOCS]


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    dot = sum(value * b.get(term, 0.0) for term, value in a.items())
    na = math.sqrt(sum(value * value for value in a.values()))
    nb = math.sqrt(sum(value * value for value in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def answer(text: str, threshold: float = 0.22) -> tuple[str, float, str]:
    query = vector(features(text))
    scored = [(cosine(query, vec), index) for index, vec in enumerate(VECTORS)]
    score, index = max(scored)
    matched, response = EXAMPLES[index]
    if score < threshold:
        response = "没有找到足够相似的例子。"
    return response, score, matched


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="*")
    parser.add_argument("--show-match", action="store_true")
    args = parser.parse_args()
    prompts = ["".join(args.text)] if args.text else iter(lambda: input("> "), "")
    try:
        for prompt in prompts:
            response, score, matched = answer(prompt)
            print(response)
            if args.show_match:
                print(f"[nearest={matched!r}; cosine={score:.3f}]")
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == "__main__":
    main()

