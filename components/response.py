from wsgiref.handlers import format_date_time
from time import mktime
from datetime import datetime, timedelta
from http import cookies
from http.client import responses as HTTP_STATUSES
from wsgiref.headers import Headers
from json import dumps as json_dumps


class Response:
    """
    A response is always returned from an endpoint.
    """
    def __init__(
        self, 
        body: str = '', 
        status: int = 200,
        content_type: str = 'text/plain',
        charset: str = 'utf-8'
    ) -> None:
        """
        Base class for all responses.

        Args:
            body (str): Response body content.
            status (int): HTTP status code.
            content_type (str): Response body content type.
            charset (str): Response body content character encoding.
        """
        self.headers = Headers()
        self.headers.add_header('Content-Type', f'{content_type}; charset={charset}')
        self.headers.add_header('Content-Length', f'{len(body.encode(charset))}')
        self._body = str(body)
        self._status = status
        self._content_type = content_type
        self._charset = charset

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

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        self._content_type = content_type
        self.headers.add_header('Content-Type', f'{content_type}; charset={self._charset}')

    @property
    def charset(self):
        return self._charset

    @charset.setter
    def charset(self, charset):
        self._charset = charset
        self.headers.add_header('Content-Type', f'{self._content_type}; charset={charset}')
        self.headers.add_header('Content-Length', f'{len(self._body.encode(charset))}')

    def __iter__(self):
        for k in self._body:
            if isinstance(k, bytes):
                yield k
            else:
                yield k.encode('utf-8')

    def redirect(self, url: str) -> None:
        """
        Redirects client to a different endpoint or website.

        Args:
            url (str): Web address, can be relative or absolute.
        """
        self._status = 301
        self.headers.add_header('Location', url)

    def set_cookie(
        self, 
        token: str, 
        value: str, 
        expires: datetime = datetime.now() + timedelta(days=42)
    ) -> None:
        """
        Set cookie on the clients side.

        Args:
            token (str): The name of the cookie.
            value (str): The content of the cookie.
            expires (str): The expiry date for the cookie.
        """
        cookie = cookies.SimpleCookie()
        cookie[token] = value
        cookie_str = cookie.output(header='')
        stamp = mktime(expires.timetuple())
        expires_str = format_date_time(stamp)

        self.headers.add_header('Set-Cookie', f'{cookie_str}; Expires={expires_str}')

    def remove_cookie(self, token: str) -> None:
        """
        Remove cookie on the clients side.

        Args:
            token (str): The name of the cookie.
        """
        expires = datetime(1970, 1, 1)
        self.set_cookie(token, '', expires)


class JSONResponse(Response):
    """
    A response with content type "application/json".
    """
    def __init__(self, data: dict | list = {}, status: int = 200) -> None:
        """
        A response with content type "application/json".

        Args:
            data (dict or list): The data to be serialized as JSON.
            status (int): HTTP status code.
        """
        super().__init__(json_dumps(data), status, 'application/json')


class HTMLResponse(Response):
    """
    A response with content type "text/html".
    """
    def __init__(self, html: str = '', status: int = 200) -> None:
        """
        A response with content type "text/html".

        Args:
            html (str): The content to be serialized as HTML.
            status (int): HTTP status code.
        """
        super().__init__(html, status, 'text/html')


class TemplateResponse(HTMLResponse):
    """
    A response with content type "text/html".
    """
    def __init__(self, path: str, context: dict = {}, status: int = 200):
        """
        A response that lets you format an HTML file with inserted 
        variables. Example file: <h1>Hello {name}!</h1>

        Args:
            path (str): Filepath to HTML template file.
            context (dict): Variables to be inserted into the template.
            status (int): HTTP status code.
        """
        with open(path, 'r') as file:
            template = file.read()
            view = template.format(**context)

        super().__init__(view, status)