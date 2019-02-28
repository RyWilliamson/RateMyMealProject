import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyMealProject.settings')

import django
django.setup()
from meal.models import Category, Recipe


def populate():
	vegan_recipes =[
		{"recipe_name": "Vegan Chilli",
		 "views": 22,
		 "likes": 10, 
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Mushroom Burgers",
		 "views" :55,
		 "likes": 22,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Lasagne", 
		 "views": 222,
		 "likes": 222,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Brownies",
		 "views":159,
		 "likes": 158,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Falafel Burgers",
		 "views":32,
		 "likes": 0,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Thai Curry",
		 "views":96,
		 "likes": 90,
		 "recipe_data": "temp",
		 "image": ""
		}
	]

	healthy_recipes = [
		{"recipe_name": "Roasted Chickpea Wraps",
		 "views": 39,
		 "likes": 16,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Roast Pepper Pesto Pasta",
		 "views": 98,
		 "likes": 40,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Veggie Wholewheat Pot Noodle",
		 "views": 128,
		 "likes": 64,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Lean Turkey Burger",
		 "views": 90,
		 "likes": 30,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Thai Prawn and Ginger Noodles",
		 "views": 530,
		 "likes": 500,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Overnight Oats",
		 "views": 530,
		 "likes": 222,
		 "recipe_data": "temp",
		 "image": ""
		}
	]

	brunch_recipes = [
		{"recipe_name": "Huevos Rancheros",
		 "views": 67,
		 "likes": 31,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Eggs Royale",
		 "views": 300,
		 "likes": 177,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "French Toast with Maple Syrup", 
		 "views": 600,
		 "likes": 200,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Pancakes with Fresh Berries",
		 "views": 549,
		 "likes": 199,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Berry Smoothie Bowl",
		 "views": 12,
		 "likes": 12,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name":"Baked Avocado with Smoked Salmon and Egg",
		 "views":90,
		 "likes": 40,
		 "recipe_data": "temp",
		 "image": ""
		}
	]

	mexican_recipes = [
		{"recipe_name": "Pulled Pork Burrito",
		 "views": 32,
		 "likes": 10,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Chicken Fajitas",
		 "views": 80,
		 "likes": 26,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Vegetable Enchiladas",
		 "views":91,
		 "likes": 30,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Spicy Beef Quesadillas",
		 "views": 76,
		 "likes": 68,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Chilli Con Carne",
		 "views": 230,
		 "likes": 130,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Churros",
		 "views":89,
		 "likes": 30,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Jackfruit Tacos",
		 "views":35,
		 "likes": 5,
		 "recipe_data": "temp",
		 "image": ""
		}
	]

	italian_recipes = [
		{"recipe_name": "Salsiccia Piccante Pizza",
		 "views" :210,
		 "likes": 185,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Spaghetti Carbonara",
		 "views" :333,
		 "likes": 220,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Lobster Ravioli",
		 "views" :39,
		 "likes": 26,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Pollo Milanese",
		 "views" :80,
		 "likes": 36,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Risotto Quattro Stagioni",
		 "views" :12,
		 "likes": 8,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Tiramisu",
		 "views" :99,
		 "likes": 40,
		 "recipe_data": "temp",
		 "image": ""
		}
	]

	gluten_free_recipes = [
		{"recipe_name": "Scones",
		 "views": 54,
		 "likes": 48,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Bolognese",
		 "views": 300,
		 "likes": 247,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Pizza",
		 "views": 159.
		 "likes": 99,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Salmon and Brocolli Bake",
		 "views": 31,
		 "likes": 11,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Pesto, Courgette * Gryuere Polenta Tart",
		 "views": 92,
		 "likes": 46,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Self-Saucing Chocolate Pudding",
		 "views": 500,
		 "likes": 500,
		 "recipe_data": "temp",
		 "image": ""
		}
	]

	comfort_recipes = [
		{"recipe_name": "Beef Wellington",
		 "views": 35,
		 "likes": 24,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Shepherd's Pie",
		 "views": 215,
		 "likes": 126,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Chocolate Fudge Cake",
		 "views": 530.
		 "likes": 520,
		 "recipe_data": "temp",
		 "image": ""
		},
		
		{"recipe_name": "Mac n Cheese with Bacon Bits",
		 "views": 428,
		 "likes": 400,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Apple Pie",
		 "views": 92,
		 "likes": 87,
		 "recipe_data": "temp",
		 "image": ""
		},
		
		{"recipe_name": "Fried Chicken",
		 "views": 76,
		 "likes": 46,
		 "recipe_data": "temp",
		 "image": ""
		}
	]

	dairy_free_recipes = [
		{"recipe_name": "Meatloaf",
		 "views": 98,
		 "likes": 13,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Coconut and Fish Curry Parcels",
		 "views": 75,
		 "likes": 2,
		 "recipe_data": "temp",
		 "image": ""
		},
		
		{"recipe_name": "Chocolate, Orange & Hazelnut Cake",
		 "views": 145,
		 "likes": 136,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Salmon & Lemon Mini Fishcakes",
		 "views": 530,
		 "likes": 381,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Lentil Lasagne",
		 "views": 200,
		 "likes": 137,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Sausage & Bean One-Pot",
		 "views": 237,
		 "likes": 100,
		 "recipe_data": "temp",
		 "image": ""
		}
	]
	
	kid_friendly_recipes = [
		{"recipe_name": "Crispy Fish Sticks",
		 "views": 117,
		 "likes": 10,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Burger Sliders",
		 "views": 54,
		 "likes": 33,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Spaghetti Meatballs",
		 "views": 77,
		 "likes": 67,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Cheesy Chicken Casserole",
		 "views": 8,
		 "likes": 4,
		 "recipe_data": "temp",
		 "image": ""
		},

		{"recipe_name": "Vegetable Fried Rice",
		 "views": 22,
		 "likes": 16,
		 "recipe_data": "temp",
		 "image": ""
		},
		

		{"recipe_name": "Beef Stew and Dumplings",
		 "views": 10,
		 "likes": 5,
		 "recipe_data": "temp",
		 "image": ""
		}
	]
		
		
	cats =  {"Vegan/Vegetarian Meals": {"pages": vegan_recipes, "views":128, "likes":64}, 
		"Healthy Meals": {"pages": healthy_recipes, "views":64,"likes":32},
		"Brunch Ideas": {"pages": brunch_recipes, "views":32, "likes":16},
		"Mexican Meals": {"pages": mexican_recipes, "views":72,"likes":32},
		"Italian Meals": {"pages": italian_recipes, "views":82,"likes":12},
		"Gluten Free Meals": {"pages": gluten_free_recipes, "views":25,"likes":11},
		"Comfort Food": {"pages": comfort_recipes, "views":55,"likes":41},
		"Dairy Free Meals": {"pages": dairy_free_recipes, "views":99,"likes":65},
		"Kid Friendly Meals": {"pages": kid_friendly_recipes, "views":88,"likes":21}
	}
	
	for cat, cat_data in cats.items():
		c = add_cat(cat, cat_data["views"], cat_data["likes"])
		for p in cat_data["pages"]:
			add_page(c, p["recipe_name"], p["url"], p["views"])
			
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, recipe_name, views=0):
	p = Page.objects.get_or_create(category=cat, recipe_name=recipe_name)[0]
	p.views = views
	p.save()
	return p
	
def add_cat(name,views,likes):
	c =  Category.objects.get_or_create(name=name, views = views, likes=likes)[0]
	c.save()
	return c

if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
