from typing import Callable
from wsgiref.simple_server import make_server
from .components.server import Request
from .components.router import Router
from .components.server import Server


class Pipeline:

    def __init__(self):
        self.get_router = Router()
        self.post_router = Router()

    def run(self, port: int = 3000):
        self.port = port
        self.server = Server
        self.server.get_router = self.get_router
        self.server.post_router = self.post_router

        try:
            with make_server('', self.port, self.server.create) as app:
                app.serve_forever()
                
        except KeyboardInterrupt:
            app.server_close()
    
    def get(self, path: str):
        def inner(handler: Callable[[Request], any]):
            self.get_router.add_route(path, handler)
        return inner

    def post(self, path: str):
        def inner(handler: Callable[[Request], any]):
            self.post_router.add_route(path, handler)
        return inner