"""
PH7 - Python native HTML rendering
"""

from . import css, html, style


class _KebabCase:  # pylint: disable=too-few-public-methods
    def __getattribute__(self, __name: str) -> str:
        """Get attribute."""
        return __name.replace("_", "-")


kebab = _KebabCase()

__all__ = (
    "html",
    "css",
    "style",
)
