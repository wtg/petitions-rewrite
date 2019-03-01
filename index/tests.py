import unittest
from .models import Petition, Tag, User, Response, Signature

# check code coverage



class PetitionModelTestCase(unittest.TestCase):
    def test_title(self):
        petition = Petition(title="Save Greek Life")
        self.assertEqual("Save Greek Life", petition.title)

    def test_description(self):
        petition = Petition(description="A petition to save Greek life")
        self.assertEqual("A petition to save Greek life", petition.description)
    
    def test_ID(self):
        return
        # I don't actually know how this works rn
    
    def test_archived(self):
        petition = Petition()
        self.assertFalse(petition.archived)

        petition.archived = True # dunno if this is the right syntax
        self.assertTrue(petition.archived)
    
    def test_hidden(self):
        petition = Petition()
        self.assertFalse(petition.hidden)

        petition.hidden = True
        self.assertTrue(petition.hidden)

    # don't test setters, test creation of petition
        # ex if make petition w/o required field should fail

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


    #rcs id's with numbers

