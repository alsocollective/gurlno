from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from galleries.models import *

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

	print gallery
	print time
	return render(request,'gallery.html',{"gal":gallery,"time":time,"shows":shows})


def gswipelist(request):
	if not request.user.is_authenticated():
		return redirect('/login')

	galleries = Gallery.objects.all()
	time = HoursOfOp.objects.all()
	return render(request,'list/swipegallery.html',{"gallery":galleries,"time":time})	













