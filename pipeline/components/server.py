from typing import Callable
from .request import Request
from .response import Response
from .router import Router


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
                handler, params = cls.get_router.match(environ['PATH_INFO'])
            elif method == "POST":
                handler, params = cls.post_router.match(environ['PATH_INFO'])
            elif method == "PUT":
                handler, params = cls.put_router.match(environ['PATH_INFO'])
            elif method == "DELETE":
                handler, params = cls.delete_router.match(environ['PATH_INFO'])
            else:
                raise Exception
            
            request = Request(environ, params)
            response = handler(request)
            
        except Exception as e:
            print(e)
            response = Response('NOT FOUND!', 404)

        start_response(response.status, response.headers.items())

        return response