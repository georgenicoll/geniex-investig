# geniex-investig

A small scratch project for trying out [`geniex`](https://pypi.org/project/geniex/), used to explore running LLMs locally via Qualcomm's QAIRT runtime (NPU-accelerated inference) using models from the AI Hub model zoo.

## What's here

- **`src/geniex_investig/main.py`** — an interactive CLI chat loop. Loads a causal LM (`ai-hub-models/Gemma-4-E4B-it`) with `device_map="qairt"`, then repeatedly prompts for input, applies the model's chat template, and streams the generated response token-by-token until you type `/q`.
- **`src/geniex_investig/verify.py`** — a minimal smoke test that imports `geniex` and prints its version, to confirm the install/environment is working.

## Requirements

- Python >= 3.10
- [`uv`](https://docs.astral.sh/uv/) for dependency management

## Setup

```bash
uv sync
```

## Usage

Verify the `geniex` install:

```bash
uv run python src/geniex_investig/verify.py
```

Run the interactive chat:

```bash
uv run geniex_investig
```

or directly:

```bash
uv run python src/geniex_investig/main.py
```
