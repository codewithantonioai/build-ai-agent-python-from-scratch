# Lesson 7 · Knowing when to stop

▶ [Watch this lesson](https://youtu.be/Wv-xnSiJM2g?t=1038) (starts at 17:18)

## Goal

Lesson seven. Knowing when to stop.

## Commands and files (as shown in the video)

### `src/agent/__init__.py` · vscode max steps

```python
import json

from openai import OpenAI

from agent.tools import TOOLS, run_tool

client = OpenAI()
MODEL = "gpt-6-luna"
MAX_STEPS = 10
INSTRUCTIONS = (
    "You are a helpful assistant for the user's notes. "
    "Use the tools to read and write files in the workspace. "
    "Never invent what a file says: read it first."
)


def run_agent(messages):
    tokens = 0
    for step in range(1, MAX_STEPS + 1):
        response = client.responses.create(
            model=MODEL,
            instructions=INSTRUCTIONS,
            tools=TOOLS,
            input=messages,
        )
        messages += response.output
        tokens += response.usage.total_tokens
        calls = [item for item in response.output if item.type == "function_call"]
        if not calls:
            print(f"  ({step} steps, {tokens} tokens)")
            return response.output_text
        for call in calls:
            args = json.loads(call.arguments)
            print(f"  -> {call.name}({args})")
            messages.append({
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": run_tool(call.name, args),
            })
    return "I stopped: too many steps."


def main() -> None:
    messages = []
    print("Agent ready. Type 'exit' to quit.")
    while True:
        user = input("\nYou: ")
        if user.strip().lower() in ("exit", "quit"):
            break
        messages.append({"role": "user", "content": user})
        print("\nAgent:", run_agent(messages))
```

### Terminal · term final demo

```bash
# You: What day is it? Make me a to-do list for the rest of the week from my notes and save it as todo.md
```

### Terminal · term todo

```bash
cat workspace/todo.md
```

### Terminal · term limit

```bash
# You: Summarize every note in my workspace.
```

## Recap

So: always put a cap on the steps. Several tool calls in one response just work with our loop. And tokens are what you pay for, so measure them.
