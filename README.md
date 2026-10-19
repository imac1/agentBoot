# agentBoot

A small coding agent in Python that receives a task and let it work through the code.

Following along with [Boot.dev course](https://www.boot.dev/courses/build-ai-agent-python).

Here's how it works:

1. It receives a coding task.
2. It picks from a set of predefined functions to list files in a directory, read a file, overwrite a file, or run a Python file.
3. It keeps calling those functions until the task is done—or it fails miserably, which is definitely possible.

For example, with a buggy calculator app, the agent would inspect the files, find the problem, edit the code, and run it to check the fix.

## Run it

You'll need Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Create a `.env` file in the project folder and add your [OpenRouter](https://openrouter.ai/) API key:

```dotenv
OPENROUTER_API_KEY=your_api_key_here
```

Then send it a prompt:

```bash
uv run main.py "Help me debug a Python calculator"
```

Add `--verbose` to see the prompt and token counts:

```bash
uv run main.py "Help me debug a Python calculator" --verbose
```

## Source

[GitHub repository](https://github.com/imac1/agentBoot)
