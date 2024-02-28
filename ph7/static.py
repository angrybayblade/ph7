"""
Static content helpers.
"""

from ph7.base import node
from ph7.css import CSSObject
from ph7.css import render as crender
from ph7.html import style


def include(*objs: CSSObject) -> node:
    """Include css objects."""
    return style(crender(*objs, min=True))
