from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from galleries.models import *

def home(request):
	galleries = Gallery.objects.all()
	artists = Artist.objects.all()
	return render(request,'home.html',{"data":{"gallery":galleries,"artist":artists}})