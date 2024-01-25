from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets
from . import models
from . import serializers

# for registration and activation link making
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
# for sending mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.


class PatientViewsets(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer



class UserRegistrationAPIView(APIView):
    serializer_class = serializers.UserRegistrationSerializer
    
    # jehetu form er data post hobe tai post method use korbo
    def post(self, request):
        serializer = self.serializer_class(data=request.data) # form a motoi same ekhane just serializer user kora hoise, form er data anar jonno, form a request.POST kora hoto
        
        if serializer.is_valid():
            user = serializer.save()
            
            # making a activation token for this user, and this is one time token, we can sent it for mail verification and password reset for the user
            token = default_token_generator.make_token(user)
            # making uid user.pk mane user er primary key, eta force_bytes byte a convert korbe, r urlsafe_base64_encode korbe jeta user er jonno unique hobe
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
            
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            
            return Response("Check your mail for confirmation!")
        return Response(serializer.errors) # jodi email confirm na hoi tobe error show korbe


# function based activate account and check below has class based view

# def activate(request, uid64, token):
#     try:
#         uid = urlsafe_base64_decode(uid64).decode()
#         user = User._default_manager.get(pk=uid)
#     except(User.DoesNotExist):
#         user = None 
    
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return redirect('login')
#     else:
#         return redirect('register')
    
class ActivateAccount(View):
    def get(self, request, uid64, token):
        try:
            uid = urlsafe_base64_decode(uid64).decode()
            user = User._default_manager.get(pk=uid)
        except User.DoesNotExist:
            user = None 

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True 
            user.save()
            return redirect('login')
        else:
            return redirect('register')


class UserLoginAPIView(APIView):
    def post(self, request):  # jehetu login korte form post kora lage tai only post use korlam
        serializer = serializers.UserLoginSerializer(data=self.request.data) # same to same jemon form = forms.UserLoginForm(user=self.request.user) kortam
        # jodi form valid hoi tobe
        if serializer.is_valid(): 
            username = serializer.validated_data['username'] # user er post form theke username nilam
            password = serializer.validated_data['password'] # user er post form theke password nilam
            
            
            # user authenticate kina chek korlam username and password die
            user = authenticate(username=username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)# token = token thakbe or  _ = toaken create hobe
                print(token)
                print(_)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid Credentials!'})
        return Response(serializer.errors)
    
    
class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete() # toiri kora token ta delete kora holo jeno logout korar por same token die login na korte pare
        logout(request)
        return redirect('login')
