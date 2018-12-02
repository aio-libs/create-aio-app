from pathlib import Path
from typing import Optional, List

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
from {{ cookiecutter.project_name }}.utils.common import init_config


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


async def database(app: web.Application) -> None:
    '''
    A function that, when the aiohttp server is started, connects to postgresql,
    and after stopping it breaks the connection (after yield)
    '''
    config = app['config']['postgres']

    engine = await aiopg.sa.create_engine(**config)
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()
{%- endif %}
{%- if cookiecutter.use_redis == 'y' %}


async def redis(app: web.Application) -> None:
    '''
    A function that, when the aiohttp server is started, connects to redis,
    and after stopping it breaks the connection (after yield)
    '''
    config = app['config']['redis']

    create_redis = partial(
        aioredis.create_redis,
        f'redis://{config["host"]}:{config["port"]}'
    )

    sub = await create_redis()
    pub = await create_redis()

    app['redis_sub'] = sub
    app['redis_pub'] = pub
    app['create_redis'] = create_redis

    yield

    app['redis_sub'].close()
    app['redis_pub'].close()

    await app['redis_sub'].wait_closed()
    await app['redis_pub'].wait_closed()
{%- endif %}


def init_app(config: Optional[List[str]] = None) -> web.Application:
    app = web.Application()

    init_jinja2(app)
    init_config(app, config=config)
    init_routes(app)
    {%- if cookiecutter.use_postgres == 'y' and cookiecutter.use_redis == 'y' %}

    app.cleanup_ctx.extend([
        redis,
        database,
    ])
    {%- elif cookiecutter.use_postgres == 'y' %}

    app.cleanup_ctx.extend([
        database,
    ])
    {%- elif cookiecutter.use_redis == 'y' %}

    app.cleanup_ctx.extend([
        redis,
    ])
    {%- endif %}

    return app
