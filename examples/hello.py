from ph7.html import body, div, html

template = html(
    body(
        div(
            "Hello, World!",
        )
    )
)

print(template)
