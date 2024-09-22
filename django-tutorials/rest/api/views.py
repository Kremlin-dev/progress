from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import userinfo

from .serializer import userinfoSerializer

# Create your views here.
@api_view(['GET'])
def getdata(request):

    data = userinfo.objects.all()

    serializer = userinfoSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def postdata(request):
    serializer = userinfoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
         return Response(serializer.data)