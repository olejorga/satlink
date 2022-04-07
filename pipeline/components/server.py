from typing import Callable
from .request import Request
from .response import Response
from .router import Router
from .error import Error


class Server:
    get_router: Router
    post_router: Router
    put_router: Router
    delete_router: Router

    @classmethod
    def create(cls, environ: dict, start_response: Callable) -> Response:
        try:
            method = environ['REQUEST_METHOD']

            if method == "GET":
                controller, params = cls.get_router.match(environ['PATH_INFO'])
            elif method == "POST":
                controller, params = cls.post_router.match(environ['PATH_INFO'])
            elif method == "PUT":
                controller, params = cls.put_router.match(environ['PATH_INFO'])
            elif method == "DELETE":
                controller, params = cls.delete_router.match(environ['PATH_INFO'])
            else:
                raise Error(500, f"HTTP method not supported for route {environ['PATH_INFO']}")
            
            request = Request(environ, params)
            response = controller(request)
            
        except Error as err:
            print(err)
            response = err.response

        start_response(response.status, response.headers.items())

        return response