"""Web APIs"""

import typing as t
from io import BytesIO

from typing_extensions import NotRequired, Protocol, TypedDict

# pylint: disable=unused-argument,multiple-statements,missing-function-docstring,missing-class-docstring,redefined-builtin,too-many-lines,too-many-public-methods
# mypy: disable-error-code="empty-body"

ReadableStream = t.IO


string = str
number = int


class Blob(Protocol):
    size: int
    type: str

    async def arrayBuffer(self) -> bytes:
        ...

    def slice(
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
    def __iter__(self) -> t.Iterator[t.Tuple[str, FormDataEntryValue]]:
        ...

    def entries(self) -> t.Iterable[t.Tuple[str, FormDataEntryValue]]:
        ...

    def keys(self) -> t.Iterable[str]:
        ...

    def values(self) -> t.Iterable[FormDataEntryValue]:
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

    def clone(self) -> "Response":
        ...


Request = str

Method = t.Literal["GET", "POST", "DELETE", "PATCH", "OPTIONS", "HEADER"]


class RequestInit(TypedDict):
    body: NotRequired[t.Union[None, str, bytes, bytearray]]
    cache: NotRequired[str]
    credentials: NotRequired[str]
    headers: NotRequired[t.Union[None, dict, t.List]]
    integrity: NotRequired[str]
    keepalive: NotRequired[bool]
    method: NotRequired[Method]
    mode: NotRequired[str]
    redirect: NotRequired[str]
    referrer: NotRequired[str]
    referrerPolicy: NotRequired[str]
    signal: NotRequired[t.Union[None, object]]
    window: NotRequired[t.Union[None, object]]


class Console:
    def assert_(self, condition, *data: t.Any) -> None:
        ...

    def clear(self) -> None:
        ...

    def count(self, label: str = "") -> None:
        ...

    def countReset(self, label: str = "") -> None:
        ...

    def debug(self, *data: t.Any) -> None:
        ...

    def dir(self, item, options=None) -> None:
        ...

    def dirxml(self, *data: t.Any) -> None:
        ...

    def error(self, *data: t.Any) -> None:
        ...

    def group(self, *data: t.Any) -> None:
        ...

    def groupCollapsed(self, *data: t.Any) -> None:
        ...

    def groupEnd(self) -> None:
        ...

    def info(self, *data: t.Any) -> None:
        ...

    def log(self, *data: t.Any) -> None:
        ...

    def table(self, tabularData, properties=None) -> None:
        ...

    def time(self, label: str = "") -> None:
        ...

    def timeEnd(self, label: str = "") -> None:
        ...

    def timeLog(self, *data: t.Any, label: str = "") -> None:
        ...

    def timeStamp(self, label: str = "") -> None:
        ...

    def trace(self, *data: t.Any) -> None:
        ...

    def warn(self, *data: t.Any) -> None:
        ...


class Attr:
    pass


class DOMTokenList:
    length: int
    value: str

    def add(self, *tokens: str) -> None:
        ...

    def contains(self, token: str) -> bool:
        ...

    def item(self, index: int) -> t.Optional[str]:
        ...

    def remove(self, *tokens: str) -> None:
        ...

    def replace(self, token: str, new_token: str) -> bool:
        ...

    def supports(self, token: str) -> bool:
        ...

    def toggle(self, token: str, force: t.Optional[bool] = None) -> bool:
        ...

    def forEach(
        self,
        callbackfn: t.Callable[[str, int, "DOMTokenList"], None],
        this_arg: t.Optional[object] = None,
    ) -> None:
        ...

    def __getitem__(self, index: int) -> str:
        ...


class NamedNodeMap:
    length: int
    attributes: t.List[Attr]


class ShadowRoot:
    ...


class StylePropertyMapReadOnly:
    ...


class DOMRect:
    ...


class DOMRectList:
    ...


HTMLCollectionOf = t.List


class Element:
    attributes: NamedNodeMap
    classList: DOMTokenList
    className: str
    clientHeight: int
    clientLeft: int
    clientTop: int
    clientWidth: int
    id: str
    localName: str
    namespaceURI: t.Optional[str]
    onfullscreenchange: t.Optional[t.Callable]
    onfullscreenerror: t.Optional[t.Callable]
    outerHTML: str
    ownerDocument: "Document"
    part: DOMTokenList
    prefix: t.Optional[str]
    scrollHeight: int
    scrollLeft: int
    scrollTop: int
    scrollWidth: int
    shadowRoot: t.Optional[ShadowRoot]
    slot: str
    tagName: str

    def attachShadow(self, init: dict) -> ShadowRoot:
        ...

    def checkVisibility(self, options: t.Optional[dict] = None) -> bool:
        ...

    def closest(self, selectors: str) -> t.Union["Element", None]:
        ...

    def computedStyleMap(self) -> StylePropertyMapReadOnly:
        ...

    def getAttribute(self, qualifiedName: str) -> t.Optional[str]:
        ...

    def getAttributeNS(
        self, namespace: t.Optional[str], localName: str
    ) -> t.Optional[str]:
        ...

    def getAttributeNames(self) -> t.List[str]:
        ...

    def getAttributeNode(self, qualifiedName: str) -> t.Optional["Attr"]:
        ...

    def getAttributeNodeNS(
        self, namespace: t.Optional[str], localName: str
    ) -> t.Optional["Attr"]:
        ...

    def getBoundingClientRect(self) -> DOMRect:
        ...

    def getClientRects(self) -> DOMRectList:
        ...

    def getElementsByClassName(self, classNames: str) -> HTMLCollectionOf["Element"]:
        ...

    def getElementsByTagName(
        self, qualifiedName: str
    ) -> HTMLCollectionOf["HTMLElement"]:
        ...

    def hasAttribute(self, qualifiedName: str) -> bool:
        ...

    def hasAttributeNS(self, namespace: t.Optional[str], localName: str) -> bool:
        ...

    def hasAttributes(self) -> bool:
        ...

    def hasPointerCapture(self, pointerId: int) -> bool:
        ...

    def insertAdjacentElement(
        self, where: str, element: "Element"
    ) -> t.Union["Element", None]:
        ...

    def insertAdjacentHTML(self, position: str, text: str) -> None:
        ...

    def insertAdjacentText(self, where: str, data: str) -> None:
        ...

    def matches(self, selectors: str) -> bool:
        ...

    def releasePointerCapture(self, pointerId: int) -> None:
        ...

    def removeAttribute(self, qualifiedName: str) -> None:
        ...

    def removeAttributeNS(self, namespace: t.Optional[str], localName: str) -> None:
        ...

    def removeAttributeNode(self, attr: "Attr") -> "Attr":
        ...

    def requestFullscreen(
        self, options: t.Optional[dict] = None
    ) -> t.Coroutine[None, None, None]:
        ...

    def requestPointerLock(self) -> None:
        ...

    def scroll(
        self,
        options: t.Optional[dict] = None,
        x: t.Optional[int] = None,
        y: t.Optional[int] = None,
    ) -> None:
        ...

    def scrollBy(
        self,
        options: t.Optional[dict] = None,
        x: t.Optional[int] = None,
        y: t.Optional[int] = None,
    ) -> None:
        ...

    def scrollIntoView(self, arg: t.Optional[t.Union[bool, dict]] = None) -> None:
        ...

    def scrollTo(
        self,
        options: t.Optional[dict] = None,
        x: t.Optional[int] = None,
        y: t.Optional[int] = None,
    ) -> None:
        ...

    def setAttribute(self, qualifiedName: str, value: str) -> None:
        ...

    def setAttributeNS(
        self, namespace: t.Optional[str], qualifiedName: str, value: str
    ) -> None:
        ...

    def setAttributeNode(self, attr: "Attr") -> t.Optional["Attr"]:
        ...

    def setAttributeNodeNS(self, attr: "Attr") -> t.Optional["Attr"]:
        ...

    def setPointerCapture(self, pointerId: int) -> None:
        ...

    def toggleAttribute(
        self, qualifiedName: str, force: t.Optional[bool] = None
    ) -> bool:
        ...

    def webkitMatchesSelector(self, selectors: str) -> bool:
        ...

    def addEventListener(
        self,
        type: str,
        listener: t.Callable,
        options: t.Optional[t.Union[bool, dict]] = None,
    ) -> None:
        ...

    def removeEventListener(
        self,
        type: str,
        listener: t.Callable,
        options: t.Optional[t.Union[bool, dict]] = None,
    ) -> None:
        ...


class ElementCSSInlineStyle:
    ...


class ElementContentEditable:
    ...


class GlobalEventHandlers:
    ...


class HTMLOrSVGElement:
    ...


class ElementInternals:
    ...


class Node:
    ...


class DocumentOrShadowRoot:
    ...


class FontFaceSource:
    ...


class NonElementParentNode:
    ...


class ParentNode:
    ...


class XPathEvaluatorBase:
    ...


class HTMLAllCollection:
    ...


class HTMLAnchorElement:
    ...


class HTMLEmbedElement:
    ...


class HTMLFormElement:
    ...


class HTMLHeadElement:
    ...


class HTMLImageElement:
    ...


class HTMLScriptElement:
    ...


class Location:
    ...


class DocumentType:
    ...


class DOMImplementation:
    ...


class DocumentTimeline:
    ...


class AnimationEvent:
    ...


class AnimationPlaybackEvent:
    ...


class AudioProcessingEvent:
    ...


class BeforeUnloadEvent:
    ...


class BlobEvent:
    ...


class ClipboardEvent:
    ...


class CloseEvent:
    ...


class CompositionEvent:
    ...


class CustomEvent:
    ...


class DeviceMotionEvent:
    ...


class DeviceOrientationEvent:
    ...


class DragEvent:
    ...


class ErrorEvent:
    ...


class Event:
    ...


class Events:
    ...


class FocusEvent:
    ...


class FontFaceSetLoadEvent:
    ...


class FormDataEvent:
    ...


class GamepadEvent:
    ...


class HashChangeEvent:
    ...


class IDBVersionChangeEvent:
    ...


class InputEvent:
    ...


class KeyboardEvent:
    ...


class MIDIConnectionEvent:
    ...


class MIDIMessageEvent:
    ...


class MediaEncryptedEvent:
    ...


class MediaKeyMessageEvent:
    ...


class MediaQueryListEvent:
    ...


class MediaStreamTrackEvent:
    ...


class MessageEvent:
    ...


class MouseEvent:
    ...


class MouseEvents:
    ...


class MutationEvent:
    ...


class MutationEvents:
    ...


class OfflineAudioCompletionEvent:
    ...


class PageTransitionEvent:
    ...


class PaymentMethodChangeEvent:
    ...


class PaymentRequestUpdateEvent:
    ...


class PictureInPictureEvent:
    ...


class PointerEvent:
    ...


class PopStateEvent:
    ...


class ProgressEvent:
    ...


class PromiseRejectionEvent:
    ...


class RTCDTMFToneChangeEvent:
    ...


class RTCDataChannelEvent:
    ...


class RTCErrorEvent:
    ...


class RTCPeerConnectionIceErrorEvent:
    ...


class RTCPeerConnectionIceEvent:
    ...


class RTCTrackEvent:
    ...


class SecurityPolicyViolationEvent:
    ...


class SpeechSynthesisErrorEvent:
    ...


class SpeechSynthesisEvent:
    ...


class StorageEvent:
    ...


class SubmitEvent:
    ...


class ToggleEvent:
    ...


class TouchEvent:
    ...


class TrackEvent:
    ...


class TransitionEvent:
    ...


class UIEvent:
    ...


class UIEvents:
    ...


class WebGLContextEvent:
    ...


class WheelEvent:
    ...


class Range:
    ...


class TreeWalker:
    ...


class NodeIterator:
    ...


class ProcessingInstruction:
    ...


class Comment:
    ...


class DocumentFragment:
    ...


class Text:
    ...


class CDATASection:
    ...


class Selection:
    ...


class WindowProxy:
    ...


class HTMLAreaElement:
    ...


class SVGSVGElement:
    ...


class NodeFilter:
    ...


class ElementCreationOptions:
    ...


class SVGElement:
    ...


class MathMLElement:
    ...


class PopoverInvokerElement:
    ...


class AutoFill:
    ...


class FileList:
    ...


class HTMLLabelElement:
    ...


class HTMLDataListElement:
    ...


class ValidityState:
    ...


class FileSystemEntry:
    ...


class SelectionMode:
    ...


class Date:
    ...


class HTMLInputElement(PopoverInvokerElement):
    accept: str
    align: str
    alt: str
    autocomplete: AutoFill
    capture: str
    checked: bool
    defaultChecked: bool
    defaultValue: str
    dirName: str
    disabled: bool
    files: t.Union[FileList, None]
    form: t.Union[HTMLFormElement, None]
    formAction: str
    formEnctype: str
    formMethod: str
    formNoValidate: bool
    formTarget: str
    height: int
    indeterminate: bool
    labels: t.Union[t.List[HTMLLabelElement], None]
    list: t.Union[HTMLDataListElement, None]
    max: str
    maxLength: int
    min: str
    minLength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    readOnly: bool
    required: bool
    selectionDirection: t.Union[str, None]
    selectionEnd: t.Union[int, None]
    selectionStart: t.Union[int, None]
    size: int
    src: str
    step: str
    type: str
    useMap: str
    validationMessage: str
    validity: ValidityState
    value: str
    valueAsDate: t.Union[Date, None]
    valueAsNumber: int
    webkitEntries: t.List[FileSystemEntry]
    webkitdirectory: bool
    width: int
    willValidate: bool

    def checkValidity(self) -> bool:
        ...

    def reportValidity(self) -> bool:
        ...

    def select(self) -> None:
        ...

    def setCustomValidity(self, error: str) -> None:
        ...

    def setRangeText(
        self,
        replacement: str,
        start: t.Optional[int] = None,
        end: t.Optional[int] = None,
        selectionMode: t.Optional[SelectionMode] = None,
    ) -> None:
        ...

    def setSelectionRange(
        self,
        start: t.Optional[int] = None,
        end: t.Optional[int] = None,
        direction: t.Optional[str] = None,
    ) -> None:
        ...

    def showPicker(self) -> None:
        ...

    def stepDown(self, n: t.Optional[int] = None) -> None:
        ...

    def stepUp(self, n: t.Optional[int] = None) -> None:
        ...

    def addEventListener(
        self,
        type: str,
        listener: t.Callable,
        options: t.Optional[t.Union[bool, dict]] = None,
    ) -> None:
        ...

    def removeEventListener(
        self,
        type: str,
        listener: t.Callable,
        options: t.Optional[t.Union[bool, dict]] = None,
    ) -> None:
        ...


class HTMLElement(
    Element,
    ElementCSSInlineStyle,
    ElementContentEditable,
    GlobalEventHandlers,
    HTMLOrSVGElement,
    HTMLInputElement,
):
    accessKey: str
    accessKeyLabel: str
    autocapitalize: str
    dir: str
    draggable: bool
    hidden: bool
    inert: bool
    innerText: str
    lang: str
    offsetHeight: int
    offsetLeft: int
    offsetParent: t.Optional[Element]
    offsetTop: int
    offsetWidth: int
    outerText: str
    popover: t.Optional[str]
    spellcheck: bool
    title: str
    translate: bool

    def attachInternals(self) -> "ElementInternals":
        ...

    def click(self) -> None:
        ...

    def hidePopover(self) -> None:
        ...

    def showPopover(self) -> None:
        ...

    def togglePopover(self, force: t.Optional[bool] = None) -> None:
        ...

    def addEventListener(
        self,
        type: str,
        listener: t.Callable,
        options: t.Optional[t.Union[bool, dict]] = None,
    ) -> None:
        ...

    def removeEventListener(
        self,
        type: str,
        listener: t.Callable,
        options: t.Optional[t.Union[bool, dict]] = None,
    ) -> None:
        ...


class Document(Element):
    URL: str
    alinkColor: str
    all: HTMLAllCollection
    anchors: t.List[HTMLAnchorElement]
    applets: t.List[HTMLElement]
    bgColor: str
    body: HTMLElement
    characterSet: str
    charset: str
    compatMode: str
    contentType: str
    cookie: str
    currentScript: t.Optional[HTMLOrSVGElement]
    defaultView: t.Optional[WindowProxy]
    designMode: str
    dir: str
    doctype: t.Optional[t.Union[DocumentType, None]]
    documentElement: HTMLElement
    documentURI: str
    domain: str
    embeds: t.List[HTMLEmbedElement]
    fgColor: str
    forms: t.List[HTMLFormElement]
    fullscreen: bool
    fullscreenEnabled: bool
    head: HTMLHeadElement
    hidden: bool
    images: t.List[HTMLImageElement]
    implementation: DOMImplementation
    inputEncoding: str
    lastModified: str
    linkColor: str
    links: t.List[t.Union[HTMLAnchorElement, HTMLAreaElement]]
    location: Location
    onfullscreenchange: t.Optional[t.Callable]
    onfullscreenerror: t.Optional[t.Callable]
    onpointerlockchange: t.Optional[t.Callable]
    onpointerlockerror: t.Optional[t.Callable]
    onreadystatechange: t.Optional[t.Callable]
    onvisibilitychange: t.Optional[t.Callable]
    ownerDocument: "Document"
    pictureInPictureEnabled: bool
    plugins: t.List[HTMLEmbedElement]
    readyState: str
    referrer: str
    rootElement: t.Optional[t.Union[SVGSVGElement, None]]
    scripts: t.List[HTMLScriptElement]
    scrollingElement: t.Optional[t.Union[Element, None]]
    timeline: DocumentTimeline
    title: str
    visibilityState: str
    vlinkColor: str

    def adoptNode(self, node: Node) -> Node:
        ...

    def captureEvents(self) -> None:
        ...

    def caretRangeFromPoint(self, x: int, y: int) -> t.Optional[Range]:
        ...

    def clear(self) -> None:
        ...

    def close(self) -> None:
        ...

    def createAttribute(self, localName: str) -> Attr:
        ...

    def createAttributeNS(self, namespace: t.Optional[str], qualifiedName: str) -> Attr:
        ...

    def createCDATASection(self, data: str) -> CDATASection:
        ...

    def createComment(self, data: str) -> Comment:
        ...

    def createDocumentFragment(self) -> DocumentFragment:
        ...

    def createElement(
        self,
        tagName: str,
        options: t.Optional[ElementCreationOptions] = None,
    ) -> t.Union[HTMLElement, type]:
        ...

    def createElementNS(
        self,
        namespaceURI: t.Optional[str],
        qualifiedName: str,
        options: t.Optional[t.Union[str, ElementCreationOptions]] = None,
    ) -> Element:
        ...

    def createEvent(
        self, eventInterface: str
    ) -> t.Union[AnimationEvent, AnimationPlaybackEvent]:
        ...

    def createNodeIterator(
        self,
        root: Node,
        whatToShow: t.Optional[int] = None,
        filter: t.Optional[t.Union[NodeFilter, None]] = None,
    ) -> NodeIterator:
        ...

    def createProcessingInstruction(
        self, target: str, data: str
    ) -> ProcessingInstruction:
        ...

    def createRange(self) -> Range:
        ...

    def createTextNode(self, data: str) -> Text:
        ...

    def createTreeWalker(
        self,
        root: Node,
        whatToShow: t.Optional[int] = None,
        filter: t.Optional[t.Union[NodeFilter, None]] = None,
    ) -> TreeWalker:
        ...

    def execCommand(
        self,
        commandId: str,
        showUI: t.Optional[bool] = None,
        value: t.Optional[str] = None,
    ) -> bool:
        ...

    def exitFullscreen(self) -> t.Coroutine[None, None, None]:
        ...

    def exitPictureInPicture(self) -> t.Coroutine[None, None, None]:
        ...

    def exitPointerLock(self) -> None:
        ...

    def getElementById(self, elementId: str) -> HTMLElement:
        ...

    def getElementsByClassName(self, classNames: str) -> t.List[Element]:
        ...

    def getElementsByName(self, elementName: str) -> t.List[HTMLElement]:
        ...

    def getElementsByTagName(self, qualifiedName: str) -> t.List[HTMLElement]:
        ...

    def getElementsByTagNameNS(
        self, namespaceURI: t.Optional[str], localName: str
    ) -> t.List[t.Union[HTMLElement, SVGElement, MathMLElement, Element]]:
        ...

    def getSelection(self) -> t.Optional[Selection]:
        ...

    def hasFocus(self) -> bool:
        ...

    def hasStorageAccess(self) -> t.Coroutine[None, None, bool]:
        ...

    def importNode(self, node: Node, deep: t.Optional[bool] = None) -> Node:
        ...

    def open(self, *text: str) -> None:
        ...

    def queryCommandEnabled(self, commandId: str) -> bool:
        ...

    def queryCommandIndeterm(self, commandId: str) -> bool:
        ...

    def queryCommandState(self, commandId: str) -> bool:
        ...

    def queryCommandSupported(self, commandId: str) -> bool:
        ...

    def queryCommandValue(self, commandId: str) -> str:
        ...

    def releaseEvents(self) -> None:
        ...

    def requestStorageAccess(self) -> t.Coroutine[None, None, None]:
        ...

    def write(self, *text: str) -> None:
        ...

    def writeln(self, *text: str) -> None:
        ...

    def addEventListener(
        self,
        type: str,
        listener: t.Callable,
        options: t.Optional[t.Union[bool, dict]] = None,
    ) -> None:
        ...

    def removeEventListener(
        self,
        type: str,
        listener: t.Callable,
        options: t.Optional[t.Union[bool, dict]] = None,
    ) -> None:
        ...


class JSON:
    @staticmethod
    def parse(text: str, reviver=None) -> t.Dict:
        ...

    @staticmethod
    def strify(
        value: t.Dict,
        replacer: t.Optional[str] = None,
        space: t.Optional[str] = None,
    ) -> str:
        ...


async def fetch(url: Request, init: RequestInit) -> Response:
    ...


def setInterval(handler: t.Callable, timeout: int, *args: t.List[t.Any]) -> int:
    ...


def setTimeout(handler: t.Callable, timeout: int, *args: t.List[t.Any]) -> int:
    ...


console = Console()

document = Document()
