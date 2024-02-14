"""
Base class for defining HTML nodes.
"""

import typing as t

from ph7.formatters import aformat, hformat, sformat
from ph7.js import Events as DOMEvents
from ph7.style import Style
from ph7.style import attributes as _styles


def _wrap(child: "ChildType") -> "node":
    """Warp child as node type."""
    if isinstance(child, node):
        return child

    if callable(child):
        return wrapper(view=child)

    return data(value=child)


class node:
    """Html node."""

    _render_cache: str
    _is_wrapper: bool
    _wrapper: t.Optional[str]

    def __init__(
        self,
        *children: "ChildType",
        attributes: t.Optional[t.Dict[str, t.Optional[str]]] = None,
        style: t.Optional[Style] = None,
        handlers: t.Optional[DOMEvents] = None,
        render: t.Optional[t.Callable[[t.Dict], str]] = None,
        name: t.Optional[str] = None,
        content_allowed: bool = True,
    ) -> None:
        """Initialize object."""
        if len(children) > 0 and render is not None:
            raise ValueError("Cannot provide both children and render function.")

        self.children = tuple(map(_wrap, children))
        self.style = style or {}
        self.handlers = handlers or DOMEvents({})
        self.attributes = attributes or {}
        self.context_render = render
        self.name = name or self.__class__.__name__
        self.content_allowed = content_allowed

        self.wrappers = {}
        for child in self.children:
            if child._is_wrapper:
                self.wrappers[child._wrapper] = child
            for nm, nd in child.wrappers.items():
                if nm in self.wrappers:
                    raise ValueError(f"Found multiple wrappers with same name: {nm}")
                self.wrappers[nm] = nd

        self._is_wrapper = False
        self._wrapper = None
        self._cache()

    @property
    def wrapper(self) -> str:
        """Set the node to wrapper name."""
        if self._is_wrapper:
            return t.cast(str, self._wrapper)
        raise ValueError("Node is not a wrapper node.")

    @property
    def is_wrapper(self) -> bool:
        """If the node is a wrapper node."""
        return self._is_wrapper

    def as_wrapper(self, name: str) -> "node":
        """Convert the node to a wrapper node."""
        self._is_wrapper = True
        self._wrapper = name
        return self

    def __call__(
        self,
        *args: "ChildType",
        copy: bool = True,
        **kwargs: t.Union["ChildType", t.Tuple["ChildType", ...]],
    ) -> "node":
        """Hydrate wrapper node."""

        if len(args) > 0 and copy:
            return node(
                *args,
                attributes=self.attributes,
                style=self.style,
                handlers=self.handlers,
                render=self.context_render,
                name=self.name,
                content_allowed=self.content_allowed,
            )

        if len(args) > 0:
            self.children = tuple(map(_wrap, args))
            return self

        cls = self.copy()
        for name, children in kwargs.items():
            if name not in cls.wrappers:
                raise ValueError(f"Invalid wrapper name: {name}")

            children = children if isinstance(children, tuple) else (children,)
            cls.wrappers[name] = cls.wrappers[name](
                *(_wrap(child=child) for child in children),
                copy=False,
            )

        return cls

    def copy(self) -> "node":
        """Create a copy of the node."""
        cls = node(
            *(child.copy() for child in self.children),
            attributes=self.attributes,
            style=self.style,
            handlers=self.handlers,
            render=self.context_render,
            name=self.name,
            content_allowed=self.content_allowed,
        )
        if self.is_wrapper:
            return cls.as_wrapper(self.wrapper)
        return cls

    def _cache(self) -> None:
        """Generate cache."""
        style = {_styles[attr]: val for attr, val in self.style.items()}
        if self.content_allowed:
            self._render_cache = (
                f"<{self.name}"
                + f"{aformat(self.attributes)}"
                + f"{sformat(style)}"
                + f"{hformat(t.cast(t.Dict,self.handlers))}"
                + ">"
                + "{content}"
                + f"</{self.name}>"
            )
            return
        self._render_cache = (
            f"<{self.name}"
            + f"{aformat(self.attributes)}"
            + f"{sformat(style)}"
            + f"{hformat(t.cast(t.Dict,self.handlers))}"
            + "/>"
        )

    def _render(self, context: t.Dict) -> str:
        return "".join(map(lambda x: x.render(context=context), self.children))

    def render(self, context: t.Optional[t.Dict] = None) -> str:
        """Render"""
        if not self.content_allowed:
            return self._render_cache
        return self._render_cache.format(content=self._render(context=context or {}))

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.render()


class wrapper(node):
    """View wrapper node."""

    def __init__(self, view: "CallableAsView") -> None:
        """Initialize data node."""
        self.view = view
        self.wrappers = {}
        self._is_wrapper = False
        self._wrapper = None

    def copy(self) -> "node":
        """Copy data node."""
        return wrapper(view=self.view)

    def render(self, context: t.Optional[t.Dict] = None) -> str:
        """Render string."""
        context = context or {}
        return self.view(context).render(context=context)


class data(node):
    """Data node."""

    def __init__(self, value: t.Any) -> None:
        """Initialize data node."""
        self.sub, self.value = None, value
        if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
            self.sub, self.value = value.replace("${", "").replace("}", "").split("|")

        self.wrappers = {}
        self._is_wrapper = False
        self._wrapper = None

    def copy(self) -> "node":
        """Copy data node."""
        return data(value=self.value)

    def render(self, context: t.Optional[t.Dict] = None) -> str:
        """Render string."""
        context = context or {}
        if self.sub is not None:
            return str(context.get(self.sub, self.value))
        return str(self.value)


CallableAsView = t.Callable[[t.Dict], node]

ChildType = t.Union[node, str, int, float, bool, CallableAsView]
