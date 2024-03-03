"""
Static content helpers.
"""

from ph7.base import node
from ph7.css import CSSObject
from ph7.css import render as crender
from ph7.html import style


def include(*objs: CSSObject, minify: bool = True) -> node:
    """Include css objects."""
    return style(("" if minify else "\n") + crender(*objs, minify=minify))
