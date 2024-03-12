from javascript.templates.script import fetchDog
from javascript.templates.styles import container, image

from ph7.context import ctx
from ph7.html import body, button, div, head, html, img

ctx.static.view(__name__)


def _fetch():
    return button(
        "Click to fetch a dog",
        on={
            "click": fetchDog(),
        },
    )


template = html(
    head(
        ctx.static.include,
    ),
    body(
        div(
            img(
                src="#",
                id="image",
                alt="Click to fetch dog",
                class_name=image,
            ),
            _fetch,
            class_name=container,
        )
    ),
)


if __name__ == "__main__":
    print(template.render({"_view": __name__}))
