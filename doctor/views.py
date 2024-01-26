from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
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



# particular doctor id er jonno Available Time filter korbo, tai django filter use kortesi, installed app a add kora lagbe
class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id") # patient er jonno jemon kora hoise same ekahne 
        if doctor_id:
            return query_set.filter(doctor = doctor_id) # Doctor model ache tai eta automatic small doctor likha jabe, jehetu related_name use korinai 
        return query_set
    
        
class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    # filter korar jonno filter_backends built-in variable use kora holo
    filter_backends = [AvailableTimeForSpecificDoctor]
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer    
