# Lesson 4 · The agent loop

▶ [Watch this lesson](https://youtu.be/Wv-xnSiJM2g?t=581) (starts at 9:41)

## Goal

Lesson four. The agent loop.

## Commands and files (as shown in the video)

### `src/agent/tools.py` · vscode tools py

```python
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("workspace").resolve()


def get_current_time():
    return datetime.now().strftime("%A %d %B %Y, %H:%M")


def list_files():
    return "\n".join(path.name for path in sorted(WORKSPACE.iterdir()))


def read_file(filename):
    return (WORKSPACE / filename).read_text()


FUNCTIONS = {
    "get_current_time": get_current_time,
    "list_files": list_files,
    "read_file": read_file,
}


def run_tool(name, args):
    return str(FUNCTIONS[name](**args))


def tool(name, description, **params):
    return {
        "type": "function",
        "name": name,
        "description": description,
        "parameters": {
            "type": "object",
            "properties": {
                key: {"type": "string", "description": text}
                for key, text in params.items()
            },
            "required": list(params),
            "additionalProperties": False,
        },
        "strict": True,
    }


TOOLS = [
    tool("get_current_time", "Get the current local date and time."),
    tool("list_files", "List the files in the notes workspace."),
    tool("read_file", "Read a file from the workspace.", filename="A file name, like week.md"),
]
```

### `src/agent/__init__.py` · vscode run agent

```python
import json

from openai import OpenAI

from agent.tools import TOOLS, run_tool

client = OpenAI()
MODEL = "gpt-6-luna"


def run_agent(messages):
    while True:
        response = client.responses.create(model=MODEL, tools=TOOLS, input=messages)
        messages += response.output
        calls = [item for item in response.output if item.type == "function_call"]
        if not calls:
            return response.output_text
        for call in calls:
            args = json.loads(call.arguments)
            print(f"  -> {call.name}({args})")
            messages.append({
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": run_tool(call.name, args),
            })


def main() -> None:
    messages = [{"role": "user", "content": "When is my dentist appointment?"}]
    print(run_agent(messages))
```

### Terminal · term dentist

```bash
ls workspace
uv run --env-file .env agent
```

## Recap

So: the agent loops until the model stops asking for tools. The tools live in their own file, with a dictionary to find them. And the model picks the steps; we only run them. But ask it a second question, and it has forgotten the first. Let's give it memory.
