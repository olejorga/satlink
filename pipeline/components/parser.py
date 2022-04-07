from json import loads as json_loads
from typing import Any


class Parser:
    """
    Base class for parser. A helper class for deserializing 
    datatypes from string.
    """
    def __new__(cls, data: str) -> Any:
        """
        A helper class for deserializing 
        datatypes from string.

        Args:
            data (str): Data to be deserialized from string.
        """
        return cls._deserialize(data)

    @classmethod
    def _deserialize(cls, data: str) -> Any:
        pass


class JSONParser(Parser):
    """
    A parser for stringified JSON data.
    """

    # OVERRIDE
    @classmethod
    def _deserialize(cls, data: str) -> dict | list:
        return json_loads(data)