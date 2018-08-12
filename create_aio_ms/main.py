# coding: utf-8
import argparse
import os
import pathlib
import shutil


def find_replace(directory, find, replace):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in files:
            filepath = os.path.join(path, filename)

            if '__pycache__' in filepath:
                continue

            with open(filepath, mode="r", encoding="utf-8") as f:
                s = f.read()

            s = s.replace(find, replace)

            with open(filepath, "w", encoding='utf-8') as f:
                f.write(s)


SAMPLES_DIR = pathlib.Path(__file__).parent / 'buckets'
MS_PATH = SAMPLES_DIR / '_ms_'


def init_project(args):
    '''

    :return:
    '''

    shutil.copytree(MS_PATH, args.name)


def rename_project(args):
    '''

    :param args:
    :return:
    '''
    shutil.move('./%s/_ms_' % args.name, './%s/%s' % (args.name, args.name))


def parse_arguments():
    '''

    :return:
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'name',
        help='Name of future microservice.'
    )
    parser.add_argument(
        '--redis',
        action='store_true',
        help='Added the redis to boilerplate.'
    )

    return parser.parse_args()


def main():
    '''

    :return:
    '''
    args = parse_arguments()
    init_project(args)
    rename_project(args)
    find_replace(f'./{args.name}', '_ms_', args.name)

    # TODO: added color print
    print('\n\nSuccessfully generated!\n')
    print(f'cd {args.name}/')
    print('make run\n\n')
