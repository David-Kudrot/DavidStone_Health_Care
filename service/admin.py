from django.contrib import admin
from .models import ServiceModel, ExtraService
# Register your models here.


admin.site.register(ServiceModel)
admin.site.register(ExtraService)