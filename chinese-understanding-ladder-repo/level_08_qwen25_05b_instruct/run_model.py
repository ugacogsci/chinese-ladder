#!/usr/bin/env python3
"""Run Qwen/Qwen2.5-0.5B-Instruct with Hugging Face Transformers."""

from __future__ import annotations

import argparse


MODEL_ID = 'Qwen/Qwen2.5-0.5B-Instruct'
BASE_MODEL = False
LARGE_MODEL = False
MODEL_CARD = "https://huggingface.co/" + MODEL_ID


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")
    parser.add_argument("--max-new-tokens", type=int, default=160)
    parser.add_argument("--allow-large-download", action="store_true")
    args = parser.parse_args()

    if LARGE_MODEL and not args.allow_large_download:
        raise SystemExit(
            "This checkpoint is intentionally not downloaded without an explicit acknowledgement.\n"
            f"Use a hosted provider from {MODEL_CARD}, or rerun with --allow-large-download."
        )

    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID, device_map="auto", torch_dtype="auto"
    )
    if BASE_MODEL:
        inputs = tokenizer(args.prompt, return_tensors="pt").to(model.device)
    else:
        inputs = tokenizer.apply_chat_template(
            [{"role": "user", "content": args.prompt}],
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(model.device)
    output = model.generate(
        **inputs,
        max_new_tokens=args.max_new_tokens,
        do_sample=True,
        temperature=0.7,
    )
    continuation = output[0][inputs["input_ids"].shape[-1]:]
    print(tokenizer.decode(continuation, skip_special_tokens=True))


if __name__ == "__main__":
    main()
