from http.client import responses as HTTP_STATUSES
from wsgiref.headers import Headers


class Response:

    def __init__(
        self, 
        body: str = '', 
        status: int = 200,
        content_type: str = 'text/plain',
        charset: str = 'utf-8'
        ):
        self.headers = Headers()
        self.headers.add_header('content-type', f'{content_type}; charset={charset}')
        self.headers.add_header('content-length', f'{len(body.encode(charset))}')
        self._body = body
        self._status = status

    @property
    def body(self) -> str:
        return self._body

    @property
    def status(self) -> str:
        status_message = HTTP_STATUSES.get(self._status, 'UNKNOWN')
        return f"{self._status} {status_message}"

    def __iter__(self):
        for k in self.body:
            if isinstance(k, bytes):
                yield k
            else:
                yield k.encode('utf-8')