from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields =["title", "content", "created_at", "updated_at"]

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        newuser = User(
            username = validated_data["username"],
            email = validated_data["email"],
        )
        newuser.set_password(validated_data["password"])
        newuser.save()

        return newuser