from typing import Dict
import subprocess  # nosec
import click
import re
from functools import partial
from pathlib import Path

req_dir = Path(".").parent.parent / "requirements"
pip_list = "pip list -o --format=freeze"


def upgrade_requirements() -> None:
    warning_message = False
    req_files = [
        req_file for req_file in req_dir.iterdir() if req_file.is_file()
    ]

    for req_file in req_files:
        with req_file.open() as f:
            old_req = f.read()
            fresh_version = (
                subprocess.check_output(pip_list, shell=True)  # nosec
                .decode("utf-8")
                .split("\n")
            )

            packages: Dict[str, str] = dict(
                package.split("==")  # type: ignore
                for package in fresh_version
                if package
            )

        with req_file.open("w") as f:
            new_req = old_req
            for name, version in packages.items():
                new_req = re.sub(
                    fr"{name}==[\d .]*",
                    f"{name}=={version}",
                    new_req,
                )
            f.seek(0)
            f.write(new_req)
            f.truncate()

        if old_req != new_req:
            warning_message = True

    if warning_message:
        echo = partial(click.echo, err=True)
        echo(
            click.style(
                "Please rebuild your docker container with ",
                fg="bright_green",
            )
            + click.style("'make build'", fg="bright_blue")
        )


if __name__ == "__main__":
    upgrade_requirements()
