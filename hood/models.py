from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
    health = models.CharField(max_length = 30, null=True)
    police = models.CharField(max_length=30,null=True)
    

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def get_hood_by_id(cls,id):
        home = cls.objects.filter(pk=id)
        return home


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True,blank=True, upload_to='avatars/')
    bio = models.TextField(null=True,blank=True,max_length=500)
    hood = models.ForeignKey(Hood, related_name='prohood',null=True)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

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

    @classmethod
    def get_post_by_neighborhood(cls,id):
        hoodie = cls.objects.filter(hood__pk=id)
        return hoodie

class Comments(models.Model):
    comment = models.TextField(max_length=280)
    created = models.DateTimeField(auto_now_add = True,null = True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,related_name='pst')
