from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_no', 'email']
    
    def first_name(self, obj): # jehetu user foreign key tai user theke first_name pete gele obj.user.first_name likhate hobe
        return obj.user.first_name
    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(Patient, PatientAdmin)