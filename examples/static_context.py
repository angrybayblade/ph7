from examples.script import alertHello
from examples.style import textbox
from ph7.context import ctx
from ph7.html import body, div, head, html

ctx.static.view(__name__)


template = html(
    head(
        ctx.static.include,
    ),
    body(
        div(
            div(
                "Click Here",
                class_name=[textbox.text],
                handlers={
                    "onclick": alertHello("John Doe"),
                },
            ),
            class_name=[textbox],
        )
    ),
)

print(template.render(context={"_view": __name__}))
