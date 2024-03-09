"""Javascipt helpers."""

import json
import typing as t

from typing_extensions import Concatenate, ParamSpec

from .events import Events
from .lib import JSON, alert, console, document
from .lib.api import fetch
from .transpile import as_js, to_js

Param = ParamSpec("Param")
ReturnType = t.TypeVar("ReturnType")
OriginalFunc = t.Callable[Param, ReturnType]
DecoratedFunc = t.Callable[Concatenate[str, Param], ReturnType]


def serialize(args: t.List[t.Any]) -> t.List[str]:
    """Serialize arguments."""
    dumped = []
    for arg in args:
        try:
            dumped.append(json.dumps(arg).replace('"', "'"))
        except Exception:  # pylint: disable=broad-exception-caught
            dumped.append(arg)
    return dumped


class JSCallable:
    """Javascript callable."""

    def __init__(
        self,
        func: t.Callable,
        args: t.Optional[t.Tuple[t.Any, ...]] = None,
        kwds: t.Optional[t.Dict[t.Any, t.Any]] = None,
    ) -> None:
        """Callable."""
        self.func = func
        self.args = args or ()
        self.kwds = kwds or {}

    def __str__(self) -> str:
        return (
            f"{self.func.__name__}("
            + ",".join(serialize([*self.args, *self.kwds.values()]))
            + ")"
        )

    def __call__(self, *args: t.Any, **kwds: t.Any) -> t.Any:
        return JSCallable(
            func=self.func,
            args=args,
            kwds=kwds,
        )


JavaScriptObject = t.Union[t.Callable, t.Coroutine, JSCallable]


def js_callable(func: OriginalFunc) -> DecoratedFunc:
    """Decorate method as javascript callable."""
    return JSCallable(func)


__all__ = (
    "Events",
    "document",
    "fetch",
    "console",
    "js_callable",
    "alert",
    "JSON",
    "to_js",
    "as_js",
)
