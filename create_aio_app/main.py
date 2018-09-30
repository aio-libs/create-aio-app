from cookiecutter.main import cookiecutter
import os

from create_aio_app.utils.config import parse_arguments




def main():
    '''

    :return:
    '''
    args = parse_arguments()

    print(os.path.dirname(os.path.abspath(__file__)))
    cookiecutter(f'{os.path.dirname(os.path.abspath(__file__))}/template/')

    print('\n\nSuccessfully generated!\n')
    print(f'cd {args["name"]}/')
    print('make run\n\n')
