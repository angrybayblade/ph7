"""Web APIs"""

import typing as t
from io import BytesIO

from typing_extensions import NotRequired, Protocol, TypedDict

# pylint: disable=missing-function-docstring,missing-class-docstring,unused-argument

ReadableStream = t.IO


class Blob(Protocol):
    size: int
    type: str

    async def arrayBuffer(self) -> bytes:
        ...

    def slice(  # type: ignore
        self,
        start: t.Optional[int] = None,
        end: t.Optional[int] = None,
        content_type: t.Optional[str] = None,
    ) -> "Blob":
        ...

    async def stream(self) -> "ReadableStream":
        ...

    async def text(self) -> str:
        ...


class FormDataEntryValue(Protocol):
    pass


class FormData(Protocol):
    def __iter__(self) -> t.Iterator[t.Tuple[str, FormDataEntryValue]]:  # type: ignore
        ...

    def entries(self) -> t.Iterable[t.Tuple[str, FormDataEntryValue]]:  # type: ignore
        ...

    def keys(self) -> t.Iterable[str]:  # type: ignore
        ...

    def values(self) -> t.Iterable[FormDataEntryValue]:  # type: ignore
        ...


class Body(Protocol):
    body: t.Union[None, BytesIO]
    bodyUsed: bool

    async def arrayBuffer(self) -> bytes:
        ...

    async def blob(self) -> "Blob":
        ...

    async def formData(self) -> "FormData":
        ...

    async def json(self) -> t.Any:
        ...

    async def text(self) -> str:
        ...


class Response(Body):
    headers: dict
    ok: bool
    redirected: bool
    status: int
    statusText: str
    type: str
    url: str

    def clone(self) -> "Response":  # type: ignore
        ...


Request = str

Method = t.Literal["GET", "POST", "DELETE", "PATCH", "OPTIONS", "HEADER"]


class RequestInit(TypedDict):
    body: NotRequired[t.Union[None, str, bytes, bytearray]]
    cache: NotRequired[str]
    credentials: NotRequired[str]
    headers: NotRequired[t.Union[None, dict, list]]
    integrity: NotRequired[str]
    keepalive: NotRequired[bool]
    method: NotRequired[Method]
    mode: NotRequired[str]
    redirect: NotRequired[str]
    referrer: NotRequired[str]
    referrerPolicy: NotRequired[str]
    signal: NotRequired[t.Union[None, object]]
    window: NotRequired[t.Union[None, object]]


async def fetch(url: Request, init: RequestInit) -> Response:  # type: ignore
    ...


def setInterval(handler: t.Callable, timeout: int, *args: t.List[t.Any]) -> int:  # type: ignore
    ...


def setTimeout(handler: t.Callable, timeout: int, *args: t.List[t.Any]) -> int:  # type: ignore
    ...


class Console:
    def assert_(self, condition, *data: t.Any) -> None:  # type: ignore
        ...

    def clear(self) -> None:  # type: ignore
        ...

    def count(self, label: str = "") -> None:  # type: ignore
        ...

    def countReset(self, label: str = "") -> None:  # type: ignore
        ...

    def debug(self, *data: t.Any) -> None:  # type: ignore
        ...

    def dir(self, item, options=None) -> None:  # type: ignore
        ...

    def dirxml(self, *data: t.Any) -> None:  # type: ignore
        ...

    def error(self, *data: t.Any) -> None:  # type: ignore
        ...

    def group(self, *data: t.Any) -> None:  # type: ignore
        ...

    def groupCollapsed(self, *data: t.Any) -> None:  # type: ignore
        ...

    def groupEnd(self) -> None:  # type: ignore
        ...

    def info(self, *data: t.Any) -> None:  # type: ignore
        ...

    def log(self, *data: t.Any) -> None:  # type: ignore
        ...

    def table(self, tabularData, properties=None) -> None:  # type: ignore
        ...

    def time(self, label: str = "") -> None:  # type: ignore
        ...

    def timeEnd(self, label: str = "") -> None:  # type: ignore
        ...

    def timeLog(self, *data: t.Any, label: str = "") -> None:  # type: ignore
        ...

    def timeStamp(self, label: str = "") -> None:  # type: ignore
        ...

    def trace(self, *data: t.Any) -> None:  # type: ignore
        ...

    def warn(self, *data: t.Any) -> None:  # type: ignore
        ...


console = Console()
