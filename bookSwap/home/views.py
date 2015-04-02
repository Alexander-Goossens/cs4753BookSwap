from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
def index(request):
	return render(request, 'home/index.html')

def login(request):
	return render(request, 'home/login.html')