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
from ph7.style import attributes as css_attr
from typing_extensions import Literal

class CSSObject:
    \"\"\"CSS class representation.\"\"\"

    _name: t.Optional[str] = None

    {properties}

    @classmethod
    def name(cls) -> str:
        \"\"\"Name string.\"\"\"
        if cls._name is not None:
            return cls._name
        return cls.__name__.replace("_", "-")
    @classmethod
    def properties(cls) -> t.Dict[str, str]:
        \"\"\"Returns properties mapping.\"\"\"
        properties = {{}}
        for base in cls.__bases__:
            if hasattr(base, "properties"):
                properties.update(base.properties())
        for prop, val in cls.__dict__.items():
            if isinstance(val, str) and not prop.startswith("__"):
                properties[css_attr[prop]] = val
        return properties

    @classmethod
    def subclasses(cls) -> t.List["CSSObject"]:
        \"\"\"Returns the list of available subclasses.\"\"\"
        cs = []
        for c in cls.__dict__.values():
            if hasattr(c, "properties"):
                cs.append(c)
        return cs


def _render(obj: CSSObject, parent: str, container: t.Dict) -> None:
    \"\"\"Render CSS object.\"\"\"
    container[f"{{parent}} .{{obj.name()}}"[1:]] = obj.properties()
    for subc in obj.subclasses():
        _render(
            obj=subc,
            parent=f"{{parent}} .{{obj.name()}}",
            container=container,
        )


def render(*objs: CSSObject, min: bool = False) -> str:
    \"\"\"Render CSS stylesheet.\"\"\"
    sheet = ""
    container: t.Dict[str, t.Dict] = {{}}
    separator = "" if min else " "
    newline = "" if min else "\\n"
    tab = "" if min else "  "
    for obj in objs:
        _render(obj=obj, parent="", container=container)
    for cls in sorted(container):
        sheet += f"{{cls}}" + "{{" + newline
        for prop, val in container[cls].items():
            sheet += f"{{tab}}{{prop}}:{{separator}}{{val}};{{newline}}"
        sheet += "}}" + newline
    return sheet

"""

properties = ""

for tag in tags:
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


Path("ph7/css.py").write_text(
    format_str(
        code.format(properties=properties),
        mode=Mode(),
    )
)
