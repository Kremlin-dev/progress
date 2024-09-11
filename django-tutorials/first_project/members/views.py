from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import login

from .forms import userform

def home(request):

    users = login.objects.all().values()
    template = loader.get_template('index.html')
    context ={
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method=="POST":
        form = userform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(username, email, password)

            return HttpResponse("Form submitted successfully")

    form = userform()

    context ={
        'form':form
    }
    template = loader.get_template('index.html')

    return HttpResponse(template.render(context, request))

