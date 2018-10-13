{%- if cookiecutter.use_postgres == 'y' or cookiecutter.use_redis == 'y' %}import socket
import time

from {{ cookiecutter.project_name }}.utils.common import get_config, DEFAULT_CONFIG_PATH

if __name__ == '__main__':
    {%- if cookiecutter.use_postgres == 'y' %}
    postgres = get_config(['-c', DEFAULT_CONFIG_PATH.as_posix()])['postgres']
    {%- endif %}
    {%- if cookiecutter.use_redis == 'y' %}
    redis = get_config(['-c', DEFAULT_CONFIG_PATH.as_posix()])['redis']
    {%- endif %}
    while True:
        {%- if cookiecutter.use_postgres == 'y' %}
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((postgres['host'], postgres['port']))
                break
        except socket.error:
            time.sleep(0.1)
        {%- endif %}
        {%- if cookiecutter.use_redis == 'y' %}
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((redis['host'], redis['port']))
                break
        except socket.error:
            time.sleep(0.1)
        {%- endif %}
{%- endif %}
