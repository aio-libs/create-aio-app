from aiohttp import web

from .app import init_app


def create_app() -> web.Application:
    import aiohttp_debugtoolbar

    app = init_app()
    aiohttp_debugtoolbar.setup(app, check_host=False)

    return app


def main():
    app = init_app()
    app_settings = app['config']['app']

    web.run_app(
        app,
        host=app_settings['host'],
        port=app_settings['port'],
    )


if __name__ == '__main__':
    main()
