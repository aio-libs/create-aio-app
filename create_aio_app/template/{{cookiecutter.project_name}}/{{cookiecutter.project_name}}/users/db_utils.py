{%- if cookiecutter.use_postgres == 'asyncpg' %}
import asyncpg
{%- endif %}
{%- if cookiecutter.use_postgres == 'aiopg' %}
from aiopg.sa import SAConnection
from aiopg.sa.result import RowProxy
{%- endif %}
from {{cookiecutter.project_name}}.users.tables import users{%- if cookiecutter.use_postgres == 'asyncpg' %}, dialect {%- endif %}

__all__ = ['select_user_by_id', 'select_user_by_id_query']


def select_user_by_id_query(key):
    query = users\
        .select()\
        .where(users.c.id == key)\
        .order_by(users.c.id)

    return query


{%- if cookiecutter.use_postgres == 'asyncpg' %}
async def select_user_by_id(conn, key):
    query = str(select_user_by_id_query(key).compile(dialect=dialect))
    result = await conn.fetchrow(query)
    return result
{%- endif %}
{%- if cookiecutter.use_postgres == 'aiopg' %}
async def select_user_by_id(conn: SAConnection, key: int) -> RowProxy:
    cursor = await conn.execute(select_user_by_id_query(key))
    return await cursor.fetchone()
{%- endif %}
