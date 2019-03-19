import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RateMyMealProject.settings')

import django
django.setup()
from meal.models import Category, Recipe, Professional, Casual, UserProfile

def populate():
	casual_chefs = [
		{"username": "MotherMartha1978",
		 "email": "mothermartha1984@gmail.com",
		 "password": "marthasmonkies",
		 "profile_picture": ""
		},

		{"username": "JustJack99",
		 "email": "MadJacko@gmail.com",
		 "password": "justjackthings99",
		 "profile_picture": ""
		}
	]

	professional_chefs = [
		{"username": "RaymondBolt",
		 "email": "stoneeagle@gmail.com",
		 "password": "cheddar",
		 "profile_picture": "RaymondBolt.jpg"
		},

		{"username": "HayleyBean",
		 "email": "hayleybean@gmail.com",
		 "password": "s6n*cjd(&4ds",
		 "profile_picture": "HayleyBean.jpg"
		},

		{"username": "TheRealStanleySpears",
		 "email": "therealstanleyspears@gmail.com",
		 "password": "l&^5bkw2'!p)",
		 "profile_picture": "TheRealStanleySpears.jpg"
		},

		{"username": "ItsaMarioManini",
		 "email": "mariomanini@gmail.com",
		 "password": "i'mperfect",
		 "profile_picture": "ItsaMarioManini"
		},

		{"username": "AidanMack",
		 "email": "aidanmack@gmail.com",
		 "password": "je86^jka%33mn)1",
		 "profile_picture": "AidanMack.jpg"
		},

		{"username": "HenryMichaels",
		 "email": "henrymichaels@gmail.com",
		 "password": "sajq76&(*3bmn1",
		 "profile_picture": "HenryMichaels.jpg"
		}
	]

	vegan_recipes =[
		{"recipe_name": "Vegan Chilli",
		 "views": 22,
		 "likes": 10, 
		 "recipe_data": "temp",
		 "image": "vegan-chilli.jpg"
		},

		{"recipe_name": "Mushroom Burgers",
		 "views" :55,
		 "likes": 22,
		 "recipe_data": "temp",
		 "image": "mushroom-burgers.jpg"
		},

		{"recipe_name": "Lasagne", 
		 "views": 222,
		 "likes": 222,
		 "recipe_data": "temp",
		 "image": "lasagne.jpg"
		},

		{"recipe_name": "Brownies",
		 "views":159,
		 "likes": 158,
		 "recipe_data": "temp",
		 "image": "brownies.jpg"
		},

		{"recipe_name": "Falafel Burgers",
		 "views":32,
		 "likes": 0,
		 "recipe_data": "temp",
		 "image": "falafel-burgers.jpg"
		},

		{"recipe_name": "Thai Curry",
		 "views":96,
		 "likes": 90,
		 "recipe_data": "temp",
		 "image": "thai-curry.jpg"
		}
	]

	healthy_recipes = [
		{"recipe_name": "Roasted Chickpea Wraps",
		 "views": 39,
		 "likes": 16,
		 "recipe_data": "temp",
		 "image": "roasted-chickpea-wraps.jpg"
		},

		{"recipe_name": "Roast Pepper Pesto Pasta",
		 "views": 98,
		 "likes": 40,
		 "recipe_data": "temp",
		 "image": "roast-pepper-pesto-pasta.jpg"
		},

		{"recipe_name": "Veggie Wholewheat Pot Noodle",
		 "views": 128,
		 "likes": 64,
		 "recipe_data": "temp",
		 "image": "veggie-wholewheat-pot-noodle.jpg"
		},

		{"recipe_name": "Lean Turkey Burger",
		 "views": 90,
		 "likes": 30,
		 "recipe_data": "temp",
		 "image": "lean-turkey-burger.jpg"
		},

		{"recipe_name": "Thai Prawn and Ginger Noodles",
		 "views": 530,
		 "likes": 500,
		 "recipe_data": "temp",
		 "image": "thai-prawn-and-ginger-noodles.jpg"
		},

		{"recipe_name": "Overnight Oats",
		 "views": 530,
		 "likes": 222,
		 "recipe_data": "temp",
		 "image": "overnight-oats.jpg"
		}
	]

	brunch_recipes = [
		{"recipe_name": "Huevos Rancheros",
		 "views": 67,
		 "likes": 31,
		 "recipe_data": "temp",
		 "image": "huevos-rancheros.jpg"
		},

		{"recipe_name": "Eggs Royale",
		 "views": 300,
		 "likes": 177,
		 "recipe_data": "temp",
		 "image": "eggs-royale.jpg"
		},

		{"recipe_name": "French Toast with Maple Syrup", 
		 "views": 600,
		 "likes": 200,
		 "recipe_data": "temp",
		 "image": "french-toast-with-maple-syrup.jpg"
		},

		{"recipe_name": "Pancakes with Fresh Berries",
		 "views": 549,
		 "likes": 199,
		 "recipe_data": "temp",
		 "image": "pancakes-with-fresh-berriess.jpg"
		},

		{"recipe_name": "Berry Smoothie Bowl",
		 "views": 12,
		 "likes": 12,
		 "recipe_data": "temp",
		 "image": "berrry-smoothie-bowl.jpg"
		},

		{"recipe_name":"Baked Avocado with Smoked Salmon and Egg",
		 "views":90,
		 "likes": 40,
		 "recipe_data": "temp",
		 "image": "baked-avocado-with-smoked-salmon-and-egg.jpg"
		}
	]

	mexican_recipes = [
		{"recipe_name": "Pulled Pork Burrito",
		 "views": 32,
		 "likes": 10,
		 "recipe_data": "temp",
		 "image": "pulled-pork-burrito.jpg"
		},

		{"recipe_name": "Chicken Fajitas",
		 "views": 80,
		 "likes": 26,
		 "recipe_data": "temp",
		 "image": "chicken-fajitas.jpg"
		},

		{"recipe_name": "Vegetable Enchiladas",
		 "views":91,
		 "likes": 30,
		 "recipe_data": "temp",
		 "image": "vegetable-enchiladas.jpg"
		},

		{"recipe_name": "Spicy Beef Quesadillas",
		 "views": 76,
		 "likes": 68,
		 "recipe_data": "temp",
		 "image": "spicy-beef-quesadillas.jpg"
		},

		{"recipe_name": "Chilli Con Carne",
		 "views": 230,
		 "likes": 130,
		 "recipe_data": "temp",
		 "image": "chilli-con-carne.jpg"
		},

		{"recipe_name": "Churros",
		 "views":89,
		 "likes": 30,
		 "recipe_data": "temp",
		 "image": "churros.jpg"
		},

		{"recipe_name": "Jackfruit Tacos",
		 "views":35,
		 "likes": 5,
		 "recipe_data": "temp",
		 "image": "jackfruit-tacos.jpg"
		}
	]

	italian_recipes = [
		{"recipe_name": "Salsiccia Piccante Pizza",
		 "views" :210,
		 "likes": 185,
		 "recipe_data": "temp",
		 "image": "salsiccia-piccante-pizza.jpg"
		},

		{"recipe_name": "Spaghetti Carbonara",
		 "views" :333,
		 "likes": 220,
		 "recipe_data": "temp",
		 "image": "spaghetti-carbonara.jpg"
		},

		{"recipe_name": "Lobster Ravioli",
		 "views" :39,
		 "likes": 26,
		 "recipe_data": "temp",
		 "image": "lobster-ravioli.jpg"
		},

		{"recipe_name": "Pollo Milanese",
		 "views" :80,
		 "likes": 36,
		 "recipe_data": "temp",
		 "image": "pollo-milanese.jpg"
		},

		{"recipe_name": "Risotto Quattro Stagioni",
		 "views" :12,
		 "likes": 8,
		 "recipe_data": "temp",
		 "image": "risotto-quattro-stagioni.jpg"
		},

		{"recipe_name": "Tiramisu",
		 "views" :99,
		 "likes": 40,
		 "recipe_data": "temp",
		 "image": "tiramisu.jpg"
		}
	]

	gluten_free_recipes = [
		{"recipe_name": "Scones",
		 "views": 54,
		 "likes": 48,
		 "recipe_data": "temp",
		 "image": "scones.jpg"
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
		 "image": "pizza.jpg"
		},

		{"recipe_name": "Salmon and Broccolli Bake",
		 "views": 31,
		 "likes": 11,
		 "recipe_data": "temp",
		 "image": "salmon-and-broccolli-bake.jpg"
		},

		{"recipe_name": "Pesto & Courgette Gryuere Polenta Tart",
		 "views": 92,
		 "likes": 46,
		 "recipe_data": "temp",
		 "image": "pesto-&-courgette-gryuere-polenta-tart.jpg"
		},

		{"recipe_name": "Self-Saucing Chocolate Pudding",
		 "views": 500,
		 "likes": 500,
		 "recipe_data": "temp",
		 "image": "self-saucing-chocolate-pudding.jpg"
		}
	]

	comfort_recipes = [
		{"recipe_name": "Beef Wellington",
		 "views": 35,
		 "likes": 24,
		 "recipe_data": "temp",
		 "image": "beef-wellington.jpg"
		},

		{"recipe_name": "Shepherd's Pie",
		 "views": 215,
		 "likes": 126,
		 "recipe_data": "temp",
		 "image": "shepherd's-pie.jpg"
		},

		{"recipe_name": "Chocolate Fudge Cake",
		 "views": 530,
		 "likes": 520,
		 "recipe_data": "temp",
		 "image": "chocolate-fudge-cake.jpg"
		},
		
		{"recipe_name": "Mac n Cheese with Bacon Bits",
		 "views": 428,
		 "likes": 400,
		 "recipe_data": "temp",
		 "image": "mac-n-cheese-with-bacon-bits.jpg"
		},

		{"recipe_name": "Apple Pie",
		 "views": 92,
		 "likes": 87,
		 "recipe_data": "temp",
		 "image": "apple-pie.jpg"
		},
		
		{"recipe_name": "Fried Chicken",
		 "views": 76,
		 "likes": 46,
		 "recipe_data": "temp",
		 "image": "fried-chicken.jpg"
		}
	]

	dairy_free_recipes = [
		{"recipe_name": "Meatloaf",
		 "views": 98,
		 "likes": 13,
		 "recipe_data": "temp",
		 "image": "meatloaf.jpg"
		},

		{"recipe_name": "Coconut and Fish Curry Parcels",
		 "views": 75,
		 "likes": 2,
		 "recipe_data": "temp",
		 "image": "coconut-and-fish-curry-parcels.jpg"
		},
		
		{"recipe_name": "Chocolate, Orange & Hazelnut Cake",
		 "views": 145,
		 "likes": 136,
		 "recipe_data": "temp",
		 "image": "chocolate,-orange-&-hazelnut-cake.jpg"
		},

		{"recipe_name": "Salmon & Lemon Mini Fishcakes",
		 "views": 530,
		 "likes": 381,
		 "recipe_data": "temp",
		 "image": "salmon-&-lemon-mini-fishcakes.jpg"
		},

		{"recipe_name": "Lentil Lasagne",
		 "views": 200,
		 "likes": 137,
		 "recipe_data": "temp",
		 "image": "lentil-lasagne.jpg"
		},

		{"recipe_name": "Sausage & Bean One-Pot",
		 "views": 237,
		 "likes": 100,
		 "recipe_data": "temp",
		 "image": "sausage-&-bean-one-pot.jpg"
		}
	]
	
	kid_friendly_recipes = [
		{"recipe_name": "Crispy Fish Sticks",
		 "views": 117,
		 "likes": 10,
		 "recipe_data": "temp",
		 "image": "crispy-fish-sticks.jpg"
		},

		{"recipe_name": "Burger Sliders",
		 "views": 54,
		 "likes": 33,
		 "recipe_data": "temp",
		 "image": "burger-sliders.jpg"
		},

		{"recipe_name": "Spaghetti Meatballs",
		 "views": 77,
		 "likes": 67,
		 "recipe_data": "temp",
		 "image": "spaghetti-meatballs.jpg"
		},

		{"recipe_name": "Cheesy Chicken Casserole",
		 "views": 8,
		 "likes": 4,
		 "recipe_data": "temp",
		 "image": "chessy-chicken-casserole.jpg"
		},

		{"recipe_name": "Vegetable Fried Rice",
		 "views": 22,
		 "likes": 16,
		 "recipe_data": "temp",
		 "image": "vegetable-fried-rice.jpg"
		},
		

		{"recipe_name": "Beef Stew and Dumplings",
		 "views": 10,
		 "likes": 5,
		 "recipe_data": "temp",
		 "image": "beef-stew-and-dumplings.jpg"
		}
	]
		
		
	cats =  {"Vegan/Vegetarian Meals": {"recipes": vegan_recipes, "views":128, "likes":64, "chef": "RaymondBolt"}, 
		"Healthy Meals": {"recipes": healthy_recipes, "views":64,"likes":32, "chef": "RaymondBolt"},
		"Brunch Ideas": {"recipes": brunch_recipes, "views":32, "likes":16, "chef": "HayleyBean"},
		"Mexican Meals": {"recipes": mexican_recipes, "views":72,"likes":32, "chef": "TheRealStanleySpears"},
		"Italian Meals": {"recipes": italian_recipes, "views":82,"likes":12, "chef": "ItsaMarioManini"},
		"Gluten Free Meals": {"recipes": gluten_free_recipes, "views":25,"likes":11, "chef": "ItsaMarioManini"},
		"Comfort Food": {"recipes": comfort_recipes, "views":55,"likes":41, "chef": "AidanMack"},
		"Dairy Free Meals": {"recipes": dairy_free_recipes, "views":99,"likes":65, "chef": "HenryMichaels"},
		"Kid Friendly Meals": {"recipes": kid_friendly_recipes, "views":88,"likes":21, "chef": "HenryMichaels"}
	}

	with open('recipes.json', 'r') as f:
		recipes_dict = json.load(f)

	for chef_data in casual_chefs:
		add_chef(chef_data['username'], chef_data['email'], chef_data['password'],
		 os.path.join("profile_image", chef_data['profile_picture']), Casual)

	for chef_data in professional_chefs:
		add_chef(chef_data['username'], chef_data['email'], chef_data['password'],
		 os.path.join("profile_image", chef_data['profile_picture']), Professional)
	
	for cat, cat_data in cats.items():
		c = add_cat(cat, cat_data["views"], cat_data["likes"])
		cur_chef = Professional.objects.get(username = cat_data['chef'])
		for p in cat_data["recipes"]:
			add_recipe(c, p["recipe_name"], 
			 os.path.join("recipe_images", c.slug, p["image"]),
			 UserProfile.objects.get(user = cur_chef),
			 p["views"], p["likes"],
			 json.dumps(recipes_dict['categories'][cat][p["recipe_name"]]['ingredients']),
			 recipes_dict['categories'][cat][p["recipe_name"]]['directions'])
			
	for c in Category.objects.all():
		for p in Recipe.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

	for profile in UserProfile.objects.all():
		print("- {0}".format(str(profile.user)))

def add_recipe(cat, recipe_name, image, chef, views=0, likes=0, recipe_ingredients="", recipe_directions=""):
	p = Recipe.objects.get_or_create(category=cat, recipe_name=recipe_name, chef=chef)[0]
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

def add_chef(username, email, password, profile_picture, chef_class):
	chef = chef_class.objects.get_or_create(username = username, email = email, password = password)[0]
	chef.save()
	profile = UserProfile.objects.get_or_create(user = chef, picture = profile_picture)[0]
	profile.save()
	return profile



if __name__ == '__main__':
	print("Starting RateMyMeal population script...")
	populate()
