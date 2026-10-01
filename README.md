# Build Your First AI Agent from Scratch in Python (No Frameworks)

Companion repository for the **Code with Antonio** video course · [Watch on YouTube](https://youtu.be/Wv-xnSiJM2g).

Build Your First AI Agent from Scratch in Python, with no frameworks: tools, the agent loop, memory, human approval and step limits.

## What you'll build

A notes agent for your terminal: it tells the time, lists, reads and writes the files in a workspace folder, remembers the conversation, asks before it saves anything and knows when to stop.

## Lessons

| # | Lesson | Video | Folder |
|---|---|---|---|
| 1 | What is an AI agent, really? | [0:00](https://youtu.be/Wv-xnSiJM2g?t=0) | [lessons/01-what-is-an-ai-agent-really](lessons/01-what-is-an-ai-agent-really) |
| 2 | Set up the project with uv | [2:59](https://youtu.be/Wv-xnSiJM2g?t=179) | [lessons/02-set-up-the-project-with-uv](lessons/02-set-up-the-project-with-uv) |
| 3 | Give the model its first tool | [6:53](https://youtu.be/Wv-xnSiJM2g?t=413) | [lessons/03-give-the-model-its-first-tool](lessons/03-give-the-model-its-first-tool) |
| 4 | The agent loop | [9:41](https://youtu.be/Wv-xnSiJM2g?t=581) | [lessons/04-the-agent-loop](lessons/04-the-agent-loop) |
| 5 | Memory: a chat that remembers | [11:58](https://youtu.be/Wv-xnSiJM2g?t=718) | [lessons/05-memory-a-chat-that-remembers](lessons/05-memory-a-chat-that-remembers) |
| 6 | Tools that act — safely | [14:28](https://youtu.be/Wv-xnSiJM2g?t=868) | [lessons/06-tools-that-act-safely](lessons/06-tools-that-act-safely) |
| 7 | Knowing when to stop | [17:18](https://youtu.be/Wv-xnSiJM2g?t=1038) | [lessons/07-knowing-when-to-stop](lessons/07-knowing-when-to-stop) |

## Requirements

- OpenAI Python SDK 3.22.1 · Responses API · gpt-6-luna · uv 0.12.21 · Python 3.12 · Ubuntu (Linux)
- Python 3.12+ and [uv](https://docs.astral.sh/uv/)

## Run the final project

```bash
cd app
uv sync
cp .env.example .env   # then add your own keys (e.g. OPENAI_API_KEY)
uv run --env-file .env agent
```

## Repository structure

```
README.md          this file
lessons/           one folder per lesson: goal, timestamp, commands and files exactly as in the video
app/               the final working project
assets/            thumbnail
```

## License

MIT — use it for anything, credit appreciated.

---
Generated on 2026-10-01 from the course scripts. Code with Antonio · AI tutor.