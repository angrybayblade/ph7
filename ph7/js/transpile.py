"""Python to JavaScript transpiler."""

import ast
import inspect
import typing as t


def _stack_level() -> t.Dict:
    """Stack level."""
    return {"variables": set()}


class Visitor(ast.NodeVisitor):
    """Inspect Python code."""

    level: int
    code: str
    scope: t.List[t.Dict]

    def __init__(
        self,
        separator: t.Optional[str] = None,
        indent: t.Optional[str] = None,
    ) -> None:
        """Initialize VisitorNode object."""
        super().__init__()
        self.separator = separator or ""
        self._indent = indent or ""

        self.code = ""
        self.level = 0
        self.scope = [_stack_level()]

    def increase_stack(self) -> None:
        """Increase stack level."""
        self.scope.append(_stack_level())

    def decrese_stack(self) -> None:
        """Decrease stack level."""
        if len(self.scope) == 1:
            return
        self.scope.pop()

    def increase_level(self) -> None:
        """Increase level."""
        self.level += 1

    def decrese_level(self) -> None:
        """Decrease level."""
        self.level -= 1

    @property
    def indent(self) -> str:
        """Return indent."""
        return self.level * self._indent

    def visit_Return(self, node: ast.Return) -> t.Any:
        """Visit return node."""
        self.code += f"{self.indent}{ast.unparse(node)};{self.separator}"

    def visit_Assign(self, node: ast.Assign) -> t.Any:
        """Visit assign."""
        targets = ast.unparse(node.targets)  # type: ignore
        value = ast.unparse(node.value)

        if targets in self.scope[-1]["variables"]:
            self.code += f"{self.indent}{targets} = {value};{self.separator}"
            return

        self.scope[-1]["variables"].add(targets)
        if "." in targets:
            self.code += f"{self.indent}{targets} = {value};{self.separator}"
            return

        self.code += f"{self.indent}let {targets} = {value};{self.separator}"

    def visit_Call(self, node: ast.Call) -> t.Any:
        """Visit function call"""
        func = ast.unparse(node)
        if ast.unparse(node.func) == "print":
            func = func.replace("print", "console.log")
        self.code += f"{self.indent}{func};{self.separator}"

    def visit_If(self, node: ast.If, elseif: bool = False) -> t.Any:
        """Visit if condition"""
        test = (
            ast.unparse(node.test)
            .replace(" is ", " === ")
            .replace(" or ", " || ")
            .replace(" and ", " && ")
        )
        self.code += f"{' ' if elseif else self.indent}if({test}){{{self.separator}"
        self.increase_level()
        for body in node.body:
            self.visit(body)
        self.decrese_level()
        self.code += f"{self.indent}}};{self.separator}"
        if len(node.orelse) == 0:
            return

        self.code = self.code[:-2]
        for orelse in node.orelse:
            if isinstance(orelse, ast.If):
                self.code += " else"
                self.visit_If(orelse, elseif=True)
                continue

            self.code += f" else{{{self.separator}"
            self.increase_level()
            self.generic_visit(orelse)
            self.decrese_level()
            self.code += f"{self.indent}}};{self.separator}"

    def visit_For(self, node: ast.For) -> t.Any:
        """Visit for loop."""
        iterstr = ast.unparse(node.iter)
        if "range" not in iterstr:
            raise ValueError(f"Invalid for loop: {ast.unparse(node)}")

        range_call = t.cast(ast.Call, node.iter)

        if len(range_call.args) == 1:
            start, step = "0", "1"
            (end,) = list(map(ast.unparse, range_call.args))

        elif len(range_call.args) == 2:
            step = "1"
            (start, end) = list(map(ast.unparse, range_call.args))
        else:
            (start, end, step) = list(map(ast.unparse, range_call.args))

        self.code += (
            f"{self.indent}for(let {node.target.id}={start}; "  # type: ignore
            f"{node.target.id}<{end}; "
            f"{node.target.id}=i+{step}){{{self.separator}"
        )
        self.increase_level()
        for _node in node.body:
            self.visit(node=_node)
        self.decrese_level()
        self.code += f"{self.indent}}}{self.separator}"

    def visit_FunctionDef(self, node: ast.FunctionDef) -> t.Any:
        """Visit function definition."""
        args = ", ".join([arg.arg for arg in node.args.args])
        self.code += f"""{self.indent}function {node.name}({args}){{{self.separator}"""
        self.increase_level()
        self.generic_visit(node=node)
        self.decrese_stack()
        self.decrese_level()
        self.code += f"""}}{self.separator}"""

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> t.Any:
        """Visit async function def."""
        args = ", ".join([arg.arg for arg in node.args.args])
        self.code += (
            f"{self.indent}async function {node.name}({args}){{{self.separator}"
        )
        self.increase_level()
        self.increase_stack()
        self.generic_visit(node=node)
        self.decrese_stack()
        self.decrese_level()
        self.code += f"""}};{self.separator}"""


def as_js(obj: t.Any, minify: bool = True) -> str:
    """Convert Python object to JavaScript code."""
    visitor = Visitor(
        separator="" if minify else "\n",
        indent="" if minify else "  ",
    )
    visitor.visit(
        ast.parse(
            inspect.getsource(
                obj,
            )
        )
    )
    return visitor.code


def to_js(*objs: t.Any, minify: bool = True) -> str:
    """Convert Python object to JavaScript code."""
    script = ""
    for obj in objs:
        script += as_js(obj=obj, minify=minify)
    return script
