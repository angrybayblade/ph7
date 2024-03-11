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
