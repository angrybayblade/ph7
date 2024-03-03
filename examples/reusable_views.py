from ph7.html import body, div, html

text = div(
    style={
        "font_size": "16px",
        "font_weight": "600",
        "letter_spacing": "0.75px",
    }
)

template = html(
    body(
        div(
            text("Text 1"),
            text("Text 2"),
            text("Text 3", class_name=["active"]),
        )
    )
)

print(template)
