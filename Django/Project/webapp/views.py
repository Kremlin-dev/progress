from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Authentication

def authenticate(request):
    username ='Kremlin'
    email = "kremlin27@gmail.com"
    password = "********"

    newUser = Authentication(
    username = username,
    email = email,
    password = password

)
    newUser.save()

    template = loader.get_template("index.html")
    return HttpResponse(template.render())

