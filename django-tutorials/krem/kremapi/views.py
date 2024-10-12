from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simeplejwt.authentication import JWTAthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSeriliazer

from django.contrib.auth import User
from .serializers import UserSeralizer

@api_view(['POST'])
def register(requst):

    serializer = UserSeralizer(data = requst.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)


@api_view(['POST'])
def login(request):

    serializer = TokenObtainPairSeriliazer(data = request.data)

    if serializer.is_valid():

        user = serializer.user

        refresh = RefreshToken.for_user(user)
        access = refresh.aceess_token

        return Response(
            {
                'refresh': str(refresh),
                'access': str(access),
                'username': user.username,
                'email': user.email
            }
        )




# Create your views here.
