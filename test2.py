from wsgiref.headers import Headers
from wsgiref.simple_server import make_server, demo_app
from http.client import responses as HTTP_STATUSES
from urllib.parse import parse_qs as QUERY_PARSER

def get(path: str):
    def outer(handler):
        def inner(environ, start_response):
            request = Request(environ)
            response = handler(request)

            start_response(response.status, response.headers.items())

            return response
        return inner
    return outer


class Request:

    def __init__(self, environ) -> None:
        self._environ = environ

    @property
    def query(self):
        parameters = QUERY_PARSER(self._environ['QUERY_STRING'])
        return {key:value[0] for key, value in parameters.items()}


class Response:

    def __init__(self, body: str = '', status: int = 200) -> None:
        self.headers = Headers()
        self.headers.add_header('content-type', 'text/html; charset=utf-8')
        self._status_code = status
        self.body = body

    @property
    def status(self):
        status_message = HTTP_STATUSES.get(self._status_code, 'UNKNOWN')
        return f"{self._status_code} {status_message}"

    def __iter__(self):
        for k in self.body:
            if isinstance(k, bytes):
                yield k
            else:
                yield k.encode('utf-8')


@get('/users')
def my_app(request):
    name = request.query.get('name', 'WORLD')
    return Response(f"HELLO {name}!")


class Pipeline


if __name__ == "__main__":
    with make_server('', 3000, my_app) as server:
        server.serve_forever()