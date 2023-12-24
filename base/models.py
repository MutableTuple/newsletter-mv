import uuid
from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(max_length=500, blank=True,null=True)
    
    def __str__(self):
        name = self.email.split("@")
        return (f'{name[0]} - {self.email}')
        
        

class Page(models.Model):
    title = models.CharField(max_length=255)
    views = models.IntegerField(default=0)