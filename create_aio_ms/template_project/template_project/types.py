{% if not without_postgres %}
from typing import List

from aiopg.sa.result import RowProxy


RowsProxy = List[RowProxy]{% endif %}