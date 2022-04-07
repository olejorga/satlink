from http.cookies import SimpleCookie
from urllib.parse import parse_qs as query_parser


class Request:

    def __init__(self, environ: dict, params: dict) -> None:
        self._environ = environ
        self._params = params

    @property
    def body(self) -> str:
        """
        Request body content.
        """
        length = int(self._environ['CONTENT_LENGTH'])
        charset = self._environ.get('LC_CTYPE', 'utf-8')
        return self._environ['wsgi.input'].read(length).decode(charset)

    @property
    def method(self) -> str:
        """
        HTTP method used.
        """
        return self._environ['REQUEST METHOD']

    @property
    def params(self) -> dict:
        """
        Variables derived from the url parameters.
        """
        return self._params

    @property
    def path(self) -> str:
        """
        Requested path, relative to domain.
        """
        return self._environ['PATH_INFO']

    @property
    def query(self) -> dict:
        """
        Variables derived from the query parameters.
        """
        params = query_parser(self._environ['QUERY_STRING'])
        return {key:value[0] for key, value in params.items()}

    @property
    def cookies(self) -> dict:
        """
        Client side cookies.
        """
        cookies = SimpleCookie(self._environ['HTTP_COOKIE'])
        box = {}
        
        for token, value in cookies.items():
            box[token] = value.value

        return box