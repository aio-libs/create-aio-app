import shutil
import os

from create_aio_app.constants import (
    DATABASE_TEMPLATE_DIRS,
    DATABASE_TEMPLATE_FILES,
    WAIT_SERVICES_FILES
)


def remove_database_dirs_and_files() -> None:
    for dir_name in DATABASE_TEMPLATE_DIRS:
        shutil.rmtree(f'{{ cookiecutter.project_name }}/{dir_name}')

    for file_name in DATABASE_TEMPLATE_FILES:
        os.remove(f'{file_name}')

    for wait_file in WAIT_SERVICES_FILES:
        os.remove(f'{{ cookiecutter.project_name }}/{wait_file}')


def main() -> None:
    if "{{ cookiecutter.use_postgres }}".lower() == "n":
        remove_database_dirs_and_files()


if __name__ == "__main__":
    main()
