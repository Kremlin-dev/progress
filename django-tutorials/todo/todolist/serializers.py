from rest_framework import serializers
from .models import todolist
from django.contrib.auth.models import User

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = todolist
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password"]
    def create(self, validated_data):
        newUser = User(
        username = validated_data['username'],
    )
        newUser.set_password(validated_data["password"])
        newUser.save()
        return newUser




