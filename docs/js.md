> Currently PH7 has very limited JavaScript support

## Functions

You can write Python functions as JavaScript functions with limited WebApis. You can directly refer the function as event handler, PH7 will take care of the rest.

<!-- {"type": "html", "file": "examples/js_function.py"} -->
```python
from ph7 import include
from ph7.html import body, button, div, head, html, img
from ph7.js import console, document, fetch


async def fetchDog():
    console.log("Fetching dog")
    response = await fetch(
        "https://dog.ceo/api/breeds/image/random",
        {"method": "GET"},
    )
    if response.status != 200:
        response_body = await response.text()
        console.log("Error fetching dog; " + response_body)
        return
    data = await response.json()
    console.log("Dog fetched")
    document.getElementById("image").src = data.message


template = html(
    head(
        include(fetchDog),
    ),
    body(
        div(
            img(
                src="#",
                id="image",
                alt="Click to fetch dog",
                style={"height": "200px", "width": "400px"},
            ),
            button(
                "Click to fetch a dog",
                handlers={
                    "onclick": fetchDog,
                },
            ),
        )
    ),
)

print(template)
```

```html
<html>
  <head>
    <script>
      async function fetchDog() {
        console.log('Fetching dog');
        let response = await fetch('https://dog.ceo/api/breeds/image/random', {
          'method': 'GET'
        });
        if (response.status != 200) {
          let response_body = await response.text();
          console.log('Error fetching dog; ' + response_body);
          return;
        };
        let data = await response.json();
        console.log('Dog fetched');
        document.getElementById('image').src = data.message;
      };
    </script>
  </head>
  <body>
    <div><img src="#" alt="Click to fetch dog" id="image" style="height:200px;width:400px"></img><button onclick=fetchDog()>Click to fetch a dog</button></div>
  </body>
</html>
```
<!-- end -->

## Arguments

You can define function with arguments using `ph7.js.js_callable` decorator.


<!-- {"type": "html", "file": "examples/js_function_arguments.py"} -->
```python
from ph7 import include
from ph7.html import body, button, div, head, html, img, node
from ph7.js import document, fetch, js_callable


@js_callable
async def fetchUserProfilePicture(user: str):
    response = await fetch(
        "/api/users/" + user,
        {"method": "GET"},
    )
    data = await response.json()
    document.getElementById("image-" + user).src = data.profile_picture


def _user(name: str) -> node:
    return div(
        img(src="#", style={"height": "200px", "width": "400px"}, id=f"image-{name}"),
        button(
            f"Click to fetch {name}'s  profile picture.",
            handlers={
                "onclick": fetchUserProfilePicture(user=name),
            },
        ),
    )


def _users(context: dict) -> node:
    """List users."""
    return div(_user(name=name) for name in context["users"])


template = html(
    head(
        include(fetchUserProfilePicture),
    ),
    body(
        _users,
    ),
)

print(template.render(context={"users": ["john.doe", "jane.doe"]}))
```

```html
<html>
  <head>
    <script>
      async function fetchUserProfilePicture(user) {
        let response = await fetch('/api/users/' + user, {
          'method': 'GET'
        });
        let data = await response.json();
        document.getElementById('image-' + user).src = data.profile_picture;
      };
    </script>
  </head>
  <body>
    <div>
      <div><img src="#" id="image-john.doe" style="height:200px;width:400px"></img><button onclick=fetchUserProfilePicture('john.doe')>Click to fetch john.doe's profile picture.</button></div>
      <div><img src="#" id="image-jane.doe" style="height:200px;width:400px"></img><button onclick=fetchUserProfilePicture('jane.doe')>Click to fetch jane.doe's profile picture.</button></div>
    </div>
  </body>
</html>
```
<!-- end -->

These function calls are also type checkable.

## Static Context

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
                handlers={
                    "onclick": alertHello("John Doe"),
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
    <script id="js.examples.script">
      function alertHello(user) {
        alert('Hello, ' + user);
      }
    </script>
  </head>
  <body>
    <div class="textbox">
      <div class="text" onclick=alertHello('John Doe')>Click Here</div>
    </div>
  </body>
</html>
```
<!-- end -->

<!-- {"type": "html", "file": "examples/static_context.py", "env": {"DEVELOPMENT": "0"}} -->
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
                handlers={
                    "onclick": alertHello("John Doe"),
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
    <link href="/static/css/examples_style.css" rel="stylesheet" id="css.examples.style" />
    <script src="/static/js/examples_script.js" id="js.examples.script"></script>
  </head>
  <body>
    <div class="textbox">
      <div class="text" onclick=alertHello('John Doe')>Click Here</div>
    </div>
  </body>
</html>
```
<!-- end -->

<!-- {"type": "js", "cmd": ["cat", "static/js/examples_script.js"], "env": {"DEVELOPMENT": "0"}} -->
```bash
$ cat static/js/examples_script.js
```

```js
function alertHello(user) {
  alert('Hello, ' + user);
}
```
<!-- end -->
