{%- if cookiecutter.use_uvloop == 'y' %}
import uvloop
{%- endif %}
from aiohttp import web

from .app import init_app
{%- if cookiecutter.use_sentry == 'y' %}
from .app import init_sentry
{%- endif %}


def create_app() -> web.Application:
    import aiohttp_debugtoolbar

    app = init_app()
    aiohttp_debugtoolbar.setup(app, check_host=False)

    return app


def main() -> None:
    app = init_app()
    app_settings = app['config']['app']

    {%- if cookiecutter.use_uvloop == 'y' %}
    uvloop.install()
    {%- endif %}

    {%- if cookiecutter.use_sentry == 'y' %}
    init_sentry(app)
    {%- endif %}

    web.run_app(
        app,
        host=app_settings['host'],
        port=app_settings['port'],
    )


if __name__ == '__main__':
    main()
