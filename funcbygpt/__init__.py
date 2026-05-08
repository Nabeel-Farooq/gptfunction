from openai import OpenAI
from dotenv import load_dotenv

import contextlib
import io
import os
from functools import wraps
from typing import Callable, Any

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@contextlib.contextmanager
def capture_stdout():
    """
    Capture stdout output safely.
    """
    buffer = io.StringIO()

    with contextlib.redirect_stdout(buffer):
        yield buffer


def generate_python_code(prompt: str) -> str:
    """
    Ask OpenAI to translate an algorithm into Python code.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Python code generator. "
                    "Return ONLY valid Python code."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"{prompt}\n\n"
                    "Translate the above algorithm into clean Python code."
                ),
            },
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()


def funcbygpt(func: Callable) -> Callable:
    """
    Decorator that converts a prompt into executable Python code.
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        prompt = func(*args, **kwargs)

        if not isinstance(prompt, str):
            raise TypeError("Decorated function must return a string prompt.")

        # Flags
        should_print = "--print" in prompt
        should_return = "--return" in prompt

        # Remove flags
        prompt = (
            prompt.replace("--print", "")
                  .replace("--return", "")
                  .strip()
        )

        try:
            code = generate_python_code(prompt)

            if should_print:
                print("\nGenerated Code:\n")
                print(code)
                print()

            # Restricted execution environment
            exec_globals = {
                "__builtins__": __builtins__,
            }

            exec_locals = {}

            if should_return:
                with capture_stdout() as output:
                    exec(code, exec_globals, exec_locals)

                return output.getvalue()

            exec(code, exec_globals, exec_locals)

        except Exception as e:
            print(f"Error: {e}")

    return wrapper
