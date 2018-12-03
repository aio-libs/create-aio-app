import os
import re
from pathlib import Path
from setuptools import find_packages, setup

REGEXP = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")


def read_version():
    init_py = os.path.join(
        os.path.dirname(__file__),
        '{{ cookiecutter.project_name }}',
        '__init__.py',
    )

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f'Cannot find version in ${init_py}'
            raise RuntimeError(msg)


def read_requirements():
    my_file = Path("requirements/production.txt")
    if my_file.is_file():
        with open(my_file) as req:
            return req.read().split('\n')


setup(
    name='{{ cookiecutter.project_name }}',
    version=read_version(),
    description='{{ cookiecutter.project_name }}',
    platforms=['POSIX'],
    packages=find_packages(),
    package_data={
        '': ['config/*.*']
    },
    include_package_data=True,
    install_requires=read_requirements(),
    zip_safe=False,
)
