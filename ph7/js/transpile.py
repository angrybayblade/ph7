"""Python to JavaScript transpiler."""

import ast
import inspect
import typing as t

# pylint: disable=unused-argument


def _stack_level() -> t.Dict:
    """Stack level."""
    return {"variables": set()}


class Visitor(ast.NodeVisitor):  # pylint: disable=too-many-public-methods
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

    def visit(self, node: ast.AST, end: t.Optional[str] = None) -> None:
        """Visit a node."""
        method = "visit_" + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        visitor(node, end)

    def generic_visit(self, node: ast.AST, end: t.Optional[str] = None) -> None:
        """Called if no explicit visitor function exists for a node."""
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item, end=end)
            elif isinstance(value, ast.AST):
                self.visit(value, end=end)

    def visit_Constant(self, node: ast.Constant, end: t.Optional[str] = None) -> t.Any:
        """Visit constant."""
        self.code += ast.unparse(node)

    def visit_Dict(self, node: ast.Dict, end: t.Optional[str] = None) -> t.Any:
        """Visit dictionary."""
        self.code += "{"
        for key, val in zip(node.keys, node.values):
            self.visit(key, end="")  # type: ignore
            self.code += " : "
            self.visit(val, end="")  # type: ignore
            self.code += ","
        if self.code.endswith(","):
            self.code = self.code[:-1]
        self.code += "}"
        self.code += end if end is not None else f";{self.separator}"

    def visit_Name(self, node: ast.Name, end: t.Optional[str] = None) -> t.Any:
        """Visit name."""
        self.code += ast.unparse(node)

    def visit_Add(self, node: ast.Add, end: t.Optional[str] = None) -> t.Any:
        """Visit name."""
        self.code += " + "

    def visit_JoinedStr(
        self, node: ast.JoinedStr, end: t.Optional[str] = None
    ) -> t.Any:
        """Visit joined string."""
        for value in node.values:
            if isinstance(value, ast.Constant):
                self.code += ast.unparse(value) + " + "
            if isinstance(value, ast.FormattedValue):
                self.code += ast.unparse(value)[3:-2] + " + "
        self.code = self.code[:-3]

    def visit_BinOp(self, node: ast.BinOp, end: t.Optional[str] = None) -> t.Any:
        """Visit binary operation."""
        self.visit(node.left)
        self.visit(node.op)
        self.visit(node.right)

    def visit_Return(self, node: ast.Return, end: t.Optional[str] = None) -> t.Any:
        """Visit return node."""
        self.code += f"{self.indent}{ast.unparse(node)};{self.separator}"

    def visit_Attribute(
        self, node: ast.Attribute, end: t.Optional[str] = None
    ) -> t.Any:
        """Visit attribute node."""
        if isinstance(node.value, ast.Call):
            self.decrese_level()
            self.visit_Call(node=node.value, end="")
            self.increase_level()
        else:
            self.visit(node.value)
        self.code += "." + node.attr

    def visit_Assign(self, node: ast.Assign, end: t.Optional[str] = None) -> t.Any:
        """Visit assign."""
        targets = ast.unparse(node.targets)  # type: ignore
        value = ast.unparse(node.value)

        if "." in targets:
            self.code += f"{self.indent}"
            for target in node.targets:
                self.visit(target)
        elif targets in self.scope[-1]["variables"]:
            self.code += f"{self.indent}{targets} = {value};{self.separator}"
        else:
            self.scope[-1]["variables"].add(targets)
            self.code += f"{self.indent}let {targets}"

        self.code += " = "
        self.visit(node.value, end="")
        self.code += f";{self.separator}"

    def visit_If(
        self, node: ast.If, elseif: bool = False, end: t.Optional[str] = None
    ) -> t.Any:
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

    def visit_For(self, node: ast.For, end: t.Optional[str] = None) -> t.Any:
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

    def visit_Try(self, node: ast.Try, end: t.Optional[str] = None) -> t.Any:
        """Visit try/except block."""
        self.code += f"{self.indent}try{{{self.separator}"
        self.increase_level()
        for expr in node.body:
            self.visit(expr)
        self.decrese_level()

        if len(node.handlers) > 1:
            raise ValueError(
                f"Only exception handler allowed per try block; Line no: {node.lineno}"
            )
        (handler,) = node.handlers
        handler = t.cast(ast.ExceptHandler, handler)
        self.code += f"{self.indent}}} catch({handler.name}){{{self.separator}"
        self.increase_level()
        for expr in handler.body:
            self.visit(expr)
        self.decrese_level()
        if len(node.finalbody) == 0:
            self.code += f"{self.indent}}};{self.separator}"
            return

        self.code += f"{self.indent}}} finally{{{self.separator}"
        self.increase_level()
        for expr in node.finalbody:
            self.visit(expr)
        self.decrese_level()
        self.code += f"{self.indent}}};{self.separator}"

    def visit_Raise(self, node: ast.Raise, end: t.Optional[str] = None) -> t.Any:
        """Visit raise statement."""
        self.code += f"{self.indent}throw new Error("
        if isinstance(node.exc, ast.Call):
            for expr in node.exc.args:
                self.visit(expr, end="")
        self.code += f");{self.separator}"

    def visit_Await(self, node: ast.Await, end: t.Optional[str] = None) -> t.Any:
        """Visit await."""
        self.code += "await "
        _level = self.level
        self.level = 0
        self.visit(node.value, end="")
        self.level = _level
        self.code += end if end is not None else f";{self.separator}"

    def visit_Call(self, node: ast.Call, end: t.Optional[str] = None) -> t.Any:
        """Visit function call"""
        func = ast.unparse(node.func)
        if func == "print":
            func = "console.log"
        self.code += f"{self.indent}{func}("
        self.increase_level()
        for arg in node.args:
            self.visit(arg, end="")
            self.code += ","
        if self.code.endswith(","):
            self.code = self.code[:-1]
        self.decrese_level()
        self.code += ")"
        self.code += end if end is not None else f";{self.separator}"

    def visit_FunctionDef(
        self, node: ast.FunctionDef, end: t.Optional[str] = None
    ) -> t.Any:
        """Visit function definition."""
        args = ", ".join([arg.arg for arg in node.args.args])
        self.code += f"""{self.indent}function {node.name}({args}){{{self.separator}"""
        self.increase_level()
        for stmnt in node.body:
            self.visit(node=stmnt)
        self.decrese_stack()
        self.decrese_level()
        self.code += f"""}}{self.separator}"""

    def visit_AsyncFunctionDef(
        self, node: ast.AsyncFunctionDef, end: t.Optional[str] = None
    ) -> t.Any:
        """Visit async function def."""
        args = ", ".join([arg.arg for arg in node.args.args])
        self.code += (
            f"{self.indent}async function {node.name}({args}){{{self.separator}"
        )
        self.increase_level()
        self.increase_stack()
        for stmnt in node.body:
            self.visit(node=stmnt)
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
