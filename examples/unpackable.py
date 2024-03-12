import typing as t

from ph7 import kebabc, titlec
from ph7.html import HtmlNode, a, body, div, html, title, unpack

NAVIGATION = [
    "home",
    "about_us",
    "contact_us",
]

button = div(class_name=[kebabc.btn, kebabc.btn_primary])
navbar = div(class_name="nav").overridable("navbar")

base = html(title("Templates Example"), body(navbar, unpack().overridable("container")))


def render_navbar(context: t.Dict) -> HtmlNode:
    """Render navbar"""

    def _btn(page: str) -> HtmlNode:
        return button(
            a(
                titlec(page),
                href=f"/{page}",
                class_name=kebabc.active if page == context["page"] else "",
            )
        )

    return div(
        (_btn(page=page) for page in NAVIGATION),
        class_name="navigation",
    )


template = base(
    navbar=render_navbar,
    container=(
        div("Hello"),
        div("World"),
    ),
)

template.write(
    file="index.html",
    context={
        "n": 10,
        "page": "home",
    },
)
