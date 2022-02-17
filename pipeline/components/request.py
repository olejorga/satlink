from urllib.parse import parse_qs as QUERY_PARSER


class Request:

    def __init__(self, environ) -> None:
        self._environ = environ

    @property
    def query(self):
        parameters = QUERY_PARSER(self._environ['QUERY_STRING'])
        return {key:value[0] for key, value in parameters.items()}