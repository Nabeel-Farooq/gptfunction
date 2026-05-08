import shutil
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve()

BUILD_DIRS = [
    "build",
    "dist",
    "funcbygpt.egg-info",
]


def clean():
    """
    Remove build artifacts.
    """
    for path in BUILD_DIRS:
        target = ROOT_DIR / path

        if target.exists():
            shutil.rmtree(target)
            print(f"Removed: {target}")
        else:
            print(f"Skipped: {target} (not found)")


def build():
    """
    Build source and wheel distributions.
    """
    subprocess.run(
        [sys.executable, "setup.py", "sdist", "bdist_wheel"],
        check=True,
    )


def upload():
    """
    Upload package to PyPI using twine.
    """
    subprocess.run(
        ["twine", "upload", "dist/*"],
        shell=True,
        check=True,
    )


COMMANDS = {
    "clean": clean,
    "build": build,
    "upload": upload,
}


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python publish.py [clean|build|upload]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command not in COMMANDS:
        print(f"Unknown command: {command}")
        print(f"Available commands: {', '.join(COMMANDS)}")
        sys.exit(1)

    try:
        COMMANDS[command]()
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        sys.exit(e.returncode)


if __name__ == "__main__":
    main()
