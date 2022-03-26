from typing import Callable
from wsgiref.simple_server import make_server
from .components.request import Request
from .components.response import Response
from .components.router import Router
from .components.server import Server


class Pipeline:
    """
    A light web framework - part of a project in Frameworks at HiØ, 
    written with love in Python <3
    """
    def __init__(self) -> None:
        """
        Create an instance of a webserver.
        """
        self.__get_router = Router()
        self.__post_router = Router()
        self.__put_router = Router()
        self.__delete_router = Router()

    def run(self, port: int = 3000) -> None:
        """
        Start webserver on preferred port.

        Arguments:
            port (int) - Desired host port.
        """
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
    
    def get(self, route: str) -> Callable[[]]:
        """
        Decorator for defining an endpoint with a GET-method and 
        a user specified controller function.

        Args:
            route (str): Desired route within the domain.

        Returns:
            Callable[[]]: Takes a controller as its only argument.
        """
        def inner(handler: Callable[[Request], Response]):
            self.__get_router.add_route(route, handler)

        return inner

    def post(self, route: str) -> Callable[[]]:
        """
        Decorator for defining an endpoint with a POST-method and 
        a user specified controller function.

        Args:
            route (str): Desired route within the domain.

        Returns:
            Callable[[]]: Takes a controller as its only argument.
        """
        def inner(handler: Callable[[Request], Response]):
            self.__post_router.add_route(route, handler)

        return inner

    def put(self, route: str) -> Callable[[]]:
        """
        Decorator for defining an endpoint with a PUT-method and 
        a user specified controller function.

        Args:
            route (str): Desired route within the domain.

        Returns:
            Callable[[]]: Takes a controller as its only argument.
        """
        def inner(handler: Callable[[Request], Response]):
            self.__put_router.add_route(route, handler)

        return inner

    def delete(self, route: str) -> Callable[[]]:
        """
        Decorator for defining an endpoint with a DELETE-method and 
        a user specified controller function.

        Args:
            route (str): Desired route within the domain.

        Returns:
            Callable[[]]: Takes a controller as its only argument.
        """
        def inner(handler: Callable[[Request], Response]):
            self.__delete_router.add_route(route, handler)

        return inner