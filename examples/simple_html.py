from ph7.html import body, div, h1, head, html, title

template = html(
    head(
        title(
            "H1 Tag Example",
        ),
    ),
    body(
        div(
            h1(
                "This is an example of H1 tag",
            )
        )
    ),
)

print(template)
