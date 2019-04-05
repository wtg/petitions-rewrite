from django_cas_ng.backends import CASBackend


class StudentCASBackend(CASBackend):
    def user_can_authenticate(self, user):
        # TODO: add WTG identity to check if user is a student
        return True
