from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def login(request):
    return HttpResponse("please login")

# views are python functions that take Http request and return http responses

# Create your views here.
