import pathlib

__all__ = ['TEMPLATE_DIR', 'TEMPLATE_NAME', 'RENDER_ACCESS_FORMATS', 'DATABASE_TEMPLATE_DIRS']


TEMPLATE_NAME = 'template_project'
TEMPLATE_DIR = pathlib.Path(__file__).parent / TEMPLATE_NAME
DATABASE_TEMPLATE_DIRS = ['users', 'migrations',]

RENDER_ACCESS_FORMATS = [
    'py',
    'yml',
    'yaml',
    'md',
    'Dockerfile',
    'Makefile',
    'ini',
]
