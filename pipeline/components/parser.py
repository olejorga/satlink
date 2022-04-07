from json import loads as json_loads
from typing import Any


class Parser:

    @classmethod
    def run(cls, data: Any) -> Any:
        return cls._deserialize(data)

    @classmethod
    def _deserialize(cls, data: Any) -> Any:
        pass


class JSONParser(Parser):

    # OVERRIDE
    @classmethod
    def _deserialize(cls, data: str) -> dict | list:
        return json_loads(data)