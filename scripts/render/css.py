import json
from pathlib import Path

from black import Mode, format_str

tags = json.loads((Path.cwd() / "data" / "css.json").read_text())

special_properties = {
    "animation-iteration-count": "animation-iter-count",
    "animation-timing-function": "animation-timing-fn",
    "charset": "@charset",
    "font-face": "@font-face",
    "keyframes": "@keyframes",
    "media": "@media",
    "transition-timing-function": "transition-timing-function",
}

propt = """
    {property}: {type}
    \"\"\"{annotation}\"\"\"
"""

code = """\"\"\"
This file is auto generated using scripts/render/css.py
\"\"\"

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals

import typing as t

from typing_extensions import Literal

from ph7.core.css import CSSNode, to_css

class CSSObject(CSSNode):
    \"\"\"CSS class representation.\"\"\"

    {properties}

    def __str__(self) -> str:
        \"\"\"String representation.\"\"\"
        return to_css(self)

    __repr__ = __str__
"""

properties = ""

for tag in tags:
    type_ = "str"
    if tags[tag]["options"]:
        type_ = (
            "Literal[ # type: ignore\n"
            + ",".join(map(lambda x: f'"{x}"', tags[tag]["options"]))
            + ", str]"
        )
    properties += propt.format(
        property=tag.replace("-", "_"),
        type=type_,
        annotation=tags[tag]["syntax"] or "No syntax rule available",
    )


Path("ph7/css.py").write_text(
    format_str(
        code.format(properties=properties),
        mode=Mode(),
    ),
    encoding="utf-8",
)
