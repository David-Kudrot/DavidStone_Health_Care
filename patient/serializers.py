from . import models
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False) # ekhane output a patient view a patient ta number dekhabe, name ta dekhate StringRelatedField use kora holo r many=False kora holo karon OneToOne field ache, ManytoMany field thakle many=True likha hoto
    class Meta:
        model = models.Patient
        fields = '__all__'