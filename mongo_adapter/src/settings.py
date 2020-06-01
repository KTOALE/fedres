from os import environ

MONGO_HOST = environ.get("MONGO_HOST", "localhost")
MONGO_PORT = environ.get("MONGO_PORT", "27017")
NATS_HOST = environ.get("NATS_HOST", "localhost")
NATS_PORT = environ.get("NATS_PORT", "4222")
DB_NAME = environ.get("DB_NAME", "fedres_messages")
COLL_NAME = environ.get("COLL_NAME", "tasks")
MONGO_CONN_DATA = {
    "host": MONGO_HOST,
    "port": int(MONGO_PORT),
}
TOPICS_TO_LISTEN = environ.get(
    "TOPICS_TO_LISTEN",
    "mongo_adapter.set,mongo_adapter.get".split(",")
)

nats_conn_str = f"nats://{NATS_HOST}:{NATS_PORT}"
