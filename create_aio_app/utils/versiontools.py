"""Version tools set."""

import os
import re
import click 
import json
import create_aio_app
import urllib.request
from typing import Callable, Optional, Union

from setuptools_scm import get_version


def get_version_from_scm_tag(
        *,
        root: str = '.',
        relative_to: Optional[str] = None,
        local_scheme: Union[Callable, str] = 'node-and-date',
) -> str:
    """Retrieve the version from SCM tag in Git or Hg."""
    try:
        return get_version(
            root=root,
            relative_to=relative_to,
            local_scheme=local_scheme,
        )
    except LookupError:
        return 'unknown'


def cut_local_version_on_upload(version):
    """Return empty local version if uploading to PyPI."""
    is_pypi_upload = os.getenv('PYPI_UPLOAD') == 'true'
    if is_pypi_upload:
        return ''

    import setuptools_scm.version  # only available during setup time
    return setuptools_scm.version.get_local_node_and_date(version)


def get_self_version():
    """Calculate the version of the dist itself."""
    return get_version_from_scm_tag(local_scheme=cut_local_version_on_upload)


def version_check():
    """Checks if the current version of the application is the latest"""
    PYPI_URL = "https://pypi.org/pypi/create-aio-app/json"

    try: 
        request = urllib.request.Request(PYPI_URL)
        with urllib.request.urlopen(req) as response:
        res = json.loads(response.read())

        code_version_long = create_aio_app.__version__
        code_version_installed = re.sub(r'([0-9].[0-9].[0-9]).*', r'\1',code_version_long)
        code_version_latest = res['info']['version']

        if code_version_installed < code_version_latest:
            print ("You are running an old version", code_version_installed,"upgrade with ", end='')
            click.secho('pip install --upgrade create-aio-app',fg='yellow')
    except:
        pass
