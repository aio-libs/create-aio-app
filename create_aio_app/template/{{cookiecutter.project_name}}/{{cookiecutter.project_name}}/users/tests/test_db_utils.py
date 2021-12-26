import typing as t

import pytest

from {{ cookiecutter.project_name }}.users.db_utils import select_user_by_id


@pytest.mark.asyncio
async def test_select_user(tables: t.Any, sa_engine: t.Any) -> None:
    async with sa_engine.acquire() as conn:
        res = await select_user_by_id(conn, 1)

    assert res.id == 1
