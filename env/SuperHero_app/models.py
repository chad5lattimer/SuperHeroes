from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SuperHero (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User )
    name= models.CharField(max_length= 25 )
    universe= models.CharField(max_length= 25 )
    description= models.TextField()
    powerstats= models.TextField()


    def __str__(self):
        return self.name



