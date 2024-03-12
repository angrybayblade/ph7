"""Context classes."""

import os
import sys
import typing as t
from pathlib import Path

from ph7.css import CSSObject, to_css
from ph7.js import JavaScriptObject, JSCallable
from ph7.js.transpile import to_js


class StaticContext:
    """Static context."""

    _view: str

    def __init__(self, path: t.Optional[Path] = None, debug: bool = False) -> None:
        """Initialize object."""
        self._view = ""
        self.path = path or (Path.cwd() / "static")
        self.debug = os.environ.get("DEVELOPMENT", "0") == "1"
        if debug:
            self.debug = debug

        self.views: t.Dict[str, t.Dict[str, t.List[str]]] = {"js": {}, "css": {}}
        self.cache: t.Dict[str, t.Dict[str, str]] = {"js": {}, "css": {}}
        self.files: t.Dict[str, t.Dict[str, Path]] = {"js": {}, "css": {}}
        self.resources: t.Dict[str, t.Dict[str, t.Any]] = {"js": {}, "css": {}}

        (self.path / "css").mkdir(exist_ok=True, parents=True)
        (self.path / "js").mkdir(exist_ok=True, parents=True)

    def view(self, name: str) -> None:
        """Set view."""
        self._view = name

    def _add_css(self, resource: CSSObject) -> None:
        """Add css resource."""
        module = resource.__module__
        if module not in self.resources["css"]:
            self.resources["css"][module] = {}

        cls, *_ = (
            str(resource)
            .replace("<class '", "")
            .replace("'>", "")
            .replace(f"{module}.", "")
            .split(".")
        )
        if cls not in self.resources["css"][module]:
            self.resources["css"][module][cls] = getattr(sys.modules[module], cls)

        self.cache["css"][module] = to_css(
            *self.resources["css"][module].values(),
            minify=not self.debug,
        )

        if not self.debug:
            self.files["css"][module] = (
                self.path / "css" / ("_".join(module.split(".")) + ".css")
            )
            self.files["css"][module].write_text(self.cache["css"][module])

        if self.view not in self.views:
            self.views["css"][self._view] = []

        if module not in self.views["css"][self._view]:
            self.views["css"][self._view].append(module)

    def _add_js(self, resource: JavaScriptObject) -> None:
        """Add js resource."""

        module = (
            resource.func.__module__
            if isinstance(resource, JSCallable)
            else resource.__module__
        )

        if module not in self.resources["js"]:
            self.resources["js"][module] = sys.modules[module]

        self.cache["js"][module] = to_js(
            self.resources["js"][module],
            minify=not self.debug,
        )

        if not self.debug:
            self.files["js"][module] = (
                self.path / "js" / ("_".join(module.split(".")) + ".js")
            )
            self.files["js"][module].write_text(self.cache["js"][module])

        if self.view not in self.views:
            self.views["js"][self._view] = []

        if module not in self.views["js"][self._view]:
            self.views["js"][self._view].append(module)

    def add(self, resource: t.Union[CSSObject, JavaScriptObject]) -> None:
        """Add a resource."""
        if hasattr(resource, "__css__"):
            self._add_css(t.cast(CSSObject, resource))
            return
        self._add_js(t.cast(JavaScriptObject, resource))

    def _include_css(self, view: str) -> t.Any:
        """Render stylesheet."""
        from ph7.html import link  # pylint: disable=import-outside-toplevel
        from ph7.html import style  # pylint: disable=import-outside-toplevel

        if view not in self.views["css"]:
            return ()

        if self.debug:
            return (
                style(
                    self.cache["css"][module],
                    id=f"css.{module}",
                )
                for module in self.views["css"][view]
            )

        return (
            link(
                rel="stylesheet",
                href="/static/css/" + self.files["css"][module].name,
                id=f"css.{module}",
            )
            for module in self.views["css"][view]
        )

    def _include_js(self, view: str) -> t.Any:
        """Render script."""
        from ph7.html import script  # pylint: disable=import-outside-toplevel

        if view not in self.views["js"]:
            return ()

        if self.debug:
            return (
                script(
                    self.cache["js"][module],
                    id=f"js.{module}",
                    type="text/javascript",
                )
                for module in self.views["js"][view]
            )

        return (
            script(
                src="/static/js/" + self.files["js"][module].name,
                id=f"js.{module}",
                type="text/javascript",
            )
            for module in self.views["js"][view]
        )

    def include(self, context: t.Dict) -> t.Any:
        """Include static files."""
        from ph7.html import unpack  # pylint: disable=import-outside-toplevel

        view = context["_view"]

        if view not in self.views["css"] and view not in self.cache["js"]:
            return unpack()

        return unpack(
            *self._include_css(view=view),
            *self._include_js(view=view),
        )


class AppContext:
    """App context."""

    def __init__(self) -> None:
        """Initialize object."""
        self.static = StaticContext()


ctx = AppContext()
