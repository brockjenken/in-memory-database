import multiprocessing
from gunicorn.app.base import BaseApplication

from app.app import create_app
from app.resources import setup_routes


class Application(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def start_app():
    app = create_app()
    setup_routes(app)
    Application(app).run()


if __name__ == "__main__":
    start_app()
