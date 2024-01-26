from django.shortcuts import render
from rest_framework import viewsets, pagination
from . import models
from . import serializers
# Create your views here.


# doctor er jonno pagination set kortesi, previous and next button a click korle page change hoi jabe,  front-end a perdoctor er jonno pagination set kora jabe

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # page size 1 dilam mane 1ta kore doctor dekhabe, joto dibo tot ta kore show korbe
    page_size_query_param = page_size
    max_page_size = 100

class DoctorViewsets(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    pagination_class = DoctorPagination # pagination built-in variable/attribute er modhe uporer DoctorPagination class ta add kore dilam
    serializer_class = serializers.DoctorSerializer


class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    
class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer
    
class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer    
