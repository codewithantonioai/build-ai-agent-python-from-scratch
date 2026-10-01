# Lesson 2 · Set up the project with uv

▶ [Watch this lesson](https://youtu.be/Wv-xnSiJM2g?t=179) (starts at 2:59)

## Goal

Lesson two. Set up the project with uv.

## Commands and files (as shown in the video)

### Terminal · term uv install

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
uv --version
```

### Terminal · term uv init

```bash
uv init agent
```

### Terminal · term hello

```bash
cat src/agent/__init__.py
uv run agent
```

### Terminal · term uv add

```bash
uv add openai
```

### Terminal · term env

```bash
cat .env.example
echo ".env" >> .gitignore
```

### `src/agent/__init__.py` · vscode first call

```python
from openai import OpenAI

client = OpenAI()


def main() -> None:
    response = client.responses.create(
        model="gpt-6-luna",
        input="What time is it right now?",
    )
    print(response.output_text)
```

### Terminal · term first call

```bash
uv run --env-file .env agent
```

## Recap

So: uv created, installed and ran the project. The key lives in dot env, and git ignores it. And GPT six Luna gave us its first answer, but it can't tell the time. In the next lesson, we give it its first tool.
