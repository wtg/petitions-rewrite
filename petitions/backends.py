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
        key = str(os.environ.get("IDENTITY_KEY"))
        r = requests.get(url, headers={"Authorization": "Token " + key})
        error = r.json()["error"]
        if error:
            return False
        student = r.json()["user_type"] == "Student"
        if not student:
            return False

        return True
