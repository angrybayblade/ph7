from django import forms

from ph7.html import body, div, form, html, title


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
            ),
        )
    ),
)
