## Install
```
pip3 install ph7
```
## Quickstart
Write your first block of markup
<!-- {"type": "html", "file": "examples/hello.py"} -->
```python
from ph7.html import body, div, html

template = html(
    body(
        div(
            "Hello, World!",
        )
    )
)

print(template)
```

```html
<html>
  <body>
    <div>Hello, World!</div>
  </body>
</html>
```
<!-- end -->

Add some style

![Stylesheet Autocomplete](/img/style-autocomplete.gif)

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

Or use `CSSObject` to define reusable stylesheets.

<!-- {"type": "html", "file": "examples/css_nesting.py"} -->
```python
from ph7 import CSSObject, include
from ph7.html import body, div, head, html


class flex_center(CSSObject):
    """Flex center."""

    display = "flex"
    align_items = "center"
    justify_content = "center"


class textbox(flex_center):
    """Text container."""

    height = "100vh"
    width = "100vw"

    class text(CSSObject):
        """Text styling."""

        font_size = "12px"
        font_weight = "500"
        font_family = "Lucida Console, Monaco, monospace"


template = html(
    head(
        include(textbox, minify=True),
    ),
    body(
        div(
            div(
                "Hello, World!",
                class_name=[textbox.text],
            ),
            class_name=[textbox],
        )
    ),
)

print(template)
```

```html
<html>
  <head>
    <style>
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
  </head>
  <body>
    <div class="textbox">
      <div class="text">Hello, World!</div>
    </div>
  </body>
</html>
```
<!-- end -->

> Note: use `include` function for development only, for production use static context to include stylsheets.

---
## Next Steps
- [Writing HTML](/html)
- [Writing CSS](/css)
