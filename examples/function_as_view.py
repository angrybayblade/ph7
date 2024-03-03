import typing as t

from ph7.html import body, div, html, node

user = div(class_name="user")
users = div(class_name="user")
nousers = div("Error, Users not found", class_name="error")


def render_users(context: t.Dict) -> node:
    """Render users."""
    if "number_of_users" not in context:
        return nousers
    return users(user(f"User {i}") for i in range(context["number_of_users"]))


template = html(
    body(
        render_users,
    )
)

print("With `number_of_users` parameter")
print(template.render(context={"number_of_users": 5}), end="\n\n")

print("Without `number_of_users` parameter")
print(template.render(context={}))
