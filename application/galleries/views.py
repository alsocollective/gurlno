from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from galleries.models import *
from django.core import serializers
from django.forms.models import model_to_dict

import json

def home(request):
	if request.user.is_authenticated():
		galleries = Gallery.objects.all()
		artists = Artist.objects.all()
		return render(request,'home.html',{"data":{"gallery":galleries,"artist":artists}})
	else:
		return redirect('/login')


def expara(request):
	galleries = Gallery.objects.all()
	artists = Artist.objects.all()	
	return render(request,'expara.html',{"data":{"gallery":galleries,"artist":artists}})

def gallerylist(request):
	if request.user.is_authenticated():
		galleries = Gallery.objects.all()
		return render(request,'list/gallery.html',{"data":{"gallery":galleries}})
	else:
		return redirect('/login')

def showlist(request):
	if request.user.is_authenticated():
		shows = Show.objects.all()
		return render(request,'list/shows.html',{"data":{"shows":shows}})
	else:
		return redirect('/login')	

def gallery(request,slug):
	if not request.user.is_authenticated():
		return redirect('/login')

	try:
		gallery = Gallery.objects.get(slug=slug)
		time = HoursOfOp.objects.get(parent=gallery)
		shows = Show.objects.filter(gallery=gallery)
	except Exception, e:
		return HttpResponse("not much")
		pass
	return render(request,'gallery.html',{"gal":gallery,"time":time,"shows":shows})


def gswipelist(request):
	if not request.user.is_authenticated():
		return redirect('/login')
	return render(request,'list/swipegallery.html')	

def getShow(gallery):
	try:
		return Show.objects.filter(gallery=gallery)[0].title
	except Exception:
		return None
def getTime(gallery):
	try:
		return json.loads(serializers.serialize("json",HoursOfOp.objects.filter(parent = gallery)))[0]["fields"]
	except Exception,e:
		return None

def galJsonSimple(request):
	if not request.user.is_authenticated():
		return redirect('/login')

	out = []
	galleries = Gallery.objects.all()
	for gal in galleries:
		out.append({ 
			'gal': gal.title,
			'time': getTime(gal),
			'show' : getShow(gal)
			})

	return HttpResponse(json.dumps(out), content_type="application/json")












