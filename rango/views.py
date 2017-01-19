from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello " + '<a href="/rango/about/">About</a>')
	

def about(request):
	return HttpResponse("THIS IS AN ABOUT PAGE")