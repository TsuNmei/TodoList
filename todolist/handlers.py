from revauth.handlers import BaseHandler
from django.contrib.auth.models import User
from revauth.jwt import JWTCryptor
from django.db.utils import IntegrityError
from django.conf import settings

import re
import requests


class Handler(BaseHandler):
    issuer = 'register-test'

    def send_validation(self, identity):
        if EmailField(identity).validator():
            resp = requests.post(self.auth_host, json={'identity': identity})
            resp_json = resp.json()
            resp.raise_for_status()

            return resp_json

    def on_register(self, decoded, password, **kwargs):
        try:
            identity = decoded['idy']

            user = User.objects.create_user(username=identity, password=password, email=identity)

        except IntegrityError:
            raise exceptions.UserExistsError

        except KeyError:
            raise exceptions.JWTDecodeError

        data = {self.identity_type: identity}

        try:
            profile = user.profile
        except:
            profile = self.profile_class.objects.create(user=user, name=kwargs['username'], phone=kwargs['phone'])

        for key, value in data.items():
            setattr(profile, key, value)

        profile.save()

        return profile

    def on_login_success(self, profile):
        serialized = self.jwt_serializer_class(profile).data
        tokens = JWTCryptor().encode(serialized)
        return {**tokens, **serialized}
