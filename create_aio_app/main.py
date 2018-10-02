import pathlib

from cookiecutter.main import cookiecutter

from create_aio_app.utils.config import parse_arguments

parent = pathlib.Path(__file__).parent


def main():
    args = parse_arguments()
    template_path = str(parent / 'template')

    if not args.get('name'):
        cookiecutter(template_path)
    else:
        ctx = {
            'project_name': args.get('name'),
            'use_postgres': 'n' if args.get('without_postgres') else 'y',
            'use_redis': 'y' if args.get('without_postgres') else 'n',
        }

        cookiecutter(template_path, no_input=True, extra_context=ctx)

    print('\n\nSuccessfully generated!\n')
    print(f'cd {args["name"] or "app"}/')
    print('make run\n\n')
