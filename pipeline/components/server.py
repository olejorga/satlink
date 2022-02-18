from .request import Request
from .response import Response
from .router import Router


class Server:
    get_router: Router
    post_router: Router

    @classmethod
    def create(cls, environ, start_response):
        try:
            method = environ['REQUEST_METHOD']

            if method == "GET":
                handler, params = cls.get_router.match(environ['PATH_INFO'])
            elif method == "POST":
                handler, params = cls.post_router.match(environ['PATH_INFO'])
            
            request = Request(environ, params)
            response = handler(request)
            
        except:
            response = Response('NOT FOUND!', 404)

        start_response(response.status, response.headers.items())

        return response