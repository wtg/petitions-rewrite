from django_cas_ng.backends import CASBackend
from django.conf import settings
import requests
import os


class StudentCASBackend(CASBackend):
    def user_can_authenticate(self, user):
        url = (
            "https://webtech.union.rpi.edu/services/identity/valid/"
            + str(user.username).lower()
        )
        key = settings.IDENTITY_KEY
        r = requests.get(url, headers={"Authorization": "Token " + key})
        r.raise_for_status()
        error = r.json()["error"]
        if error:
            return False
        student = r.json()["user_type"] == "Student"
        if not student:
            return False

        user.first_name = r.json()["first_name"]
        user.last_name = r.json()["last_name"]

        if settings.DEBUG == True:
            user.is_staff = True
            user.is_superuser = True

        user.save()
        return True
