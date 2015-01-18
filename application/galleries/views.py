from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from galleries.models import *
from application.settings import MEDIA_URL

import json, datetime

def offSetTimeBy(diff):
	return datetime.timedelta(hours=diff) + datetime.datetime.now()

def loadMainGalleryList(request):
	now = offSetTimeBy(-5).date()
	shows = Show.objects.all().filter(date_end__gte=now)
	return render(request,'rev2/index.html',{"data":{"shows":shows}})


def home(request):
	if request.user.is_authenticated():
		return loadMainGalleryList(request)
	else:
		return redirect('/login')

def currentshow(request,slug):
	try:
		now = offSetTimeBy(-5).date()
		gallery = Gallery.objects.get(slug = slug)
		show = Show.objects.all().filter(date_end__gte=now, gallery=gallery)[0]
		out = {"gal":gallery,"show":show}
	except Exception, e:
		print e
		out = {"erro":"no show found by that name"}
		pass
	return render(request,'rev2/currentshow.html',{"data":out})	
