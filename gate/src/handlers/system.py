from aiohttp.web_request import Request
from aiohttp.web import Response


async def index(request: Request):
    print("INDEX PAGE")
    return Response(
        text="OK",
        content_type="text/plain",
        status=200
    )
