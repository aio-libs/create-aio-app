{%- if cookiecutter.use_postgres == 'aiopg' %}
from typing import List

from aiopg.sa.result import RowProxy


RowsProxy = List[RowProxy]
{%- endif %}
