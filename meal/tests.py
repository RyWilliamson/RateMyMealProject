from django.test import TestCase
from meal.models import Category
from django.core.urlresolvers import reverse
from meal.models import Category,Recipe

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
        add_cat('test',1,1)

        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test")

        add_recipe(cat='test2', recipe_name='test1', views=0, likes=0, recipe_ingredients="", recipe_directions="")
        #self.assertEqual((cat.views>=0),True)