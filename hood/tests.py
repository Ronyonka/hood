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
        hood=Hood.get_hood_by_id(self.hood)
        self.assertTrue(hood!=None)
