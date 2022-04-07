from .response import Response


class Error(Exception):
    """
    Base class for error. An error abstraction, also containing 
    a response object. Can be raised as an exception.

    Props:
        response (Response): Dynamic error response.
    """
    def __init__(self, status: int, message: str = '') -> None:
        """
        An error abstraction, also containing a response object.

        Args:
            status (int): HTTP status code.
            message (str): Exception message.
        """
        super().__init__(message)
        self.response = Response(status=status)
        self.response = Response(self.response.status, status)