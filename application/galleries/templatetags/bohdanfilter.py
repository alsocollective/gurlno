from django import template
import json
from django.utils.safestring import mark_safe
import datetime

register = template.Library()

@register.filter(name="mapsgen")
def mapsgen(addres):
	return "https://www.google.com/maps/embed/v1/place?q=%sCanada&key=AIzaSyBdpJO3FCVQ7UyWvOkRDfVpqMX-gjBmW1k"%urllib.quote("%s,%s ON, "%(addres.addr,addres.area))

@register.filter(name="timeline")
def timeline(timeObject):
	return ""

	"""
		<div class="time">
			<span class="date-time {% if not time.mon_start %}notopen{% endif %}">mon - {% if time.mon_start %} {{time.mon_start}} till {{time.mon_end}} {% else %} not Open {% endif %}</span>
			<span class="date-time {% if not time.tue_start %}notopen{% endif %}">tue - {% if time.tue_start %} {{time.tue_start}} till {{time.tue_end}} {% else %} not Open {% endif %}</span>
			<span class="date-time {% if not time.wed_start %}notopen{% endif %}">wed - {% if time.wed_start %} {{time.wed_start}} till {{time.wed_end}} {% else %} not Open {% endif %}</span>
			<span class="date-time {% if not time.thu_start %}notopen{% endif %}">thu - {% if time.thu_start %} {{time.thu_start}} till {{time.thu_end}} {% else %} not Open {% endif %}</span>
			<span class="date-time {% if not time.fri_start %}notopen{% endif %}">fri - {% if time.fri_start %} {{time.fri_start}} till {{time.fri_end}} {% else %} not Open {% endif %}</span>
			<span class="date-time {% if not time.sat_start %}notopen{% endif %}">sat - {% if time.sat_start %} {{time.sat_start}} till {{time.sat_end}} {% else %} not Open {% endif %}</span>
			<span class="date-time {% if not time.sun_start %}notopen{% endif %}">sun - {% if time.sun_start %} {{time.sun_start}} till {{time.sun_end}} {% else %} not Open {% endif %}</span>
		</div>
	"""

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
	day = offSetTimeBy(-5).weekday()
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

	return "%s till %s" %(timeObject.__getattribute__("%s_start"%short),timeObject.__getattribute__("%s_end"%short))
	return dir(timeObject)

@register.filter(name="dirIt")
def dirIt(obj):
	return dir(obj)


