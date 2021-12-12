# This file comes from the Kludex/uvicorn image - Feel free to override it.


async def app(scope, receive, send):
    if scope["type"] == "lifespan":
        while True:
            message = await receive()
            if message["type"] == "lifespan.startup":
                await send({"type": "lifespan.startup.complete"})
            elif message["type"] == "lifespan.shutdown":
                return await send({"type": "lifespan.shutdown.complete"})
    elif scope["type"] == "http":
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [[b"content-type", b"text/html"]],
            }
        )
        await send({"type": "http.response.body", "body": b"<h1>Hello, world!</h1>"})
