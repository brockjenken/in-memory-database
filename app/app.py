import falcon


def create_app() -> falcon.API:
    app = falcon.API()
    return app
