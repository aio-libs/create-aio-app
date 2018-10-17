import shutil
import os

from create_aio_app.constants import (
    DATABASE_TEMPLATE_DIRS,
    DATABASE_TEMPLATE_FILES,
    WAIT_SCRIPT_FILE
)


def remove_wait_script() -> None:
    os.remove(f'{{ cookiecutter.project_name }}/{WAIT_SCRIPT_FILE}')


def remove_database_dirs_and_files() -> None:
    for dir_name in DATABASE_TEMPLATE_DIRS:
        shutil.rmtree(f'{{ cookiecutter.project_name }}/{dir_name}')

    for file_name in DATABASE_TEMPLATE_FILES:
        os.remove(f'{file_name}')


def main() -> None:
    without_postgres = "{{ cookiecutter.use_postgres | lower }}" == "n"
    without_redis = "{{ cookiecutter.use_redis | lower }}" == 'n'
    if without_postgres:
        remove_database_dirs_and_files()
    if without_postgres and without_redis:
        remove_wait_script()


if __name__ == "__main__":
    main()
