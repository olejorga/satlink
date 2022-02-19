from typing import Callable
from wsgiref.simple_server import make_server
from .components.request import Request
from .components.response import Response
from .components.router import Router
from .components.server import Server


class Pipeline:

    def __init__(self):
        self.__get_router = Router()
        self.__post_router = Router()
        self.__put_router = Router()
        self.__delete_router = Router()

    def run(self, port: int = 3000):
        server = Server
        server.get_router = self.__get_router
        server.post_router = self.__post_router
        server.put_router = self.__put_router
        server.delete_router = self.__delete_router

        try:
            with make_server('', port, server.create) as app:
                app.serve_forever()
                
        except KeyboardInterrupt:
            app.server_close()
    
    def get(self, path: str):
        def inner(handler: Callable[[Request], Response]):
            self.__get_router.add_route(path, handler)

        return inner

    def post(self, path: str):
        def inner(handler: Callable[[Request], Response]):
            self.__post_router.add_route(path, handler)

        return inner

    def put(self, path: str):
        def inner(handler: Callable[[Request], Response]):
            self.__put_router.add_route(path, handler)

        return inner

    def delete(self, path: str):
        def inner(handler: Callable[[Request], Response]):
            self.__delete_router.add_route(path, handler)

        return inner