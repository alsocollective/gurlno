from django import template
import json
from django.utils.safestring import mark_safe
import datetime

register = template.Library()

@register.filter(name="mapsgen")
def mapsgen(addres):
	return "https://www.google.com/maps/embed/v1/place?q=%sCanada&key=AIzaSyBdpJO3FCVQ7UyWvOkRDfVpqMX-gjBmW1k"%urllib.quote("%s,%s ON, "%(addres.addr,addres.area))


@register.filter(name="timeAsJsonObject")
def timeAsJsonObject(timeObject):
	out = [
		["%s"%timeObject.sun_start,"%s"%timeObject.sun_end],	
		["%s"%timeObject.mon_start,"%s"%timeObject.mon_end],
		["%s"%timeObject.tue_start,"%s"%timeObject.tue_end],
		["%s"%timeObject.wed_start,"%s"%timeObject.wed_end],
		["%s"%timeObject.thu_start,"%s"%timeObject.thu_end],
		["%s"%timeObject.fri_start,"%s"%timeObject.fri_end],
		["%s"%timeObject.sat_start,"%s"%timeObject.sat_end],
	]
	return mark_safe(json.dumps(out))

def offSetTimeBy(diff):
	return datetime.timedelta(hours=diff) + datetime.datetime.now()

@register.filter(name="todayTimes")
def todayTimes(timeObject):
	# return '{{show.gallery.wed_start|date:"fA"}} &#8212; {{show.gallery.wed_end|date:"fA"}}'
	timeObject = timeObject.gallery
	currenttime = offSetTimeBy(-5)
	day = currenttime.weekday()
	short = "mon"
	if(day == 1):
		short = "tue"
	elif(day == 2):
		short = "wed"
	elif(day == 3):
		short = "thu"
	elif(day == 4):
		short = "fri"
	elif(day == 5):
		short = "sat"
	elif(day == 6):
		short = "sun"
		print "%s_start"%short
	timeformat = "%I:%M%p"


 	starttime = timeObject.__getattribute__("%s_start"%short)
 	if not starttime:
 		return "<h4 class='hours' data-open='false'> CLOSED </h4>"
	startten = starttime.strftime("%H.")
	startten += str(int(starttime.strftime("%M"))/60)
	start = starttime.strftime(timeformat)

	endtime = timeObject.__getattribute__("%s_end"%short)
	endten = endtime.strftime("%H.")
	endten += str(int(endtime.strftime("%M"))/60)
	end = endtime.strftime(timeformat)

	isOpen = "false"
	currenttime = currenttime.time()

	if currenttime < starttime and currenttime > endtime:
		isOpen = "true"

	return "<h4 class='hours' data-start='%s' data-end='%s'  data-open='%s'>%s &#8212; %s</h4>" %(startten,endten,isOpen,start,end)



