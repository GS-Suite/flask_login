from responses.standard_response_body import StandardResponseBody
import flask


class LoginResponseBody(StandardResponseBody):

    def __init__(self, status, message, token):
        StandardResponseBody.__init__(self, status, message)
        self.token = token
        self.__dict__ = { 'status': status, 'message': message, 'token': token }