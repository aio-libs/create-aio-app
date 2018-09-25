import os
import sys
import re

from setuptools import find_packages, setup


REGEXP = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")


if sys.version_info < (3, 5):
    raise RuntimeError(
        "create-aio-app doesn't support Python version prior 3.5"
    )


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


def read_version():

    init_py = os.path.join(
        os.path.dirname(__file__),
        'create_aio_app',
        '__init__.py'
    )

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f'Cannot find version in ${init_py}'
            raise RuntimeError(msg)


install_requires = [
    'Jinja2',
]


path = os.path.join(
    os.path.dirname(__file__),
    'create_aio_app',
    'template_project'
)


setup(
    name="create-aio-app",
    version=read_version(),
    description="Mykhailo Havelia",
    platforms=["POSIX"],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    author_email="misha.gavela@gmail.com",
    install_requires=install_requires,
    license="MIT",
    url="https://github.com/Arfey/create-aio-app",
    package_data={
        '': package_files(path),
    },
    entry_points={
        'console_scripts': ['create-aio-app=create_aio_app:main.main'],
    },
)
