from django.shortcuts import render
from .serializers import TodolistSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import todolist

@api_view(['POST'])
def postodo(request):
    data = TodolistSerializer(data = request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)

@api_view(['GET'])
def getalltodo(request):
    data = todolist.objects.all()
    serializer = TodolistSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def gettodo(request, id):
    data = todolist.objects.get(id = id)

    if data is not None:
       serializer = TodolistSerializer(data,many = False)
       return Response(serializer.data)


@api_view(['PUT'])
def puttodo(request, id):
    data = todolist.objects.get(id=id)
    if data is not None:
        data = TodolistSerializer(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
@api_view(['DELETE'])
def deletetodo(request, id):
    note = todolist.objects.get(id =id)
    if note is not None:
         note.delete()
         return Response({"message":"deleted"})
    


# Create your views here.
