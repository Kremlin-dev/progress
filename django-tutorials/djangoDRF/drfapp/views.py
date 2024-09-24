from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view['POST']
def create_note(request):
    pass

@api_view['GET']
def get_note(request):
    pass


@api_view['PATCH']
def update_note(request):
    pass


@api_view['DELETE']
def delete_note(request):
    pass


# Create your views here.
