from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('list', views.PatientViewsets)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationAPIView.as_view(), name='register'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    # path('active/<uid64>/<token>/', views.activate, name = 'activate'),# function based activation
    path('active/<str:uid64>/<str:token>', views.ActivateAccount.as_view(), name='activate_account'), # class based activation
   path('logout/', views.UserLogoutView.as_view(), name='logout'),
]

