from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.



# IMPORTANT NOTE : url theke kivabe parameter er madhome data data show korbo jemon --- jdi url http://127.0.0.1:8000/appointment/1/ di tobe 1 no id apponitment wala sob details show korbe, but jodi ami http://127.0.0.1:8000/appointment/?patient_id=1 eivabe 'patient_id' param die search kori tobe amake nicher ei view te built get_queryset() function kora lagbe.......

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all() # Appointment model er sob data asbe
    serializer_class = serializers.AppointmentSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset() # uporer queryset theke all data queryset variable a rakhlam karon eta k patient_id die filter kore override korbo
        
        patient_id = self.request.query_params.get('patient_id') # url er parameter patient_id k get korlam 
        # jodi patient_id thake tobe filter korlam oi patient_id die r queryset k return korlam 
        if patient_id: 
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
    
    
# ebare http://127.0.0.1:8000/appointment/?patient_id=1 eta die search korlei 1 no id die all details dekhabe
        
    
    