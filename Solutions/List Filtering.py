from typing import Any

def filter_list(l: list[Any]) -> list[Any]:
    return [x for x in l if not isinstance(x, str)]