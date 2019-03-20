from django.shortcuts import render
from django.template import RequestContext
from meal.models import Category, Recipe, UserProfile, Professional
from meal.forms import UserFormRegular,UserFormChef, UserProfileForm, RecipeForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse 
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.models import Permission
from meal.webhose_search import run_query
from django.db.models import Q

from django.http import HttpResponse

# This is the view representing the all categories page.
def categories(request):
    context_dict = {}
    categories = Category.objects.all()
    chunks = [categories[i::3] for i in range(0, 3)]
    context_dict['column1'] = chunks[0]
    context_dict['column2'] = chunks[1]
    context_dict['column3'] = chunks[2]

    return render(request, 'meal/categories.html', context_dict)

# This is the view for the page representing individual categories.
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        recipe = Recipe.objects.filter(category=category)

        chunks = [recipe[i::3] for i in range(0, 3)]
        context_dict['column1'] = chunks[0]
        context_dict['column2'] = chunks[1]
        context_dict['column3'] = chunks[2]

        context_dict['recipes'] = recipe
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['recipes'] = None
        context_dict['category'] = None

    return render(request, 'meal/category.html', context_dict)

# This is the view for the page representing each individual recipes.
def show_recipe(request, category_name_slug, recipe_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug = category_name_slug)
        recipe = Recipe.objects.get(slug = recipe_name_slug)
        context_dict['recipe'] = recipe
        context_dict['ingredients'] = recipe.get_ingredients()
        context_dict['category'] = category
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None
        context_dict['ingredients'] = None
        context_dict['category'] = None

    visitor_cookie_handler(request)
    
    views1=Recipe.objects.get(id=recipe.id)
    views1.views=views1.views+1
    views1.save()
    context_dict['views'] = views1.views
    
        
    response = render(request, 'meal/recipe.html', context_dict)
    #response.set_cookie('views',recipe.views)
    return response

def show_chef(request, chef_name_slug):
    context_dict = {}

    professional = [Professional.objects.get(slug = chef_name_slug)]
    chef = UserProfile.objects.get(user__in = professional)
    recipes = Recipe.objects.filter(chef = chef)
    context_dict['chef'] = chef
    context_dict['recipes'] = recipes

    return render(request, 'meal/chef.html', context_dict)
	
# This is the view for representing the add recipe page.
def add_recipe(request):
    context_dict = {}
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():

            page = form.save(commit=False)
            page.set_ingredients(page.recipe_ingredients.replace('\r', '').split("\n"))
            page.views = 0
            
            if 'image' in request.FILES:
                page.picture = request.FILES['image']

            
            page.save()
            return HttpResponseRedirect(reverse('base'))

               
        else:
            print (form.errors)
    else:
        form = RecipeForm()

    context_dict = {'form':form}
    return render(request, 'meal/add_recipe.html', context_dict)

# This is the view representing the about page.
def about(request):
	return render(request, 'meal/about.html', {})

# This is the view representing the base page.
def base(request):
    context_dict = {}

    professionals = Professional.objects.all()
    chefs = UserProfile.objects.filter(user__in = professionals)
    chefs = chefs.order_by('-created')[:6]
    context_dict['chefs'] = chefs

    
    
    return render(request, 'meal/base.html', context_dict)

# This is the view representing the trending page.
def trending(request):
    request.session.set_test_cookie()
    recipe_likes = Recipe.objects.order_by('-likes')[:2]
    recipe_views = Recipe.objects.order_by('-views')[:2]

    context_dict = {"recipe_likes" : recipe_likes, "recipe_views":recipe_views}
    
    response = render(request, 'meal/trending.html', context=context_dict)
    return response

# This is the view representing the user sign up page.
def signUp(request):
	return render(request, 'meal/signup.html', {})

# This is the view representing the register page for the casual chefs.
def registerRegular(request):
    registered = False

    if request.method == 'POST':
        user_form = UserFormRegular(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            return redirect_to_login('meal/login.html')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserFormRegular()
        profile_form = UserProfileForm()

    context_dict = { 'user_form':user_form,
                     'profile_form':profile_form,
                     'registered':registered}

    return render(request, 'meal/registerRegular.html', context_dict)

# This is the view representing the register page for the professional chefs.
def registerChef(request):
    registered = False

    if request.method == 'POST':
        user_formChef = UserFormChef(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_formChef.is_valid() and profile_form.is_valid():
            permission = Permission.objects.get(name='Can read Chef')
            
            user = user_formChef.save()
            user.set_password(user.password)
            user.save()
            user.user_permissions.add(permission)
            profile = profile_form.save(commit=False)
            profile.user=user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            return redirect_to_login('meal/login.html')
        else:
            print(user_formChef.errors,profile_form.errors)
    else:
        user_formChef = UserFormChef()
        profile_form = UserProfileForm()

    context_dict = { 'user_form':user_formChef,
                     'profile_form':profile_form,
                     'registered':registered}

    return render(request,'meal/registerChef.html',context_dict)

# This is the view representing the user login page.
def user_login(request):
    try:
        user = authenticate(username = request.POST['username'],
            password = request.POST['password'])
    except KeyError:
        return render(request, 'meal/login.html',{
            'login_message' : 'Please Enter Your Username and Password',}) 
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            return render(request, 'meal/login.html',{
                'login_message' : 'Your Account Has Been Banned',})
    else:
        return render(request, 'meal/login.html',{
            'login_message' : 'Please Enter Your Username and Password correctly',})
    return HttpResponseRedirect(reverse('base'))

# This view allows the user to logout.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))

# This view is used for allowing a user to like a recipe.
@login_required
def like_recipe(request):
    context = RequestContext(request)
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['recipe_id']
        likes = 0
        if cat_id:
            cat = Recipe.objects.get(id=int(cat_id))
            if cat:
                likes = cat.likes + 1
                cat.likes = likes
                cat.save()
    return HttpResponse(likes)

# This is the view for the search page.
def search(request):
	query =  request.GET.get('q')
	recipeResults = Recipe.objects.filter(recipe_name__icontains=query)
	categoryResults = Category.objects.filter(name__icontains=query)
	return render(request,"meal/search.html",{"query":query,"results":recipeResults, "catResults":categoryResults})

def visitor_cookie_handler(request):

    views = int(get_server_side_cookie(request, 'views', '1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit',
    str(datetime.now()))

    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
    '%Y-%m-%d %H:%M:%S')
    
    if (datetime.now() - last_visit_time).days > -1:
        views = views + 1
        
        request.session['last_visit'] = str(datetime.now())

    else:
    # set the last visit cookie
        request.session['last_visit'] = last_visit_cookie
# Update/set the visits cookie
    request.session['views'] = views



def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val
