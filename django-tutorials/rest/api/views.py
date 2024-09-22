from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getdata(request):


    return Response(data)

@api_view(["POST"])
def postdata(request):



    return Response(data)