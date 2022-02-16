from typing import Callable


class Pipeline:
    DEFAULT_PORT = 3000

    def __init__(self, port: int = DEFAULT_PORT):
        pass

    def run(self, port: int = DEFAULT_PORT) -> None:
        pass

    def route(self):
        pass
    
    def get(self, path: str) -> None:
        def inner(handler: Callable[[any], any]):
            pass
        return inner

    def post(self, path: str) -> None:
        def inner(handler: Callable[[any], any]):
            pass
        return inner

    def put(self, path: str) -> None:
        def inner(handler: Callable[[any], any]):
            pass
        return inner

    def patch(self, path: str) -> None:
        def inner(handler: Callable[[any], any]):
            pass
        return inner

    def delete(self, path: str) -> None:
        def inner(handler: Callable[[any], any]):
            pass
        return inner