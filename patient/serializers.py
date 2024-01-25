from . import models
from rest_framework import serializers
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False) # ekhane output a patient view a patient ta number dekhabe, name ta dekhate StringRelatedField use kora holo r many=False kora holo karon OneToOne field ache, ManytoMany field thakle many=True likha hoto
    class Meta:
        model = models.Patient
        fields = '__all__'
        
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True) # serializer a 2nd password thakena tai, eta declare kora holo r required=True kora holo
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        
        
    def save(self):
            username = self.validated_data['username']
            first_name = self.validated_data['first_name']
            last_name = self.validated_data['last_name']
            email = self.validated_data['email']
            password = self.validated_data['password']
            password2 = self.validated_data['confirm_password'] # ekhane confirm_password dewa holo karon fields a confirm_password dewa ache
            
            # jodi password match na kore tobe error show kora holo
            if password != password2:
                raise serializers.ValidationError({'error': "Password didn't match!"})
            
            # jodi email already exists hoi tobe error show kora holo
            if User.objects.filter(email = email).exists():
                raise serializers.ValidationError({'error': "Email already exists!"})
            
            account = User(username=username, email=email, first_name=first_name, last_name=last_name)
            
            account.set_password(password) # set_password() function die password set kora holo 
            
            account.is_active = False # eta registration er time a false thakbe, email verification er time on kore dewa hobe nahole user login korte parbe na
            
            account.save() # db te save kora holo
            return account
        

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)