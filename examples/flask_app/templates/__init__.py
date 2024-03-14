from ph7.context import ctx
from ph7.html import body, div, head, html

template = html(
    head(
        ctx.static.include,
    ),
    body(
        div(
            "Hello, World!",
        )
    ),
)
