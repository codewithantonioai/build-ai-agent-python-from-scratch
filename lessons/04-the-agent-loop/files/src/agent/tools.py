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
