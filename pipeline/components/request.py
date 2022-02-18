from os import environ
from urllib.parse import parse_qs as QUERY_PARSER


class Request:

    def __init__(self, environ: dict, params: dict) -> None:
        self._environ = environ
        self._params = params

    @property
    def method(self):
        return self._environ['REQUEST METHOD']

    @property
    def params(self):
        return self._params

    @property
    def path(self):
        return self._environ['PATH_INFO']

    @property
    def query(self):
        parameters = QUERY_PARSER(self._environ['QUERY_STRING'])
        return {key:value[0] for key, value in parameters.items()}