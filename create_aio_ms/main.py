from create_aio_ms.utils.config import parse_arguments
from create_aio_ms.utils.generator import (
    copy_template,
    rename_dirs,
    render_project_template,
)


def main():
    '''

    :return:
    '''
    args = parse_arguments()

    copy_template(args['name'])
    rename_dirs(args['name'])

    render_project_template(args)

    print('\n\nSuccessfully generated!\n')
    print(f'cd {args.name}/')
    print(f'pip install -e ./')
    print('make run\n\n')
