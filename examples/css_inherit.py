from ph7 import CSSObject, include
from ph7.html import body, div, head, html


class flex_center(CSSObject):
    """Flex center."""

    display = "flex"
    align_items = "center"
    justify_content = "center"


class textbox(flex_center):
    """Text container."""

    height = "100vh"
    width = "100vw"


template = html(
    head(
        include(textbox, minify=True),
    ),
    body(
        div(
            div(
                "Hello, World!",
                class_name=[textbox],
            ),
            class_name=[textbox],
        )
    ),
)

print(template)
