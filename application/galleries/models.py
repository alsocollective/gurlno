from django.db import models
from django.template.defaultfilters import slugify
from easy_thumbnails.fields import ThumbnailerImageField

class WorkMedium(models.Model):
	medium = models.CharField(max_length=500)
	varient_off = models.ManyToManyField('self',blank=True,null=True) 

	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.medium)
		super(WorkMedium, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.medium

class Tag(models.Model):
	tag = models.CharField(max_length=500)

	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.tag)
		super(Tag, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.slug

class Artist(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	website = models.URLField(blank=True,null=True)
	facebook = models.URLField(blank=True,null=True)
	tublr = models.URLField(blank=True,null=True)
	instagram = models.CharField(max_length=50,blank=True,null=True)
	twitter = models.CharField(max_length=50,blank=True,null=True)
	bio = models.TextField(max_length=1000,blank=True,null=True)
	email = models.CharField(max_length=150,blank=True,null=True)	
	phone = models.CharField(max_length=50,blank=True,null=True)
	gallorist = models.ManyToManyField('Gallery',blank=True,null=True)

	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify("%s %s"%(self.first_name,self.last_name))
		super(Artist, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.slug

class WorkImage(models.Model):
	title = models.CharField(max_length=500)
	alttext = models.CharField(max_length=500)
	Image = ThumbnailerImageField(upload_to='work-img',blank=True,null=True)
	description = models.TextField(max_length=1000,blank=True,null=True)	
	medium = models.ManyToManyField(WorkMedium,blank=True,null=True)
	creator = models.ManyToManyField(Artist)

	slug = models.SlugField(blank=True)

	def __unicode__(self):
		return self.title

class Neighbourhood(models.Model):
	title = models.CharField(max_length=300)
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Neighbourhood, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.title

class HoursOfOp(models.Model):
	mon_start = models.DateTimeField(blank=True,null=True)
	mon_end = models.DateTimeField(blank=True,null=True)
	tue_start = models.DateTimeField(blank=True,null=True)
	tue_end = models.DateTimeField(blank=True,null=True)
	wed_start = models.DateTimeField(blank=True,null=True)
	wed_end = models.DateTimeField(blank=True,null=True)
	thu_start = models.DateTimeField(blank=True,null=True)
	thu_end = models.DateTimeField(blank=True,null=True)
	fri_start = models.DateTimeField(blank=True,null=True)
	fri_end = models.DateTimeField(blank=True,null=True)
	sat_start = models.DateTimeField(blank=True,null=True)
	sat_end = models.DateTimeField(blank=True,null=True)
	sun_start = models.DateTimeField(blank=True,null=True)
	sun_end = models.DateTimeField(blank=True,null=True)

class Gallery(models.Model):
	title = models.CharField(max_length=50)
	logo = ThumbnailerImageField(upload_to='gal-logo',blank=True,null=True)
	url =  models.URLField(blank=True,null=True)
	description = models.TextField(max_length=1000)
	facebook = models.URLField(blank=True,null=True)	
	instagram = models.CharField(max_length=50,blank=True,null=True)
	twitter = models.CharField(max_length=50,blank=True,null=True)	
	location = models.CharField(max_length=600,blank=True,null=True)
	log = models.FloatField(default=0,blank=True,null=True)
	lat = models.FloatField(default=0,blank=True,null=True)
	email = models.CharField(max_length=150,blank=True,null=True)	
	phone = models.CharField(max_length=50,blank=True,null=True)	
	neighbourhood = models.ManyToManyField(Neighbourhood,blank=True,null=True)
	normal_hours = models.ForeignKey(HoursOfOp)
	google_place_key = models.CharField(max_length=50,blank=True,null=True)
	gallorist = models.ManyToManyField(Artist,blank=True,null=True)

	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Gallery, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name_plural = "Galleries"

class artType(models.Model):
	title = models.CharField(max_length=150)	
	logo = ThumbnailerImageField(upload_to='art-icon')
	description = models.TextField(max_length=1000)
	includes_meediums = models.ManyToManyField(WorkMedium,blank=True,null=True)
	tags = models.ManyToManyField(Tag,blank=True,null=True)

	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(artType, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Day(models.Model):
	start = models.DateTimeField(blank=True,null=True)
	end = models.DateTimeField(blank=True,null=True)

class Event(models.Model):
	title = models.CharField(max_length=150)	
	gallery = models.ForeignKey(Gallery)
	date_start = models.DateTimeField()
	date_end = models.DateTimeField()
	opening_start = models.DateTimeField()
	opening_end = models.DateTimeField()
	cover = models.FloatField(default=0,blank=True,null=True)
	description = models.TextField(max_length=1000,blank=True,null=True)
	link = models.URLField(blank=True)
	includes_artists = models.ManyToManyField(Artist,blank=True,null=True)
	cover_work = models.ForeignKey(WorkImage,blank=True,null=True,related_name="cover_work")
	includes_works = models.ManyToManyField(WorkImage,blank=True,null=True,related_name='works') 
	facebook = models.URLField(blank=True,null=True)	
	arttype = models.ManyToManyField(artType,blank=True,null=True)
	hours = models.ForeignKey(HoursOfOp,blank=True,null=True)
	days_showing = models.ManyToManyField(Day,blank=True,null=True)

	slug = models.SlugField(blank=True)
	def __unicode__(self):
		return self.title	

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Event, self).save(*args, **kwargs)

