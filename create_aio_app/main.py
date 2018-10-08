from pathlib import Path

from cookiecutter.exceptions import OutputDirExistsException
from cookiecutter.main import cookiecutter

from create_aio_app.utils.config import parse_arguments

parent = Path(__file__).parent


def main():
    args = parse_arguments()
    template_path = str(parent / 'template')

    kwargs = {}

    if args.get('name'):
        kwargs = {
            'no_input': True,
            'extra_context': {
                'project_name': args.get('name'),
                'use_postgres': 'n' if args.get('without_postgres') else 'y',
                'use_redis': 'y' if args.get('redis') else 'n',
            },
        }

    try:
        result = cookiecutter(template_path, **kwargs)
    except OutputDirExistsException as exc:
        print('\n\n\033[91mDirectory with such name already exists!\033[00m\n')
        return

    folder = Path(result).name

    print('\n\n\033[92mSuccessfully generated!\033[00m\n')
    print(f'cd \33[94m{folder}/\033[00m')
    print('make run\n\n')
