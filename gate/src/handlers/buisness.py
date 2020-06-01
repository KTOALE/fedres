from json import loads, dumps

from aiohttp.web import Response

from settings import nats_conn_str, CREATE_TASK_TOPIC

from utils.nats_controller import NatsController
from utils.msgs_maker import make_secret_msg
from utils.additional_tools import get_post_data


async def create_task(request):
    resp_params = {
        "text": "OK",
        "status": 200,
    }
    nats_ctrl = NatsController(nats_conn_str)
    try:
        create_data = await get_post_data(request)
        create_data["make_bytes"]=True
        payload = make_secret_msg(**create_data)
        resp = loads(await nats_ctrl.request(CREATE_TASK_TOPIC, payload=payload))
        resp_params["text"] = dumps(
            {"guid": resp.get("guid"),}
        )
    except Exception as e:
        print(f"Error happens!!! {e}")
        resp_params.update({
            "status": 500,
            "text": "Server Internal Error",
        })
    return Response(**resp_params)


async def get_task(request):
    pass
