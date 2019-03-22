from django.test import TestCase, Client
from meal.models import Category
from django.core.urlresolvers import reverse
from meal.models import Category, Recipe, Like, UserProfile, Chef
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


def add_cat(name,views,likes):
	c =  Category.objects.get_or_create(name=name, views = views, likes=likes)[0]
	c.save()
	return c

def add_recipe(cat, recipe_name, views=0, likes=0, recipe_ingredients="", recipe_directions=""):
	p = Recipe.objects.get_or_create(category=cat, recipe_name=recipe_name)[0]
	p.views = views
	p.likes = likes
	p.recipe_ingredients = recipe_ingredients
	p.recipe_directions = recipe_directions
	p.save()
	return p

def add_chef(username, email="", password="", profile_picture=""):
	c = Chef.objects.get_or_create(username = username, email = email, password = password)[0]
	c.save()
	p = UserProfile.objects.get_or_create(user = c, picture = profile_picture)[0]
	p.save()
	return c

def add_like(recipe_id, user_id):
        r = Like.objects.get_or_create(chef=Chef.objects.filter(id=user_id)[0],
                                       recipe_id=recipe_id)
        r.save()
        return r


class CategoryMethodTests(TestCase):
    def test_ensures_views_are_positive(self):
        cat = Category(name='test',views=1,likes=0)
        cat.save()
        self.assertEqual((cat.views>=0),True)

    def test_slug_line_creation(self):
        cat = Category(name='Random Category String',views=1,likes=0)
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')

    def test_ensures_likes_are_positive(self):
        cat = Category(name='test',views=1,likes=0)
        cat.save()
        self.assertEqual((cat.likes>=0),True)

class CategoryViewTests(TestCase):
    def test_category_view_with_no_categories(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_category_view_with_categories(self):
        add_cat('test',1,1)
        add_cat('temp',1,1)
        add_cat('tmp',1,1)
        add_cat('tmp test temp',1,1)

        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test")

class RecipeMethodTests(TestCase):
    def test_ensures_views_are_positive(self):
        add_cat('test2',1,1)

        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test2")
        test = Category.objects.get(slug="test2")

        add_recipe(test, recipe_name='test1', views=1, likes=1, recipe_ingredients="", recipe_directions="")
        test1 = Recipe.objects.get(slug='test1')
        self.assertEqual((test1.views>=0),True)

    def test_ensures_trending_works(self):
        add_cat('test2', 1, 1)

        response = self.client.get(reverse('categories'))
        test = Category.objects.get(slug="test2")

        add_recipe(test, recipe_name="test1", views = 1000, likes = 1, recipe_ingredients = "", recipe_directions = "")
        add_recipe(test, recipe_name="test3", views = 1, likes = 1000, recipe_ingredients = "", recipe_directions = "")
        test1 = Recipe.objects.get(slug = 'test1')
        response = self.client.get(reverse('trending'))

        self.assertContains(response, 'test1')
        self.assertContains(response, 'test3')

class AboutBaseSignUpViews(TestCase):
    def test_ensures_base_works(self):
        response = self.client.get(reverse('base'))
        self.assertEqual(response.status_code, 200)

    def test_ensures_about_works(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_ensures_SignUp_works(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

class SignupView(TestCase):
    def setUp(self):
        self.client = Client()
        self.newUser = {'username':"cat", 'email':"cat@gmail.com", 'password':"hello"}          
        
    def test_new_user(self):
        response = self.client.post(reverse('registerRegular'),self.newUser)
        self.assertTrue(response.status_code, 302)

    def test_new_user_login(self):
        response = self.client.post(reverse('registerRegular'),self.newUser)
        self.assertTrue(response.status_code, 302)
        response2 = self.client.post(reverse('login'),self.newUser)
        self.assertTrue(response2.status_code, 302)

    def test_user_logout(self):
        response = self.client.post(reverse('registerRegular'),self.newUser)
        self.assertTrue(response.status_code, 302)
        response2 = self.client.post(reverse('login'),self.newUser)
        self.assertTrue(response2.status_code, 302)
        response3 = self.client.post(reverse('logout'),self.newUser)
        self.assertTrue(response3.status_code, 302)
                
