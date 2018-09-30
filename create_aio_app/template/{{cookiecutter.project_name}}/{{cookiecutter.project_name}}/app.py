from pathlib import Path
{%- if cookiecutter.use_redis == 'y' %}
from functools import partial
{%- endif %}

import aiohttp_jinja2
{%- if cookiecutter.use_postgres == 'y' %}
import aiopg.sa
{%- endif %}
from aiohttp import web
{%- if cookiecutter.use_redis == 'y' %}
import aioredis
{%- endif %}
import jinja2

from {{ cookiecutter.project_name }}.routes import init_routes
from {{ cookiecutter.project_name }}.utils import init_config


path = Path(__file__).parent


def init_jinja2(app: web.Application) -> None:
    '''
    Initialize jinja2 template for application.
    '''
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(str(path / 'templates'))
    )
{%- if cookiecutter.use_postgres == 'y' %}


async def init_database(app: web.Application) -> None:
    '''
    This is signal for success creating connection with database
    '''
    config = app['config']['postgres']

    engine = await aiopg.sa.create_engine(**config)
    app['db'] = engine
{%- endif %}
{%- if cookiecutter.use_redis == 'y' %}


async def init_redis(app: web.Application) -> None:
    '''
    This is signal for success creating connection with redis
    '''
    config = app['config']['redis']

    sub = await aioredis.create_redis(
        f'redis://{config["host"]}:{config["port"]}'
    )
    pub = await aioredis.create_redis(
        f'redis://{config["host"]}:{config["port"]}'
    )

    create_redis = partial(
        aioredis.create_redis,
        f'redis://{config["host"]}:{config["port"]}'
    )

    app['redis_sub'] = sub
    app['redis_pub'] = pub
    app['create_redis'] = create_redis
{%- endif %}
{%- if cookiecutter.use_postgres == 'y' %}


async def close_database(app: web.Application) -> None:
    '''
    This is signal for success closing connection with database before shutdown
    '''
    app['db'].close()
    await app['db'].wait_closed()
{% endif %}
{%- if cookiecutter.use_redis == 'y' %}


async def close_redis(app: web.Application) -> None:
    '''
    This is signal for success closing connection with redis before shutdown
    '''
    app['redis_sub'].close()
    app['redis_pub'].close()
{%- endif %}


def init_app(config: dict = None) -> web.Application:
    app = web.Application()

    init_jinja2(app)
    init_config(app, config=config)
    init_routes(app)
    {% if cookiecutter.use_postgres == 'y' and cookiecutter.use_redis == 'y' %}

    app.on_startup.extend([
        init_redis,
        init_database,
    ])
    app.on_cleanup.extend([
        close_redis,
        init_database,
    ])
    {% elif cookiecutter.use_postgres == 'y' %}

    app.on_startup.extend([
        init_database,
    ])
    app.on_cleanup.extend([
        init_database,
    ])
    {% elif cookiecutter.use_redis == 'y' %}

    app.on_startup.extend([
        init_redis,
    ])
    app.on_cleanup.extend([
        close_redis,
    ])
    {% endif %}

    return app
