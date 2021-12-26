import os
import re
import pathlib
from typing import List

from setuptools import find_packages, setup

REGEXP = re.compile(r'^__version__\W*=\W*"([\d.abrc]+)"')
PARENT = pathlib.Path(__file__).parent


def read_version():
    init_py = os.path.join(
        os.path.dirname(__file__),
        "{{ cookiecutter.project_name }}",
        "__init__.py",
    )

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f"Cannot find version in ${init_py}"
            raise RuntimeError(msg)


def read_requirements(path: str) -> List[str]:
    file_path = PARENT / path
    with open(file_path) as f:
        return f.read().split("\n")


setup(
    name="{{ cookiecutter.project_name }}",
    version=read_version(),
    description="{{ cookiecutter.project_name }}",
    platforms=["POSIX"],
    packages=find_packages(),
    package_data={"": ["config/*.*"]},
    include_package_data=True,
    install_requires=read_requirements("requirements/production.txt"),
    zip_safe=False,
)
