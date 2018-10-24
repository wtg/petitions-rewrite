from django.db import models

class Petitions(models.Model):
	title = models.CharField(max_length=200)	#title of petition
	description = models.TextField()			#the paragraph description
				
	created_date = models.DateTimeField(default=timezone.now)	#files the date created
	expected_sig = models.IntegerField(300)		#the expected signature to move to the next step

	author = models.ForeignKey(User, related_name= 'petitions')	#the author of the petition
	tags = models.ManyToField(Tag, related_name='petititons')	#the tags, probably a max of 3
	signatures = models.ManyToField(Signature, related_name='petitions')	#the signature

	committeFormed = models.BooleanField(default = False)	#whether or a senate commitee has been formed
	senateResponse = models.TextField()		#If the senate has responded , their answer

	def __unicode__(self):
        return self.title		#returns title when asked for the item

#creates a tag, there can be many in a single petition
class Tag(models.Model):
	word = models.CharField(max_length=15)	

	def __unicode__(self):
        return self.word

#logs a signature, there can be many in a single petition
class Signature(models.Model):
	signer = models.ForeignKey(User, related_name = 'signatures')	#the person trying to sign the petition
	signed_date = models.DateTimeField(default=timezone.now)	#when they signed 
	def __unicode__(self):
		return self.signer	#returns the signer when asked for the initials

class User(models.Model):
	rcs_id = models.CharField(max_length=10)	#rcs id	
	name = models.CharField(max_length=50)	#the author name
	admin = models.BooleanField(default = False)	#is admin?
	banned = models.BooleanField(default = False)	#is the person banned?-- not very likely
	initials = models.CharField(max_length = 2)		#their initials

	def __unicode__(self):
		return self.name 	#returns their name
