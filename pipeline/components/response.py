from http.client import responses as HTTP_STATUSES
from wsgiref.headers import Headers
from json import dumps as json_dumps


class Response:

    def __init__(
        self, 
        body: str = '', 
        status: int = 200,
        content_type: str = 'text/plain',
        charset: str = 'utf-8'
    ) -> None:
        self.headers = Headers()
        self.headers.add_header('content-type', f'{content_type}; charset={charset}')
        self.headers.add_header('content-length', f'{len(body.encode(charset))}')
        self._body = str(body)
        self._status = status

    @property
    def body(self) -> str:
        return str(self._body)

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

    def redirect(self, url: str) -> None:
        self._status = 301
        self.headers.add_header("location", url)


class JSONResponse(Response):

    def __init__(self, data: dict | list = {}, status: int = 200) -> None:
        super().__init__(json_dumps(data), status, 'application/json')


class HTMLResponse(Response):

    def __init__(self, html: str = '', status: int = 200) -> None:
        super().__init__(html, status, 'text/html')


class CSVResponse(Response):

    def __init__(self, html: str = '', status: int = 200):
        super().__init__(html, status, 'text/html')