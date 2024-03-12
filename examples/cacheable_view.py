import time
import typing as t
from functools import lru_cache

from ph7.html import body, div, html, HtmlNode

user = div(class_name="user")
users = div(class_name="user")
nousers = div("Error, Users not found", class_name="error")


@lru_cache
def _render_users(n: int) -> HtmlNode:
    """Render users."""
    return users(user(f"User {i}") for i in range(n))


def render_users(context: t.Dict) -> HtmlNode:
    """Render users."""
    if "number_of_users" not in context:
        return nousers
    return _render_users(n=context["number_of_users"])


template = html(
    body(
        render_users,
    )
)

tick = time.perf_counter()
template.render(context={"number_of_users": 300000})
print(f"First render: {time.perf_counter() - tick}")

tick = time.perf_counter()
template.render(context={"number_of_users": 300000})
print(f"Second render: {time.perf_counter() - tick}")

tick = time.perf_counter()
template.render(context={"number_of_users": 300000})
print(f"Third render: {time.perf_counter() - tick}")
