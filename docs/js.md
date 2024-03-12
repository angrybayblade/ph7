Currently PH7 has very limited JavaScript support. But the transpiler API allows you to write your JavaScript code in pure python. PH7 also provides a set of mock APIs that can be used for autocomplete and type checking. 

The list of mock APIs

* `alert`
* `console`
* `fetch`
* `document`

## Functions

Write your functions in python and refer them as event handler, PH7 will take care of the rest.

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
        console.log(f"Error fetching dog; {response_body}")
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
                on={
                    "click": fetchDog,
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
    <script type="text/javascript">
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
    <div><img src="#" alt="Click to fetch dog" id="image" style="height:200px;width:400px" /><button onclick=fetchDog()>Click to fetch a dog</button></div>
  </body>
</html>
```
<!-- end -->

## Arguments

If you want to render a function call with arguments you can decorate a method with `ph7.js.js_callable` and it'll allow you to render function calls with arguments.

<!-- {"type": "html", "file": "examples/js_function_arguments.py"} -->
```python
from ph7 import include
from ph7.html import HtmlNode, body, button, div, head, html, img
from ph7.js import document, fetch, js_callable


@js_callable
async def fetchUserProfilePicture(user: str) -> None:
    response = await fetch(
        "/api/users/" + user,
        {"method": "GET"},
    )
    data = await response.json()
    document.getElementById(f"image-{user}").src = data.profile_picture


def _user(name: str) -> HtmlNode:
    return div(
        img(src="#", style={"height": "200px", "width": "400px"}, id=f"image-{name}"),
        button(
            f"Click to fetch {name}'s  profile picture.",
            on={
                "click": fetchUserProfilePicture(name),
            },
        ),
    )


def _users(context: dict) -> HtmlNode:
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
    <script type="text/javascript">
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
      <div><img src="#" id="image-john.doe" style="height:200px;width:400px" /><button onclick=fetchUserProfilePicture('john.doe')>Click to fetch john.doe's profile picture.</button></div>
      <div><img src="#" id="image-jane.doe" style="height:200px;width:400px" /><button onclick=fetchUserProfilePicture('jane.doe')>Click to fetch jane.doe's profile picture.</button></div>
    </div>
  </body>
</html>
```
<!-- end -->

These function calls are also type checkable.

## Conditionals

<!-- {"type": "js", "file": "examples/js_conditionals.py", "read": "stdout", "class": "side-by-side", "lines": {"input": [3, -11]}} -->
<div class='side-by-side'>
```python
def checkCondition(number: int):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


def fizzBuzz(number: int):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)


def strictEqual(number: int):
    if number % 2 is 0:
        print("even")
    else:
        print("odd")
```

```js
function checkCondition(number) {
  if (number % 2 == 0) {
    console.log('even');
  } else {
    console.log('odd');
  };
}
function fizzBuzz(number) {
  if (number % 3 == 0 && number % 5 == 0) {
    console.log('fizzbuzz');
  } else if (number % 3 == 0) {
    console.log('fizz');
  } else if (number % 5 == 0) {
    console.log('buzz');
  } else {
    console.log(number);
  };
}
function strictEqual(number) {
  if (number % 2 === 0) {
    console.log('even');
  } else {
    console.log('odd');
  };
}
```
</div>
<!-- end -->

## For Loop

<!-- {"type": "js", "file": "examples/js_for_loop.py", "read": "stdout", "class": "side-by-side", "lines": {"input": [3, -11]}} -->
<div class='side-by-side'>
```python
def oddEven(n: int):
    for i in range(n):
        if i % 2 is 0:
            print(i + " is even")
        else:
            print(i + " is odd")


def oddEvenStartEnd(start: int, end: int):
    for i in range(start, end):
        if i % 2 is 0:
            print(i + " is even")
        else:
            print(i + " is odd")


def oddEvenStartEndStep(start: int, end: int, step: int):
    for i in range(start, end, step):
        if i % 2 is 0:
            print(i + " is even")
        else:
            print(i + " is odd")
```

```js
function oddEven(n) {
  for (let i = 0; i < n; i = i + 1) {
    if (i % 2 === 0) {
      console.log(i + ' is even');
    } else {
      console.log(i + ' is odd');
    };
  }
}
function oddEvenStartEnd(start, end) {
  for (let i = start; i < end; i = i + 1) {
    if (i % 2 === 0) {
      console.log(i + ' is even');
    } else {
      console.log(i + ' is odd');
    };
  }
}
function oddEvenStartEndStep(start, end, step) {
  for (let i = start; i < end; i = i + step) {
    if (i % 2 === 0) {
      console.log(i + ' is even');
    } else {
      console.log(i + ' is odd');
    };
  }
}
```
</div>
<!-- end -->

## Try/Catch

<!-- {"type": "js", "file": "examples/js_try_catch.py", "read": "stdout", "class": "side-by-side", "lines": {"input": [3, -11]}} -->
<div class='side-by-side'>
```python
def tryCatch():
    try:
        print("try something")
    except Exception as e:
        print(f"Error: {e}")


def tryCatchFinally():
    try:
        print("try something")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("finally")


def tryRaiseCatch():
    try:
        raise Exception("Some error")
    except Exception as e:
        print(f"Error: {e}")
```

```js
function tryCatch() {
  try {
    console.log('try something');
  } catch (e) {
    console.log('Error: ' + e);
  };
}
function tryCatchFinally() {
  try {
    console.log('try something');
  } catch (e) {
    console.log('Error: ' + e);
  } finally {
    console.log('finally');
  };
}
function tryRaiseCatch() {
  try {
    throw new Error('Some error');
  } catch (e) {
    console.log('Error: ' + e);
  };
}
```
</div>
<!-- end -->

## Static Context

PH7 has a runtime context object which can be used for managing the static resource. To use a static context, import `ph7.context.ctx`, add `ctx.static.view(__name__)` at the top of your template and add `ctx.static.include` in your view. In the following example we'll use a function defined in an external module.

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
      <div class="text" onclick=alertHello('John Doe')>Click Here</div>
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


