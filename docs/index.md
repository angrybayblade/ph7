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

## Next Steps

* [Writing HTML](/html)
* [Writing CSS](/css)
* [Writing JS](/js)
* [Django Integration](/django)