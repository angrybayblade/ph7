"""JS Lib."""

from ._mock import _ApiMock
from .api import JSON, console, document, fetch, setInterval, setTimeout

alert = _ApiMock("alert")


__all__ = (
    "document",
    "fetch",
    "console",
    "alert",
    "fetch",
    "setInterval",
    "setTimeout",
    "JSON",
)
