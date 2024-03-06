"""Javascipt helpers."""

import json
import typing as t

from typing_extensions import Concatenate, ParamSpec

from .events import Events
from .lib import alert, console, document
from .lib.api import fetch

Param = ParamSpec("Param")
ReturnType = t.TypeVar("ReturnType")
OriginalFunc = t.Callable[Param, ReturnType]
DecoratedFunc = t.Callable[[Concatenate[str, Param]], ReturnType]


def dump(args):
    dumped = []
    for arg in args:
        try:
            dumped.append(json.dumps(arg).replace('"', "'"))
        except Exception:
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
            + ",".join(dump([*self.args, *self.kwds.values()]))
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
    return JSCallable(func)


__all__ = (
    "Events",
    "document",
    "fetch",
    "console",
    "js_callable",
    "alert",
)
