 <div style="display:flex; align-items: center; justify-content: center;">
    <h1>💧 PH7</h1>
</div>
<div style="display:flex; align-items: center; justify-content: center;">
    Python native HTML rendering
</div>

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


Links:

* [Documentation](http://ph7.angrybayblade.me)
* [Changelog](https://github.com/angrybayblade/ph7/blob/main/docs/CHANGELOG)
* [Issue Tracker](https://github.com/angrybayblade/ph7/issues)
