"""
Static content helpers.
"""

import typing as t

from ph7.core.html import HtmlNode
from ph7.css import CSSObject, to_css
from ph7.html import script, style, unpack
from ph7.js import JavaScriptObject, JSCallable
from ph7.js.transpile import to_js


def is_css(obj: t.Any):
    """Check if the object is a CSS Object."""
    return hasattr(obj, "__css__")


def include(
    *objs: t.Union[CSSObject, JavaScriptObject],
    minify: bool = True,
) -> HtmlNode:
    """Include css objects."""
    styles: t.List[t.Union[CSSObject, t.Type[CSSObject]]] = []
    scripts: t.List[JavaScriptObject] = []
    for obj in objs:
        if is_css(obj=obj):
            styles.append(t.cast(CSSObject, obj))
            continue
        if isinstance(obj, JSCallable):
            scripts.append(obj.func)
            continue
        scripts.append(t.cast(JavaScriptObject, obj))

    style_node = style(
        to_css(*styles, minify=minify),
    )

    script_node = script(
        to_js(*scripts, minify=minify),
        type="text/javascript",
    )

    if len(scripts) > 0 and len(styles) > 0:
        return unpack(style_node, script_node)

    if len(scripts) > 0:
        return script_node

    if len(styles) > 0:
        return style_node

    return unpack()
