from ph7.js import console, document, fetch, js_callable, alert


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
