import pytest

from {{ name }}.users.db_utils import select_user_by_id


@pytest.mark.asyncio
async def test_select_user(tables, sa_engine):
    async with sa_engine.acquire() as conn:
        res = await select_user_by_id(conn, 1)

    assert res.id == 1
