import json as j


class Response:
    def __init__(
        self, 
        status: int = 200, 
        headers: dict = {'Content-Type': 'application/octet-stream'}, 
        body: str = ""
        ):
        self.status = status
        self.headers = headers
        self.body = body

class TEXTResponse(Response):
    def __init__(self, text: str, status: int):
        super().__init__()

        self.status = status if status else self.status
        self.headers['Content-Type'] = "text/plain"
        self.body = text

class HTMLResponse(Response):
    def __init__(self, html: str):
        super().__init__()

        self.headers['Content-Type'] = "text/html"
        self.body = html

class JSONResponse(Response):
    def __init__(self, json: dict):
        super().__init__()

        self.headers['Content-Type'] = "application/json"
        self.body = j.dumps(json)