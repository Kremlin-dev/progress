from django.shortcuts import render
from .serializers import TodolistSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import todolist
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate, login

@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up(request):
    user_serializer = UserSerializer(data = request.data)
    if user_serializer.is_valid():
        user = user_serializer.save()
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response({
            "user": user_serializer.data,
            "refresh": str(refresh),
            "access":str(access)
      })
    else:
        return Response({"message": "User data not validated"})

@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):

    serializer = TokenObtainPairSerializer(data=request.data)

    if serializer.is_valid():

        tokens = serializer.validated_data

        refresh = tokens['refresh']
        access = tokens['access']

        return Response(
            {
                "refresh": str(refresh),
                "access": str(access)
            }
        )
    return Response({"message": "Data not validated"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def postodo(request):
    data = TodolistSerializer(data = request.data)
    if data.is_valid():
        data.save()                                                   
        return Response(data.data)
    
    return Response({"message": "Data could not be saved"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getalltodo(request):
    data = todolist.objects.all()
    if data is not None:
        serializer = TodolistSerializer(data, many=True)
        return Response(serializer.data)
    return Response({"message": "No Data Found!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes({JWTAuthentication})
def gettodo(request, id):
    data = todolist.objects.get(id = id)

    if data is not None:
       serializer = TodolistSerializer(data)
       return Response(serializer.data)
    else:
        return Response({"message": "Data requested does not exist"})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def puttodo(request, id):
    data = todolist.objects.get(id=id)
    if data is not None:
        data = TodolistSerializer(instance = data, data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response({"message": "Data couldn't be validated."})

        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def deletetodo(request, id):
    note = todolist.objects.get(id =id)
    if note is not None:
         note.delete()
         return Response({"message":"deleted"})
    


# Create your views here.
