from functools import partial
from pathlib import Path

import click
from cookiecutter.exceptions import (
    FailedHookException,
    OutputDirExistsException
)
from cookiecutter.main import cookiecutter
from create_aio_app.commands import COMMON, LINTERS, DATABASE

from create_aio_app.utils.config import parse_arguments

parent = Path(__file__).parent

echo = partial(click.echo, err=True)


def print_commands(commands):
    print('\n\n')
    for name, description in commands.items():
        echo(click.style(name + ' - ', fg='yellow'))
        echo(click.style(description, fg='bright_green'))


def show_commands():
    echo(click.style('\n    Common', fg='cyan'))
    print_commands(COMMON)
    echo(click.style('\n    Linters', fg='cyan'))
    print_commands(LINTERS)
    echo(click.style('\n    Database', fg='cyan'))
    print_commands(DATABASE)


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
    # echo('make run\n\n')
    echo(click.style('\nCommands'))
    echo(click.style('\n    General commands', fg='cyan'))
