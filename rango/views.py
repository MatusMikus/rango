from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#dictionary to pass to the template engine as its context.
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	
	#return a rendered response
	return render(request, 'rango/index.html', context=context_dict)
	

def about(request):
	return render(request, 'rango/about.html')
