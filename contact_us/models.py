from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    email = models.CharField(max_length=50, null=True, blank=True)
    problem = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us" # admin panel a Contact Uss hoye jawar jonno verbose name plural use kora holo, jate Contact Us hoy
        

class Subscribe(models.Model):
    email = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Subscriber Mail : {self.email}"
    
    