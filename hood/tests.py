from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class LocationTestCase(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name='yandhi')

    def tearDown(self):
        self.location.delete()

    def testlocation(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_get_by_id(self):
        self.location.save_location()
        location = Location.get_location_by_id(self.location.id)
        self.assertTrue(location!=None)


class HoodTestCase(TestCase):

    def setUp(self):
        self.location= Location.objects.create(name='yandhi')
        self.hood=Hood.objects.create(name='yezzy',location=self.location)

    def tearDown(self):
        self.hood.delete()
        self.location.delete()

    def test_hood_instance(self):
        self.assertTrue(isinstance(self.hood, Hood))

    def test_save_hood(self):
        self.hood.save_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood)> 0)

    def test_get_by_id(self):
        self.hood.save_hood()
        hood=Hood.get_hood_by_id(self.hood.id)
        self.assertTrue(hood!=None)

class ContacTestCase(TestCase):
    def setUp(self):
        self.lctn = Location.objects.create(name='yandhi')
        self.contact = Contact.objects.create(health='test',police='test',location=self.lctn)

    def tearDown(self):
        self.contact.delete()
        self.lctn.delete()

    def test_contact_instance(self):
        self.assertTrue(isinstance(self.contact, Contact))

    def test_contact_save(self):
        self.contact.save_contact()
        cntct = Contact.objects.all()
        self.assertTrue(len(cntct)>0)

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.profile = Profile(id=1,user=self.user, avatar='path/to/avatar', bio='test bio')

    def tearDown(self):
        self.profile.delete()
        self.user.delete()

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    
    # def tearDown(self):
    #     self.profile.delete()

# class BusinessTestCase(TestCase):
#     def setUp(self):
        

