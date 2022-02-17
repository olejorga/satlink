class Response:
    def __init__(
        self, 
        body: str = '', 
        status: int = 200, 
        headers: dict = {}
    ) -> None:
        self.body = body
        self.status = status
        self.headers = headers