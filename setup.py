import os
import pathlib
import sys

from setuptools import find_packages, setup

parent = pathlib.Path(__file__).parent


if sys.version_info < (3, 5):
    raise RuntimeError(
        "create-aio-app doesn't support Python version prior 3.5"
    )


def get_text_from(f: str) -> str:
    file_path = parent / f

    with open(file_path) as f:
        return f.read().strip()


def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


setup_requires = [
    'setuptools_scm',
]


install_requires = [
    'cookiecutter',
    'click>=7.0',
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
    'Development Status :: 4 - Beta',
    'Framework :: AsyncIO',
]


setup(
    name="create-aio-app",
    description=(
        "The tool that helps quickly create a basis for "
        "the microservice on aiohttp and prepare the development "
        "environment."
    ),
    long_description=get_text_from('README.md'),
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    platforms=["POSIX"],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    author="Mykhailo Havelia",
    author_email="misha.gavela@gmail.com",
    use_scm_version=True,
    setup_requires=setup_requires,
    install_requires=install_requires,
    license="MIT",
    url="https://github.com/aio-libs/create-aio-app",
    package_data={
        '': package_files(path),
    },
    entry_points={
        'console_scripts': ['create-aio-app=create_aio_app.main:main'],
    },
    keywords=['create-aio-app', 'cookiecutter', 'aiohttp'],
    zip_safe=True,
)
