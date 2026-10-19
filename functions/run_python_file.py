import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] = []) -> str:
    working_dir = os.path.realpath(working_directory)
    target_file = os.path.realpath(os.path.join(working_dir, file_path))

    if os.path.commonpath([working_dir, target_file]) != working_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" does not exist'

    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    try:
        result = subprocess.run(
            ["python", target_file] + args,
            cwd=working_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        return (
            f"STDOUT: {result.stdout}\n"
            f"STDERR: {result.stderr}\n"
            f"Process exited with code {result.returncode}"
        )

    except subprocess.TimeoutExpired:
        return "Error: Execution timed out after 30 seconds"

    except Exception as e:
        return f"Error: {e}"
