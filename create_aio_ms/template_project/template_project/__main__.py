import aiohttp_debugtoolbar
from aiohttp import web

from .app import init_app


def create_app() -> web.Application:
    app = init_app()
    aiohttp_debugtoolbar.setup(app)

    return app


if __name__ == '__main__':
    app = create_app()
    web.run_app(app)
