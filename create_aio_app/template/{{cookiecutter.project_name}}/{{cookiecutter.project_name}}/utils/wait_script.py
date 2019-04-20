import socket
import time
import random

from {{ cookiecutter.project_name }}.utils.common import get_config, DEFAULT_CONFIG_PATH

if __name__ == '__main__':
    config = get_config(['-c', DEFAULT_CONFIG_PATH.as_posix()])
    {%- if cookiecutter.use_postgres != 'n' %}
    postgres = config['postgres']
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((postgres['host'], postgres['port']))
                print('Successfully started postgres')
                break
        except socket.error:
            print('Waiting for postgres')
            time.sleep(0.5 + (random.randint(0, 100) / 1000))
    {%- endif %}
    {%- if cookiecutter.use_redis == 'y' %}
    redis = config['redis']
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((redis['host'], redis['port']))
                print('Successfully started redis')
                break
        except socket.error:
            print('Waiting for redis')
            time.sleep(0.5 + (random.randint(0, 100) / 1000))
    {%- endif %}
