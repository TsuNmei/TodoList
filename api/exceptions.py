from revcore.django.exceptions import APIError


class InvalidUser(APIError):
    status_code = 400
    code = 100
    detail = "Invalid request"


class UserExist(APIError):
    status_code = 400
    code = 101
    detail = 'User already exist'


class UserNotFoundError(APIError):
    status_code = 404
    code = 104
    detail = 'User Not Found'


class CantNotFound(APIError):
    status_code = 400
    code = 105
    detail = 'Login Failed'
