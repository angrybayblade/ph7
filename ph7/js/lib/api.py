"""Web APIs"""

import typing as t
from io import BytesIO

from typing_extensions import NotRequired, Protocol, TypedDict, Union

ReadableStream = t.IO


class Blob(Protocol):
    size: int
    type: str

    async def arrayBuffer(self) -> bytes: ...

    def slice(
        self,
        start: t.Optional[int] = None,
        end: t.Optional[int] = None,
        content_type: t.Optional[str] = None,
    ) -> "Blob": ...

    async def stream(self) -> "ReadableStream": ...

    async def text(self) -> str: ...


class FormDataEntryValue(Protocol):
    pass


class FormData(Protocol):
    def __iter__(self) -> t.Iterator[t.Tuple[str, FormDataEntryValue]]: ...

    def entries(self) -> t.Iterable[t.Tuple[str, FormDataEntryValue]]: ...

    def keys(self) -> t.Iterable[str]: ...

    def values(self) -> t.Iterable[FormDataEntryValue]: ...


class Body(Protocol):
    body: Union[None, BytesIO]
    bodyUsed: bool

    async def arrayBuffer(self) -> bytes: ...

    async def blob(self) -> "Blob": ...

    async def formData(self) -> "FormData": ...

    async def json(self) -> t.Any: ...

    async def text(self) -> str: ...


class Response(Body):
    headers: dict
    ok: bool
    redirected: bool
    status: int
    statusText: str
    type: str
    url: str

    def clone(self) -> "Response": ...


Request = str

Method = t.Literal["GET", "POST", "DELETE", "PATCH", "OPTIONS", "HEADER"]


class RequestInit(TypedDict):
    body: Union[None, str, bytes, bytearray]
    cache: NotRequired[str]
    credentials: NotRequired[str]
    headers: Union[None, dict, list]
    integrity: NotRequired[str]
    keepalive: NotRequired[bool]
    method: NotRequired[Method]
    mode: NotRequired[str]
    redirect: NotRequired[str]
    referrer: NotRequired[str]
    referrerPolicy: NotRequired[str]
    signal: Union[None, object]
    window: Union[None, object]


async def fetch(url: Request, init: RequestInit) -> Response: ...


def setInterval(handler: t.Callable, timeout: int, *args: t.List[t.Any]) -> int: ...


def setTimeout(handler: t.Callable, timeout: int, *args: t.List[t.Any]) -> int: ...


class Console:
    def assert_(self, condition, *data: t.Any) -> None: ...

    def clear(self) -> None: ...

    def count(self, label: str = "") -> None: ...

    def countReset(self, label: str = "") -> None: ...

    def debug(self, *data: t.Any) -> None: ...

    def dir(self, item, options=None) -> None: ...

    def dirxml(self, *data: t.Any) -> None: ...

    def error(self, *data: t.Any) -> None: ...

    def group(self, *data: t.Any) -> None: ...

    def groupCollapsed(self, *data: t.Any) -> None: ...

    def groupEnd(self) -> None: ...

    def info(self, *data: t.Any) -> None: ...

    def log(self, *data: t.Any) -> None: ...

    def table(self, tabularData, properties=None) -> None: ...

    def time(self, label: str = "") -> None: ...

    def timeEnd(self, label: str = "") -> None: ...

    def timeLog(self, label: str = "", *data: t.Any) -> None: ...

    def timeStamp(self, label: str = "") -> None: ...

    def trace(self, *data: t.Any) -> None: ...

    def warn(self, *data: t.Any) -> None: ...


console = Console()
