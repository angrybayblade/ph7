from static_files.templates import styles as stylesheet

from ph7.context import ctx
from ph7.html import body, div, head, html, title

ctx.static.view(__name__)


template = html(
    title("Static Files Example"),
    head(
        ctx.static.include,
    ),
    body(
        div(
            "Hello, World!",
            class_name=stylesheet.container,
        )
    ),
)
