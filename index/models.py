from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Creates a tag, there can be at most three in a single petition
class Tag(models.Model):
    label = models.CharField(max_length=15, primary_key=True)

    # Returns label when asked for the tag
    def __unicode__(self):
        return self.label

    def __str__(self):
        return self.label

# Logs a signature, there can be many in a single petition
class Signature(models.Model):
    # The person trying to sign the petition
    signer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="signatures"
    )
    signed_date = models.DateTimeField(default=timezone.now)  # When they signed

    # Returns the signer when asked for the initials
    def __unicode__(self):
        return self.signer

    def get_initials(self):
        full_name = self.signer.get_username()
        name_modified = "".join([i for i in full_name if not i.isdigit()])
        return name_modified[-1] + name_modified[0]


# Creates a response based on whether the senate is investigating the topic of the Petition
class Response(models.Model):
    senator_investigation = models.BooleanField(default=False)
    committee_formed = models.BooleanField(default=False)
    vote_resolution = models.BooleanField(default=False)
    vote_referendum = models.BooleanField(default=False)
    refer_to_other = models.BooleanField(default=False)

    investigation_info = models.CharField(max_length=1000)
    committee_info = models.CharField(max_length=1000)
    resolution_info = models.CharField(max_length=1000)
    referendum_info = models.CharField(max_length=1000)
    refer_other_info = models.CharField(max_length=1000)

    # If there is a senate investigation in place, set
    # senator_investigation to true, false otherwise
    def set_senate(self, bool_val):
        self.senator_investigation = bool_val

    # If there was a committee creates, set
    # committee_formed to true, false otherwise
    def set_committee(self, bool_val):
        self.committee_formed = bool_val

    # If there was a resolution voted on, set
    # vote_resolution to true, false otherwise
    def set_resolution(self, bool_val):
        self.vote_resolution = bool_val

    # If there was a referendum voted on, set
    # vote_referendum to true, false otherwise
    def set_referendum(self, bool_val):
        self.vote_referendum = bool_val

    # If some other action was taken/ referred to another group,
    # set refer_to_other to true, false otherwise
    def set_other(self, bool_val):
        self.refer_to_other = bool_val

    # Add information for the senate investigation
    def add_info_senate(self, info):
        self.investigation_info = info
        return self.investigation_info

    # Add information on the committee assigned to help
    def add_info_committee(self, info):
        self.committee_info = info
        return self.committee_info

    # Add information on the resolution that was voted on
    def add_info_resolution(self, info):
        self.resolution_info = info
        return self.resolution_info

    # Add information on the referendum that wsa voted on
    def add_info_referendum(self, info):
        self.referendum_info = info
        return self.referendum_info

    # Add information on the other group that the issue was
    # referred to
    def add_info_other(self, info):
        self.refer_other_info = info
        return self.refer_other_info


class Petition(models.Model):
    title = models.CharField(max_length=200)  # Title of petition
    description = models.CharField(max_length=4000)  # The paragraph description
    ID = models.IntegerField(primary_key=True)
    archived = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)

    created_date = models.DateTimeField(
        db_index=True, default=timezone.now
    )  # Files the date created
    expected_sig = models.IntegerField(
        300
    )  # The expected signature to move to the next step

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="petitions", blank=True, null=True
    )  # The author of the petition
    tags = models.ManyToManyField(
        Tag, related_name="petitions", blank=True
    )  # The tags, probably a max of 3
    signatures = models.ManyToManyField(
        Signature, related_name="petitions", blank=True
    )  # The signature

    senate_response = models.ForeignKey(
        Response,
        on_delete=models.CASCADE,
        related_name="petitions",
        blank=True,
        null=True,
    )  # If the senate has responded , their answer

    # Returns title when asked for the item
    def __unicode__(self):
        return self.title

        # Sets the hidden variable as true if we don't want it to
        # Be displayed in the main site

    def set_hidden(self, bool_val):
        self.hidden = bool_val

        # If the petition isn't active, we can set the archived variable as true

    def set_archived(self, bool_val):
        self.archived = bool_val

        # Adds a description to the basic petitions model, with a max length
        # of 4000 words

    def add_description(self, descript):
        self.description = descript
        return True
        # Returns true if we have enough signatures on the petition

    def check_enough_sigs(self):
        if self.signatures.count() >= self.expected_sig:
            return True
        return False
        # Makes sure the we have less than three tags in the model

    def check_tags(self):
        if self.tags.count() > 3:
            return False
        return True

        # Add tag to a petition, there can be at most three in a single petition
        # def add_tag (self):

    def get_url(self):
        return reverse("petition-detail", args=[str(self.ID)])

    # register = template.Library()
    # @register.simple_tag
    # def get_sign_url(self, user):
    #     return reverse("sign", args=[str(self.ID), str(user.username)])
