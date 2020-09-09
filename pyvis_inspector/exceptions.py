
"""
This module contains the set of pyvis-inspector exceptions.
"""


class PyvisException(IOError):

    def __init__(self):
        pass


class TokenError(PyvisException):
    """A Token Error Occurred"""

    def __init__(self, status: str):
        self.status = status
        self.message = "Provided credentials failed to authenticate."

    def __str__(self) -> str:
        return f"{self.message} \n Status Message: {self.status}"
