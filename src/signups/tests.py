from django.test import TestCase

from django.contrib.auth.models import User
from models import UserProfile

"""
TESTING of the models class will create temporary, clean version of 
database which can be manipulated without consequence
"""

""" TEST user creation """

""" TEST multiple users """

""" TEST profile creation """

""" TEST beacon creation """

""" TEST Beacpn linking """

class UserTestCase(TestCase):
	def setUp(self):
		User.objects.create(username="test1", email="test1@test1.com")
		User.objects.create(username="test2", email="test2@test2.com")

	def test_user_setup(self):
		e1 = User.objects.get(username="test1")
		self.assertEqual(e1.email, "test1@test1.com")
