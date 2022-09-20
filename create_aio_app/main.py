from functools import partial
from pathlib import Path

import click
import os

from cookiecutter.exceptions import FailedHookException
from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter

from create_aio_app.utils.config import parse_arguments

parent = Path(__file__).parent

echo = partial(click.echo, err=True)


def show_commands(folder):

    try:
        os.chdir(f"{folder}/")  # nosec
        os.system("make help")  # nosec
        echo(click.style("Common commands", fg="bright_blue"))
        echo(click.style("make run (make) : Start the development server", fg = "bright_green"))
        echo(click.style("make stop : Stop docker containers", fg = "bright_green"))
        echo(click.style("make clean : Clean up of docker containers", fg = "bright_green"))
        echo(click.style("make bash : Interactive shell inside the running container (the command can be executed only if the server is running e.g. after make run)", fg = "bright_green"))
        echo(click.style("make upgrade : Upgrade dependencies", fg = "bright_green"))
        echo(click.style("Testing commands", fg="bright_blue"))
        echo(click.style("make test : Run the pytest suite inside docker", fg = "bright_green"))
        echo(click.style("make mypy : Run mypy for type checking", fg = "bright_green"))
        echo(click.style("make black : Run black code formatter", fg = "bright_green"))
        echo(click.style("make lint : Run flake8 (click.style(All the settings for flake8 can be customized in .flake8 file)", fg = "bright_green"))
        echo(click.style("make profile : Run py-spy sampling profiler. It defaults to 60 seconds. Can be change by adding the TIME variable. eg make profile TIME=30", fg = "bright_green"))
        echo(click.style("Database commands", fg="bright_blue"))
        echo(click.style("make migrations : Generate a new migration", fg = "bright_green"))
        echo(click.style("make migrate : Apply migrations", fg = "bright_green"))
        echo(click.style("make psql : Connect to the postgres inside running container", fg = "bright_green"))
        echo(click.style("Other commands", fg="bright_blue"))
        echo(click.style("make doc : Generate a sphinx documentation", fg = "bright_green"))


    except Exception as e:
        echo(f'{e}')
        echo(click.style("\nFailed to show commands\n", fg="red",))


def main():
    args = parse_arguments()
    template_path = str(parent / "template")

    kwargs = {}

    if args.get("name"):
        kwargs = {
            "no_input": True,
            "extra_context": {
                "project_name": args.get("name"),
                "use_postgres": "n" if args.get("without_postgres") else "y",
                "use_redis": "y" if args.get("redis") else "n",
                "use_uvloop": "y" if args.get("uvloop") else "n",
            },
        }

    try:
        result = cookiecutter(template_path, **kwargs)
    except (FailedHookException, OutputDirExistsException) as exc:
        if isinstance(exc, OutputDirExistsException):
            echo(
                click.style(
                    "\n\nDirectory with such name already exists!\n", fg="red")
            )
        return

    folder = Path(result).name

    echo(click.style("\n\nSuccessfully generated!\n", fg="bright_green",))
    echo("cd " + click.style(f"{folder}/", fg="bright_blue"))
    show_commands(folder)
