from http.client import responses as HTTP_STATUSES
from wsgiref.headers import Headers


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