from rest_framework import serializers
from doctor.models import Review
from . import models



# NB : jodi StringRelatedField use kori tobe API theke html form fill up a many to many field dekhabe na, but jodi StringRelatedField use na kori tobe okhane option gulo dekhabe, you can try to see this
# doctor model a field er nam ja ase, tai use korte hobe ekhane StringRelationField a onno dile show korbe na
class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False) # OneToOne relation tai many=False
    designation = serializers.StringRelatedField(many=True) # ManyToMany relation tai many=True
    specialization = serializers.StringRelatedField(many=True) # ManyToMany relation tai many=True
    available_time = serializers.StringRelatedField(many=False) # OneToOne relation tai many=False
    class Meta:
        model = models.Doctor
        fields = '__all__'



class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'
        
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Review
        fields = '__all__'


