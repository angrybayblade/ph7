"""Python to JavaScript transpiler."""

import ast
import inspect
import typing as t


class Visitor(ast.NodeVisitor):
    """Inspect Python code."""

    level = 0
    code = ""

    def __init__(
        self,
        separator: t.Optional[str] = None,
        indent: t.Optional[str] = None,
    ) -> None:
        super().__init__()
        self.separator = separator or ""
        self._indent = indent or ""

    @property
    def indent(self) -> str:
        """Return indent."""
        return self.level * self._indent

    def visit_Return(self, node: ast.Return) -> t.Any:
        """Visit return node."""
        self.code += f"{self.indent}{ast.unparse(node)};{self.separator}"

    def visit_Call(self, node: ast.Call) -> t.Any:
        """Visit function call"""
        self.code += f"{self.indent}{ast.unparse(node)};{self.separator}"

    def visit_If(self, node: ast.If, elseif: bool = False) -> t.Any:
        """Visit if condition"""
        self.code += f"{' ' if elseif else self.indent}if({ast.unparse(node.test)}){{{self.separator}"
        self.level += 1
        for body in node.body:
            self.visit(body)
        self.level -= 1
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
            self.level += 1
            self.generic_visit(orelse)
            self.level -= 1
            self.code += f"{self.indent}}};{self.separator}"

    def visit_Assign(self, node: ast.Assign) -> t.Any:
        """Visit assign."""
        targets = ast.unparse(node.targets)
        value = ast.unparse(node.value)
        if "." in targets:
            self.code += f"{self.indent}{targets} = {value};{self.separator}"
        else:
            self.code += f"{self.indent}let {targets} = {value};{self.separator}"

    def visit_FunctionDef(self, node: ast.FunctionDef) -> t.Any:
        """Visit function definition."""
        args = ", ".join([arg.arg for arg in node.args.args])
        self.code += f"""{self.indent}function {node.name}({args}){{{self.separator}"""
        self.level += 1
        self.generic_visit(node=node)
        self.level -= 1
        self.code += f"""}}{self.separator}"""

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> t.Any:
        """Visit async function def."""
        args = ", ".join([arg.arg for arg in node.args.args])
        self.code += (
            f"{self.indent}async function {node.name}({args}){{{self.separator}"
        )
        self.level += 1
        self.generic_visit(node=node)
        self.level -= 1
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
