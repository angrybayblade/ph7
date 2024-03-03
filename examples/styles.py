"""Simple hello example."""

from ph7.html import body, div, html

template = html(
    body(
        div(
            "Hello, World!",
            style={
                "height": "100vh",
                "width": "100vw",
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
            },
        )
    )
)

print(template)
