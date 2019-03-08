import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyMealProject.settings')

import django
django.setup()
from meal.models import Category, Recipe

# TODO: Update recipe images at bottom to reflect slug changes
def populate():
	casual_chefs = [
		{"username": "MotherMartha1978",
		 "email": "mothermartha1984@gmail.com",
		 "password": "marthasmonkies",
		 "website": "motheringwithmartha.co.uk",
		 "profile_picture": ""
		},

		{"username": "JustJack99",
		 "email": "MadJacko@gmail.com",
		 "password": "justjackthings99",
		 "website": "",
		 "profile_picture": ""
		}
	]

	professional_chefs = [
		{"username": "RaymondBolt",
		 "email": "stoneeagle@gmail.com",
		 "password": "cheddar",
		 "website": "",
		 "profile_picture": ""
		},

		{"username": "HayleyBean",
		 "email": "hayleybean@gmail.com",
		 "password": "s6n*cjd(&4ds",
		 "website": "",
		 "profile_picture": ""
		},

		{"username": "TheRealStanleySpears",
		 "email": "therealstanleyspears@gmail.com",
		 "password": "l&^5bkw2'!p)",
		 "website": "",
		 "profile_picture": ""
		},

		{"username": "ItsaMarioManini",
		 "email": "mariomanini@gmail.com",
		 "password": "i'mperfect",
		 "website": "",
		 "profile_picture": ""
		},

		{"username": "AidanMack",
		 "email": "aidanmack@gmail.com",
		 "password": "je86^jka%33mn)1",
		 "website": "",
		 "profile_picture": ""
		},

		{"username": "HenryMichaels",
		 "email": "henrymichaels@gmail.com",
		 "password": "sajq76&(*3bmn1",
		 "website": "",
		 "profile_picture": ""
		}
	]

	vegan_recipes =[
		{"recipe_name": "Vegan Chilli",
		 "views": 22,
		 "likes": 10, 
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Mushroom Burgers",
		 "views" :55,
		 "likes": 22,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Lasagne", 
		 "views": 222,
		 "likes": 222,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Brownies",
		 "views":159,
		 "likes": 158,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Falafel Burgers",
		 "views":32,
		 "likes": 0,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Thai Curry",
		 "views":96,
		 "likes": 90,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		}
	]

	healthy_recipes = [
		{"recipe_name": "Roasted Chickpea Wraps",
		 "views": 39,
		 "likes": 16,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Roast Pepper Pesto Pasta",
		 "views": 98,
		 "likes": 40,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Veggie Wholewheat Pot Noodle",
		 "views": 128,
		 "likes": 64,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Lean Turkey Burger",
		 "views": 90,
		 "likes": 30,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Thai Prawn and Ginger Noodles",
		 "views": 530,
		 "likes": 500,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Overnight Oats",
		 "views": 530,
		 "likes": 222,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		}
	]

	brunch_recipes = [
		{"recipe_name": "Huevos Rancheros",
		 "views": 67,
		 "likes": 31,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Eggs Royale",
		 "views": 300,
		 "likes": 177,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "French Toast with Maple Syrup", 
		 "views": 600,
		 "likes": 200,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Pancakes with Fresh Berries",
		 "views": 549,
		 "likes": 199,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Berry Smoothie Bowl",
		 "views": 12,
		 "likes": 12,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name":"Baked Avocado with Smoked Salmon and Egg",
		 "views":90,
		 "likes": 40,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		}
	]

	mexican_recipes = [
		{"recipe_name": "Pulled Pork Burrito",
		 "views": 32,
		 "likes": 10,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Chicken Fajitas",
		 "views": 80,
		 "likes": 26,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Vegetable Enchiladas",
		 "views":91,
		 "likes": 30,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Spicy Beef Quesadillas",
		 "views": 76,
		 "likes": 68,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Chilli Con Carne",
		 "views": 230,
		 "likes": 130,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Churros",
		 "views":89,
		 "likes": 30,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Jackfruit Tacos",
		 "views":35,
		 "likes": 5,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		}
	]

	italian_recipes = [
		{"recipe_name": "Salsiccia Piccante Pizza",
		 "views" :210,
		 "likes": 185,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Spaghetti Carbonara",
		 "views" :333,
		 "likes": 220,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Lobster Ravioli",
		 "views" :39,
		 "likes": 26,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Pollo Milanese",
		 "views" :80,
		 "likes": 36,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Risotto Quattro Stagioni",
		 "views" :12,
		 "likes": 8,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Tiramisu",
		 "views" :99,
		 "likes": 40,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		}
	]

	gluten_free_recipes = [
		{"recipe_name": "Scones",
		 "views": 54,
		 "likes": 48,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Bolognese",
		 "views": 300,
		 "likes": 247,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Pizza",
		 "views": 159,
		 "likes": 99,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Salmon and Brocolli Bake",
		 "views": 31,
		 "likes": 11,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Pesto, Courgette * Gryuere Polenta Tart",
		 "views": 92,
		 "likes": 46,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Self-Saucing Chocolate Pudding",
		 "views": 500,
		 "likes": 500,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		}
	]

	comfort_recipes = [
		{"recipe_name": "Beef Wellington",
		 "views": 35,
		 "likes": 24,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Shepherd's Pie",
		 "views": 215,
		 "likes": 126,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Chocolate Fudge Cake",
		 "views": 530,
		 "likes": 520,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},
		
		{"recipe_name": "Mac n Cheese with Bacon Bits",
		 "views": 428,
		 "likes": 400,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Apple Pie",
		 "views": 92,
		 "likes": 87,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},
		
		{"recipe_name": "Fried Chicken",
		 "views": 76,
		 "likes": 46,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		}
	]

	dairy_free_recipes = [
		{"recipe_name": "Meatloaf",
		 "views": 98,
		 "likes": 13,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Coconut and Fish Curry Parcels",
		 "views": 75,
		 "likes": 2,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},
		
		{"recipe_name": "Chocolate, Orange & Hazelnut Cake",
		 "views": 145,
		 "likes": 136,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Salmon & Lemon Mini Fishcakes",
		 "views": 530,
		 "likes": 381,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Lentil Lasagne",
		 "views": 200,
		 "likes": 137,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Sausage & Bean One-Pot",
		 "views": 237,
		 "likes": 100,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		}
	]
	
	kid_friendly_recipes = [
		{"recipe_name": "Crispy Fish Sticks",
		 "views": 117,
		 "likes": 10,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Burger Sliders",
		 "views": 54,
		 "likes": 33,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Spaghetti Meatballs",
		 "views": 77,
		 "likes": 67,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Cheesy Chicken Casserole",
		 "views": 8,
		 "likes": 4,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},

		{"recipe_name": "Vegetable Fried Rice",
		 "views": 22,
		 "likes": 16,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		},
		

		{"recipe_name": "Beef Stew and Dumplings",
		 "views": 10,
		 "likes": 5,
		 "recipe_data": "temp",
		 "image": "bolognese.jpg"
		}
	]
		
		
	cats =  {"Vegan/Vegetarian Meals": {"recipes": vegan_recipes, "views":128, "likes":64}, 
		"Healthy Meals": {"recipes": healthy_recipes, "views":64,"likes":32},
		"Brunch Ideas": {"recipes": brunch_recipes, "views":32, "likes":16},
		"Mexican Meals": {"recipes": mexican_recipes, "views":72,"likes":32},
		"Italian Meals": {"recipes": italian_recipes, "views":82,"likes":12},
		"Gluten Free Meals": {"recipes": gluten_free_recipes, "views":25,"likes":11},
		"Comfort Food": {"recipes": comfort_recipes, "views":55,"likes":41},
		"Dairy Free Meals": {"recipes": dairy_free_recipes, "views":99,"likes":65},
		"Kid Friendly Meals": {"recipes": kid_friendly_recipes, "views":88,"likes":21}
	}

	with open('recipes.json', 'r') as f:
		recipes_dict = json.load(f)
	
	for cat, cat_data in cats.items():
		c = add_cat(cat, cat_data["views"], cat_data["likes"])
		for p in cat_data["recipes"]:
			add_recipe(c, p["recipe_name"], os.path.join("recipe_images", c.slug, p["image"]), p["views"], p["likes"],
			 json.dumps(recipes_dict['categories'][cat][p["recipe_name"]]['ingredients']),
			 recipes_dict['categories'][cat][p["recipe_name"]]['directions'])
			
	for c in Category.objects.all():
		for p in Recipe.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_recipe(cat, recipe_name, image, views=0, likes=0, recipe_ingredients="", recipe_directions=""):
	p = Recipe.objects.get_or_create(category=cat, recipe_name=recipe_name)[0]
	p.views = views
	p.likes = likes
	p.recipe_ingredients = recipe_ingredients
	p.recipe_directions = recipe_directions
	p.image = image
	p.save()
	return p
	
def add_cat(name,views,likes):
	c =  Category.objects.get_or_create(name=name, views = views, likes=likes)[0]
	c.save()
	return c

if __name__ == '__main__':
	print("Starting RateMyMeal population script...")
	populate()
