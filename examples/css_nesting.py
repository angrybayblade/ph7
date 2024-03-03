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

    class text(CSSObject):
        """Text styling."""

        font_size = "12px"
        font_weight = "500"
        font_family = "Lucida Console, Monaco, monospace"


template = html(
    head(
        include(textbox, minify=True),
    ),
    body(
        div(
            div(
                "Hello, World!",
                class_name=[textbox.text],
            ),
            class_name=[textbox],
        )
    ),
)

print(template)
