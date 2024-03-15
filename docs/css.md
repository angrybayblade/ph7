## Adding Style

Use `style` attribute to add style to a view. The `style` attribute is defined using a `TypedDict` object which means it's a type constrained dictionary. What this means is, you can utilise the autocomplete from your IDE for writing code faster. And since it's type constriained you can also utilise a tool like `mypy` to make sure you are not defining any wrong attributes.
![Autocomplete](/img/style-autocomplete.gif)

<!-- {"type": "html", "file": "examples/styles.py"} -->
```python
"""Simple hello example."""

from ph7.html import body, div, html

template = html(
    body(
        div(
            "Hello, World!",
            style={
                "height": "100vh",
                "width": "100vw",
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
            },
        )
    )
)

print(template)
```

```html
<html>
  <body>
    <div style="height:100vh;width:100vw;display:flex;align-items:center;justify-content:center">Hello, World!</div>
  </body>
</html>
```
<!-- end -->

> The style object get's rendered and cached at the object initialization for faster template rendering.

## CSSObject

Using `style` object is not the only way to develop CSS with PH7, You can utilise a special class called `CSSObject` to define stylesheets.

<!-- {"type": "html", "file": "examples/css_cls.py", "class": "side-by-side"} -->
<div class='side-by-side'>
```python
from ph7 import CSSObject, include
from ph7.html import body, div, head, html


class flex_center(CSSObject):
    display = "flex"
    align_items = "center"
    justify_content = "center"


template = html(
    head(
        include(flex_center),
    ),
    body(
        div(
            div(
                "Hello, World!",
            ),
            class_name=[flex_center],
        )
    ),
)

print(template)
```

```html
<html>
  <head>
    <style>
      .flex-center {
        display: flex;
        align-items: center;
        justify-content: center;
      }
    </style>
  </head>
  <body>
    <div class="flex-center">
      <div>Hello, World!</div>
    </div>
  </body>
</html>
```
</div>
<!-- end -->

A `CSSObject` can also be reused via class inheritance. You can define a base CSS class and reuse it however many times you like.

<!-- {"type": "css", "file": "examples/css_inherit.py", "class": "side-by-side"} -->
<div class='side-by-side'>
```python
from ph7 import CSSObject


class flex_center(CSSObject):
    display = "flex"
    align_items = "center"
    justify_content = "center"


class textbox(flex_center):
    height = "100vh"
    width = "100vw"


print(textbox())
```

```css
.textbox {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
}
```
</div>
<!-- end -->

Furthermore `CSSObject` also allows for nesting by sub classes.

<!-- {"type": "css", "file": "examples/css_nesting.py", "class": "side-by-side"} -->
<div class='side-by-side'>
```python
from ph7 import CSSObject


class flex_center(CSSObject):
    display = "flex"
    align_items = "center"
    justify_content = "center"


class textbox(flex_center):
    height = "100vh"
    width = "100vw"

    class text(CSSObject):
        font_size = "12px"
        font_weight = "500"
        font_family = "Lucida Console, Monaco, monospace"


print(textbox())
```

```css
.textbox {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
}
.textbox .text {
  font-size: 12px;
  font-weight: 500;
  font-family: Lucida Console, Monaco, monospace;
}
```
</div>
<!-- end -->

To make your styles more manageable and reusable, you can define the styles in a separate module and import them throughout your codebase. Following section provides an example of a reusable stylesheet module.

## Pseudo Classes and Elements

A pseudo class can be defined by adding `_` at the beginning of class name, for selecting a child you can set `child` parameter. For pseudo, elements add `__` at the beginning of the class name.

<!-- {"type": "css", "file": "examples/css_pseudo_class.py", "class": "side-by-side"} -->
<div class='side-by-side'>
```python
from ph7 import CSSObject


class item(CSSObject):
    height = "30px"
    width = "100%"

    margin_top = "5px"

    class _nth_child(CSSObject, n=1):
        margin_top = "0px"

    class __before(CSSObject):
        content = '">"'


print(item())
```

```css
.item {
  height: 30px;
  width: 100%;
  margin-top: 5px;
}
.item::before {
  content: ">";
}
.item:nth-child(1) {
  margin-top: 0px;
}
```
</div>
<!-- end -->


## Static Context

PH7 has a runtime context object which can be used for managing the static resource. To use a static context, import `ph7.context.ctx`, add `ctx.static.view(__name__)` at the top of your template and add `ctx.static.include` in your view. In the following example we'll use an external stylesheet for styling our view.

<!-- {"type": "html", "file": "examples/static_context.py", "env": {"DEVELOPMENT": "1"}} -->
```python
from examples.script import alertHello
from examples.style import textbox
from ph7.context import ctx
from ph7.html import body, div, head, html

ctx.static.view(__name__)


template = html(
    head(
        ctx.static.include,
    ),
    body(
        div(
            div(
                "Click Here",
                class_name=[textbox.text],
                on={
                    "click": alertHello("John Doe"),
                },
            ),
            class_name=[textbox],
        )
    ),
)

print(template.render(context={"_view": __name__}))
```

```html
<html>
  <head>
    <style id="css.examples.style">
      .textbox {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100vw;
      }
      .textbox .text {
        font-size: 12px;
        font-weight: 500;
        font-family: Lucida Console, Monaco, monospace;
      }
    </style>
    <script type="text/javascript" id="js.examples.script">
      function alertHello(user) {
        alert('Hello, ' + user);
      }
    </script>
  </head>
  <body>
    <div class="textbox">
      <div class="text" onclick="alertHello('John Doe')">Click Here</div>
    </div>
  </body>
</html>
```
<!-- end -->

As you can see, the static context collects the various static resources and includes them as part of the view. The output above is produced with the mode set to development by exporting `DEVELOPMENT="1"`. When not in development mode, PH7 will compile static resources, write them as files and reference those files. Here's and example of production render of the same template

<!-- {"type": "html", "file": "examples/static_context.py", "env": {"DEVELOPMENT": "0"}, "output_only": true} -->
```html
<html>
  <head>
    <link href="/static/css/examples_style.css" rel="stylesheet" id="css.examples.style" />
    <script src="/static/js/examples_script.js" type="text/javascript" id="js.examples.script"></script>
  </head>
  <body>
    <div class="textbox">
      <div class="text" onclick="alertHello('John Doe')">Click Here</div>
    </div>
  </body>
</html>
```
<!-- end -->

And here's what the CSS file looks like.

<!-- {"type": "css", "cmd": ["cat", "static/css/examples_style.css"], "env": {"DEVELOPMENT": "0"}} -->
```bash
$ cat static/css/examples_style.css
```

```css
.textbox {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
}
.textbox .text {
  font-size: 12px;
  font-weight: 500;
  font-family: Lucida Console, Monaco, monospace;
}
```
<!-- end -->
