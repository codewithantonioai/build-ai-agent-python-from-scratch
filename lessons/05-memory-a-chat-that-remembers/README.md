# Lesson 5 · Memory: a chat that remembers

▶ [Watch this lesson](https://youtu.be/Wv-xnSiJM2g?t=718) (starts at 11:58)

## Goal

Lesson five. Memory: a chat that remembers.

## Commands and files (as shown in the video)

### `src/agent/__init__.py` · vscode repl

```python
import json

from openai import OpenAI

from agent.tools import TOOLS, run_tool

client = OpenAI()
MODEL = "gpt-6-luna"
INSTRUCTIONS = (
    "You are a helpful assistant for the user's notes. "
    "Use the tools to read files in the workspace. "
    "Never invent what a file says: read it first."
)


def run_agent(messages):
    while True:
        response = client.responses.create(
            model=MODEL,
            instructions=INSTRUCTIONS,
            tools=TOOLS,
            input=messages,
        )
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
    print("Agent ready. Type 'exit' to quit.")
    while True:
        messages = []
        user = input("\nYou: ")
        if user.strip().lower() in ("exit", "quit"):
            break
        messages.append({"role": "user", "content": user})
        print("\nAgent:", run_agent(messages))
```

### Terminal · term forgets

```bash
# You: Hi! My name is Antonio.
# You: What's my name?
```

### `src/agent/__init__.py` · vscode one line

```python
import json

from openai import OpenAI

from agent.tools import TOOLS, run_tool

client = OpenAI()
MODEL = "gpt-6-luna"
INSTRUCTIONS = (
    "You are a helpful assistant for the user's notes. "
    "Use the tools to read files in the workspace. "
    "Never invent what a file says: read it first."
)


def run_agent(messages):
    while True:
        response = client.responses.create(
            model=MODEL,
            instructions=INSTRUCTIONS,
            tools=TOOLS,
            input=messages,
        )
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
    messages = []
    print("Agent ready. Type 'exit' to quit.")
    while True:
        user = input("\nYou: ")
        if user.strip().lower() in ("exit", "quit"):
            break
        messages.append({"role": "user", "content": user})
        print("\nAgent:", run_agent(messages))
```

### Terminal · term remembers

```bash
# You: Hi! My name is Antonio.
# You: What's my name?
```

### Terminal · term groceries

```bash
# You: What's on my grocery list?
```

## Recap

So: every request is stateless. The memory is simply the list of messages we send again. And instructions ride along with every call. So far our agent can only read. Next, we let it write, carefully.
