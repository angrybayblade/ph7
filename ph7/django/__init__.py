"""Django template engine."""

import typing as t

from django.http import HttpRequest, HttpResponse, StreamingHttpResponse
from django.template.loader import get_template

from ph7.django.engine import PH7Templates, Template
from ph7.html import input, node


def csrf_token(context: t.Dict) -> node:
    """CSRF Token input generator."""
    return input(
        hidden="true",
        value=context["csrf_token"],
        id="csrfmiddlewaretoken",
        name="csrfmiddlewaretoken",
    )


def render(  # pylint: disable=too-many-arguments
    request: HttpRequest,
    template_name: str,
    context: t.Optional[t.Dict] = None,
    content_type: t.Optional[str] = None,
    status: t.Optional[int] = None,
    using: t.Optional[str] = None,
    stream: bool = False,
):
    """Render a template with given settings."""
    template = t.cast(Template, get_template(template_name, using=using))
    content = template.render(
        context=context,
        request=request,
        stream=stream,
    )
    if not stream:
        return HttpResponse(
            content=content,
            content_type=content_type,
            status=status,
        )
    return StreamingHttpResponse(
        streaming_content=content,
        content_type=content_type,
        status=status,
    )


__all__ = (
    "PH7Templates",
    "render",
)
