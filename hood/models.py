from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Location(models.Model):
    name = models.CharField(max_length=140)

class Neighbourhood(models.Model):
    name = models.CharField(max_length= 140)
    location = models.ForeignKey(Location)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True,blank=True, upload_to='avatars/')
    bio = models.TextField(null=True,blank=True,max_length=500)
    hood = models.ForeignKey(Neighbourhood, related_name='prohood')
    location = models.ForeignKey(Location, related_name='prolocation')

class Business(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True,null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)

class Posts(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField(max_length=500)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
