from typing import Callable
from .context import Context


class Pipeline:

    def __init__(self) -> None:
        pass

    def run(self, port: int = 3000) -> None:
        pass
    
    def get(self, path: str) -> None:
        def inner(handler: Callable[[Context], any]):
            handler(Context())
        return inner