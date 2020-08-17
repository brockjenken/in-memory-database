import falcon

from .root import get_routes as root_routes


def setup_routes(app: falcon.API):
    for routes in [root_routes]:
        routes(app)
