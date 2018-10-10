from django.db import models

class Petitions(models.Model):
	title = models.CharField(max_length = 200)
	author = models.CharField(max_length = 50)

	description = models.TextField()
	email = EmailField(max_length = 254)
	createdDate = models.DateTimeField(default= timezone.now)
	expectedSig = integerField(300)

	tags = models.ManyToField(Tag, related_name = 'petititons')
	signatures = models.ManyToField(Signature, related_name = 'petitions')


	def __unicode__(self):
        return self.title

class Tag(model.Model):
	word = CharField(max_length = 50)

	def __unicode__(self):
        return self.word

class Signature(model.Model):
	signerInitials = CharField(max_length = 3)

	def __unicode__(self):
		return self.signerInitials