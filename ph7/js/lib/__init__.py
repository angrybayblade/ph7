"""JS Lib."""

from ._mock import _ApiMock
from .api import console, fetch, setInterval, setTimeout

document = _ApiMock("document")
alert = _ApiMock("alert")


__all__ = (
    "document",
    "fetch",
    "console",
    "alert",
    "fetch",
    "setInterval",
    "setTimeout",
)
