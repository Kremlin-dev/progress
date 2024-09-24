from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from  .serializer import NoteSerializer
from .models import Note




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_note(request):
    
    data = NoteSerializer(data = request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_note(request):
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)

    return Response(serializer.data)

@api_view(['PATCH'])
def update_note(request,id):

    note = Note.objects.filter(id =id)

    if note is not None:
        serializer = NoteSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
    


@api_view(['DELETE'])
def delete_note(request, id):

     note = Note.objects.filter(id =id)

     if note is not None:
         note.delete()

         return Response({"message0":"deleted"})
    


# Create your views here.
