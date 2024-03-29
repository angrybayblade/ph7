"""
Substitute blocks in the documentation
"""

import json
import subprocess
import sys
import typing as t
from pathlib import Path
from tempfile import TemporaryDirectory

from clea import Boolean, Directory, File, command, run
from typing_extensions import Annotated

BLOCK_DEF = "<!-- {blockd} -->\n"

BLOCK_END = "<!-- end -->"

CODE_BLOCK = """```{type}
{code}
```
"""

JSBEAUTIFY_CONFIG = Path(__file__).parent.parent.parent / ".jsbeautify"


def prettify(code: str, tp: str) -> str:
    """Prettify HTML/CSS/JS."""
    with TemporaryDirectory() as tempd:
        file = Path(tempd, "fmt." + tp)
        file.write_text(code, encoding="utf-8")
        data = (
            t.cast(
                t.IO[bytes],
                subprocess.Popen(
                    [
                        "js-beautify",
                        "--config",
                        str(JSBEAUTIFY_CONFIG),
                        "--type",
                        tp,
                        file,
                    ],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                ).stdout,
            )
            .read()
            .decode(encoding="utf-8")
            .strip()
        )
        data = "\n".join([line for line in data.split("\n") if line.strip()])
        return data


def run_example(file: str, read: str, env: t.Optional[t.Dict] = None) -> str:
    """Run example."""
    process = subprocess.Popen(
        [sys.executable, file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )

    if read == "stdout":
        return (
            t.cast(t.IO[bytes], process.stdout).read().decode(encoding="utf-8").strip()
        )

    if read == "stderr":
        return (
            t.cast(t.IO[bytes], process.stderr).read().decode(encoding="utf-8").strip()
        )

    return (
        t.cast(t.IO[bytes], process.stdout).read().decode(encoding="utf-8").strip()
        + t.cast(t.IO[bytes], process.stderr).read().decode(encoding="utf-8").strip()
    )


def run_cmd(cmd: t.List[str], env: t.Optional[t.Dict] = None) -> str:
    """Run example."""
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    return (
        t.cast(t.IO[bytes], process.stdout).read().decode(encoding="utf-8").strip()
        + "\n"
        + t.cast(t.IO[bytes], process.stderr).read().decode(encoding="utf-8").strip()
    )


def code_block(blockd: t.Dict) -> str:
    """Build code block."""
    block = BLOCK_DEF.format(blockd=json.dumps(blockd))
    if blockd.get("class") is not None:
        block += f"<div class='{blockd['class']}'>\n"
    if not blockd.get("output_only", False):
        code = (
            Path(
                blockd["file"],
            )
            .read_text(
                encoding="utf-8",
            )
            .strip()
        )
        if "lines" in blockd and "input" in blockd["lines"]:
            code = "\n".join(code.split("\n")[slice(*blockd["lines"]["input"])])
        block += CODE_BLOCK.format(
            code=code,
            type="python",
        )
        block += "\n"
    if not blockd.get("input_only", False):
        code = run_example(
            file=blockd["file"],
            read=blockd.get("read", "all"),
            env=blockd.get("env"),
        )
        if "lines" in blockd and "output" in blockd["lines"]:
            code = "\n".join(code.split("\n")[slice(*blockd["lines"]["output"])])
        if blockd["type"] in ("html", "css", "js"):
            code = prettify(code=code, tp=blockd["type"])
        block += CODE_BLOCK.format(
            code=code,
            type=blockd["type"],
        )
    if blockd.get("class") is not None:
        block += "</div>\n"
    block += BLOCK_END
    block += "\n"
    return block


def cmd_block(blockd: t.Dict) -> str:
    """Build code block."""
    block = BLOCK_DEF.format(blockd=json.dumps(blockd))
    if not blockd.get("output_only", False):
        block += CODE_BLOCK.format(
            code=f"""$ {" ".join(blockd["cmd"])}""",
            type="bash",
        )
        block += "\n"
    code = run_cmd(cmd=blockd["cmd"], env=blockd.get("env"))
    if "lines" in blockd:
        code = "\n".join(code.split("\n")[slice(*blockd["lines"])])
    if blockd["type"] in ("html", "css", "js"):
        code = prettify(code=code, tp=blockd["type"])
    block += CODE_BLOCK.format(
        code=code,
        type=blockd["type"],
    )
    block += BLOCK_END
    block += "\n"
    return block


def update(file: Path) -> None:
    """Update document."""
    updated = ""
    content = file.read_text(encoding="utf-8")
    lines = content.split("\n")
    while len(lines):
        line = lines.pop(0)
        if "<!-- {" in line:
            blockd = json.loads(
                line.replace(
                    "<!-- ",
                    "",
                ).replace(
                    " -->",
                    "",
                )
            )
            if "cmd" in blockd:
                block = cmd_block(blockd=blockd)
            else:
                block = code_block(blockd=blockd)
            while line != BLOCK_END:
                line = lines.pop(0)
            updated += block
        else:
            updated += line + "\n"
    file.write_text(updated[:-1], encoding="utf-8")


def update_all(path: Path) -> None:
    """Update document."""
    for file in path.glob("**/*.md"):
        update(file=file)


@command
def sub(
    check: Annotated[bool, Boolean(help="Perform check.")],
    docs: Annotated[Path, Directory(help="Path to documentation.")] = Path(
        "./docs",
    ),
    file: Annotated[
        t.Optional[Path],
        File(
            help="File to perform substitutions or check.",
            long_flag="--file",
        ),
    ] = None,
) -> None:
    """
    Substitute {{example:FILE}} blocks in the documentation
    """
    if check:
        ...

    if file is not None:
        update(file=file)
        return

    update_all(path=docs)


if __name__ == "__main__":
    run(sub)
