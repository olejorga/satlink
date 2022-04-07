from .response import Response


class Error(Exception):

    def __init__(self, status: int, message: str = '') -> None:
        super().__init__(message)
        self.response = Response(status=status)
        self.response = Response(self.response.status, status)