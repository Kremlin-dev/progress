from rest_framework import serializers
from django.contrib.auth import User

class UserSeralizer(serializers.ModelSerializer):

    class meta:
      model = User
      fields = ["username", "email"]

    def create(self, validated_data):
       
       newuser = User(
          Username = validated_data["username"],
          email = validated_data["password"]   
       )
       newuser.set_password(validated_data["passsword"])
       newuser.save()
       return newuser.username
