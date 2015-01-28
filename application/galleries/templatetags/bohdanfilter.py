from django import template
import json
from django.utils.safestring import mark_safe
import datetime

register = template.Library()

@register.filter(name="artistLink")
def artistLink(artist):
	if(artist.website):
		return artist.website
	if(artist.facebook):
		return artist.facebook
	if(artist.tublr):
		return artist.tublr
	if(artist.instagram):
		return artist.instagram
	if(artist.twitter):
		return artist.twitter
