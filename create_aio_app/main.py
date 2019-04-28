from functools import partial
from pathlib import Path

import click
from cookiecutter.exceptions import (
    FailedHookException,
    OutputDirExistsException
)
from cookiecutter.main import cookiecutter

from create_aio_app.utils.config import parse_arguments

parent = Path(__file__).parent

echo = partial(click.echo, err=True)


def main():
    args = parse_arguments()
    template_path = str(parent / 'template')

    kwargs = {}

    if args.get('name'):
        kwargs = {
            'no_input': True,
            'extra_context': {
                'project_name': args.get('name'),
                'use_postgres': 'n' if args.get('without_postgres') else 'y',
                'use_redis': 'y' if args.get('redis') else 'n',
                'use_uvloop': 'y' if args.get('uvloop') else 'n',
            },
        }

    try:
        result = cookiecutter(template_path, **kwargs)
    except (FailedHookException, OutputDirExistsException) as exc:
        if isinstance(exc, OutputDirExistsException):
            echo(click.style(
                '\n\nDirectory with such name already exists!\n',
                fg='red',
            ))
        return

    folder = Path(result).name

    echo(click.style(
        '\n\nSuccessfully generated!\n',
        fg='bright_green',
    ))
    echo('cd ' + click.style(f'{folder}/', fg='bright_blue'))
    echo('make run\n\n')
