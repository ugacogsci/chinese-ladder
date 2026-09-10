#!/usr/bin/env python3
"""Minimal Kimi K3 client using Moonshot's OpenAI-compatible API.

Set KIMI_API_KEY in the environment. This file does not contain or print the key.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.request


ENDPOINT = "https://api.moonshot.ai/v1/chat/completions"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")
    parser.add_argument("--reasoning-effort", choices=("low", "high", "max"), default="max")
    args = parser.parse_args()
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        raise SystemExit("Set KIMI_API_KEY before running this demo.")

    payload = json.dumps({
        "model": "kimi-k3",
        "messages": [{"role": "user", "content": args.prompt}],
        "reasoning_effort": args.reasoning_effort,
    }, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        result = json.load(response)
    message = result["choices"][0]["message"]
    if message.get("reasoning_content"):
        print("[reasoning content returned but hidden in this presentation demo]")
    print(message.get("content", ""))


if __name__ == "__main__":
    main()
