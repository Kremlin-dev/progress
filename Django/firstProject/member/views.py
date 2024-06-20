from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def home(request):
    return HttpResponse("Hello World")

def index(request):
    firstName ="Isaac"
    lastName="Amponsah"
    email="yawamp27@gmail.com"
    password="password"

    user = User(
        firstName=firstName,
        lastName=lastName,
        email=email,
        password=password
    )
    user.save()
    template = loader.get_template('index.html')
    return HttpResponse(template.render())