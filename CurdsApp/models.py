from typing import Any
from django.db import models

# Create your models here.
# user profile 
class Profile(models.Model):
    BLOOD = (
        ('B+','B+',),
        ('B-','B-',),
        ('A+','A+',),
        ('AB+','AB+',),
        ('AB-','AB-',),
        ('O-','O-',),
        ('O+','O+',),
    )
    GENDER = (
        ('Male','Male',),
        ('Female','Female',),
        ('Others','Others',),
    )
    RELIGION = (
        ('Islam','Islam',),
        ('Hindu','Hindu',),
        ('Buddha','Buddha',),
        ('Others','Others',),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100,null=True, blank=True)
    phone = models.CharField(max_length=16,null=True,)
    age = models.PositiveIntegerField()
    birth_date = models.DateField()
    image = models.ImageField(upload_to='prof_pc/',default='defProf.jpg')
    blood = models.CharField(choices=BLOOD,max_length=100)
    gender = models.CharField(choices=GENDER,max_length=50)
    religion = models.CharField(choices=RELIGION,max_length=50)
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name