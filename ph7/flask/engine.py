"""Template engine for flask."""

import typing as t
from importlib.machinery import SourceFileLoader
from pathlib import Path

from ph7.core.html import HtmlNode


class _MockContext:
    def __init__(self, name: str, data: t.Optional[t.Dict] = None) -> None:
        """Mock context."""
        self.name = name
        self.data = data or {}

    def __setitem__(self, __key: str, __value: t.Any) -> None:
        """Set mock value."""
        self.data[__key] = __value

    def __getitem__(self, name: str) -> "_MockContext":
        """Get mock item."""
        return self.data.get(
            name,
            _MockContext(
                f"{self.name}->{name=}",
                data=self.data,
            ),
        )

    def __hash__(self) -> int:
        return hash(self.name)


class Template:
    """Template class."""

    def __init__(self, template: HtmlNode, view: str) -> None:
        """Initialize object."""
        self.view = view
        self.template = template

    def render(self, context: t.Optional[t.Dict] = None, stream: bool = False):
        """Render template."""
        if context is None:
            context = {}
        context["_view"] = self.view
        if stream:
            return self.template.stream(context=context)
        return self.template.render(context)


class PH7Templates:
    """PH7 Templates helper."""

    def __init__(
        self,
        templates_path: t.Union[str, Path],
        mock_context: t.Any = None,
    ) -> None:
        """Initialize object."""
        self.templates_path = Path(templates_path).resolve()
        self.templates = {}

        cwd = Path.cwd()
        for template in self.templates_path.glob("**/*.py"):
            if "styles" in template.parts:
                continue
            template = template.relative_to(cwd)
            *path, name = template.parts
            if name == "__init__.py":
                fullname = ".".join(template.parts[1:-1])
            else:
                name = name.replace(".py", "")
                path = [*path, name]
                fullname = ".".join([*template.parts[1:-1], name])

            module = SourceFileLoader(  # pylint: disable=deprecated-method,no-value-for-parameter
                fullname=fullname,
                path=str(template),
            ).load_module()
            self.templates[".".join(path[1:]) or "root"] = module
            self._dry_run(
                module=module,
                context=mock_context
                or t.cast(
                    dict,
                    _MockContext("mock"),
                ),
            )

    def _dry_run(self, module: t.Any, context: t.Any) -> None:
        """Perform a dry run for a template module."""
        errors = []
        context["_view"] = module.__name__
        for name in dir(module):
            obj = getattr(module, name)
            if not isinstance(obj, HtmlNode):
                continue
            try:
                obj.render(context=context)
            except Exception as e:  # pylint: disable=broad-exception-caught
                errors.append(str(e))

        if len(errors) == 0:
            return

        print(
            "\n- ".join(
                [
                    f"[WARNING] Errors found while performing dry run for {module}",
                    *errors,
                ]
            )
        )

    def get(self, name: str, cls: t.Optional[str] = None) -> "Template":
        """Get PH7 node for `name`"""
        cls = cls or "template"
        if ":" in name:
            name, cls = name.split(":")

        module = self.templates.get(name)
        if module is None:
            raise ValueError(f"Template '{name}' not found")

        template = getattr(module, cls, None)
        if template is None:
            raise AttributeError(f"View '{cls}' not found in template {name}")
        return Template(template=template, view=module.__name__)

    def render(
        self,
        name: str,
        context: t.Optional[t.Dict] = None,
        stream: bool = False,
    ) -> str:
        """Render PH7 template."""
        context = context or {}
        return self.get(name=name).render(context=context, stream=stream)
