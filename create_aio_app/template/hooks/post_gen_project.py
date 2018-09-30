import shutil

from create_aio_app.constants import DATABASE_TEMPLATE_DIRS


def remove_database_dirs() -> None:
    for dir_name in DATABASE_TEMPLATE_DIRS:
        shutil.rmtree(f'{{ cookiecutter.project_name }}/{dir_name}')


def main() -> None:
    if "{{ cookiecutter.use_postgres }}".lower() == "n":
        remove_database_dirs()


if __name__ == "__main__":
    main()
