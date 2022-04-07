from wsgiref.handlers import format_date_time
from time import mktime
from datetime import datetime, timedelta
from http import cookies
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
        self.headers.add_header('Content-Type', f'{content_type}; charset={charset}')
        self.headers.add_header('Content-Length', f'{len(body.encode(charset))}')
        self._body = str(body)
        self._status = status

    @property
    def body(self) -> str:
        return str(self._body)

    @body.setter
    def body(self, body: str):
        self._body = str(body)

    @property
    def status(self) -> str:
        status_message = HTTP_STATUSES.get(self._status, 'UNKNOWN')
        return f"{self._status} {status_message}"

    @status.setter
    def status(self, status: int) -> str:
        self._status = status

    def __iter__(self):
        for k in self.body:
            if isinstance(k, bytes):
                yield k
            else:
                yield k.encode('utf-8')

    def redirect(self, url: str) -> None:
        self._status = 301
        self.headers.add_header('Location', url)

    def set_cookie(
        self, 
        token: str, 
        value: str, 
        expires: datetime = datetime.now() + timedelta(days=42)
    ) -> None:
        cookie = cookies.SimpleCookie()
        cookie[token] = value
        cookie_str = cookie.output(header='')
        stamp = mktime(expires.timetuple())
        expires_str = format_date_time(stamp)

        self.headers.add_header('Set-Cookie', f'{cookie_str}; Expires={expires_str}')

    def remove_cookie(self, token: str) -> None:
        expires = datetime(1970, 1, 1)
        self.set_cookie(token, '', expires)


class JSONResponse(Response):

    def __init__(self, data: dict | list = {}, status: int = 200) -> None:
        super().__init__(json_dumps(data), status, 'application/json')


class HTMLResponse(Response):

    def __init__(self, html: str = '', status: int = 200) -> None:
        super().__init__(html, status, 'text/html')


class TemplateResponse(HTMLResponse):

    def __init__(self, path: str, context: dict = {}, status: int = 200):
        with open(path, 'r') as file:
            template = file.read()
            view = template.format(**context)

        super().__init__(view, status)