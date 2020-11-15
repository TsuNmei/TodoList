from revcore.django.exceptions import APIError

class InvalidUser(APIError):
    status_code = 400
    code = "invalid_user_error"
    detail = "This {user_id} is invalid"