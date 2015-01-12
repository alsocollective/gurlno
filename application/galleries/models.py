from django.db import models
from django.template.defaultfilters import slugify
from easy_thumbnails.fields import ThumbnailerImageField
import datetime

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

	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify("%s %s"%(self.first_name,self.last_name))
		super(Artist, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.slug

class Gallorist(models.Model):
	prefix = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)	
	artist = models.ForeignKey(Artist,blank=True,null=True)
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify("%s %s %s"%(self.prefix,self.first_name,self.last_name))
		super(Gallorist, self).save(*args, **kwargs)
	
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

class Gallery_Type(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField(max_length=1000,blank=True,null=True)	
	image = ThumbnailerImageField(upload_to='gallery-type',blank=True,null=True)
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Gallery_Type, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.title

class Gallery(models.Model):
	title = models.CharField(max_length=50)
	logo = ThumbnailerImageField(upload_to='gal-logo',blank=True,null=True)
	url =  models.URLField(blank=True,null=True)
	description = models.TextField(max_length=1000)
	facebook = models.URLField(blank=True,null=True)	
	instagram = models.CharField(max_length=50,blank=True,null=True)
	twitter = models.CharField(max_length=50,blank=True,null=True)	
	address = models.CharField(max_length=600,blank=True,null=True)
	log = models.FloatField(default=0,blank=True,null=True)
	lat = models.FloatField(default=0,blank=True,null=True)
	email = models.CharField(max_length=150,blank=True,null=True)	
	phone = models.CharField(max_length=50,blank=True,null=True)	
	neighbourhood = models.ManyToManyField(Neighbourhood,blank=True,null=True)
	google_place_key = models.CharField(max_length=50,blank=True,null=True)
	gallorist = models.ManyToManyField(Gallorist,blank=True,null=True)
	gallery_tyle = models.ManyToManyField(Gallery_Type,blank=True,null=True)


	slug = models.SlugField(blank=True)

	mon_start = models.TimeField(blank=True,null=True)
	mon_end = models.TimeField(blank=True,null=True)
	tue_start = models.TimeField(blank=True,null=True)
	tue_end = models.TimeField(blank=True,null=True)
	wed_start = models.TimeField(blank=True,null=True)
	wed_end = models.TimeField(blank=True,null=True)
	thu_start = models.TimeField(blank=True,null=True)
	thu_end = models.TimeField(blank=True,null=True)
	fri_start = models.TimeField(blank=True,null=True)
	fri_end = models.TimeField(blank=True,null=True)
	sat_start = models.TimeField(blank=True,null=True)
	sat_end = models.TimeField(blank=True,null=True)
	sun_start = models.TimeField(blank=True,null=True)
	sun_end = models.TimeField(blank=True,null=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Gallery, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name_plural = "Galleries"
		
class HoursOfOp(models.Model):
	parent = models.ForeignKey(Gallery,blank=True,null=True)
	mon_start = models.TimeField(blank=True,null=True)
	mon_end = models.TimeField(blank=True,null=True)
	tue_start = models.TimeField(blank=True,null=True)
	tue_end = models.TimeField(blank=True,null=True)
	wed_start = models.TimeField(blank=True,null=True)
	wed_end = models.TimeField(blank=True,null=True)
	thu_start = models.TimeField(blank=True,null=True)
	thu_end = models.TimeField(blank=True,null=True)
	fri_start = models.TimeField(blank=True,null=True)
	fri_end = models.TimeField(blank=True,null=True)
	sat_start = models.TimeField(blank=True,null=True)
	sat_end = models.TimeField(blank=True,null=True)
	sun_start = models.TimeField(blank=True,null=True)
	sun_end = models.TimeField(blank=True,null=True)

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

	title = models.CharField(max_length=150,blank=True,null=True)
	description = models.TextField(max_length=1000,blank=True,null=True)
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		if(self.title):
			self.slug = slugify(self.title)
		else:
			self.slug = "no-title"
		super(Day, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Show(models.Model):
	title = models.CharField(max_length=150)	
	gallery = models.ForeignKey(Gallery)
	date_start = models.DateField(blank=True,null=True)
	date_start_time = models.TimeField(blank=True,null=True)
	date_end = models.DateField(blank=True,null=True)
	date_end_time = models.TimeField(blank=True,null=True)
	opening_start = models.DateField(blank=True,null=True)
	opening_start_time = models.TimeField(blank=True,null=True)
	opening_end = models.DateField(blank=True,null=True)
	opening_end_time = models.TimeField(blank=True,null=True)
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
	currator = models.ManyToManyField(Gallorist,blank=True,null=True)
	tags = models.ManyToManyField(Tag,blank=True,null=True)
	published = models.BooleanField(default=True)
	slug = models.SlugField(blank=True)

	# finds if the gallery is open, open that day, reception if day
	# => string
	def checkIfOpen(self):
		#TODO set back time -10 to -5
		time = datetime.timedelta(hours=-5) + datetime.datetime.now()
		reception = ""
		opened = ""

		if(self.opening_start and self.opening_start == time.date()):
			reception = "reception"
			if self.opening_end_time:
				if(self.opening_start_time < time.time() < self.opening_end_time):
					opened = "doorsopen"
			elif(self.opening_start_time < time.time()):
				opened = "doorsopen"

		else:
			day = time.strftime("%a").lower()
			#TODO remove the set day to friday...
			day = "fri"
 			starttime = self.gallery.__getattribute__("%s_start"%day)
			endtime = self.gallery.__getattribute__("%s_end"%day)
			if starttime:
				if endtime:
					if starttime < time.time() < endtime:
						opened = "doorsopen"
				elif starttime < time.time():
					opened = "doorsopen"
		return "%s %s" %(reception, opened)

	# returns the eles as a html h4 element
	# => <h4 data-open="18" data-close="20.5"> 6:00pm - 8:30pm </h4>
	# => <h4> closed </h4>
	def getHoursOpen(self):
		out = "<h4> CLOSED </h4>"
		#TODO set back time -10 to -5
		time = datetime.timedelta(hours=-5) + datetime.datetime.now()
		if(self.opening_start and self.opening_start == time.date()):
			start = self.TimeToString(self.opening_start_time)
			if self.opening_end_time:
				end = self.TimeToString(self.opening_end_time)
			else:
				end = [24,"unknown"]
			out = "<h4 class='hours' data-start='%s' data-end='%s' >%s &#8212; %s</h4>" %(start[0],end[0],start[1],end[1])
		else:
			day = time.strftime("%a").lower()
			#TODO remove the set day to friday...
			day = "fri"
 			starttime = self.gallery.__getattribute__("%s_start"%day)
			endtime = self.gallery.__getattribute__("%s_end"%day)
			if starttime:
				if endtime:
					start = self.TimeToString(starttime) 
					end = self.TimeToString(endtime)					
					out = "<h4 class='hours' data-start='%s' data-end='%s' >%s &#8212; %s</h4>" %(start[0],end[0],start[1],end[1])
				else:
					start = self.TimeToString(starttime) 
					out = [24,"unknown"]
					out = "<h4 class='hours' data-start='%s' data-end='%s' >%s &#8212; %s</h4>" %(start[0],end[0],start[1],end[1])
		return out

	def TimeToString(self,time):
		timeformat = "%I:%M%p"
		timeDec = time.strftime("%H.")
		timeDec += str(int(time.strftime("%M"))/60)
		time = time.strftime(timeformat)
		return (timeDec,time)

	def __unicode__(self):
		return self.title	

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Show, self).save(*args, **kwargs)