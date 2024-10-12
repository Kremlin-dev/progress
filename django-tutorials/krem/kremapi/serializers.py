from rest_framework import serializers
from django.contrib.auth.models import User

class registerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
      model = User
      fields = ["username", "email", "password"]

    def create(self, validated_data):
       
       newuser = User(
          username = validated_data["username"],
          email = validated_data["email"]   
       )
       newuser.set_password(validated_data['password'])
       newuser.save()
       return newuser
