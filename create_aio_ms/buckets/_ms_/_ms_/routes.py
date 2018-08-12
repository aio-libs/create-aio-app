import pathlib

from _ms_.main.views import index


PROJECT_PATH = pathlib.Path(__file__).parent


def init_routes(app):
    add_route = app.router.add_route

    add_route('*', '/', index, name='index')

    # added static dir
    app.router.add_static(
        '/static/',
        path=(PROJECT_PATH / 'static'),
        name='static',
    )
