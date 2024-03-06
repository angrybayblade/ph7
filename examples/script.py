from ph7.js import alert, js_callable


@js_callable
def alertHello(user: str):
    alert("Hello, " + user)
