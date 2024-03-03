from ph7.html import body, div, html

template = html(
    body(
        div(
            "Hello, ${name|John Doe}, I'm ${age} years old and I like ${food|Coffee}",
        )
    )
)

print(template)
