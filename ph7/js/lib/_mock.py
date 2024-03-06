"""API mock helper."""

import json
from typing import Any


def dump(args):
    dumped = []
    for arg in args:
        try:
            dumped.append(json.dumps(arg))
        except Exception:
            dumped.append(arg)
    return dumped


class _ApiMock:
    """ApiMock"""

    def __init__(
        self,
        name: str,
        is_callable: bool = False,
        args=None,
        parents=None,
    ) -> None:
        """Initialize object."""
        self.name = name
        self.is_callable = is_callable
        self.args = args
        self.parents = parents or []

    def __getattribute__(self, __name: str) -> str:
        """Get attribute."""
        return _ApiMock(
            __name,
            parents=[*super().__getattribute__("parents"), self],
        )

    def __call__(self, *args: Any) -> Any:
        return _ApiMock(
            name=super().__getattribute__("name"),
            is_callable=True,
            args=args,
            parents=super().__getattribute__("parents").copy(),
        )

    def __mod__(self, other):
        rep = super().__getattribute__("name")
        if super().__getattribute__("is_callable"):
            args = super().__getattribute__("args")
            rep = rep + "(" + ", ".join(dump(args)) + ")"
        return f"{rep}.{other}"

    def __str__(self) -> str:
        """String representation."""
        rep = super().__getattribute__("name")
        if super().__getattribute__("is_callable"):
            args = super().__getattribute__("args")
            rep = rep + "(" + ", ".join(dump(args)) + ")"

        parents = super().__getattribute__("parents")
        if parents:
            for parent in reversed(parents):
                rep = parent % rep
        return rep

    __repr__ = __str__
