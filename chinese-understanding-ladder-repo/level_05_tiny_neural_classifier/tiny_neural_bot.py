#!/usr/bin/env python3
"""A tiny neural intent classifier with transparent, human-written responses.

The network learns its input-to-intent weights from examples at startup. It is
genuinely learned, but it is not a language model: response text and a small
amount of slot handling remain explicit. NumPy is the only dependency.
"""

from __future__ import annotations

import argparse
import hashlib
import re

import numpy as np


TRAINING = {
    "greeting": ["你好", "您好", "嗨", "早上好", "晚上好", "很高兴见到你"],
    "identity": ["你是谁", "你是什么", "介绍一下自己", "你是机器人吗", "你叫什么"],
    "event": ["昨天小林把地图借给阿明了吗", "谁把地图还给小林", "小王把杯子送给谁", "这件事在记录里吗", "查一下昨天的事情"],
    "chain": [
        "最后在谁那里",
        "后来谁拿着杯子",
        "经过两次转交东西归谁",
        "先借给他后来还给她最后是谁的",
        "最后一个收到的人是谁",
        "如果小王把杯子借给阿明后来阿明把杯子还给美玲杯子最后在谁那里",
        "小林先把地图给阿明后来阿明给小王地图最后在谁那里",
        "经过阿明和美玲两次转交杯子最后归谁",
    ],
    "translation": ["翻译成英文", "理解用英语怎么说", "这个词英文是什么", "把这句话翻译一下", "中译英"],
    "explanation": ["为什么", "请解释", "有什么区别", "原因是什么", "这说明了什么", "为什么看起来像理解"],
}

RESPONSES = {
    "greeting": "你好！",
    "identity": "我是一个很小的神经分类器；我先预测问题类型，再选择人工写好的回答。",
    "event": "我把它判断为事件查询，但这个微型模型没有完整的事件数据库。",
    "chain": "我把它判断为多步归属问题；下面的名字提取器会尝试给出最后接收者。",
    "translation": "“理解”常译为 understanding；“模仿”常译为 imitation。",
    "explanation": "规则、训练数据和内部状态都能改善行为；更像理解的表现并不能单独决定是否真的理解。",
}

LABELS = sorted(TRAINING)
DIM = 192
HIDDEN = 20
RNG = np.random.default_rng(7)


def hashed_features(text: str) -> np.ndarray:
    text = re.sub(r"\s+", "", text)
    units = list(text) + [text[i:i + 2] for i in range(len(text) - 1)]
    vector = np.zeros(DIM, dtype=np.float64)
    for unit in units:
        # Unlike Python's built-in hash(), this mapping is stable across runs.
        bucket = int.from_bytes(
            hashlib.blake2b(unit.encode("utf-8"), digest_size=4).digest(), "big"
        ) % DIM
        vector[bucket] += 1.0
    norm = np.linalg.norm(vector)
    return vector / norm if norm else vector


X = np.stack([hashed_features(text) for label in LABELS for text in TRAINING[label]])
Y_INDEX = np.array([index for index, label in enumerate(LABELS) for _ in TRAINING[label]])
Y = np.eye(len(LABELS))[Y_INDEX]

W1 = RNG.normal(0, 0.12, (DIM, HIDDEN))
B1 = np.zeros(HIDDEN)
W2 = RNG.normal(0, 0.12, (HIDDEN, len(LABELS)))
B2 = np.zeros(len(LABELS))


def softmax(values: np.ndarray) -> np.ndarray:
    shifted = values - values.max(axis=1, keepdims=True)
    exp = np.exp(shifted)
    return exp / exp.sum(axis=1, keepdims=True)


def train(epochs: int = 700, rate: float = 0.22) -> None:
    global W1, B1, W2, B2
    for _ in range(epochs):
        hidden = np.tanh(X @ W1 + B1)
        probabilities = softmax(hidden @ W2 + B2)
        delta2 = (probabilities - Y) / len(X)
        grad_w2 = hidden.T @ delta2
        grad_b2 = delta2.sum(axis=0)
        delta1 = (delta2 @ W2.T) * (1 - hidden * hidden)
        grad_w1 = X.T @ delta1
        grad_b1 = delta1.sum(axis=0)
        W1 -= rate * grad_w1
        B1 -= rate * grad_b1
        W2 -= rate * grad_w2
        B2 -= rate * grad_b2


def classify(text: str) -> tuple[str, float]:
    x = hashed_features(text)[None, :]
    probabilities = softmax(np.tanh(x @ W1 + B1) @ W2 + B2)[0]
    index = int(np.argmax(probabilities))
    return LABELS[index], float(probabilities[index])


def answer(text: str) -> tuple[str, str, float]:
    label, confidence = classify(text)
    response = RESPONSES[label]
    if label == "chain":
        names = re.findall(r"小林|小王|阿明|美玲", text)
        if names:
            response += f" 按最后出现的接收者猜测：{names[-1]}。"
    return response, label, confidence


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="*")
    parser.add_argument("--show-class", action="store_true")
    args = parser.parse_args()
    train()
    prompts = ["".join(args.text)] if args.text else iter(lambda: input("> "), "")
    try:
        for prompt in prompts:
            response, label, confidence = answer(prompt)
            print(response)
            if args.show_class:
                print(f"[intent={label}; confidence={confidence:.3f}; learned parameters={W1.size + B1.size + W2.size + B2.size}]")
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == "__main__":
    main()
