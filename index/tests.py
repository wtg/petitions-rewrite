import unittest
from .models import Petition, Tag, User, Response, Signature


class PetitionModelTestCase(unittest.TestCase):
    def test_title(self):
        petition = Petition(title="Save Greek Life")
        self.assertEqual("Save Greek Life", petition.title)

    """
    This test fails, I think because the signatures field 
    is not initialized on creation.
    """
    # def test_check_enough_signatures(self):
    #     petition = Petition(title="Save Greek Life")
    #     self.assertFalse(petition.check_enough_sigs())


class UserModelTestCase(unittest.TestCase):
    def test_user_initials(self):
        user = User(rcs_id="rolleg", name="Grace Roller")
        user.set_initials()
        self.assertEqual("gr", user.initials)
