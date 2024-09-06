from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import login

def home(request):

    users = login.objects.all().values()
    print(users)
    template = loader.get_template('index.html')
    context ={
        'users': users,
    }
    return HttpResponse(template.render(context, request))

# def login(request):
#     return HttpResponse("please login")

# views are python functions that take Http request and return http responses

# Create your views here.
