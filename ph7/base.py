"""
Base class for defining HTML nodes.
"""

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals

import re
import typing as t
from pathlib import Path

from typing_extensions import NotRequired, TypedDict

from ph7.css import CSSObject
from ph7.formatters import aformat, cformat, hformat, sformat
from ph7.js import Events as DOMEvents
from ph7.style import Style
from ph7.style import attributes as _styles

TEMPLATE_RE = re.compile(r"\$\{([a-z0-9_]+)(\|([a-zA-Z0-9_\. ]+))?\}")


def _wrap(child: "ChildType") -> t.Tuple["node", ...]:
    """Warp child as node type."""
    if isinstance(child, node):
        return (child,)

    if callable(child):
        return (wrapper(view=child),)

    if isinstance(child, t.Generator):
        return t.cast(t.Tuple["node", ...], tuple(child))

    return (data(value=child),)


def _unpack(children: t.Tuple["ChildType", ...]) -> t.Tuple["node", ...]:
    """Unpack children."""
    unpacked: t.List["node"] = []
    for child in children:
        unpacked.extend(_wrap(child=child))
    return tuple(unpacked)


class _RenderCache(TypedDict):
    """Render cache."""

    start: NotRequired[str]
    end: NotRequired[str]


class node:  # pylint: disable=too-many-instance-attributes
    """Html node."""

    _render_cache: _RenderCache
    _is_overridable: bool
    _overridable_name: t.Optional[str]

    def __init__(
        self,
        *children: "ChildType",
        attributes: t.Optional[t.Dict[str, t.Optional[str]]] = None,
        style: t.Optional[Style] = None,
        on: t.Optional[DOMEvents] = None,
        render: t.Optional[t.Callable[[t.Dict], str]] = None,
        name: t.Optional[str] = None,
        content_allowed: bool = True,
        cache: t.Optional[_RenderCache] = None,
    ) -> None:
        """Initialize object."""
        if len(children) > 0 and render is not None:
            raise ValueError("Cannot provide both children and render function.")

        self.children = _unpack(children=children)
        self.style = style or {}
        self.on = on or DOMEvents({})
        self.attributes = attributes or {}
        self.context_render = render
        self.name = name or self.__class__.__name__
        self.content_allowed = content_allowed

        self.templates = {}
        for child in self.children:
            if child._is_overridable:
                self.templates[child._overridable_name] = child
            for nm, nd in child.templates.items():
                if nm in self.templates:
                    raise ValueError(f"Found multiple templates with same name: {nm}")
                self.templates[nm] = nd

        self._is_overridable = False
        self._overridable_name = None
        self._render_cache = cache or self._cache()

    def _cache(self) -> _RenderCache:
        """Generate cache."""
        style = {_styles[attr]: val for attr, val in self.style.items()}
        return _RenderCache(
            {
                "start": (
                    f"<{self.name}"
                    + f"{aformat(self.attributes)}"
                    + f"{sformat(style)}"
                    + f"{hformat(t.cast(t.Dict,self.on))}"
                    + (">" if self.content_allowed else "/>")
                ),
                "end": f"</{self.name}>",
            }
        )

    @property
    def template(self) -> str:
        """Set the node to template name."""
        if self._is_overridable:
            return t.cast(str, self._overridable_name)
        raise ValueError("Node is not a template node.")

    @property
    def is_template(self) -> bool:
        """If the node is a template node."""
        return self._is_overridable

    def overridable(self, name: str) -> "node":
        """Convert the node to a template node."""
        self._is_overridable = True
        self._overridable_name = name
        return self

    def __call__(
        self,
        *args: "ChildType",
        copy: bool = True,
        style: t.Optional[Style] = None,
        class_name: t.Optional[
            t.Union[
                t.List[
                    t.Union[
                        str,
                        CSSObject,
                        t.Type[CSSObject],
                    ]
                ],
                t.Union[
                    str,
                    CSSObject,
                    t.Type[CSSObject],
                ],
            ]
        ] = None,
        **kwargs: t.Union["ChildType", t.Tuple["ChildType", ...]],
    ) -> "node":
        """Hydrate template node."""
        if len(args) > 0 and copy:
            if style is None and class_name is None:
                return node(
                    *args,
                    cache=self._render_cache,
                )
            return node(
                *args,
                attributes=(
                    self.attributes
                    if class_name is None
                    else {
                        **self.attributes,
                        "class": cformat(
                            class_name=class_name,
                        ),
                    }
                ),
                style=style or self.style,
                on=self.on,
                render=self.context_render,
                name=self.name,
                content_allowed=self.content_allowed,
            )

        if len(args) > 0:
            self.children = _unpack(children=args)
            return self

        cls = self.copy()
        for name, children in kwargs.items():
            if name not in cls.templates:
                raise ValueError(f"Invalid template name: {name}")
            children = children if isinstance(children, tuple) else (children,)
            cls.templates[name] = cls.templates[name](
                *_unpack(children=children),
                copy=False,
            )
        cls.style = style or self.style
        cls.attributes = (
            self.attributes
            if class_name is None
            else {
                **self.attributes,
                "class": cformat(
                    class_name=class_name,
                ),
            }
        )
        return cls

    def copy(self) -> "node":
        """Create a copy of the node."""
        cls = node(
            *(child.copy() for child in self.children),
            attributes=self.attributes,
            style=self.style,
            on=self.on,
            render=self.context_render,
            name=self.name,
            content_allowed=self.content_allowed,
        )
        if self.is_template:
            return cls.overridable(self.template)
        return cls

    def _render(self, context: t.Dict) -> str:
        return "".join([child.render(context=context) for child in self.children])

    def render(self, context: t.Dict) -> str:
        """Render"""
        if not self.content_allowed:
            return self._render_cache["start"]
        return f"""{self._render_cache["start"]}{self._render(context=context)}{self._render_cache["end"]}"""

    def _stream(self, context: t.Dict) -> t.Generator[str, None, None]:
        """Render and stream children content."""
        for child in self.children:
            yield from child.stream(context=context)

    def stream(self, context: t.Dict) -> t.Generator[str, None, None]:
        """Stream chunks of response."""
        yield self._render_cache["start"]
        if not self.content_allowed:
            return
        yield from self._stream(context=context)
        yield self._render_cache["end"]

    def write(
        self, file: t.Union[str, Path], context: t.Optional[t.Dict] = None
    ) -> None:
        """Write to a file."""
        Path(file).write_text(
            self.render(context=context or {}),
            encoding="utf-8",
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.render({})


class wrapper(node):
    """View wrapper node."""

    def __init__(self, view: "CallableAsView") -> None:
        """Initialize data node."""
        super().__init__()
        self.view = view
        self.templates = {}
        self._is_overridable = False
        self._overridable_name = None

    def copy(self) -> "node":
        """Copy data node."""
        return wrapper(view=self.view)

    def render(self, context: t.Dict) -> str:
        """Render string."""
        return self.view(context).render(context=context)

    def stream(
        self,
        context: t.Dict,
    ) -> t.Generator[str, None, None]:
        """Stream chunks of response."""
        yield from self.view(context).stream(context=context)


class data(node):
    """Data node."""

    def __init__(self, value: t.Any) -> None:
        """Initialize data node."""
        super().__init__()
        self.subs = []
        self.value = value
        if isinstance(value, str):
            subs = TEMPLATE_RE.findall(value)
            if len(subs) > 0:
                for key, _, default in subs:
                    self.subs.append(
                        (
                            (f"${{{key}|{default}}}" if default else f"${{{key}}}"),
                            key,
                            default,
                        )
                    )
        self.templates = {}
        self._is_overridable = False
        self._overridable_name = None

    def copy(self) -> "node":
        """Copy data node."""
        return data(value=self.value)

    def parse(self, context: t.Dict) -> str:
        """Parse value."""
        if len(self.subs) > 0:
            content = t.cast(str, self.value)
            for placeholder, key, default in self.subs:
                subtitute = context.get(key, str(default))
                if not subtitute:
                    raise ValueError(
                        f"Error rendering '{self.value}'; "
                        f"Value for '{key}' not provided"
                    )
                content = content.replace(placeholder, str(subtitute))
            return content
        return str(self.value)

    def render(self, context: t.Dict) -> str:
        """Render string."""
        return self.parse(context=context)

    def stream(
        self,
        context: t.Dict,
    ) -> t.Generator[str, None, None]:
        """Stream chunks of response."""
        yield from self.parse(context=context)


class unpack(node):
    """Unpackable node."""

    def __init__(self, *children: "ChildType") -> None:
        super().__init__(*children)

    def copy(self) -> "node":
        """Copy node."""
        if self.is_template:
            return unpack(*self.children).overridable(self.template)
        return unpack(*self.children)

    def render(self, context: t.Dict) -> str:
        return self._render(context=context)

    def _stream(
        self,
        context: t.Dict,
    ) -> t.Generator[str, None, None]:
        """Render and stream children content."""
        for child in self.children:
            yield from child.stream(context=context)

    def stream(
        self,
        context: t.Dict,
    ) -> t.Generator[str, None, None]:
        """Stream chunks of response."""
        yield from self._stream(context=context)


CallableAsView = t.Callable[[t.Dict], node]

ChildTypeMeta = t.Union[node, str, int, float, bool, CallableAsView]

ChildType = t.Union[
    node,
    str,
    int,
    float,
    bool,
    CallableAsView,
    t.Generator[
        ChildTypeMeta,
        None,
        None,
    ],
]
