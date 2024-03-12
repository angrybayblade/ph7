"""Template engine implementation."""

import typing as t
from importlib.machinery import SourceFileLoader
from pathlib import Path

from typing_extensions import NotRequired, TypedDict

from ph7.core.html import HtmlNode

try:
    from django.http.request import HttpRequest
    from django.template import TemplateDoesNotExist, TemplateSyntaxError
    from django.template.backends.base import BaseEngine
    from django.template.backends.utils import csrf_token_lazy
    from django.template.utils import get_app_template_dirs

    DJANGO_INSTALLED = True
except ModuleNotFoundError:

    class HttpRequest:  # type: ignore
        """Dummy HttpRequest class."""

    class BaseEngine:  # type: ignore
        """Dummy BaseEngine class."""

    class TemplateSyntaxError(Exception):  # type: ignore
        """Dummy TemplateSyntaxError class."""

    class TemplateDoesNotExist(Exception):  # type: ignore
        """Dummy TemplateDoesNotExist class."""

    def csrf_token_lazy(request: t.Any) -> t.Any:
        """Dummy csrf_token_lazy function."""
        return request

    def get_app_template_dirs(dirname: str) -> t.Tuple[Path, ...]:
        """Dummy get_app_template_dirs function."""
        return tuple(Path(dirname).iterdir())

    DJANGO_INSTALLED = False


class NotFound(Exception):
    """Template not found."""


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


class EngineOptions(TypedDict):
    """Engine options."""

    mock_context: NotRequired[t.Any]


class Environment:
    """Templates environment."""

    def __init__(self, mock_context: t.Any = None) -> None:
        """Initialize object."""
        if not DJANGO_INSTALLED:
            raise RuntimeError(
                "Cannot use Django template engine, Django is not installed."
            )

        self.app_dirs = get_app_template_dirs(dirname="templates")
        self.templates = {}

        cwd = Path.cwd()
        for _dir in self.app_dirs:
            for template in _dir.glob("**/*.py"):
                if "styles" in template.parts:
                    continue
                template = template.relative_to(cwd)
                app, _, *path, name = template.parts
                if name == "__init__.py":
                    path = [app, *path]
                    fullname = ".".join(template.parts[:-1])
                else:
                    name = name.replace(".py", "")
                    path = [app, *path, name]
                    fullname = ".".join([*template.parts[:-1], name])

                module = SourceFileLoader(  # pylint: disable=deprecated-method,no-value-for-parameter
                    fullname=fullname,
                    path=str(template),
                ).load_module()
                self.templates[".".join(path)] = module
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
            raise NotFound(f"Template '{name}' not found")

        template = getattr(module, cls, None)
        if template is None:
            raise AttributeError(f"View '{cls}' not found in template {name}")
        return Template(template=template, view=module.__name__)


class PH7Templates(BaseEngine):
    """PH7 templates backend for django."""

    def __init__(self, params: t.Dict[str, t.Any]) -> None:
        """Initialize object."""
        self.options = EngineOptions(params.pop("OPTIONS"))  # type: ignore
        self.environment = Environment(
            mock_context=self.options.get("mock_context"),
        )
        super().__init__(params)

    @property
    def app_dirname(self) -> str:
        """App directory"""
        return "templates"

    def from_string(self, template_code: str) -> None:
        """Load from string."""
        raise TemplateSyntaxError(
            "PH7 Does not have support for loading templates from string."
        )

    def get_template(self, template_name: str) -> "Template":
        """Get PH7 template."""
        try:
            return self.environment.get(template_name)
        except AttributeError as e:
            raise TemplateSyntaxError(
                f"Invalid template; '{template_name}' "
                "does not have 'template' attribute"
            ) from e
        except NotFound as e:
            raise TemplateDoesNotExist(e.args, backend=self) from e


class Template:
    """Template class."""

    def __init__(self, template: HtmlNode, view: str) -> None:
        """Initialize object."""
        self.view = view
        self.template = template

    def render(
        self,
        context: t.Optional[t.Dict] = None,
        request: t.Optional[HttpRequest] = None,
        stream: bool = False,
    ):
        """Render template."""
        if context is None:
            context = {}
        if request is not None:
            context["request"] = request
            context["csrf_token"] = csrf_token_lazy(request)
        context["_view"] = self.view
        if stream:
            return self.template.stream(context=context)
        return self.template.render(context)
