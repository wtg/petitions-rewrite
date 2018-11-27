from django.db import models

class Petition(models.Model):
	title = models.CharField(max_length=200)	#title of petition
	description = models.CharField(max_length=4000)	#the paragraph description
	ID = models.IntegerField(999999, primary_key=True)
	archived = models.BooleanField(default=False)
	hidden = models.BooleanField(default=False)
				
	created_date = models.DateTimeField(db_index=True, default=timezone.now)	#files the date created
	expected_sig = models.IntegerField(300)		#the expected signature to move to the next step

	author = models.ForeignKey(User, related_name='petitions')	#the author of the petition
	tags = models.ManyToManyField(Tag, related_name='petitions')	#the tags, probably a max of 3
	signatures = models.ManyToManyField(Signature, related_name='petitions')	#the signature

	senate_response = models.ForeignKey(Responses, related_name='petitions')		#If the senate has responded , their answer

	

	def __unicode__(self):
        return self.title		#returns title when asked for the item

    def check_enough_sigs(self):
    	if self.signatures.count() >= self.expected_sig:
    		return True
    	return False

    def check_tags(self):
    	if self.tags.count() > 3 :
    		return False
    	return True



#creates a tag, there can be many in a single petition
class Tag(models.Model):
	word = models.CharField(max_length=15, primary_key=True)	

	def __unicode__(self):
        return self.word

#logs a signature, there can be many in a single petition
class Signature(models.Model):
	signer = models.ForeignKey(User, related_name='signatures')	#the person trying to sign the petition
	signed_date = models.DateTimeField(default=timezone.now)	#when they signed 
	
	def __unicode__(self):
		return self.signer	#returns the signer when asked for the initials

class User(models.Model):
	rcs_id = models.CharField(max_length=10, primary_key = True)	#rcs id	
	name = models.CharField(max_length=50)	#the author name
	admin = models.BooleanField(default=False)	#is admin?
	banned = models.BooleanField(default=False)	#is the person banned?-- not very likely
	initials = models.CharField(max_length=2)		#their initials

	def __unicode__(self):
		return self.name 	#returns their name

	def get_initials(self):
		return self.initials

	def get_name(self):
		return self.name

	def get_status(self):
		if self.admin
			return True

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



'''
FUNCTIONS TO MAKE:
	Petitions-
		create_a_petition
		//check_enough_sigs
		//check_tags
		add_tag

		delete_a petition
		is_commitee_formed
		add_senate_response
	Tag-
		create_tag
		delete_tag

	Signature-
		add signer
		get_signer_initials

	User-
		verify_user_status
		get_initials
		get_name
		get_status
'''
