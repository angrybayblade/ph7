"""Template engine implementation."""

import types
import typing as t
from importlib.machinery import SourceFileLoader
from pathlib import Path

from django.http.request import HttpRequest
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
from django.template.utils import get_app_template_dirs
from typing_extensions import TypedDict

from ph7.base import node


class NotFound(Exception):
    """Template not found."""


class EngineOptions(TypedDict):
    """Engine options."""


class Environment:
    """Templates environment."""

    def __init__(self) -> None:
        """Initialize object."""
        self.app_dirs = get_app_template_dirs(dirname="templates")
        self.templates = {}

        cwd = Path.cwd()
        for _dir in self.app_dirs:
            for template in _dir.glob("**/*.py"):
                template = template.relative_to(cwd)
                if template.name in ("__init__.py", "base.py", "styles.py"):
                    continue
                app, _, *path, name = template.parts
                name = name.replace(".py", "")
                path = [app, *path, name]
                module = SourceFileLoader(
                    fullname=".".join(
                        [*template.parts[:-1], template.name.replace(".py", "")]
                    ),
                    path=str(template),
                ).load_module()
                self.templates["/".join(path)] = module
                if name == "index":
                    self.templates["/".join(path[:-1])] = module

    def get(self, name: str) -> types.ModuleType:
        """Get PH7 node for `name`"""
        if name not in self.templates:
            raise NotFound(f"Template '{name}' not found")
        return self.templates[name]


class PH7Templates(BaseEngine):
    """PH7 templates backend for django."""

    def __init__(self, params: t.Dict[str, t.Any]) -> None:
        """Initialize object."""
        self.options = EngineOptions(params.pop("OPTIONS"))  # type: ignore
        self.environment = Environment()

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
            module = self.environment.get(template_name)
            return Template(template=module.template, view=module.__name__)
        except AttributeError:
            raise TemplateSyntaxError(
                f"Invalid template; '{template_name}' "
                "does not have 'template' attribute"
            )
        except NotFound as exc:
            raise TemplateDoesNotExist(exc.args, backend=self)


class Template:
    """Template class."""

    def __init__(self, template: node, view: str) -> None:
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
            context["csrf_input"] = csrf_input_lazy(request)
            context["csrf_token"] = csrf_token_lazy(request)
        context["_view"] = self.view
        if stream:
            return self.template.stream(context=context)
        return self.template.render(context)
