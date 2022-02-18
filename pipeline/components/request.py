from urllib.parse import parse_qs as query_parser


class Request:

    def __init__(self, environ: dict, params: dict):
        self._environ = environ
        self._params = params

    @property
    def body(self) -> str:
        length = int(self._environ['CONTENT_LENGTH'])
        charset = self._environ['LC_CTYPE']

        return self._environ['wsgi.input'].read(length).decode(charset)

    @property
    def method(self) -> str:
        return self._environ['REQUEST METHOD']

    @property
    def params(self) -> dict:
        return self._params

    @property
    def path(self) -> str:
        return self._environ['PATH_INFO']

    @property
    def query(self) -> dict:
        parameters = query_parser(self._environ['QUERY_STRING'])
        return {key:value[0] for key, value in parameters.items()}