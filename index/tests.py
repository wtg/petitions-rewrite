import unittest
from index.models import Petition, Tag, User, Response, Signature

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

        petition.archived = True  # dunno if this is the right syntax
        self.assertTrue(petition.archived)

    def test_hidden(self):
        petition = Petition()
        self.assertFalse(petition.hidden)

        petition.hidden = True
        self.assertTrue(petition.hidden)

    # don't test setters, test creation of petition
    # ex if make petition w/o required field should fail
    # are there any required fiels when creating petition right now?
    # yes

    """
    This test fails, I think because the signatures field 
    is not initialized on creation.
    """

    def test_check_enough_signatures(self):
        petition = Petition(title="Save Greek Life")
        petition.expected_sig = 300  # should be a required field
        petition.save()
        self.assertFalse(petition.check_enough_sigs())

    """
    # check this, will it break bc of no initialization
    def test_check_tags_notags(self):
        petition = Petition()
        petition.save()
        self.assertTrue(petition.check_tags())

    def test_check_tags_onetag(self):
        petition = Petition()
        petition.save()
        tag1 = Tag(label="Athletics")
        tag1.save()
        
        petition.tags.add(tag1)
        self.assertTrue(petition.check_tags())

    # make the saves better
    def test_check_tags_fourtags(self):
        petition = Petition()
        petition.save()
        tag1 = Tag(label="Athletics")
        tag1.save()
        tag2 = Tag(label="Community")
        tag2.save()
        tag3 = Tag(label="Facilities")
        tag3.save()
        tag4 = Tag(label="Traditions")
        tag4.save()

        petition.tags.add(tag1, tag2, tag3, tag4)
        self.assertFalse(petition.check_tags())
    """


class UserModelTestCase(unittest.TestCase):
    def test_user_initials_alpha(self):
        user = User(rcs_id="rolleg", name="Grace Roller")
        user.set_initials()
        self.assertEqual("gr", user.initials)

    # rcs id's with numbers
    def test_user_initials_withint(self):
        user = User(rcs_id="linl6", name="Lucy Lin")
        user.set_initials()
        self.assertEqual("ll", user.initials)
