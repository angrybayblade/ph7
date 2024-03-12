"""
Attribute formatters for HTML nodes.
"""

import typing as t

from ph7.context import ctx
from ph7.css import CSSObject
from ph7.js import JSCallable


def sformat(style: t.Dict) -> str:
    """Style formatter."""
    if len(style) == 0:
        return ""
    return ' style="' + ";".join(map(lambda x: f"{x[0]}:{x[1]}", style.items())) + '" '


def aformat(attributes: t.Dict) -> str:
    """Attributes formatter."""
    attrs = " ".join(
        [f'{key}="{value}"' for key, value in attributes.items() if value is not None]
    )
    if attrs:
        return f" {attrs} "
    return ""


def hformat(handlers: t.Dict) -> str:
    """Handler formatter."""
    if len(handlers) == 0:
        return ""

    formatted = " "
    for name, handler in handlers.items():
        if isinstance(handler, str):
            if "(" in handler and handler.endswith(")"):
                formatted += f"on{name}='{handler}'"
                continue
            formatted += f"on{name}='{handler}()'"
            continue
        if isinstance(handler, JSCallable):
            formatted += f"on{name}={handler}"
            ctx.static.add(handler)
            continue
        ctx.static.add(handler)
        formatted += f"on{name}={handler.__name__}()"
    return formatted


def cformat(
    class_name: t.Optional[
        t.Union[
            t.List[
                t.Union[
                    str,
                    CSSObject,
                    t.Type[CSSObject],
                ]
            ],
            t.Union[str, CSSObject, t.Type[CSSObject], t.Type[CSSObject]],
        ]
    ]
) -> t.Optional[str]:
    """Format classname."""
    if class_name is None:
        return None

    if hasattr(class_name, "name"):
        ctx.static.add(resource=t.cast(CSSObject, class_name))
        return t.cast(CSSObject, class_name).format()

    if isinstance(class_name, str):
        return class_name

    cls_name = ""
    for cls in class_name:
        if hasattr(cls, "name"):
            ctx.static.add(resource=t.cast(CSSObject, cls))
            cls_name += f"{t.cast(CSSObject, cls).format()} "
            continue
        cls_name += f"{cls} "
    return cls_name[:-1]
