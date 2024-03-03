## PH7 Template Engine
To configure your Django application to use PH7 templates, update `settings.py` to use PH7's Django template engine.
```python
TEMPLATES = [
    {
        "NAME": "PH7",
        "BACKEND": "ph7.django.PH7Templates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]
```
## Write Templates
```bash
|_ app
 |_ templates
   |_ __init__.py # default view
```
Define your view in `__init__.py`, when defining the view you need to name the default view `template`, for example
```python
from ph7.html import body, html, title, div
template = html(
    title("Hello World"),
    body(
        div(
            "Hello, World!",
        )
    )
)
```
When rendering the view, refer to this template using relative path
```python
from django.shortcuts import render
def home(request):
    return render(
        request=request,
        template_name="app" # or "app.index",
    )
```
If you name your view anything other than `template`, you can specify the view name using `module:view` format. For example if you name your view `home`, you can specify the template as `app:home`.
