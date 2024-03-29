from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter() # making a router, router toiri korlaam
router.register('', views.ContactUsViewsets) # router er antena toiri korlam 
router.register('subscriber', views.SubscribeViewsets)


urlpatterns = [
    path('', include(router.urls)),
]
