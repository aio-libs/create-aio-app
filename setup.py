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
    for (path, _, filenames) in os.walk(directory):
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
    'cookiecutter'
]


path = os.path.join(
    os.path.dirname(__file__),
    'create_aio_app',
    'template'
)


classifiers = [
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Operating System :: POSIX',
    'Development Status :: 4 - Beta'
    'Framework :: AsyncIO',
]


setup(
    name="create-aio-app",
    version=read_version(),
    description=("The tool that helps quickly create a basis for "
                 "the microservice on aiohttp and prepare the development "
                 "environment."),
    classifiers=classifiers,
    platforms=["POSIX"],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    author="Mykhailo Havelia",
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
    keywords=['create-aio-app', 'cookiecutter', 'aiohttp'],
    zip_safe=True,
)
