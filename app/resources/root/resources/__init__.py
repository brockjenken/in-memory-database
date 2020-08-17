import falcon

from .root import Root


def get_routes(app: falcon.API):
    app.add_route("/", Root())
