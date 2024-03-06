## Writing HTML
Writing HTML with PH7 might be a bit weird at first since it does not follow the open/close bracket format. But once you get used to it, it can be ridiculously fast with autocomplete and type checking.
<!-- {"type": "html", "file": "examples/simple_html.py"} -->
```python
from ph7.html import body, div, h1, head, html, title

template = html(
    head(
        title(
            "H1 Tag Example",
        ),
    ),
    body(
        div(
            h1(
                "This is an example of H1 tag",
            )
        )
    ),
)

print(template)
```

```html
<html>
  <head>
    <title>H1 Tag Example</title>
  </head>
  <body>
    <div>
      <h1>This is an example of H1 tag</h1>
    </div>
  </body>
</html>
```
<!-- end -->
## Attributes
HTML attributes can be passed down as function arguments, all of the HTML tag functions are defined with arguments representing the attributes as keyword arguments so you that can also utilise your autocomplete for faster development.
<!-- {"type": "html", "file": "examples/attributes.py"} -->
```python
from ph7.html import body, div, h1, head, html, title

template = html(
    head(
        title("HTML Attributes"),
    ),
    body(
        div(
            div(
                "Example for different attributes",
                class_name=["text", "bold", "teal"],
                id="child",
            ),
            div(
                "Clickable div",
                handlers={
                    "onclick": "sayHello",
                },
            ),
            class_name="container",
            id="container",
        )
    ),
    lang="en",
)

print(template)
```

```html
<html lang="en">
  <head>
    <title>HTML Attributes</title>
  </head>
  <body>
    <div id="container" class="container">
      <div id="child" class="text bold teal">Example for different attributes</div>
      <div onclick='sayHello()'>Clickable div</div>
    </div>
  </body>
</html>
```
<!-- end -->
## Placeholders
PH7 allows you to define placeholders for data which can be filled out at when rendering a view using `context` argument.
A placeholder can be defined with a default value
```
Hello ${name|John Doe}
```
and without a default value
```
Hello ${name}
```
<!-- {"type": "html", "file": "examples/placeholders.py"} -->
```python
from ph7.html import body, div, html

template = html(
    body(
        div(
            "Hello, ${name|John Doe}, I'm ${age} years old and I like ${food|Coffee}",
        )
    )
)

print(template.render(context={"name": "Jane Doe", "age": 24}))
```

```html
<html>
  <body>
    <div>Hello, Jane Doe, I'm 24 years old and I like Coffee</div>
  </body>
</html>
```
<!-- end -->
Not providing value for placeholder without default value will result in error
<!-- {"type": "text", "file": "examples/missing_placeholders.py", "lines": {"output":[-1, null]}} -->
```python
from ph7.html import body, div, html

template = html(
    body(
        div(
            "Hello, ${name|John Doe}, I'm ${age} years old and I like ${food|Coffee}",
        )
    )
)

print(template)
```

```text
ValueError: Error rendering 'Hello, ${name|John Doe}, I'm ${age} years old and I like ${food|Coffee}'; Value for 'age' not provided
```
<!-- end -->
## Reusable views
You can define empty views with specific attributes and hydrate them later with data. When hydrating or rehydrating a view, you can also override the attributes.
<!-- {"type": "html", "file": "examples/reusable_views.py"} -->
```python
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
```

```html
<html>
  <body>
    <div>
      <div style="font-size:16px;font-weight:600;letter-spacing:0.75px">Text 1</div>
      <div style="font-size:16px;font-weight:600;letter-spacing:0.75px">Text 2</div>
      <div class="active" style="font-size:16px;font-weight:600;letter-spacing:0.75px">Text 3</div>
    </div>
  </body>
</html>
```
<!-- end -->
## Overridable views
You can define a block as overridable by using `overridable` method, these blocks can be filled with content when hydrating/rehydrating the parent component.
<!-- {"type": "html", "file": "examples/overridable_views.py"} -->
```python
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
```

```html
<html>
  <title>Templates Example</title>
  <body>
    <div class="nav">
      <div>
        <div class="btn btn-primary active">Home</div>
        <div class="btn btn-primary">About Us</div>
        <div class="btn btn-primary">Contact Us</div>
      </div>
    </div>
    <div class="container">
      <div class="flex-center">
        <div class="greeting">Hello Jane Doe</div>
      </div>
    </div>
    <div class="footer">© Organisation 2024 | Made by <a href="https://github.com/angrybayblade">angrybayblade</a></div>
  </body>
</html>
```
<!-- end -->
Using overridable views and reusable views you can create a modular and reusable codebase and save a lot of time an effort in the process.
## Function As View
You can define your view as a python function create views based on conditions, using for loops or any other kind of logical operation to build your view.
<!-- {"type": "html", "file": "examples/function_as_view.py"} -->
```python
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

print("<!-- With `number_of_users` parameter -->\n")
print(template.render(context={"number_of_users": 5}), end="\n\n")

print("<!-- Without `number_of_users` parameter -->\n")
print(template.render(context={}))
```

```html
<!-- With `number_of_users` parameter -->
<html>
  <body>
    <div class="user">
      <div class="user">User 0</div>
      <div class="user">User 1</div>
      <div class="user">User 2</div>
      <div class="user">User 3</div>
      <div class="user">User 4</div>
    </div>
  </body>
</html>
<!-- Without `number_of_users` parameter -->
<html>
  <body>
    <div class="error">Error, Users not found</div>
  </body>
</html>
```
<!-- end -->
## Caching
Since you can define your views as python functions you can also use caching utilities like `functools.lru_cache` to reduce rendering time.
<!-- {"type": "stdout", "file": "examples/cacheable_view.py"} -->
```python
import time
import typing as t
from functools import lru_cache

from ph7.html import body, div, html, node

user = div(class_name="user")
users = div(class_name="user")
nousers = div("Error, Users not found", class_name="error")


@lru_cache
def _render_users(n: int) -> node:
    """Render users."""
    return users(user(f"User {i}") for i in range(n))


def render_users(context: t.Dict) -> node:
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
```

```stdout
First render: 6.0718302500000005
Second render: 0.35541508400000055
Third render: 0.38755016700000056
```
<!-- end -->


When making a view cacheable, make sure the view satisfies following constrains

* View only depends on the data provided by the arguments and does not fetch any external data
* View does not return very large objects, or you might run into out of memory error after a while. If a view returns very large objects and you still want to cache it, you can use a smaller cache stack size on `functools.lru_cache`.
