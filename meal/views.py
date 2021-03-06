from django.shortcuts import render
from django.template import RequestContext
from meal.models import Category, Recipe, UserProfile, Professional, Like, Chef
from meal.forms import UserFormRegular,UserFormChef, UserProfileForm, RecipeForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse 
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.models import Permission
from django.db.models import Q

from django.http import HttpResponse

# This is the view representing the all categories page.
def categories(request):
    context_dict = {}

    try:
        # Queries data base for all categories
        categories = Category.objects.all()

        # Splits the categories list into three separate lists for presentation.
        chunks = [categories[i::3] for i in range(0, 3)]
        context_dict['categories'] = categories
        context_dict['column1'] = chunks[0]
        context_dict['column2'] = chunks[1]
        context_dict['column3'] = chunks[2]
    except Category.DoesNotExist:
        context_dict['categories'] = None

    return render(request, 'meal/categories.html', context_dict)

# This is the view for the page representing individual categories.
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        # Queries database for all recipes of the representative category.
        category = Category.objects.get(slug=category_name_slug)
        recipe = Recipe.objects.filter(category=category)

        # Splits the recipe list into three separate lists for presentation.
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
        # Queries database for a single recipe, identified by parameters passed in.
        category = Category.objects.get(slug = category_name_slug)
        recipe = Recipe.objects.get(slug = recipe_name_slug)

        context_dict['recipe'] = recipe
        context_dict['ingredients'] = recipe.get_ingredients()
        context_dict['category'] = category

        views1=Recipe.objects.get(id=recipe.id)
        views1.views=views1.views + 1
        views1.save()
        context_dict['views'] = views1.views
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None
        context_dict['ingredients'] = None
        context_dict['category'] = None
        context_dict['views'] = None
    
        
    response = render(request, 'meal/recipe.html', context_dict)
    #response.set_cookie('views',recipe.views)
    return response

# This is the view for the page representing chegs.
def show_chef(request, chef_name_slug):
    context_dict = {}

    try:
        # Queries the database to get the chef and the chefs recipes.
        professional = [Professional.objects.get(slug = chef_name_slug)]
        chef = UserProfile.objects.get(user__in = professional)
        recipes = Recipe.objects.filter(chef = chef)

        context_dict['chef'] = chef
        context_dict['recipes'] = recipes
    except Professional.DoesNotExist:
        context_dict['chef'] = None
        context_dict['recipes'] = None

    return render(request, 'meal/chef.html', context_dict)
	
# This is the view for representing the add recipe page.
def add_recipe(request):
    context_dict = {}
    if request.method == 'POST':

        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():

            page = form.save(commit=False)
            page.set_ingredients(page.recipe_ingredients.replace('\r', '').split("\n"))
            page.chef = UserProfile.objects.get(user = request.user)
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

    # Queries the database to get the 6 most recent chefs
    try:
        professionals = Professional.objects.all()
        chefs = UserProfile.objects.filter(user__in = professionals)
        chefs = chefs.order_by('-created')[:6]

        context_dict['chefs'] = chefs
    except Professional.DoesNotExist:
        context_dict['chefs'] = None
    
    return render(request, 'meal/base.html', context_dict)

# This is the view representing the trending page.
def trending(request):
    request.session.set_test_cookie()

    # Queries the database to get the recipes corresponding to the two most liked and viewed recipes.
    try:
        recipe_likes = Recipe.objects.order_by('-likes')[:3]
        recipe_views = Recipe.objects.order_by('-views')[:3]

        context_dict = {"recipe_likes" : recipe_likes, "recipe_views":recipe_views}
    except Recipe.DoesNotExist:
        context_dict = {"recipe_likes" : None, "recipe_views" : None}
    
    response = render(request, 'meal/trending.html', context=context_dict)
    return response

# This is the view representing the user sign up page.
def signUp(request):
	return render(request, 'meal/signup.html', {})

# This is the view representing the register page for the casual chefs.
def registerRegular(request):
    registered = False

    if request.method == 'POST':
        user_formRegular = UserFormRegular(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_formRegular.is_valid() and profile_form.is_valid():
            user = user_formRegular.save()
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
            print(user_form.errors + "\n" + profile_form.errors + "\n")
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
            print(user_formChef.errors, profile_form.errors)
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
    rec_id = None
    if request.method == 'GET':
        rec_id = request.GET['recipe_id']
        user_id = request.GET['user_id']
        likes = 0
        if rec_id and user_id:
            rec = Recipe.objects.get(id=int(rec_id))
            exists = Like.new(user_id, rec_id)
            if rec and not exists:
                likes = rec.likes + 1
                rec.likes = likes
                rec.save()
            else:
                likes = rec.likes
    return HttpResponse(likes)

# This view is used for allowing a user to unlike a recipe.
@login_required
def unlike_recipe(request):
    context = RequestContext(request)
    rec_id = None
    if request.method == 'GET':
        rec_id = request.GET['recipe_id']
        user_id = request.GET['user_id']
        likes = 0
        if rec_id and user_id:
            rec = Recipe.objects.get(id=int(rec_id))
            exists = Like.new(user_id, rec_id)
            if rec and exists:
                likes = rec.likes - 1
                rec.likes = likes
                rec.save()
                Like.objects.filter(chef=Chef.objects.filter(id=user_id)[0],
                                     recipe_id=rec_id).delete()
            else:
                likes = rec.likes
    return HttpResponse(likes)

# This view is used to check if a user has liked a recipe
@login_required
def like_exists(request):
    context = RequestContext(request)
    rec_id = request.GET['recipe_id']
    user_id = request.GET['user_id']
    exists = 0
    if rec_id and user_id:
        try:
            like = Like.objects.get(chef=Chef.objects.filter(id=user_id)[0],
                                                       recipe_id=rec_id)
        except Like.DoesNotExist:
            exists = 1
    return HttpResponse(exists)


# This is the view for the search page.
def search(request):
    
    query =  request.GET.get('q')

    # Queries database for recipes and categories that contains query.
    try:
        recipeResults = Recipe.objects.filter(recipe_name__icontains=query)
    except Recipe.DoesNotExist:
        recipeResults = None
        
    try:
        categoryResults = Category.objects.filter(name__icontains=query)
    except Category.DoesNotExist:
        categoryResults = None
        
    return render(request,"meal/search.html",{"query":query,"results":recipeResults, "catResults":categoryResults})
