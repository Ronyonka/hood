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
    user = models.OneToOneField(User,)
