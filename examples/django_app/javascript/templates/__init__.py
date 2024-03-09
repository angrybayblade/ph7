from ph7.html import body, button, div, head, html, img
from ph7.context import ctx
from javascript.templates.script import fetchDog
from javascript.templates.styles import main, image

ctx.static.view(__name__)

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
            button(
                "Click to fetch a dog",
                handlers={
                    "onclick": fetchDog(),
                },
            ),
            class_name=main,
        )
    ),
)


if __name__ == "__main__":
    print(template.render({"_view": __name__}))
