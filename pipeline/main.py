from operator import imod
from typing import Callable
from components.context import Context

class Pipeline:

    def __init__(self, port: int) -> None:
        pass

    def run(self, port: int) -> None:
        pass
    
    def get(self, path: str, controller: Callable[[Context], str]) -> None:
        pass

    def post(self, path: str, controller: Callable[[Context], str]) -> None:
        pass

    def put(self, path: str, controller: Callable[[Context], str]) -> None:
        pass

    def delete(self, path: str, controller: Callable[[Context], str]) -> None:
        pass