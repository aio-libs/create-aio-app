from pathlib import Path
{% if redis %}
from functools import partial
{% endif %}

import aiohttp_jinja2
{% if not without_postgres %}
import aiopg.sa
{% endif %}
from aiohttp import web
{% if redis %}
import aioredis
{% endif %}
import jinja2

from {{name}}.routes import init_routes
from {{name}}.utils import init_config


path = Path(__file__).parent


def init_jinja2(app: web.Application) -> None:
    '''
    Initialize jinja2 template for application.
    '''
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(str(path / 'templates'))
    )
{% if not without_postgres %}


async def init_database(app: web.Application) -> None:
    '''
    This is signal for success creating connection with database
    '''
    config = app['config']['postgres']

    engine = await aiopg.sa.create_engine(**config)
    app['db'] = engine
{% endif %}
{% if redis %}


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
{% endif %}
{% if not without_postgres %}


async def close_database(app: web.Application) -> None:
    '''
    This is signal for success closing connection with database before shutdown
    '''
    app['db'].close()
    await app['db'].wait_closed()
{% endif %}
{% if redis %}


async def close_redis(app: web.Application) -> None:
    '''
    This is signal for success closing connection with redis before shutdown
    '''
    app['redis_sub'].close()
    app['redis_pub'].close()
{% endif %}


def init_app(config: dict = None) -> web.Application:
    app = web.Application()

    init_jinja2(app)
    init_config(app, config=config)
    init_routes(app)
    {% if not without_postgres and redis %}

    app.on_startup.extend([
        init_redis,
        init_database,
    ])
    app.on_cleanup.extend([
        close_redis,
        init_database,
    ])
    {% elif not without_postgres %}

    app.on_startup.extend([
        init_database,
    ])
    app.on_cleanup.extend([
        init_database,
    ])
    {% elif redis %}

    app.on_startup.extend([
        init_redis,
    ])
    app.on_cleanup.extend([
        close_redis,
    ])
    {% endif %}

    return app
