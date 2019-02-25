import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():
	vegan_pages =[
		{"recipe_name": "Vegan Chilli", "views":22},
		{"recipe_name":"Mushroom Burgers", "views" :55},
		{"recipe_name":"Lasagne", "views":222},
		{"recipe_name":"Brownies", "views":159},
		{"recipe_name":"Falafel Burgers", "views":32},
		{"recipe_name":"Thai Curry", "views":96}]
	healthy_pages = [
		{"recipe_name":"Roasted Chickpea Wraps",  "views":39}, 
		{"recipe_name":"Roast Pepper Pesto Pasta", "views":98},
		{"recipe_name":"Veggie Wholewheat Pot Noodle", "views": 128},
		{"recipe_name":"Lean Turkey Burger", "views":90},
		{"recipe_name":"Thai Prawn and Ginger Noodles", "views":530},
		{"recipe_name":"Overnight Oats", "views":530},]
	brunch_pages = [
		{"recipe_name":"Huevos Rancheros", "views":67},
		{"recipe_name":"Eggs Royale", "views":300},
		{"recipe_name":"French Toast with Maple Syrup", "views":600},
		{"recipe_name":"Pancakes with Fresh Berries", "views":549},
		{"recipe_name":"Berry Smoothie Bowl", "views":12},
		{"recipe_name":"Baked Avocade with Smoked Salmon and Egg", "views":90}]
	mexican_pages = [
		{"recipe_name":"Pulled Pork Burrito", "views":32},
		{"recipe_name":"Chicken Fajitas", "views":80} ,
		{"recipe_name":"Vegetable Enchiladas", "views":91},
		{"recipe_name":"Spicy Beef Quesadillas", "views":76},
		{"recipe_name":"Chilli Con Carne", "views":230},
		{"recipe_name":"Churros", "views":89},
		{"recipe_name":"Jackfruit Tacos", "views":35},]
	italian_pages = [
		{"recipe_name":"Salsiccia Piccante Pizza", "views":210},
		{"recipe_name":"Spaghetti Carbonara", "views":333},
		{"recipe_name":"Lobster Ravioli", "views":39},
		{"recipe_name":"Pollo Milanese", "views":80},
		{"recipe_name":"Risotto Quattro Stagioni", "views":12},
		{"recipe_name":"Tiramisu", "views":99}]
	gluten_free_pages = [
		{"recipe_name":"Scones", "views":54},
		{"recipe_name":"Bolognese", "views":300},
		{"recipe_name":"Pizza", "views":159},
		{"recipe_name":"Salmon and Brocolli Bake", "views":31},
		{"recipe_name":"Pesto, Courgette * Gryuere Polenta Tart", "views":92},
		{"recipe_name":"Self-Saucing Chocolate Pudding", "views":500},]
	comfort_pages = [
		{"recipe_name":"Beef Wellington", "views":35},
		{"recipe_name":"Shepherd's Pie", "views":215},
		{"recipe_name":"Chocolate Fudge Cake", "views":530},
		{"recipe_name":"Mac n Cheese with Bacon Bits", "views":50},
		{"recipe_name":"Apple Pie", "views":92},
		{"recipe_name":"Fried Chicken", "views":76}]
	dairy_free_pages = [
		{"recipe_name":"Meatloaf", "views":98},
		{"recipe_name":"Coconut and Fish Curry Parcels", "views":75}
		{"recipe_name":"Chocolate, Orange & Hazelnut Cake", "views":145},
		{"recipe_name":"Salmon & Lemon Mini Fishcakes", "views":530},
		{"recipe_name":"Lentil Lasagne", "views":200},
		{"recipe_name":"Sausage & Bean One-Pot", "views":237}]
	
	kid_friendly_pages = [
		{"recipe_name":"Crispy Fish Sticks", "views":117},
		{"recipe_name":"Burger Sliders", "views":54},
		{"recipe_name":"Spaghetti Meatballs", "views":77},
		{"recipe_name":"Cheesy Chicken Casserole", "views":8},
		{"recipe_name":"Vegetable Fried Rice", "views":22},
		{"recipe_name":"Beef Stew and Dumplings", "views":10}]
		
		
	cats =  {"Vegan/Vegetarian Meals": {"pages": vegan_pages, "views":128, "likes":64}, 
		"Healthy Meals": {"pages": healthy_pages, "views":64,"likes":32},
		"Brunch Ideas": {"pages": brunch_pages, "views":32, "likes":16},
		"Mexican Meals": {"pages": mexican_pages, "views":72,"likes":32},
		"Italian Meals": {"pages": italian_pages, "views":82,"likes":12},
		"Gluten Free Meals": {"pages": gluten_free_pages, "views":25,"likes":11},
		"Comfort Food": {"pages": comfort_pages, "views":55,"likes":41},
		"Dairy Free Meals": {"pages": dairy_free_pages, "views":99,"likes":65},
		"Kid Friendly Meals": {"pages": kid_friendly_pages, "views":88,"likes":21}}
	
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
