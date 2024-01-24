from . import models
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceModel
        fields = '__all__'