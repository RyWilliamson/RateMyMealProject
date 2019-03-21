from django.test import TestCase
from meal.models import Category
from django.core.urlresolvers import reverse
from meal.models import Category,Recipe
from django.test import Client


class SignupView(TestCase):
	def setUp(self):
		self.client = Client()
		self.newUser = {'username':"cat", 'email':"cat@gmail.com", 'password':"hello", 'picture':""}



	def test_new_user(self):
		response = self.client.post(reverse('registerRegular'),self.newUser)
		
		form = response.context['form']
		self.assetTrue(form.is_valid())