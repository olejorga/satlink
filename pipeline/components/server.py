from .request import Request
from .response import Response
from .router import Router


class Server:
    get_router: Router

    @classmethod
    def create(cls, environ, start_response):
        try:
            method = environ['REQUEST_METHOD']

            if method == "GET":
                print("YES!")
                handler, args = cls.get_router.match(environ['PATH_INFO'])
            
            request = Request(environ)
            response = handler(request, *args)

        except:
            response = Response(str(environ), 404)

        start_response(response.status, response.headers.items())

        return response