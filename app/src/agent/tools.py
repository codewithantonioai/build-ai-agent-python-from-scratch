from datetime import datetime
from pathlib import Path

WORKSPACE = Path("workspace").resolve()


def get_current_time():
    return datetime.now().strftime("%A %d %B %Y, %H:%M")


def list_files():
    return "\n".join(path.name for path in sorted(WORKSPACE.iterdir()))


def safe_path(name):
    path = (WORKSPACE / name).resolve()
    if not path.is_relative_to(WORKSPACE):
        raise ValueError("that path is outside the workspace")
    return path


def read_file(filename):
    return safe_path(filename).read_text()


def write_file(filename, content):
    answer = input(f"  ? Save {filename} ({len(content)} characters)? [y/N] ")
    if answer.strip().lower() != "y":
        return "The user said no. The file was not saved."
    safe_path(filename).write_text(content)
    return f"Saved {filename}."


FUNCTIONS = {
    "get_current_time": get_current_time,
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
}


def run_tool(name, args):
    try:
        return str(FUNCTIONS[name](**args))
    except Exception as error:
        return f"Error: {error}"


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
    tool(
        "write_file",
        "Create or overwrite a file in the workspace.",
        filename="A file name, like todo.md",
        content="The full text of the file",
    ),
]
