from revauth.handlers import DefaultHandler


class CustomHandler(DefaultHandler):
    def on_login_success(self, profile):
        serialized = self.jwt_serializer_class(profile).data
        return {**serialized}
