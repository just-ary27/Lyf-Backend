from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication, exceptions

import firebase_admin.auth as auth

from user.models import LyfUser


class FirebaseAuthentication(authentication.BaseAuthentication):
    """
    Custom Authentication class that checks a firebase
    auth token for validity.
    """

    @staticmethod
    def fire_id(token: str):
        if token.split(" ")[0] == "Token":
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']

            return uid
        else:
            raise Exception

    def authenticate(self, request):
        token = request.headers.get('Authorization')

        if not token:
            return None
        else:
            try:
                uid = self.fire_id(token)

            except:
                return None

            try:
                user = LyfUser.objects.get(id=uid)
                return user, None

            except ObjectDoesNotExist:
                raise exceptions.AuthenticationFailed('No such user')
