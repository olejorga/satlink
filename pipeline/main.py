from typing import Callable
from .components.context import Context
from .components.server import Server


class Pipeline:

    def __init__(self) -> None:
        self.__server = Server()

    def run(self, port: int = 3000) -> None:
        pass
    
    def get(self, path: str) -> None:
        def inner(handler: Callable[[Context], any]):
            handler(Context())
        return inner

    def post(self, path: str) -> None:
        def inner(handler: Callable[[Context], any]):
            handler(Context())
        return inner