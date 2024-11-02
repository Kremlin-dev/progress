from rest_framework import serializers
from .models import todolist

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = todolist
        fields = '__all__'

def create(self, validated_data):
    newdata = todolist(
        title = validated_data['title'],
        description = validated_data['description'],
        completed = validated_data['completed']
    )
    newdata.save()
    return newdata




