from typing import Callable
from wsgiref.simple_server import make_server
from .components.server import Request
from .components.router import Router
from .components.server import Server


class Pipeline:

    def __init__(self):
        self.router = Router()

    def run(self, port: int = 3000):
        self.server = Server
        self.server.router = self.router

        with make_server('', 3000, self.server.create) as app:
            app.serve_forever()
    
    def route(self, path: str):
        def inner(handler: Callable[[Request], any]):
            self.router.add_route(path, handler)
        return inner