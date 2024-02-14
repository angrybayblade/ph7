from . import css, html, style


class _KebabCase:
    def __getattribute__(self, __name: str) -> str:
        """Get attribute."""
        return __name.replace("_", "-")


kebab = _KebabCase()

__all__ = (
    "html",
    "css",
    "style",
)
