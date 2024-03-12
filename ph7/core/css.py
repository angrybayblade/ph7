"""CSS base classes."""

import typing as t

from ph7.core.tags import TAGS
from ph7.style import attributes as css_attr


class CSSNode:
    """Renderable CSS node."""

    __css__: bool = True

    child: t.Optional[int] = None

    @classmethod
    def name(cls) -> str:
        """Name string."""
        name = cls.__name__.replace("_", "-")
        if name in TAGS:
            return name
        if name.startswith("--"):
            return f"::{name[2:]}"
        if name.startswith("-") and cls.child is not None:
            return f":{name[1:]}({cls.child})"
        if name.startswith("-"):
            return f":{name[1:]}"
        return f" .{name}"

    @classmethod
    def format(cls) -> str:
        """Name string."""
        name = cls.__name__.replace("_", "-")
        if name in TAGS:
            raise ValueError(
                f"{name} is a HTML tag selector, Cannot use it as a classname."
            )
        return name

    @classmethod
    def properties(cls) -> t.Dict[str, str]:
        """Returns properties mapping."""
        properties = {}
        for base in cls.__bases__:
            if hasattr(base, "properties"):
                properties.update(base.properties())
        for prop, val in cls.__dict__.items():
            if isinstance(val, str) and not prop.startswith("__"):
                properties[css_attr[prop]] = val
        return properties

    @classmethod
    def subclasses(cls) -> t.List["CSSNode"]:
        """Returns the list of available subclasses."""
        cs = []
        for c in cls.__dict__.values():
            if hasattr(c, "__css__"):
                cs.append(c)
        return cs

    @classmethod
    def dict(cls, parent: str, context: t.Dict) -> None:
        """Render CSS object."""
        context[f"{parent}{cls.name()}"[1:]] = cls.properties()
        for subc in cls.subclasses():
            subc.dict(
                parent=f"{parent}{cls.name()}",
                context=context,
            )


def to_css(*objs: t.Union[CSSNode, t.Type[CSSNode]], minify: bool = False) -> str:
    """Render CSS stylesheet."""
    sheet = ""
    container: t.Dict[str, t.Dict] = {}
    separator = "" if minify else " "
    newline = "" if minify else "\n"
    tab = "" if minify else "  "
    for obj in objs:
        obj.dict(parent="", context=container)
    for cls in sorted(container):
        sheet += f"{cls}" + "{" + newline
        for prop, val in container[cls].items():
            sheet += f"{tab}{prop}:{separator}{val};{newline}"
        sheet += "}" + newline
    return sheet
