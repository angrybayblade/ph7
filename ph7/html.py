"""
This file is auto generated using scripts/render/html.py
"""

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals

import typing as t

from typing_extensions import Literal

from ph7.base import ChildType, node
from ph7.base import unpack as _unpack
from ph7.css import CSSObject
from ph7.formatters import cformat
from ph7.js import Events as DOMEvents
from ph7.style import Style


def a(
    *children: ChildType,
    href: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    tabindex: t.Optional[str] = None,
    rel: t.Optional[
        Literal[
            "nofollow",
            "noopener",
            "noreferrer",
            "external",
            "author",
            "help",
            "license",
            "prev",
            "next",
            "bookmark",
            "search",
            "alternate",
            "tag",
        ]
    ] = None,
    target: t.Optional[
        Literal["_blank", "_self", "_parent", "_top", "framename"]
    ] = None,
    type: t.Optional[str] = None,
    hreflang: t.Optional[str] = None,
    media: t.Optional[str] = None,
    ping: t.Optional[str] = None,
    download: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """A node."""
    return node(
        *children,
        attributes={
            "href": href,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "tabindex": tabindex,
            "rel": rel,
            "target": target,
            "type": type,
            "hreflang": hreflang,
            "media": media,
            "ping": ping,
            "download": download,
        },
        style=style,
        on=on,
        name="a",
        content_allowed=True,
    )


def abbr(
    *children: ChildType,
    title: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Abbr node."""
    return node(
        *children,
        attributes={
            "title": title,
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="abbr",
        content_allowed=True,
    )


def address(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Address node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="address",
        content_allowed=True,
    )


def area(
    *children: ChildType,
    shape: t.Optional[str] = None,
    coords: t.Optional[str] = None,
    href: t.Optional[str] = None,
    target: t.Optional[
        Literal["_blank", "_self", "_parent", "_top", "framename"]
    ] = None,
    id: t.Optional[str] = None,
    tabindex: t.Optional[str] = None,
    alt: t.Optional[str] = None,
    rel: t.Optional[
        Literal[
            "nofollow",
            "noopener",
            "noreferrer",
            "external",
            "author",
            "help",
            "license",
            "prev",
            "next",
            "bookmark",
            "search",
            "alternate",
            "tag",
        ]
    ] = None,
    hreflang: t.Optional[str] = None,
    type: t.Optional[str] = None,
    media: t.Optional[str] = None,
    download: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Area node."""
    return node(
        *children,
        attributes={
            "shape": shape,
            "coords": coords,
            "href": href,
            "target": target,
            "id": id,
            "tabindex": tabindex,
            "alt": alt,
            "rel": rel,
            "hreflang": hreflang,
            "type": type,
            "media": media,
            "download": download,
        },
        style=style,
        on=on,
        name="area",
        content_allowed=True,
    )


def article(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Article node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="article",
        content_allowed=True,
    )


def aside(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Aside node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="aside",
        content_allowed=True,
    )


def audio(
    *children: ChildType,
    controls: t.Optional[str] = None,
    src: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    autoplay: t.Optional[str] = None,
    loop: t.Optional[str] = None,
    muted: t.Optional[str] = None,
    preload: t.Optional[str] = None,
    crossorigin: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Audio node."""
    return node(
        *children,
        attributes={
            "controls": controls,
            "src": src,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "autoplay": autoplay,
            "loop": loop,
            "muted": muted,
            "preload": preload,
            "crossorigin": crossorigin,
        },
        style=style,
        on=on,
        name="audio",
        content_allowed=True,
    )


def b(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """B node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="b",
        content_allowed=True,
    )


def base(
    *children: ChildType,
    href: t.Optional[str] = None,
    id: t.Optional[str] = None,
    target: t.Optional[
        Literal["_blank", "_self", "_parent", "_top", "framename"]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Base node."""
    return node(
        *children,
        attributes={
            "href": href,
            "id": id,
            "target": target,
        },
        style=style,
        on=on,
        name="base",
        content_allowed=True,
    )


def blockquote(
    *children: ChildType,
    cite: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Blockquote node."""
    return node(
        *children,
        attributes={
            "cite": cite,
            "id": id,
            "class": cformat(class_name),
            "title": title,
        },
        style=style,
        on=on,
        name="blockquote",
        content_allowed=True,
    )


def body(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Body node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="body",
        content_allowed=True,
    )


def br(
    *children: ChildType,
    clear: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Br node."""
    return node(
        *children,
        attributes={
            "clear": clear,
        },
        style=style,
        on=on,
        name="br",
        content_allowed=False,
    )


def button(
    *children: ChildType,
    type: t.Optional[Literal["button", "submit", "reset"]] = None,
    name: t.Optional[str] = None,
    value: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    tabindex: t.Optional[str] = None,
    disabled: t.Optional[str] = None,
    form: t.Optional[str] = None,
    formaction: t.Optional[str] = None,
    formenctype: t.Optional[str] = None,
    formmethod: t.Optional[Literal["get", "post"]] = None,
    formnovalidate: t.Optional[str] = None,
    formtarget: t.Optional[
        Literal["_blank", "_self", "_parent", "_top", "framename"]
    ] = None,
    autofocus: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Button node."""
    return node(
        *children,
        attributes={
            "type": type,
            "name": name,
            "value": value,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "tabindex": tabindex,
            "disabled": disabled,
            "form": form,
            "formaction": formaction,
            "formenctype": formenctype,
            "formmethod": formmethod,
            "formnovalidate": formnovalidate,
            "formtarget": formtarget,
            "autofocus": autofocus,
        },
        style=style,
        on=on,
        name="button",
        content_allowed=True,
    )


def canvas(
    *children: ChildType,
    height: t.Optional[str] = None,
    width: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Canvas node."""
    return node(
        *children,
        attributes={
            "height": height,
            "width": width,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="canvas",
        content_allowed=True,
    )


def caption(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Caption node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="caption",
        content_allowed=True,
    )


def cite(
    *children: ChildType,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Cite node."""
    return node(
        *children, attributes={}, style=style, on=on, name="cite", content_allowed=True
    )


def code(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Code node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="code",
        content_allowed=True,
    )


def col(
    *children: ChildType,
    span: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Col node."""
    return node(
        *children,
        attributes={
            "span": span,
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="col",
        content_allowed=True,
    )


def colgroup(
    *children: ChildType,
    span: t.Optional[str] = None,
    id: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Colgroup node."""
    return node(
        *children,
        attributes={
            "span": span,
            "id": id,
        },
        style=style,
        on=on,
        name="colgroup",
        content_allowed=True,
    )


def data(
    *children: ChildType,
    value: t.Optional[str] = None,
    id: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Data node."""
    return node(
        *children,
        attributes={
            "value": value,
            "id": id,
        },
        style=style,
        on=on,
        name="data",
        content_allowed=True,
    )


def datalist(
    *children: ChildType,
    id: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Datalist node."""
    return node(
        *children,
        attributes={
            "id": id,
        },
        style=style,
        on=on,
        name="datalist",
        content_allowed=True,
    )


def dd(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Dd node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="dd",
        content_allowed=True,
    )


def details(
    *children: ChildType,
    open: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Details node."""
    return node(
        *children,
        attributes={
            "open": open,
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="details",
        content_allowed=True,
    )


def div(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Div node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="div",
        content_allowed=True,
    )


def dl(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Dl node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="dl",
        content_allowed=True,
    )


def dt(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Dt node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="dt",
        content_allowed=True,
    )


def em(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Em node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="em",
        content_allowed=True,
    )


def embed(
    *children: ChildType,
    height: t.Optional[str] = None,
    width: t.Optional[str] = None,
    src: t.Optional[str] = None,
    type: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Embed node."""
    return node(
        *children,
        attributes={
            "height": height,
            "width": width,
            "src": src,
            "type": type,
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="embed",
        content_allowed=True,
    )


def fieldset(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    form: t.Optional[str] = None,
    name: t.Optional[str] = None,
    disabled: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Fieldset node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "form": form,
            "name": name,
            "disabled": disabled,
        },
        style=style,
        on=on,
        name="fieldset",
        content_allowed=True,
    )


def figcaption(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Figcaption node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="figcaption",
        content_allowed=True,
    )


def figure(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Figure node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="figure",
        content_allowed=True,
    )


def footer(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Footer node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="footer",
        content_allowed=True,
    )


def form(
    *children: ChildType,
    action: t.Optional[str] = None,
    method: t.Optional[str] = None,
    id: t.Optional[str] = None,
    enctype: t.Optional[str] = None,
    target: t.Optional[
        Literal["_blank", "_self", "_parent", "_top", "framename"]
    ] = None,
    autocomplete: t.Optional[str] = None,
    novalidate: t.Optional[str] = None,
    accept_charset: t.Optional[str] = None,
    rel: t.Optional[
        Literal[
            "nofollow",
            "noopener",
            "noreferrer",
            "external",
            "author",
            "help",
            "license",
            "next",
            "bookmark",
            "search",
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Form node."""
    return node(
        *children,
        attributes={
            "action": action,
            "method": method,
            "id": id,
            "enctype": enctype,
            "target": target,
            "autocomplete": autocomplete,
            "novalidate": novalidate,
            "accept-charset": accept_charset,
            "rel": rel,
        },
        style=style,
        on=on,
        name="form",
        content_allowed=True,
    )


def h1(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """H1 node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="h1",
        content_allowed=True,
    )


def h2(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """H2 node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="h2",
        content_allowed=True,
    )


def h3(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """H3 node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="h3",
        content_allowed=True,
    )


def h4(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """H4 node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="h4",
        content_allowed=True,
    )


def h5(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """H5 node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="h5",
        content_allowed=True,
    )


def h6(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """H6 node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="h6",
        content_allowed=True,
    )


def head(
    *children: ChildType,
    profile: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Head node."""
    return node(
        *children,
        attributes={
            "profile": profile,
        },
        style=style,
        on=on,
        name="head",
        content_allowed=True,
    )


def header(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Header node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="header",
        content_allowed=True,
    )


def hr(
    *children: ChildType,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Hr node."""
    return node(
        *children,
        attributes={
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="hr",
        content_allowed=False,
    )


def html(
    *children: ChildType,
    xmlns: t.Optional[str] = None,
    lang: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Html node."""
    return node(
        *children,
        attributes={
            "xmlns": xmlns,
            "lang": lang,
        },
        style=style,
        on=on,
        name="html",
        content_allowed=True,
    )


def i(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """I node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="i",
        content_allowed=True,
    )


def iframe(
    *children: ChildType,
    height: t.Optional[str] = None,
    width: t.Optional[str] = None,
    src: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    tabindex: t.Optional[str] = None,
    srcdoc: t.Optional[str] = None,
    name: t.Optional[str] = None,
    sandbox: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Iframe node."""
    return node(
        *children,
        attributes={
            "height": height,
            "width": width,
            "src": src,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "tabindex": tabindex,
            "srcdoc": srcdoc,
            "name": name,
            "sandbox": sandbox,
        },
        style=style,
        on=on,
        name="iframe",
        content_allowed=True,
    )


def img(
    *children: ChildType,
    src: t.Optional[str] = None,
    alt: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    loading: t.Optional[str] = None,
    height: t.Optional[str] = None,
    width: t.Optional[str] = None,
    ismap: t.Optional[str] = None,
    usemap: t.Optional[str] = None,
    srcset: t.Optional[str] = None,
    sizes: t.Optional[str] = None,
    crossorigin: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Img node."""
    return node(
        *children,
        attributes={
            "src": src,
            "alt": alt,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "loading": loading,
            "height": height,
            "width": width,
            "ismap": ismap,
            "usemap": usemap,
            "srcset": srcset,
            "sizes": sizes,
            "crossorigin": crossorigin,
        },
        style=style,
        on=on,
        name="img",
        content_allowed=False,
    )


def input(
    *children: ChildType,
    type: t.Optional[
        Literal[
            "text",
            "checkbox",
            "radio",
            "hidden",
            "button",
            "submit",
            "reset",
            "password",
            "file",
            "color",
            "date",
            "datetime-local",
            "email",
            "search",
            "image",
            "month",
            "number",
            "range",
            "tel",
            "time",
            "url",
            "week",
        ]
    ] = None,
    name: t.Optional[str] = None,
    value: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    tabindex: t.Optional[str] = None,
    lang: t.Optional[str] = None,
    checked: t.Optional[str] = None,
    placeholder: t.Optional[str] = None,
    maxlength: t.Optional[str] = None,
    required: t.Optional[str] = None,
    readonly: t.Optional[str] = None,
    disabled: t.Optional[str] = None,
    autofocus: t.Optional[str] = None,
    autocomplete: t.Optional[str] = None,
    form: t.Optional[str] = None,
    formaction: t.Optional[str] = None,
    formtarget: t.Optional[
        Literal["_blank", "_self", "_parent", "_top", "framename"]
    ] = None,
    formenctype: t.Optional[str] = None,
    formmethod: t.Optional[str] = None,
    formnovalidate: t.Optional[str] = None,
    accept: t.Optional[str] = None,
    min: t.Optional[str] = None,
    max: t.Optional[str] = None,
    step: t.Optional[str] = None,
    multiple: t.Optional[str] = None,
    pattern: t.Optional[str] = None,
    size: t.Optional[str] = None,
    src: t.Optional[str] = None,
    alt: t.Optional[str] = None,
    width: t.Optional[str] = None,
    height: t.Optional[str] = None,
    list: t.Optional[str] = None,
    dirname: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Input node."""
    return node(
        *children,
        attributes={
            "type": type,
            "name": name,
            "value": value,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "tabindex": tabindex,
            "lang": lang,
            "checked": checked,
            "placeholder": placeholder,
            "maxlength": maxlength,
            "required": required,
            "readonly": readonly,
            "disabled": disabled,
            "autofocus": autofocus,
            "autocomplete": autocomplete,
            "form": form,
            "formaction": formaction,
            "formtarget": formtarget,
            "formenctype": formenctype,
            "formmethod": formmethod,
            "formnovalidate": formnovalidate,
            "accept": accept,
            "min": min,
            "max": max,
            "step": step,
            "multiple": multiple,
            "pattern": pattern,
            "size": size,
            "src": src,
            "alt": alt,
            "width": width,
            "height": height,
            "list": list,
            "dirname": dirname,
        },
        style=style,
        on=on,
        name="input",
        content_allowed=True,
    )


def ins(
    *children: ChildType,
    datetime: t.Optional[str] = None,
    cite: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Ins node."""
    return node(
        *children,
        attributes={
            "datetime": datetime,
            "cite": cite,
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="ins",
        content_allowed=True,
    )


def kbd(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Kbd node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="kbd",
        content_allowed=True,
    )


def label(
    *children: ChildType,
    for_html: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Label node."""
    return node(
        *children,
        attributes={
            "for": for_html,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="label",
        content_allowed=True,
    )


def legend(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Legend node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="legend",
        content_allowed=True,
    )


def li(
    *children: ChildType,
    value: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Li node."""
    return node(
        *children,
        attributes={
            "value": value,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="li",
        content_allowed=True,
    )


def link(
    *children: ChildType,
    href: t.Optional[str] = None,
    rel: t.Optional[
        Literal[
            "stylesheet",
            "icon",
            "canonical",
            "dns-prefetch",
            "author",
            "help",
            "license",
            "prev",
            "next",
            "search",
            "alternate",
        ]
    ] = None,
    type: t.Optional[str] = None,
    id: t.Optional[str] = None,
    media: t.Optional[str] = None,
    sizes: t.Optional[str] = None,
    hreflang: t.Optional[str] = None,
    crossorigin: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Link node."""
    return node(
        *children,
        attributes={
            "href": href,
            "rel": rel,
            "type": type,
            "id": id,
            "media": media,
            "sizes": sizes,
            "hreflang": hreflang,
            "crossorigin": crossorigin,
        },
        style=style,
        on=on,
        name="link",
        content_allowed=False,
    )


def main(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Main node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="main",
        content_allowed=True,
    )


def map(
    *children: ChildType,
    name: t.Optional[str] = None,
    id: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Map node."""
    return node(
        *children,
        attributes={
            "name": name,
            "id": id,
        },
        style=style,
        on=on,
        name="map",
        content_allowed=True,
    )


def mark(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Mark node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="mark",
        content_allowed=True,
    )


def meta(
    *children: ChildType,
    name: t.Optional[str] = None,
    content: t.Optional[str] = None,
    http_equiv: t.Optional[str] = None,
    charset: t.Optional[str] = None,
    id: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Meta node."""
    return node(
        *children,
        attributes={
            "name": name,
            "content": content,
            "http-equiv": http_equiv,
            "charset": charset,
            "id": id,
        },
        style=style,
        on=on,
        name="meta",
        content_allowed=True,
    )


def meter(
    *children: ChildType,
    value: t.Optional[str] = None,
    min: t.Optional[str] = None,
    max: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    low: t.Optional[str] = None,
    high: t.Optional[str] = None,
    optimum: t.Optional[str] = None,
    form: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Meter node."""
    return node(
        *children,
        attributes={
            "value": value,
            "min": min,
            "max": max,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "low": low,
            "high": high,
            "optimum": optimum,
            "form": form,
        },
        style=style,
        on=on,
        name="meter",
        content_allowed=True,
    )


def nav(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Nav node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="nav",
        content_allowed=True,
    )


def noscript(
    *children: ChildType,
    id: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Noscript node."""
    return node(
        *children,
        attributes={
            "id": id,
        },
        style=style,
        on=on,
        name="noscript",
        content_allowed=True,
    )


def object(
    *children: ChildType,
    data: t.Optional[str] = None,
    type: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    height: t.Optional[str] = None,
    width: t.Optional[str] = None,
    name: t.Optional[str] = None,
    form: t.Optional[str] = None,
    usemap: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Object node."""
    return node(
        *children,
        attributes={
            "data": data,
            "type": type,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "height": height,
            "width": width,
            "name": name,
            "form": form,
            "usemap": usemap,
        },
        style=style,
        on=on,
        name="object",
        content_allowed=True,
    )


def ol(
    *children: ChildType,
    type: t.Optional[str] = None,
    start: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    reversed: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Ol node."""
    return node(
        *children,
        attributes={
            "type": type,
            "start": start,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "reversed": reversed,
        },
        style=style,
        on=on,
        name="ol",
        content_allowed=True,
    )


def optgroup(
    *children: ChildType,
    label: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    disabled: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Optgroup node."""
    return node(
        *children,
        attributes={
            "label": label,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "disabled": disabled,
        },
        style=style,
        on=on,
        name="optgroup",
        content_allowed=True,
    )


def option(
    *children: ChildType,
    label: t.Optional[str] = None,
    value: t.Optional[str] = None,
    selected: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    disabled: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Option node."""
    return node(
        *children,
        attributes={
            "label": label,
            "value": value,
            "selected": selected,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "disabled": disabled,
        },
        style=style,
        on=on,
        name="option",
        content_allowed=True,
    )


def output(
    *children: ChildType,
    for_html: t.Optional[str] = None,
    form: t.Optional[str] = None,
    name: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Output node."""
    return node(
        *children,
        attributes={
            "for": for_html,
            "form": form,
            "name": name,
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="output",
        content_allowed=True,
    )


def p(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    lang: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """P node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "lang": lang,
        },
        style=style,
        on=on,
        name="p",
        content_allowed=True,
    )


def param(
    *children: ChildType,
    name: t.Optional[str] = None,
    value: t.Optional[str] = None,
    id: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Param node."""
    return node(
        *children,
        attributes={
            "name": name,
            "value": value,
            "id": id,
        },
        style=style,
        on=on,
        name="param",
        content_allowed=True,
    )


def picture(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Picture node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="picture",
        content_allowed=True,
    )


def pre(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Pre node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="pre",
        content_allowed=True,
    )


def progress(
    *children: ChildType,
    max: t.Optional[str] = None,
    value: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Progress node."""
    return node(
        *children,
        attributes={
            "max": max,
            "value": value,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="progress",
        content_allowed=True,
    )


def q(
    *children: ChildType,
    cite: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Q node."""
    return node(
        *children,
        attributes={
            "cite": cite,
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="q",
        content_allowed=True,
    )


def rp(
    *children: ChildType,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Rp node."""
    return node(
        *children, attributes={}, style=style, on=on, name="rp", content_allowed=True
    )


def rt(
    *children: ChildType,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Rt node."""
    return node(
        *children, attributes={}, style=style, on=on, name="rt", content_allowed=True
    )


def ruby(
    *children: ChildType,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Ruby node."""
    return node(
        *children, attributes={}, style=style, on=on, name="ruby", content_allowed=True
    )


def samp(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Samp node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="samp",
        content_allowed=True,
    )


def script(
    *children: ChildType,
    src: t.Optional[str] = None,
    type: t.Optional[str] = None,
    charset: t.Optional[str] = None,
    async_node: t.Optional[str] = None,
    defer: t.Optional[str] = None,
    id: t.Optional[str] = None,
    crossorigin: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Script node."""
    return node(
        *children,
        attributes={
            "src": src,
            "type": type,
            "charset": charset,
            "async": async_node,
            "defer": defer,
            "id": id,
            "crossorigin": crossorigin,
        },
        style=style,
        on=on,
        name="script",
        content_allowed=True,
    )


def section(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Section node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="section",
        content_allowed=True,
    )


def select(
    *children: ChildType,
    name: t.Optional[str] = None,
    multiple: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    tabindex: t.Optional[str] = None,
    hidden: t.Optional[str] = None,
    disabled: t.Optional[str] = None,
    autofocus: t.Optional[str] = None,
    autocomplete: t.Optional[str] = None,
    form: t.Optional[str] = None,
    required: t.Optional[str] = None,
    size: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Select node."""
    return node(
        *children,
        attributes={
            "name": name,
            "multiple": multiple,
            "id": id,
            "class": cformat(class_name),
            "tabindex": tabindex,
            "hidden": hidden,
            "disabled": disabled,
            "autofocus": autofocus,
            "autocomplete": autocomplete,
            "form": form,
            "required": required,
            "size": size,
        },
        style=style,
        on=on,
        name="select",
        content_allowed=True,
    )


def small(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Small node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="small",
        content_allowed=True,
    )


def source(
    *children: ChildType,
    src: t.Optional[str] = None,
    srcset: t.Optional[str] = None,
    type: t.Optional[str] = None,
    media: t.Optional[str] = None,
    id: t.Optional[str] = None,
    sizes: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Source node."""
    return node(
        *children,
        attributes={
            "src": src,
            "srcset": srcset,
            "type": type,
            "media": media,
            "id": id,
            "sizes": sizes,
        },
        style=style,
        on=on,
        name="source",
        content_allowed=True,
    )


def span(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Span node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="span",
        content_allowed=True,
    )


def strong(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Strong node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="strong",
        content_allowed=True,
    )


def style(
    *children: ChildType,
    media: t.Optional[str] = None,
    type: t.Optional[str] = None,
    id: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Style node."""
    return node(
        *children,
        attributes={
            "media": media,
            "type": type,
            "id": id,
        },
        style=style,
        on=on,
        name="style",
        content_allowed=True,
    )


def sub(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Sub node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="sub",
        content_allowed=True,
    )


def summary(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Summary node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="summary",
        content_allowed=True,
    )


def sup(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Sup node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="sup",
        content_allowed=True,
    )


def svg(
    *children: ChildType,
    viewBox: t.Optional[str] = None,
    width: t.Optional[str] = None,
    height: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    preserveAspectRatio: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Svg node."""
    return node(
        *children,
        attributes={
            "viewBox": viewBox,
            "width": width,
            "height": height,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "preserveAspectRatio": preserveAspectRatio,
        },
        style=style,
        on=on,
        name="svg",
        content_allowed=True,
    )


def table(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Table node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="table",
        content_allowed=True,
    )


def tbody(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Tbody node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="tbody",
        content_allowed=True,
    )


def td(
    *children: ChildType,
    rowspan: t.Optional[str] = None,
    colspan: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    title: t.Optional[str] = None,
    headers: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Td node."""
    return node(
        *children,
        attributes={
            "rowspan": rowspan,
            "colspan": colspan,
            "id": id,
            "class": cformat(class_name),
            "title": title,
            "headers": headers,
        },
        style=style,
        on=on,
        name="td",
        content_allowed=True,
    )


def template(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Template node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="template",
        content_allowed=True,
    )


def textarea(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    tabindex: t.Optional[str] = None,
    lang: t.Optional[str] = None,
    autocomplete: t.Optional[str] = None,
    autofocus: t.Optional[str] = None,
    cols: t.Optional[str] = None,
    dirname: t.Optional[str] = None,
    disabled: t.Optional[str] = None,
    form: t.Optional[str] = None,
    maxlength: t.Optional[str] = None,
    name: t.Optional[str] = None,
    placeholder: t.Optional[str] = None,
    readonly: t.Optional[str] = None,
    required: t.Optional[str] = None,
    rows: t.Optional[str] = None,
    wrap: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Textarea node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "tabindex": tabindex,
            "lang": lang,
            "autocomplete": autocomplete,
            "autofocus": autofocus,
            "cols": cols,
            "dirname": dirname,
            "disabled": disabled,
            "form": form,
            "maxlength": maxlength,
            "name": name,
            "placeholder": placeholder,
            "readonly": readonly,
            "required": required,
            "rows": rows,
            "wrap": wrap,
        },
        style=style,
        on=on,
        name="textarea",
        content_allowed=True,
    )


def tfoot(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Tfoot node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="tfoot",
        content_allowed=True,
    )


def th(
    *children: ChildType,
    colspan: t.Optional[str] = None,
    rowspan: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    title: t.Optional[str] = None,
    headers: t.Optional[str] = None,
    scope: t.Optional[str] = None,
    abbr: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Th node."""
    return node(
        *children,
        attributes={
            "colspan": colspan,
            "rowspan": rowspan,
            "id": id,
            "class": cformat(class_name),
            "title": title,
            "headers": headers,
            "scope": scope,
            "abbr": abbr,
        },
        style=style,
        on=on,
        name="th",
        content_allowed=True,
    )


def thead(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Thead node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="thead",
        content_allowed=True,
    )


def time(
    *children: ChildType,
    datetime: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Time node."""
    return node(
        *children,
        attributes={
            "datetime": datetime,
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="time",
        content_allowed=True,
    )


def title(
    *children: ChildType,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Title node."""
    return node(
        *children, attributes={}, style=style, on=on, name="title", content_allowed=True
    )


def tr(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Tr node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
        },
        style=style,
        on=on,
        name="tr",
        content_allowed=True,
    )


def track(
    *children: ChildType,
    src: t.Optional[str] = None,
    kind: t.Optional[str] = None,
    label: t.Optional[str] = None,
    srclang: t.Optional[str] = None,
    default: t.Optional[str] = None,
    id: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Track node."""
    return node(
        *children,
        attributes={
            "src": src,
            "kind": kind,
            "label": label,
            "srclang": srclang,
            "default": default,
            "id": id,
        },
        style=style,
        on=on,
        name="track",
        content_allowed=True,
    )


def u(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """U node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="u",
        content_allowed=True,
    )


def ul(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Ul node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
        },
        style=style,
        on=on,
        name="ul",
        content_allowed=True,
    )


def var(
    *children: ChildType,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Var node."""
    return node(
        *children,
        attributes={
            "id": id,
            "class": cformat(class_name),
        },
        style=style,
        on=on,
        name="var",
        content_allowed=True,
    )


def video(
    *children: ChildType,
    height: t.Optional[str] = None,
    width: t.Optional[str] = None,
    src: t.Optional[str] = None,
    controls: t.Optional[str] = None,
    autoplay: t.Optional[str] = None,
    id: t.Optional[str] = None,
    class_name: t.Optional[
        t.Union[
            t.List[t.Union[str, CSSObject, t.Type[CSSObject]]],
            t.Union[str, CSSObject, t.Type[CSSObject]],
        ]
    ] = None,
    hidden: t.Optional[str] = None,
    title: t.Optional[str] = None,
    loop: t.Optional[str] = None,
    muted: t.Optional[str] = None,
    poster: t.Optional[str] = None,
    preload: t.Optional[str] = None,
    crossorigin: t.Optional[str] = None,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Video node."""
    return node(
        *children,
        attributes={
            "height": height,
            "width": width,
            "src": src,
            "controls": controls,
            "autoplay": autoplay,
            "id": id,
            "class": cformat(class_name),
            "hidden": hidden,
            "title": title,
            "loop": loop,
            "muted": muted,
            "poster": poster,
            "preload": preload,
            "crossorigin": crossorigin,
        },
        style=style,
        on=on,
        name="video",
        content_allowed=True,
    )


def wbr(
    *children: ChildType,
    style: t.Optional[Style] = None,
    on: t.Optional[DOMEvents] = None,
) -> node:
    """Wbr node."""
    return node(
        *children, attributes={}, style=style, on=on, name="wbr", content_allowed=True
    )


def unpack(*children: ChildType) -> node:
    """Unpackable node."""
    return _unpack(*children)
