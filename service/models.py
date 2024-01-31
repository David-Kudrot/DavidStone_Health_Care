from django.db import models

# Create your models here.
class ServiceModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images")
    
    def __str__(self):
        return self.name
    
    
class ExtraService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"ExtraService : {self.name}"