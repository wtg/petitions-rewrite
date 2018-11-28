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

    def create(cls, title):
    	petition = cls(title = title)
    	return petition

    def set_hidden(self, bool_val):
    	self.hidden = bool_val
    	return self.hidden

    def set_archived(self, bool_val):
    	self.archived = bool_val
    	return self.archived

    def add_description(self, descript)
    	self.description = descript
    	return True

    def check_enough_sigs(self):
    	if self.signatures.count() >= self.expected_sig:
    		return True
    	return False

    def check_tags(self):
    	if self.tags.count() > 3:
    		return False
    	return True

    #def add_tag (self):



#creates a tag, there can be many in a single petition
class Tag(models.Model):
	word = models.CharField(max_length=15, primary_key=True)	

	def create(cls, word):
		tag = cls(word = word)
		return tag

	def __unicode__(self):
        return self.word

#logs a signature, there can be many in a single petition
class Signature(models.Model):
	signer = models.ForeignKey(User, related_name='signatures')	#the person trying to sign the petition
	signed_date = models.DateTimeField(default=timezone.now)	#when they signed 
	
	def create(cls, signer):
		signature = cls(signer = signer)
		return signature

	def __unicode__(self):
		return self.signer	#returns the signer when asked for the initials

class User(models.Model):
	rcs_id = models.CharField(max_length=10, primary_key = True)	#rcs id	
	name = models.CharField(max_length=50)	#the author name
	admin = models.BooleanField(default=False)	#is admin?
	banned = models.BooleanField(default=False)	#is the person banned?-- not very likely
	initials = models.CharField(max_length=2)		#their initials

	def __unicode__(self):
		return self.rcs_id 	#returns their name

	def create(cls, rcs_id):
		user = cls(rcs_id = rcs_id)
		return user

	def set_initials(self):
		full = self.rcs_id
		f_modified = ''.join([i for i in full if not i.isdigit()])
		intials = f_modified[-1] + f_modified[0]
		return initals

	def get_initials(self):
		return self.initials

	def get_name(self):
		return self.name

	def get_status(self):
		if self.admin:
			return True
		return False

	#def set_admin(self):
	#def get_name(self):

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

	def set_senate(self,bool_val):
		self.senator_investigation = bool_val
		return self.senator_investigation

	def set_committee (self,bool_val):
		self.committee_formed = bool_val
		return self.committee_formed

	def set_resolution (self,bool_val):
		self.vote_resolution = bool_val
		return self.vote_resolution

	def set_referendum (self,bool_val):
		self.vote_referendum = bool_val
		return self.vote_referendum

	def set_other (self,bool_val):
		self.refer_to_other = bool_val
		return self.refer_to_other



	def add_info_senate(self,info):
		self.investigation_info = info
		return self.investigation_info

	def add_info_committee (self,info):
		self.committee_info = info
		return self.committee_info

	def add_info_resolution (self,info):
		self.resolution_info = info
		return self.resolution_info

	def add_info_referendum (self,info):
		self.referendum_info = info
		return self.referendum_info

	def add_info_other (self, info):
		self.refer_other_info = info
		return self.refer_other_info

