from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import register
from .forms import userRegistration

def home(request):

    template = loader.get_template("index.html")

    return HttpResponse(template.render())

def signup(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")

        newdata = register(

            firstName = firstName,
            lastName = lastName,
            email = email,
            telephone = telephone
        )
        newdata.save()

        template = loader.get_template("form.html")

        message = "Data Receved and saved sucessfully"
        return HttpResponse(template.render({"message": message},request))

    form = userRegistration()

    context = {
        "form" : form,
    }

    template = loader.get_template("form.html")

    return HttpResponse(template.render(context, request))





# Create your views here.
