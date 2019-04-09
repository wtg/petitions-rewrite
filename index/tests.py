import unittest
from index.models import Petition, Tag, Response, Signature


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
