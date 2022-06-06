from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Comments,Image,Followers

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.collo=Profile(pic="img.png",bio="sexy",userId=1)
    def test_instance(self):
        self.assertTrue(isinstance(self.collo,Profile))

    def test_initialization(self):
        self.assertEqual(self.collo.pic,"img.png")
        self.assertEqual(self.collo.bio,"sexy")
        self.assertEqual(self.collo.userId,1)
