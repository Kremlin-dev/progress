from rest_framework import serializers

from .models import userinfo


class userinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = userinfo
        fields = "__all__"