from pathlib import Path

from cookiecutter.main import cookiecutter

from create_aio_app.utils.config import parse_arguments

parent = Path(__file__).parent


def main():
    args = parse_arguments()
    template_path = str(parent / 'template')

    if not args.get('name'):
        result = cookiecutter(template_path)
    else:
        ctx = {
            'project_name': args.get('name'),
            'use_postgres': 'n' if args.get('without_postgres') else 'y',
            'use_redis': 'y' if args.get('redis') else 'n',
        }

        result = cookiecutter(template_path, no_input=True, extra_context=ctx)

    folder = Path(result).name

    print('\n\n\033[92mSuccessfully generated!\033[00m\n')
    print(f'cd \33[94m{folder}/\033[00m')
    print('make run\n\n')
