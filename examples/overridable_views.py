from ph7.html import a, body, div, html, title

button = div(class_name=["btn", "btn-primary"])

base = html(
    title("Templates Example"),
    body(
        div(class_name="nav").overridable("navbar"),
        div(class_name="container").overridable("container"),
        div(
            "© Organisation 2024 | Made by ",
            a("angrybayblade", href="https://github.com/angrybayblade"),
            class_name="footer",
        ),
    ),
)

template = base(
    navbar=div(
        button("Home", class_name=["btn", "btn-primary", "active"]),
        button("About Us"),
        button("Contact Us"),
    ),
    container=div(
        div(
            "Hello ",
            "${name|John Doe}",
            class_name="greeting",
        ),
        class_name="flex-center",
    ),
)

print(template.render(context={"name": "Jane Doe"}))
