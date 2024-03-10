from django import forms

from ph7.django import csrf_token
from ph7.html import body, button, div, form, html, title


class UserForm(forms.Form):
    """User form class."""

    name = forms.CharField(label="username")
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password", widget=forms.PasswordInput())


template = html(
    title("Forms Example"),
    body(
        div(
            form(
                UserForm(),
                csrf_token,
                button("submit", type="submit"),
            ),
        )
    ),
)
