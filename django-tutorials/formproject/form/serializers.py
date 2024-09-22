from rest_framework import serializers
from .model import hostel


class hostelSerializer(serializers.ModelSerializer):

    class meta:
        model = hostel
        fields = "__all__"
        # fields = ("hostelName", "location")

# converts the model to json data