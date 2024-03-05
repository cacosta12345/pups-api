from rest_framework import serializers
from .models import Pup

class PupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "name", "description", "created_at")
        model = Pup
    