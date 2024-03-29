from ph7.html import body, div, head, html, title

template = html(
    head(
        title("HTML Attributes"),
    ),
    body(
        div(
            div(
                "Example for different attributes",
                class_name=["text", "bold", "teal"],
                id="child",
            ),
            div(
                "Clickable div",
                on={
                    "click": "sayHello",
                },
            ),
            class_name="container",
            id="container",
        )
    ),
    lang="en",
)

print(template)
