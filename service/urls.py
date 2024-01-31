from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('', views.ServiceViewsets)
router.register('more', views.ExtraServiceViewsets)


urlpatterns = [
    path('', include(router.urls)),
]
