# Lesson 3 · Give the model its first tool

▶ [Watch this lesson](https://youtu.be/Wv-xnSiJM2g?t=413) (starts at 6:53)

## Goal

Lesson three. Give the model its first tool.

## Commands and files (as shown in the video)

### `src/agent/__init__.py` · vscode tool

```python
from datetime import datetime

from openai import OpenAI

client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_current_time",
        "description": "Get the current local date and time.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        "strict": True,
    },
]


def get_current_time():
    return datetime.now().strftime("%A %d %B %Y, %H:%M")
```

### `src/agent/__init__.py` · vscode two requests

```python
from datetime import datetime

from openai import OpenAI

client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_current_time",
        "description": "Get the current local date and time.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        "strict": True,
    },
]


def get_current_time():
    return datetime.now().strftime("%A %d %B %Y, %H:%M")


def main() -> None:
    messages = [{"role": "user", "content": "What time is it right now?"}]

    response = client.responses.create(model="gpt-6-luna", tools=tools, input=messages)
    messages += response.output

    for item in response.output:
        if item.type == "function_call":
            print("Tool call:", item.name, item.arguments)
            messages.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": get_current_time(),
            })

    response = client.responses.create(model="gpt-6-luna", tools=tools, input=messages)
    print(response.output_text)
```

### Terminal · term real time

```bash
uv run --env-file .env agent
```

## Recap

So: a tool is a schema for the model plus a function in your code. The model asks, and your code runs it. And the call ID ties each result to its request. But we only handled one round trip. Next, we turn it into a loop.
