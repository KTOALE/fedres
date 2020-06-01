from aiohttp import web
from handlers.buisness import create_task, get_task
from handlers.system import index
from settings import SERVER_HOST, SERVER_PORT


def conf_server_params():
    app = web.Application()

    app.add_routes(
        [
            web.get("/", index),
            web.post("/create_task", create_task),
            web.get("/get_task/{guid}", get_task),
        ]
    )
    return {
        "app": app,
        "host": SERVER_HOST,
        "port": SERVER_PORT,
    }


def launch_app():
    server_params = conf_server_params()
    web.run_app(**server_params)


if __name__ == "__main__":
    launch_app()
