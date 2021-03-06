from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from galleries.models import *
from application.settings import MEDIA_URL

import json, datetime

def offSetTimeBy(diff):
	return datetime.timedelta(hours=diff) + datetime.datetime.now()

def loadMainGalleryList(request):
	galleries = Gallery.objects.all()
	# shows = Show.objects.all().filter(date_end__gte=now)
	return render(request,'rev2/index.html',{"data":{"galleries":galleries,"MEDIA_URL":MEDIA_URL}})


def home(request):
	if request.user.is_authenticated():
		return loadMainGalleryList(request)
	else:
		return redirect('/login')

def currentshow(request,slug):
	try:
		now = offSetTimeBy(-5).date()
		gallery = Gallery.objects.get(slug = slug)
		show = Show.objects.all().filter(gallery=gallery,date_end__gte=now)[0]
		upcoming = Show.objects.all().filter(gallery=gallery,date_start__gt=now)
		out = {"gal":gallery,"show":show,"upcoming":upcoming}
	except Exception, e:
		print e
		out = {"erro":"no show found by that name"}
		pass
	return render(request,'rev2/currentshow.html',{"data":out})	
