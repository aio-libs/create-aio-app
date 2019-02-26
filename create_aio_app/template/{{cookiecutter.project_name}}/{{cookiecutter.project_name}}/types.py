{%- if cookiecutter.use_postgres == 'y' %}from typing import List

from aiopg.sa.result import RowProxy


RowsProxy = List[RowProxy]
{% endif %}