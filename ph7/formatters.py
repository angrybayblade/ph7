import typing as t

from ph7.css import css


def sformat(style: t.Dict) -> str:
    """Style formatter."""
    if len(style) == 0:
        return ""
    return ' style="' + ";".join(map(lambda x: f"{x[0]}:{x[1]}", style.items())) + '" '


def aformat(attributes: t.Dict) -> str:
    """Attributes formatter."""
    attrs = " ".join(
        [f'{key}="{value}"' for key, value in attributes.items() if value is not None]
    )
    if attrs:
        return f" {attrs} "
    return ""


def hformat(handlers: t.Dict) -> str:
    """Handler formatter."""
    if len(handlers) == 0:
        return ""
    return " ".join(map(lambda x: f'{x[0]}="{x[1]}"', handlers.items()))


def cformat(
    class_name: t.Optional[t.Union[t.List[t.Union[str, css]], t.Union[str, css]]]
) -> t.Optional[str]:
    """Format classname."""
    if class_name is None:
        return None

    if hasattr(class_name, "name"):
        return t.cast(css, class_name).name()

    if isinstance(class_name, str):
        return class_name

    cls_name = ""
    for cls in class_name:
        if hasattr(cls, "name"):
            cls_name += f"{t.cast(css, cls).name()} "
            continue
        cls_name += f"{cls} "
    return cls_name[:-1]
