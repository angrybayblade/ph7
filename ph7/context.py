"""Context classes."""

import os
import sys
import typing as t
from pathlib import Path

from ph7.css import CSSObject
from ph7.css import render as render_css


class StaticContext:
    """Static context."""

    _view: str

    def __init__(self, path: t.Optional[Path] = None) -> None:
        """Initialize object."""
        self._view = ""
        self.path = path or (Path.cwd() / "static")
        self.development_mode = os.environ.get("DEVELOPMENT", "0") == "1"

        self.views: t.Dict[str, t.List[str]] = {}
        self.cache: t.Dict[str, str] = {}
        self.files: t.Dict[str, Path] = {}
        self.resources: t.Dict = {}

        (self.path / "css").mkdir(exist_ok=True)

    def view(self, name: str) -> None:
        """Set view."""
        self._view = name

    def add(self, resource: CSSObject) -> None:
        """Add a resource."""
        module = resource.__module__
        if module not in self.resources:
            self.resources[module] = {}

        cls, *_ = (
            str(resource)
            .replace("<class '", "")
            .replace("'>", "")
            .replace(f"{module}.", "")
            .split(".")
        )
        if cls not in self.resources[module]:
            self.resources[module][cls] = getattr(sys.modules[module], cls)
        self.cache[module] = render_css(
            *self.resources[module].values(),
            minify=not self.development_mode,
        )

        if not self.development_mode:
            self.files[module] = (
                self.path / "css" / ("_".join(module.split(".")) + ".css")
            )
            self.files[module].write_text(self.cache[module])

        if self.view not in self.views:
            self.views[self._view] = []

        if module not in self.views[self._view]:
            self.views[self._view].append(module)

    def include(self, context: t.Dict) -> t.Any:
        """Include static files."""

        from ph7.html import link, style, unpack

        if context["_view"] not in self.views:
            return unpack()

        if self.development_mode:
            return unpack(
                *(
                    style(self.cache[module], id=module)
                    for module in self.views[context["_view"]]
                )
            )

        return unpack(
            *(
                link(
                    id=module,
                    href="/static/css/" + self.files[module].name,
                    rel="stylesheet",
                )
                for module in self.views[context["_view"]]
            )
        )


class AppContext:
    """App context."""

    def __init__(self) -> None:
        """Initialize object."""
        self.static = StaticContext()


ctx = AppContext()
