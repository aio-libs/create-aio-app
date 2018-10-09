{%- if cookiecutter.use_postgres == 'y' %}

import socket
import time

from {{ cookiecutter.project_name }}.utils.common import get_config, DEFAULT_CONFIG_PATH

if __name__ == '__main__':
    postgres = get_config(['-c', DEFAULT_CONFIG_PATH.as_posix()])['postgres']
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((postgres['host'], postgres['port']))
                break
        except socket.error:
            time.sleep(0.1)
{%- endif %}
