from create_aio_app.utils.config import parse_arguments
from create_aio_app.utils.generator import (
    copy_template,
    rename_dirs,
    render_project_template,
    remove_unnecessary_directories,
)


def main():
    '''

    :return:
    '''
    args = parse_arguments()

    copy_template(args['name'])
    rename_dirs(args['name'])
    remove_unnecessary_directories(args)

    render_project_template(args)

    print('\n\nSuccessfully generated!\n')
    print(f'cd {args["name"]}/')
    print('make run\n\n')
