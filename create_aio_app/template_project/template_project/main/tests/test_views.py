async def test_view(client) -> None:
    resp = await client.get('/')

    assert resp.status == 200
    assert 'Create aio app' in await resp.text()
