"""
PH7 - Python native HTML rendering
"""

from . import html, style
from .css import CSSObject
from .static import include


class _Case:
    def __call__(self, name: str) -> str:
        """Call getattr for __name"""
        return getattr(self, name)


class _KebabCase(_Case):
    def __getattribute__(self, __name: str) -> str:
        """Get attribute."""
        return __name.replace("_", "-")


class _TitleCase(_Case):
    def __getattribute__(self, __name: str) -> str:
        """Get attribute."""
        return " ".join(map(lambda x: x.title(), __name.split("_")))


kebabc = _KebabCase()
titlec = _TitleCase()


__all__ = (
    "html",
    "style",
    "include",
    "kebabc",
    "titlec",
    "CSSObject",
)
