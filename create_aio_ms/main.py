from create_aio_ms.utils.config import parse_arguments
from create_aio_ms.utils.generator import (
    copy_template,
    rename_dirs,
    render_project_template,
)


# def find_replace(directory, find, replace):
#     for path, dirs, files in os.walk(os.path.abspath(directory)):
#         for filename in files:
#             filepath = os.path.join(path, filename)
#
#             if '__pycache__' in filepath:
#                 continue
#
#             if 'static' in filepath:
#                 continue
#
#             with open(filepath, mode="r", encoding="utf-8") as f:
#                 s = f.read()
#
#             s = s.replace(find, replace)
#
#             with open(filepath, "w", encoding='utf-8') as f:
#                 f.write(s)


def main():
    '''

    :return:
    '''
    args = parse_arguments()

    copy_template(args['name'])
    rename_dirs(args['name'])

    render_project_template(args)

    # # TODO: added color print
    # print('\n\nSuccessfully generated!\n')
    # print(f'cd {args.name}/')
    # print(f'pip install -e ./')
    # print('make run\n\n')
