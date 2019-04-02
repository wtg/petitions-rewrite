import unittest
from index.models import Petition, Tag, User, Response, Signature

# check code coverage


class PetitionModelTestCase(unittest.TestCase):
    def test_set_hidden(self):
        p = Petition()
        self.assertFalse(p.hidden)

        p.set_hidden(True)
        self.assertTrue(p.hidden)

    def test_set_archived(self):
        p = Petition()
        self.assertFalse(p.archived)

        p.set_archived(True)
        self.assertTrue(p.archived)

    def test_add_description(self):
        p = Petition()
        p.add_description("Petition about Greek life")

        self.assertEqual(p.description, "Petition about Greek life")

    def test_check_enough_sigs_nosig(self):
        p = Petition(ID=1, expected_sig=300)
        self.assertFalse(p.check_enough_sigs())

    def test_check_enough_sigs_onesig(self):
        p = Petition(ID=2, expected_sig=300)
        p.save()
        u1 = User(rcs_id="linl6")
        u1.save()
        s1 = Signature(signer=u1)
        s1.save()
        p.signatures.add(s1)
        self.assertFalse(p.check_enough_sigs())

    def test_check_enough_sigs_enoughsig(self):
        p = Petition(ID=3, expected_sig=2)
        p.save()

        u1 = User(rcs_id="rolleg")
        u1.save()
        s1 = Signature(signer=u1)
        s1.save()

        u2 = User(rcs_id="linl6")
        u2.save()
        s2 = Signature(signer=u2)
        s2.save()

        p.signatures.add(s1, s2)
        self.assertTrue(p.check_enough_sigs())

    def test_check_tags_notags(self):
        p = Petition(ID=4)
        self.assertTrue(p.check_tags())

    def test_check_tags_onetag(self):
        p = Petition(ID=5, expected_sig=100)
        p.save()
        t1 = Tag(label="Athletics")
        t1.save()

        p.tags.add(t1)
        self.assertEqual(p.tags.count(), 1)
        self.assertTrue(p.check_tags())

    def test_check_tags_fourtags(self):
        p = Petition(ID=6, expected_sig=100)
        p.save()

        t1 = Tag(label="Athletics")
        t1.save()
        t2 = Tag(label="Greek")
        t2.save()
        t3 = Tag(label="Community")
        t3.save()
        t4 = Tag(label="Facilities")
        t4.save()

        p.tags.add(t1, t2, t3, t4)
        self.assertEqual(p.tags.count(), 4)
        self.assertFalse(p.check_tags())


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

    def test_set_admin(self):
        u = User(rcs_id="linl6", name="Lucy Lin")
        self.assertFalse(u.admin)

        u.set_admin(True)
        self.assertTrue(u.admin)


class ResponseModelTestCase(unittest.TestCase):
    def test_set_senate(self):
        r = Response()
        self.assertFalse(r.senator_investigation)

        r.set_senate(True)
        self.assertTrue(r.senator_investigation)

    def test_set_committee(self):
        r = Response()
        self.assertFalse(r.committee_formed)

        r.set_committee(True)
        self.assertTrue(r.committee_formed)

    def test_set_resolution(self):
        r = Response()
        self.assertFalse(r.vote_resolution)

        r.set_resolution(True)
        self.assertTrue(r.vote_resolution)

    def test_set_referendum(self):
        r = Response()
        self.assertFalse(r.vote_referendum)

        r.set_referendum(True)
        self.assertTrue(r.vote_referendum)

    def test_set_other(self):
        r = Response()
        self.assertFalse(r.refer_to_other)

        r.set_other(True)
        self.assertTrue(r.refer_to_other)

    def test_add_info_senate(self):
        r = Response()
        r.add_info_senate("More investigation info")
        self.assertEqual(r.investigation_info, "More investigation info")

    def test_add_info_committee(self):
        r = Response()
        r.add_info_committee("More committee info")
        self.assertEqual(r.committee_info, "More committee info")

    def test_add_info_resolution(self):
        r = Response()
        r.add_info_resolution("More resolution info")
        self.assertEqual(r.resolution_info, "More resolution info")

    def test_add_info_referendum(self):
        r = Response()
        r.add_info_referendum("More referendum info")
        self.assertEqual(r.referendum_info, "More referendum info")

    def test_add_info_other(self):
        r = Response()
        r.add_info_other("Other info")
        self.assertEqual(r.refer_other_info, "Other info")
