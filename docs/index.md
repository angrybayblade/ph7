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

## Next Steps

* [Writing HTML](/html)
* [Writing CSS](/ph7/css)
* [Writing JS](/ph7/js)
* [Django Integration](/ph7/django)