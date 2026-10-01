from openai import OpenAI

client = OpenAI()


def main() -> None:
    response = client.responses.create(
        model="gpt-6-luna",
        input="What time is it right now?",
    )
    print(response.output_text)
