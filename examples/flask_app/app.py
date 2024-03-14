from flask import Flask

from ph7.flask import PH7Templates

app = Flask(__name__)
templates = PH7Templates(templates_path="./templates")


@app.get("/")
def _home():
    return templates.render(
        name="root",
        context={},
    )


@app.get("/dogs")
def _dogs():
    return templates.render(
        name="dogs",
        context={},
    )


app.run(
    port=5000,
    debug=True,
)
