from django.contrib import admin
from . import models

admin.site.register(models.AvailableTime)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    
admin.site.register(models.Specialization, SpecializationAdmin)
admin.site.register(models.Designation, DesignationAdmin)

admin.site.register(models.Doctor)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewer_name', 'body', 'created', 'rating']
    
    def reviewer_name(self, obj):
        return f"{obj.reviewer.user.first_name} {obj.reviewer.user.last_name}"


admin.site.register(models.Review, ReviewAdmin)
