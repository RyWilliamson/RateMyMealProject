from django.test import TestCase
from meal.models import Category
from django.core.urlresolvers import reverse
from meal.models import Category

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

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



