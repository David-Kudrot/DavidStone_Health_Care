from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctor.views import SpecializationViewset
from . import views


router = DefaultRouter()
router.register('list', views.DoctorViewsets)
router.register('specialization', views.SpecializationViewset)
router.register('designation', views.DesignationViewset)
router.register('available_time', views.AvailableTimeViewset)
router.register('reviews', views.ReviewViewset)


urlpatterns = [
    path('', include(router.urls)),
]
