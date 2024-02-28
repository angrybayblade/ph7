"""
Static files helper.
"""

import os
import sys
import typing as t
from pathlib import Path

from ph7.base import node
from ph7.context import StaticContext as BaseStatiContext
from ph7.css import CSSObject
from ph7.css import render as render_css
from ph7.html import link, style, unpack


class StaticContext(BaseStatiContext):
    """Static context for Django."""

    def __init__(self, path: Path) -> None:
        """Initialize object."""
        super().__init__()
        self.path = path
        self.development_mode = os.environ.get("DEVELOPMENT", "0") == "1"

        self.views: t.Dict[str, t.List[str]] = {}
        self.cache: t.Dict[str, str] = {}
        self.files: t.Dict[str, Path] = {}
        self.resources: t.Dict = {}

        (self.path / "css").mkdir(exist_ok=True)

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
            min=not self.development_mode,
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

    def include(self, context: t.Dict) -> node:
        """Include static files."""
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
