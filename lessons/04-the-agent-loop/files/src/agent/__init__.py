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
