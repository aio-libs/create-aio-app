import argparse
import re

__all__ = ['parse_arguments', ]


def name_type(name: str) -> str:
    """
    The validator for the name argument.
    """

    if not re.match(r"^[a-zA-Z0-9_]*$", name):
        raise argparse.ArgumentTypeError(
            f"The format of the project name is incorrect."
        )

    return name


def parse_arguments() -> dict:
    """
    Parse console arguments and return config object.
    """
    parser = argparse.ArgumentParser(
        prog="create-aio-app",
        description=(
            "create-aio-app - a tool that helps quickly create a basis "
            "for the microservice on aiohttp and prepare the development "
            "environment."
        )
    )
    parser.add_argument(
        "name",
        type=name_type,
        metavar="<project-name>",
        help='the name of the future project.'
    )
    parser.add_argument(
        '--redis',
        action='store_true',
        help='added redis settings to the generating project'
    )
    parser.add_argument(
        '--mongodb',
        action='store_true',
        help='added mongodb settings to the generating project'
    )
    parser.add_argument(
        '--without-postgres',
        action='store_true',
        help='generate project without postgres settings'
    )

    return parser.parse_args().__dict__
