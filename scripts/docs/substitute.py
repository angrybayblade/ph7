"""
Substitute blocks in the documentation
"""

import json
import subprocess
import sys
import typing as t
from pathlib import Path
from tempfile import TemporaryDirectory

from clea import Boolean, Directory, command, run
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
            )
            .stdout.read()
            .decode(encoding="utf-8")
            .strip()
        )
        data = "\n".join([line for line in data.split("\n") if line.strip()])
        return data


def run_example(file: str, env: t.Optional[t.Dict] = None) -> t.Dict:
    """Run example."""
    process = subprocess.Popen(
        [sys.executable, file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    return (
        process.stdout.read().decode(encoding="utf-8").strip()
        + process.stderr.read().decode(encoding="utf-8").strip()
    )


def run_cmd(cmd: t.List[str], env: t.Optional[t.Dict] = None) -> t.Dict:
    """Run example."""
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    return (
        process.stdout.read().decode(encoding="utf-8").strip()
        + process.stderr.read().decode(encoding="utf-8").strip()
    )


def code_block(blockd: t.Dict) -> str:
    """Build code block."""
    block = BLOCK_DEF.format(blockd=json.dumps(blockd))
    if not blockd.get("output_only", False):
        block += CODE_BLOCK.format(
            code=Path(
                blockd["file"],
            )
            .read_text(
                encoding="utf-8",
            )
            .strip(),
            type="python",
        )
        block += "\n"
    if not blockd.get("input_only", False):
        code = run_example(file=blockd["file"], env=blockd.get("env"))
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


def update(path: Path) -> None:
    """Update document."""
    for file in path.glob("**/*.md"):
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


@command
def sub(
    check: Annotated[bool, Boolean(help="Perform check.")],
    docs: Annotated[Path, Directory(help="Path to documentation.")] = Path(
        "./docs",
    ),
) -> None:
    """
    Substitute {{example:FILE}} blocks in the documentation
    """
    if check:
        ...
    update(path=docs)


if __name__ == "__main__":
    run(sub)
