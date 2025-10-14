from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

        
    
    


    
