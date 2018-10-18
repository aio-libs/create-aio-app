import argparse
import sys

import click

from create_aio_app.utils.config import name_type


def validate_project_name(project_name: str) -> None:
    try:
        name_type(project_name)
    except argparse.ArgumentTypeError as exc:
        click.echo(str(exc), err=True)
        sys.exit(1)


def main() -> None:
    validate_project_name('{{ cookiecutter.project_name }}')


if __name__ == '__main__':
    main()
