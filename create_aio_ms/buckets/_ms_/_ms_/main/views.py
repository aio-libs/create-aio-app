import pathlib

from aiohttp import web
import markdown2
import aiohttp_jinja2


path = pathlib.Path(__file__).parent.parent.parent


@aiohttp_jinja2.template('index.html')
async def index(request: web.Request) -> dict:
    with open(path / 'README.md') as my_file:
        text = markdown2.markdown(my_file.read())
    return {"text": text}
