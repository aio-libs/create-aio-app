{%- if cookiecutter.use_postgres == 'y' or cookiecutter.use_redis == 'y' %}import socket
import time
import random

from {{ cookiecutter.project_name }}.utils.common import get_config, DEFAULT_CONFIG_PATH

if __name__ == '__main__':
    {%- if cookiecutter.use_postgres == 'y' or cookiecutter.use_redis == 'y' %}
    config = get_config(['-c', DEFAULT_CONFIG_PATH.as_posix()])
    {%- endif %}
    {%- if cookiecutter.use_postgres == 'y' %}
    postgres = config['postgres']
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((postgres['host'], postgres['port']))
                break
        except socket.error:
            time.sleep(0.1 + (random.randint(0, 100) / 1000))
    {%- endif %}
    {%- if cookiecutter.use_redis == 'y' %}
    redis = config['redis']
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((redis['host'], redis['port']))
                break
        except socket.error:
            time.sleep(0.1 + (random.randint(0, 100) / 1000))
    {%- endif %}
{%- endif %}
