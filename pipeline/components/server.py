from .request import Request
from .response import Response
from .router import Router


class Server:
    router: Router

    @classmethod
    def create(cls, environ, start_response):
        try:
            request = Request(environ)
            handler, args = cls.router.match(request._environ['PATH_INFO'])
            response = handler(request, *args)

        except:
            response = Response("NOT FOUND!", 404)

        start_response(response.status, response.headers.items())

        return response