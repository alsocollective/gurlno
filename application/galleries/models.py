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

	def firstLink(self):
		if self.website:
			return self.website
		if self.facebook:
			return self.facebook
		if self.tublr:
			return self.tublr
		if self.instagram:
			return self.instagram
		if self.twitter:
			return self.twitter
		return False

	def name(self):
		return "%s %s" %(self.first_name, self.last_name)

	def nameLink(self):
		link = self.firstLink()
		if link:
			return "<a href='%s'>%s %s</a>" %(link,self.first_name, self.last_name)
		return self.name()

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

	timeDateAsString = models.TextField(max_length=1000,blank=True,null=True)
	easyReadDate = models.TextField(max_length=1000,blank=True,null=True)

	next_show = models.ForeignKey('Show',null=True,blank=True,related_name="the_most_recent_show")

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		self.generateTimeDate();
		self.easyReadDate = self.generateEasyReadTime();
		super(Gallery, self).save(*args, **kwargs)

	def generateTimeDate(self):
		myString = """
			data-mons="%s" data-mone="%s" data-monstring="%s"
			data-tues="%s" data-tuee="%s" data-tuestring="%s"
			data-weds="%s" data-wede="%s" data-wedstring="%s"
			data-thus="%s" data-thue="%s" data-thustring="%s"
			data-fris="%s" data-frie="%s" data-fristring="%s"
			data-sats="%s" data-sate="%s" data-satstring="%s"
			data-suns="%s" data-sune="%s" data-sunstring="%s"
		""" %(
			self.TimeToString(self.mon_start),self.TimeToString(self.mon_end),self.TimeToSoftString(self.mon_start,self.mon_end),
			self.TimeToString(self.tue_start),self.TimeToString(self.tue_end),self.TimeToSoftString(self.tue_start,self.tue_end),
			self.TimeToString(self.wed_start),self.TimeToString(self.wed_end),self.TimeToSoftString(self.wed_start,self.wed_end),
			self.TimeToString(self.thu_start),self.TimeToString(self.thu_end),self.TimeToSoftString(self.thu_start,self.thu_end),
			self.TimeToString(self.fri_start),self.TimeToString(self.fri_end),self.TimeToSoftString(self.fri_start,self.fri_end),
			self.TimeToString(self.sat_start),self.TimeToString(self.sat_end),self.TimeToSoftString(self.sat_start,self.sat_end),
			self.TimeToString(self.sun_start),self.TimeToString(self.sun_end),self.TimeToSoftString(self.sun_start,self.sun_end),
			)
		self.timeDateAsString = myString

	def generateEasyReadTime(self):
		days = ["mon_start","tue_start","wed_start","thu_start","fri_start","sat_start","sun_start"]
		dayse = ["mon_end","tue_end","wed_end","thu_end","fri_end","sat_end","sun_end"]
		opens = []
		for day in range(0,len(days)):
			time = getattr(self,days[day])
			endtime = getattr(self,dayse[day])
			pc = len(opens)-1 #previous count
			if(time != None):
				if(len(opens)>0 and opens[pc]["c"]== day-1 and opens[pc]["t"]==time and opens[pc]["te"]==endtime):
					opens[pc]["e"]=days[day]
					opens[pc]["c"]=day
				else:
					opens.append({"s":days[day],"e":"","c":day,"t":time,"te":endtime})
		out = "<ul>"
		for op in opens:

			out += "<li><span>%s:</span> %s</li>" %(self.dayToSoftString(op["s"][:3],op["e"][:3]),self.TimeToSoftString(op["t"],op["te"]))
		return out + "</ul>"

	def dayToSoftString(self,start,end):
		if(not end):
			return start
		return "%s &#8212; %s" %(start,end)

	def TimeToString(self,time):
		if(not time):
			return "n/a"
		timeformat = "%I:%M%p"
		timeDec = time.strftime("%H.")
		timeDec += str(int(time.strftime("%M"))/60)
		# time = time.strftime(timeformat)
		return timeDec#,time

	def TimeToSoftString(self,time1,time2):
		if(not time1):
			return "CLOSED"
		timeformat = "%I:%M%p"
		return "%s &#8212; %s"%(time1.strftime(timeformat),time2.strftime(timeformat))

	def open(self):
		try:
			time = (datetime.timedelta(hours=-5) + datetime.datetime.now())
			day = time.weekday()
			days = ["mon_start","tue_start","wed_start","thu_start","fri_start","sat_start","sun_start"]
			dayse = ["mon_end","tue_end","wed_end","thu_end","fri_end","sat_end","sun_end"]
			if getattr(self,days[day]) == None:
				return "galisclosed"
			if(time.time() < getattr(self,days[day]) and time.time() > getattr(self,dayse[day])):
				return "galisopen"
			return "galisclosed"
		except Exception, e:
			print e
			return "error"



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
	description_author = models.CharField(max_length=150,blank=True,null=True)	
	description_link = models.URLField(blank=True)
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
		starttime = ""
		endtime = ""
		softstring = ""
		daynumber = 0

		if(self.opening_start and self.opening_start == time.date()):
			reception = "reception"
			daynumber = self.opening_start.weekday()
			if self.opening_end_time:
				starttime = self.TimeToString(self.opening_start_time)
				endtime	= self.TimeToString(self.opening_end_time)
				softstring = self.TimeToSoftString(self.opening_start_time,self.opening_end_time)
				if(self.opening_start_time < time.time() < self.opening_end_time):
					opened = "doorsopen"
			elif(self.opening_start_time < time.time()):
				opened = "doorsopen"

		else:
			day = time.strftime("%a").lower()
			#TODO remove the set day to friday...
			# day = "mon"
 			starttime = self.gallery.__getattribute__("%s_start"%day)
			endtime = self.gallery.__getattribute__("%s_end"%day)
			if starttime:
				if endtime:
					if starttime < time.time() < endtime:
						opened = "doorsopen"
				elif starttime < time.time():
					opened = "doorsopen"

		# return "class='gallery'"
		if(not reception):
			return "class='gallery %s %s'"%(reception,opened)

		return """
			class="gallery %s %s" 
			data-opening="%s" 
			data-times="%s" 
			data-timee="%s"
			data-timestring="%s"
			data-dayofweek="%d"
		""" %(reception,opened,opened,starttime[0],endtime[0],softstring,daynumber)


	def mountedAndOpening(self):
		mounted = "notmounted"
		opening = "notreception"

		time = datetime.timedelta(hours=-5) + datetime.datetime.now()
		if (self.date_start and self.date_start < time.date()):
			mounted = "mounted"
		if (self.opening_start and self.opening_start == time.date()):
			opening = "reception"

		return "%s %s"%(mounted,opening)

	def TimeToString(self,time):
		timeformat = "%I:%M%p"
		timeDec = time.strftime("%H.")
		timeDec += str(int(time.strftime("%M"))/60)
		time = time.strftime(timeformat)
		return (timeDec,time)

	def TimeToSoftString(self,time1,time2):
		if(not time1):
			return "CLOSED"
		timeformat = "%I:%M%p"
		return "%s &#8212; %s"%(time1.strftime(timeformat),time2.strftime(timeformat))

	def __unicode__(self):
		return self.title	

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		show = Show.objects.all().filter(date_end__gte=datetime.datetime.now(),gallery=self.gallery).order_by("date_start")[0]
		self.gallery.next_show = show
		self.gallery.save()

		super(Show, self).save(*args, **kwargs)