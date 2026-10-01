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
