 <div style="display:flex; align-items: center; justify-content: center;">
    <h1>💧 PH7</h1>
</div>
<div style="display:flex; align-items: center; justify-content: center;">
    Python native HTML rendering
</div>

## Why PH7?

* Native to python
* More code modularity
* Easy to write reusable components
* Out of the box editor support
    * Syntax highlighting
    * Code navvigation tools
    * Auto-completion
*  Type safety using MyPy


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

Or write a CSS class

<!-- {"type": "css", "file": "examples/css_example.py"} -->
```python
from ph7.css import CSSObject


class flex_center(CSSObject):
    """Flex center"""

    display = "flex"
    align_items = "center"
    justify_content = "center"


print(flex_center())
```

```css
.flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}
```
<!-- end -->

Or use python function as JavaScript function


<!-- {"type": "js", "file": "examples/js_example.py"} -->
```python
from ph7.js import as_js, console, document, fetch


async def fetchDog():
    response = await fetch(
        "https://dog.ceo/api/breeds/image/random",
        {"method": "GET"},
    )
    if response.status != 200:
        response_body = await response.text()
        console.log(f"Error fetching dog; {response_body}")
        return
    data = await response.json()
    document.getElementById("image").src = data.message


print(as_js(fetchDog))
```

```js
async function fetchDog() {
  let response = await fetch('https://dog.ceo/api/breeds/image/random', {
    'method': 'GET'
  });
  if (response.status != 200) {
    let response_body = await response.text();
    console.log('Error fetching dog; ' + response_body);
    return;
  };
  let data = await response.json();
  document.getElementById('image').src = data.message;
};
```
<!-- end -->

PH7 is still in beta-development. It will be production ready with following enhancements

- [ ] Remove performance bottlenecks
- [ ] Unit testing support

Further improvements

- [ ] Typed context for type safety

Links:

* [Documentation](http://ph7.angrybayblade.me)
* [Changelog](https://github.com/angrybayblade/ph7/blob/main/docs/CHANGELOG)
* [Issue Tracker](https://github.com/angrybayblade/ph7/issues)
