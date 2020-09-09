
import json
import requests as res
from requests import Response
from .exceptions import TokenError


class Token:
    """
    Class for managing Visual Inspector tokens
    """

    def __init__(self, path: str, username: str, password: str):
        self.path = path
        self.username = username
        self.password = password
        request_token = self.request_token()

        if json.loads(request_token.text)['result'] == 'success':
            self.request_token = request_token.text
        else:
            raise TokenError(status=request_token.text)

    def __repr__(self):
        return self.request_token

    def request_token(self) -> Response:
        """
        Gets a token from Visual Inspector for provided info, the token will expired in 24 hours.

        :return: request.Response for API containing generated token
        """
        return res.post(self.path + 'tokens', json={"grant_type": "password", "username": self.username,
                                                    "password": self.password})

    def get_token(self) -> str:
        """
        Gets just the token from the request.Response message

        :return: String of the token
        """
        return json.loads(self.request_token)['token']
