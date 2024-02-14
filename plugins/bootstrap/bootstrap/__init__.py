"""Bootstrap helper."""

from ph7.html import link, script

from . import css

css_minified = link(
    rel="stylesheet",
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
    crossorigin="anonymous",
)

css_optional = link(
    rel="stylesheet",
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap-theme.min.css",
    crossorigin="anonymous",
)

js_minified = script(
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
    crossorigin="anonymous",
)

__all__ = (
    "css",
    "css_minified",
    "css_optional",
    "js_minified",
)
