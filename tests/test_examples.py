"""Test examples."""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES = list((Path(__file__).parent.parent / "examples").glob("*.py"))

ALLOWED_TO_FAIL = {
    "missing_placeholders.py": (
        "Error rendering 'Hello, ${name|John Doe}, "
        "I'm ${age} years old and I like ${food|Coffee}'; "
        "Value for 'age' not provided"
    ),
}


@pytest.mark.parametrize("example", EXAMPLES)
def test_example(example: Path) -> None:
    """Test example."""
    with subprocess.Popen(
        [sys.executable, example], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ) as process:
        process.wait()
        if example.name in ALLOWED_TO_FAIL:
            assert process.returncode == 1, process.stderr.read().decode()  # type: ignore
            assert ALLOWED_TO_FAIL[example.name] in process.stderr.read().decode()  # type: ignore
        else:
            assert process.returncode == 0, process.stderr.read().decode()  # type: ignore
