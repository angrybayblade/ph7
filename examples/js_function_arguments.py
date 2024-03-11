from ph7 import include
from ph7.html import body, button, div, head, html, img, node
from ph7.js import document, fetch, js_callable


@js_callable
async def fetchUserProfilePicture(user: str) -> None:
    response = await fetch(
        "/api/users/" + user,
        {"method": "GET"},
    )
    data = await response.json()
    document.getElementById(f"image-{user}").src = data.profile_picture


def _user(name: str) -> node:
    return div(
        img(src="#", style={"height": "200px", "width": "400px"}, id=f"image-{name}"),
        button(
            f"Click to fetch {name}'s  profile picture.",
            on={
                "click": fetchUserProfilePicture(name),
            },
        ),
    )


def _users(context: dict) -> node:
    """List users."""
    return div(_user(name=name) for name in context["users"])


template = html(
    head(
        include(fetchUserProfilePicture),
    ),
    body(
        _users,
    ),
)

print(template.render(context={"users": ["john.doe", "jane.doe"]}))
