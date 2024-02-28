"""Context classes."""

import typing as t

from ph7.css import CSSObject


class StaticContext:
    """Static context."""

    _view: str

    def __init__(self) -> None:
        """Initialize object."""
        self._view = ""

    def view(self, name: str) -> None:
        """Set view."""
        self._view = name

    def add(self, resource: CSSObject) -> None:
        """Add a resource."""

    def include(self, context: t.Dict) -> t.Any:
        """Include in the final render."""
        raise NotImplementedError("Render method not implemented.")


class AppContext:
    """App context."""

    def __init__(self) -> None:
        """Initialize object."""
        self.static = StaticContext()


ctx = AppContext()
