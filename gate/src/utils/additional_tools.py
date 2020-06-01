from aiohttp.web_request import Request


async def get_post_data(request: Request):
    print(f"request_type: {type(request)}")
    print(f"url: {request.url}")
    req = await request.json()
    email = req.get("email")
    secret_phrase = req.get("secret_phrase")
    secret = req.get("secret")
    return {}
