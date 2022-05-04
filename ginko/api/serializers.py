from .models import *
from rest_framework import serializers

class actionSerializer(serializers.ModelSerializer):
    class Meta:
        model = actionModel
        fields = "__all__"

