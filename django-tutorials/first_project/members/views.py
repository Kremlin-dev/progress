from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import login

from .forms import userform, signupForm

def home(request):

    users = login.objects.all().values()
    template = loader.get_template('index.html')
    context ={
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username, email, password)

        return HttpResponse("Form submitted successfully")

    form = userform()

    context ={
        'form':form
    }
    template = loader.get_template('index.html')

    return HttpResponse(template.render(context, request))


def sign(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        print("Received the details successfully")

        context = {
            'users':[{
            'firstname': firstname,
            'lastname':lastname,
            'age':age
            }
            ]

        }

        template = loader.get_template('data.html')

        return HttpResponse(template.render(context, request))

   
    signup = signupForm()
    form = {
            'form':signup
        }

    template = loader.get_template('signup.html')

    return HttpResponse(template.render(form, request))
 
