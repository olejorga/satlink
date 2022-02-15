from typing import Callable
from .components.request import Request
from .components.response import Response

class Pipeline:

    def __init__(self, port: int):
        pass

    def run(self, port: int) -> None:
        pass
    
    def get(self, path: str, controller: Callable[[Request], Response]) -> None:
        pass

    def post(self, path: str, controller: Callable[[Request], Response]) -> None:
        pass

    def put(self, path: str, controller: Callable[[Request], Response]) -> None:
        pass

    def patch(self, path: str, controller: Callable[[Request], Response]) -> None:
        pass

    def delete(self, path: str, controller: Callable[[Request], Response]) -> None:
        pass