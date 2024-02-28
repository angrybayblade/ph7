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
    {property}: NotRequired[{type}]
    \"\"\"{annotation}\"\"\"
"""

attrt = """"{name}": "{value}",
"""

code = """\"\"\"
This file is auto generated using scripts/render/style.py
\"\"\"

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals

import typing as t
from typing_extensions import TypedDict, Literal, NotRequired


attributes = {{
    {attributes}
}}

class Style(TypedDict):
    \"\"\"CSS Properties\"\"\"

    {properties}
"""

properties = ""

attributes = ""

for tag in tags:
    attributes += attrt.format(
        name=tag.replace("-", "_"),
        value=special_properties.get(tag, tag),
    )
    type_ = "str"
    if tags[tag]["options"]:
        type_ = (
            "Literal[" + ",".join(map(lambda x: f'"{x}"', tags[tag]["options"])) + "]"
        )
    properties += propt.format(
        property=tag.replace("-", "_"),
        type=type_,
        annotation=tags[tag]["syntax"] or "No syntax rule available",
    )


Path("ph7/style.py").write_text(
    format_str(
        code.format(
            attributes=attributes,
            properties=properties,
        ),
        mode=Mode(),
    )
)
