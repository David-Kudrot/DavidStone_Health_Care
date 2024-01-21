from django.contrib import admin

# Register your models here.
from .models import ContactUs

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'problem'] # admin a ei list a dekhabe

admin.site.register(ContactUs, ContactModelAdmin)