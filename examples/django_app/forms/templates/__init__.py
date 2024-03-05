from django import forms

from ph7.context import ctx
from ph7.html import body, div, form, head, html, title

ctx.static.view(__name__)


class UserForm(forms.Form):
    """User form class."""

    name = forms.CharField(label="username")
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password", widget=forms.PasswordInput())


template = html(
    title("Forms Example"),
    head(
        ctx.static.include,
    ),
    body(
        div(
            form(
                UserForm(),
            ),
        )
    ),
)
