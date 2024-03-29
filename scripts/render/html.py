import json
import typing as t
from pathlib import Path

from black import Mode, format_str

tags = json.loads((Path.cwd() / "data" / "html.json").read_text())

content_not_allowed = ["link", "img", "br", "hr"]


template_fn = """def {tag}(
    *children: ChildType,
    {attribute_definitions}
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> HtmlNode:
    \"\"\"{title} node.\"\"\"
    return HtmlNode(
        *children,
        attributes={attribute_dict},
        style=style,
        on=on,
        name="{tag}",
        content_allowed={content_allowed}
    )
"""


unpack_node = """def unpack(*children: ChildType) -> HtmlNode:
    \"\"\"Unpackable node.\"\"\"
    return UnpackableNode(*children)
"""

code = """\"\"\"
This file is auto generated using scripts/render/html.py
\"\"\"

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals

import typing as t
from typing_extensions import Literal

from ph7.core.html import ChildType, HtmlNode, UnpackableNode
from ph7.style import Style
from ph7.formatters import cformat
from ph7.css import CSSObject
from ph7.js import Events as DOMEvents


"""


def get_class_render() -> t.Tuple[str, str, str, str]:
    """Returns template values for `class` attribute."""
    return (
        "class_name",
        (
            "t.Union[t.List[t.Union[str, CSSObject, t.Type[CSSObject]]], "
            "t.Union[str, CSSObject, t.Type[CSSObject]]]"
        ),
        "class",
        "cformat(class_name)",
    )


def get_for_render() -> t.Tuple[str, str, str, str]:
    """Returns template values for `for` attribute."""
    return (
        "for_html",
        "str",
        "for",
        "for_html",
    )


def get_async_render() -> t.Tuple[str, str, str, str]:
    """Returns template values for `async` attribute."""
    return (
        "async_node",
        "str",
        "async",
        "async_node",
    )


for tag in sorted(tags):
    if tag == "del":
        continue

    attribute_definitions = ""
    attribute_dict = "{"
    for attribute in tags[tag]:
        if attribute["name"] == "style" or attribute["name"] == "data-*":
            continue

        if attribute["name"] == "class":
            arg, type_annotation, dict_name, dict_val = get_class_render()
        elif attribute["name"] == "for":
            arg, type_annotation, dict_name, dict_val = get_for_render()
        elif attribute["name"] == "async":
            arg, type_annotation, dict_name, dict_val = get_async_render()
        else:
            arg = attribute["name"]
            type_annotation = "str"
            if attribute["options"]:
                type_annotation = (
                    "Literal["
                    + ", ".join(map(lambda x: f'"{x}"', attribute["options"]))
                    + "]"
                )
            dict_name = attribute["name"]
            dict_val = arg

        if "-" in arg:
            arg = arg.replace("-", "_")

        if "-" in dict_val:
            dict_val = dict_val.replace("-", "_")

        attribute_definitions += arg + ":" + f"t.Optional[{type_annotation}] = None,"
        attribute_dict += f'"{dict_name}": {dict_val},'
    attribute_dict += "}"

    code += template_fn.format(
        tag=tag,
        title=tag.title(),
        attribute_definitions=attribute_definitions,
        attribute_dict=attribute_dict,
        content_allowed=tag not in content_not_allowed,
    )

code += unpack_node

Path(
    "ph7/html.py",
).write_text(
    format_str(code, mode=Mode()),
    encoding="utf-8",
)
