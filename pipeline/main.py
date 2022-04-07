from typing import Callable
from wsgiref.simple_server import make_server
from .components.request import Request
from .components.response import Response
from .components.router import Router
from .components.server import Server


LOGO = """
        ____  ________  ________    _____   ________
       / __ \/  _/ __ \/ ____/ /   /  _/ | / / ____/
      / /_/ // // /_/ / __/ / /    / //  |/ / __/   
     / ____// // ____/ /___/ /____/ // /|  / /___   
    /_/   /___/_/   /_____/_____/___/_/ |_/_____/   
"""


class Pipeline:
    """
    A light web framework - part of a project in Frameworks at HiØ, 
    written with love in Python <3 

    Authors:
        (@olejorga): Ole-Jørgen Andersen
    """
    def __init__(self) -> None:
        """
        Create an instance of a webserver.
        """
        self.__get_router = Router()
        self.__post_router = Router()
        self.__put_router = Router()
        self.__delete_router = Router()

    def run(self, port: int = 3000, host: str = 'localhost') -> None:
        """
        Start webserver on preferred port.

        Args:
            port (int): Desired host port.
        """
        print(
            '\u001b[38;5;196m' + # Make console text red
            LOGO +
            '\u001b[0m' + # Reset console text styling
            Pipeline.__doc__
        )

        server = Server
        server.get_router = self.__get_router
        server.post_router = self.__post_router
        server.put_router = self.__put_router
        server.delete_router = self.__delete_router

        try:
            print('\u001b[38;5;246m') # Make console text grey
            print(f'Server started on http://{host}:{port}')

            with make_server(host, port, server.create) as app:
                app.serve_forever()
                
        except KeyboardInterrupt:
            print('\u001b[0m') # Reset console text styling
            app.server_close()
    
    def get(self, route: str) -> Callable[[Callable[[Request], Response]], None]:
        """
        Decorator for defining an endpoint with a GET-method and 
        a user specified controller function.

        Args:
            route (str): Desired route within the domain.

        Returns:
            (Callable): Takes a controller as its only argument.
        """
        def inner(controller: Callable[[Request], Response]):
            self.__get_router.add_route(route, controller)

        return inner

    def post(self, route: str) -> Callable[[Callable[[Request], Response]], None]:
        """
        Decorator for defining an endpoint with a POST-method and 
        a user specified controller function.

        Args:
            route (str): Desired route within the domain.

        Returns:
            (Callable): Takes a controller as its only argument.
        """
        def inner(controller: Callable[[Request], Response]):
            self.__post_router.add_route(route, controller)

        return inner

    def put(self, route: str) -> Callable[[Callable[[Request], Response]], None]:
        """
        Decorator for defining an endpoint with a PUT-method and 
        a user specified controller function.

        Args:
            route (str): Desired route within the domain.

        Returns:
            (Callable): Takes a controller as its only argument.
        """
        def inner(controller: Callable[[Request], Response]):
            self.__put_router.add_route(route, controller)

        return inner

    def delete(self, route: str) -> Callable[[Callable[[Request], Response]], None]:
        """
        Decorator for defining an endpoint with a DELETE-method and 
        a user specified controller function.

        Args:
            route (str): Desired route within the domain.

        Returns:
            (Callable): Takes a controller as its only argument.
        """
        def inner(controller: Callable[[Request], Response]):
            self.__delete_router.add_route(route, controller)

        return inner