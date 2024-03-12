from ph7 import CSSObject, include
from ph7.html import body, div, head, html


class flex_center(CSSObject):
    display = "flex"
    align_items = "center"
    justify_content = "center"


template = html(
    head(
        include(flex_center),
    ),
    body(
        div(
            div(
                "Hello, World!",
            ),
            class_name=[flex_center],
        )
    ),
)

print(template)
