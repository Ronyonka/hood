from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Location(models.Model):
    name = models.CharField(max_length=140)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_location_by_id(cls,id):
        lctn = cls.objects.filter(pk=id)
        return lctn

class Hood(models.Model):
    name = models.CharField(max_length= 140)
    location = models.ForeignKey(Location, related_name='place')

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def get_hood_by_id(cls,id):
        home = cls.objects.filter(pk=id)
        return home

class Contact(models.Model):
    health = models.CharField(max_length = 30)
    police = models.CharField(max_length=30)
    location = models.ForeignKey(Location, related_name='emergency')

    def save_contact(self):
        self.save()

    def delete_contact(self):
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True,blank=True, upload_to='avatars/')
    bio = models.TextField(null=True,blank=True,max_length=500)
    hood = models.ForeignKey(Hood, related_name='prohood')
    location = models.ForeignKey(Location, related_name='prolocation')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Business(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(null=True,blank=True, upload_to='business/')
    email = models.EmailField(blank=True,null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)

class Category(models.Model):
    category = models.CharField(max_length=40)

class Posts(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField(max_length=500)
    category = models.ForeignKey(Category,related_name='ctgry')
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)

class Comments(models.Model):
    comment = models.TextField(max_length=280)
    created = models.DateTimeField(auto_now_add = True,null = True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,related_name='pst')
