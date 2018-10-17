from django.db import models

class Petitions(models.Model):
	title = models.CharField(max_length=200)	#title of petition
	author = models.CharField(max_length=50)	#the author name

	description = models.TextField()			#the paragraph description
	email = models.EmailField(max_length=254)	#rcs id				
	created_date = models.DateTimeField(default=timezone.now)	#files the date created
	expected_sig = models.IntegerField(300)		#the expected signature to move to the next step

	tags = models.ManyToField(Tag, related_name='petititons')
	signatures = models.ManyToField(Signature, related_name='petitions')

	def __unicode__(self):
        return self.title		#returns title when asksed for the item

#creates a tag, there can be many in a single petition
class Tag(models.Model):
	word = models.CharField(max_length=50)	
	def __unicode__(self):
        return self.word

#logs a signature, there can be many in a single petition
class Signature(models.Model):
	signer_initials = models.CharField(max_length=3)

	def __unicode__(self):
		return self.signer_initials
