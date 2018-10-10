from django.db import models

class Petitions(models.Model):
	title = models.CharField(max_length = 200)			#title of petition
	author = models.CharField(max_length = 50)			#the author name

	description = models.TextField()					#the paragraph description
	email = EmailField(max_length = 254)				#rcs id				
	createdDate = models.DateTimeField(default= timezone.now)		#files the date created
	expectedSig = integerField(300)			#the expected signature to move to the next step

	tags = models.ManyToField(Tag, related_name = 'petititons')
	signatures = models.ManyToField(Signature, related_name = 'petitions')

	def __unicode__(self):
        return self.title		#returns title when asksed for the item

#creates a tag, there can be many in a single petition
class Tag(model.Model):
	word = CharField(max_length = 50)	
	def __unicode__(self):
        return self.word

#logs a signature, there can be many in a single petition
class Signature(model.Model):
	signerInitials = CharField(max_length = 3)		#

	def __unicode__(self):
		return self.signerInitials
