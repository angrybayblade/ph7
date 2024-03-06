from ph7 import CSSObject, include
from ph7.html import body, button, div, head, html, img
from ph7.js import console, document, fetch, js_callable


class main(CSSObject):
    display = "flex"
    justify_content = "center"
    align_items = "center"
    flex_direction = "column"

    height = "100%"
    width = "100%"


class image(CSSObject):
    height = "200px"
    width = "400px"

    margin_bottom = "25px"


@js_callable
async def fetchDog():
    console.log("Fetching dog")
    response = await fetch(
        "https://dog.ceo/api/breeds/image/random",
        {
            "method": "GET",
        },
    )
    data = await response.json()
    console.log("Dog fetched")
    document.getElementById("image").src = data.message


template = html(
    head(
        include(image, main, fetchDog),
    ),
    body(
        div(
            img(
                src="#",
                id="image",
                alt="Click to fetch dog",
                class_name=image,
            ),
            button(
                "Click to fetch a dog",
                handlers={
                    "onclick": fetchDog(),
                },
            ),
            class_name=main,
        )
    ),
)
