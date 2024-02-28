import json
import typing as t
from pathlib import Path

from black import Mode, format_str

tags = json.loads((Path.cwd() / "data" / "html.json").read_text())

content_not_allowed = ["link"]

template_cls = """class {tag}(node):
    \"\"\"{title} node.\"\"\"

    def __init__(
        self,
        *children: ChildType,
        {attribute_definitions}
        style: t.Optional[Style] = None,
        handlers: t.Optional[DOMEvents] = None,
        render: t.Optional[t.Callable[[t.Dict], str]] = None,
    ) -> None:
        \"\"\"Initialize object.\"\"\"
        super().__init__(*children, attributes={attribute_dict}, style=style,handlers=handlers,render=render)

"""

template_fn = """def {tag}(
    *children: ChildType,
    {attribute_definitions}
    style: t.Optional[Style] = None,
    handlers: t.Optional[DOMEvents] = None,
) -> node:
    \"\"\"{title} node.\"\"\"
    return node(
        *children,
        attributes={attribute_dict},
        style=style,
        handlers=handlers,
        name="{tag}",
        content_allowed={content_allowed}
    )
"""


unpack_node = """def unpack(*children: ChildType) -> node:
    \"\"\"Unpackable node.\"\"\"
    return _unpack(*children)
"""

code = """\"\"\"
This file is auto generated using scripts/render/html.py
\"\"\"

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals

import typing as t
from typing_extensions import Literal

from ph7.base import node, ChildType, unpack as _unpack
from ph7.style import Style
from ph7.formatters import cformat
from ph7.css import CSSObject
from ph7.js import Events as DOMEvents


"""


def get_class_render() -> t.Tuple[str, str, str, str]:
    """Returns template values for `class` attribute."""
    return (
        "class_name",
        "t.Union[t.List[t.Union[str, CSSObject]], t.Union[str, CSSObject]]",
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

Path("ph7/html.py").write_text(format_str(code, mode=Mode()))
