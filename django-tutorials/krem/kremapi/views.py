from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import registerSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):

    serializer = registerSerializer(data = request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)
    
    return Response({"message": "User not registerd"})


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    serializer = TokenObtainPairSerializer(data = request.data)

    if serializer.is_valid():

        user = serializer.user

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response(
            {
                'refresh': str(refresh),
                'access': str(access),
                'username': user.username,
                'email': user.email
            }
        )
    return Response({"message": "User not logged in"})




# Create your views here.
