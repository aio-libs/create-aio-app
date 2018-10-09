import argparse
import os
import pathlib
from typing import Any, Optional, List

import trafaret
from aiohttp import web
from trafaret_config import commandline


PATH = pathlib.Path(__file__).parent.parent.parent
settings_file = os.environ.get('SETTINGS_FILE', 'api.dev.yaml')
DEFAULT_CONFIG_PATH = PATH / 'config' / settings_file


CONFIG_TRAFARET = trafaret.Dict({
    trafaret.Key('app'):
        trafaret.Dict({
            'host': trafaret.String(),
            'port': trafaret.Int(),
        }),
    {%- if cookiecutter.use_postgres == 'y' %}
    trafaret.Key('postgres'):
        trafaret.Dict({
            'host': trafaret.String(),
            'port': trafaret.Int(),
            'user': trafaret.String(),
            'password': trafaret.String(),
            'database': trafaret.String(),
        }),
    {%- endif %}
    {%- if cookiecutter.use_redis == 'y' %}
    trafaret.Key('redis'):
        trafaret.Dict({
            'host': trafaret.String(),
            'port': trafaret.Int(),
        }),
    {%- endif %}
})


def get_config(argv: Any = None) -> Any:
    ap = argparse.ArgumentParser()
    commandline.standard_argparse_options(
        ap,
        default_config=DEFAULT_CONFIG_PATH,
    )
    options = ap.parse_args(argv)

    return commandline.config_from_options(options, CONFIG_TRAFARET)


def init_config(
        app: web.Application,
        *,
        config: Optional[List[str]] = None
) -> None:
    app['config'] = \
        get_config(config or ['-c', DEFAULT_CONFIG_PATH.as_posix()])
