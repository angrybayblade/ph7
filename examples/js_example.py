from ph7.js import console, document, fetch, as_js


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
