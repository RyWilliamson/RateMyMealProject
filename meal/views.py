from django.shortcuts import render
from django.template import RequestContext
from meal.models import Category, Recipe, Like, Chef
from meal.forms import UserFormRegular,UserFormChef, UserProfileForm, RecipeForm,RecipeImageForm
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
    size = len(categories)
    context_dict['column1'] = categories[0 : int(size / 3)]
    context_dict['column2'] = categories[int(size / 3) : 2 * int(size / 3)]
    context_dict['column3'] = categories[2 * int(size / 3) : size]

    return render(request, 'meal/categories.html', context_dict)

# This is the view for the page representing individual categories.
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        recipe = Recipe.objects.filter(category=category)

        size = len(recipe)
        context_dict['column1'] = recipe[0 : int(size / 3)]
        context_dict['column2'] = recipe[int(size / 3) : 2 * int(size / 3)]
        context_dict['column3'] = recipe[2 * int(size / 3) : size]

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
        
    return render(request, 'meal/recipe.html', context_dict)
	
# This is the view for representing the add recipe page.
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(data=request.POST)
        profile_form = RecipeImageForm(data=request.POST)

        if form.is_valid()and profile_form.is_valid():

            page = form.save(commit=False)
            page.set_ingredients(page.recipe_ingredients.replace('\r', '').split("\n"))
            page.views = 0
            page.save()

            profile = profile_form.save(commit=False)
            profile.recipe=page
            

            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.save()
            return HttpResponse('image upload success')

               
        else:
            print (form.errors,profile_form.errors)
    else:
        form = RecipeForm()
        profile_form = RecipeImageForm()

    context_dict = {'form':form,'profile_form':profile_form}
    return render(request, 'meal/add_recipe.html', context_dict)

# This is the view representing the about page.
def about(request):
	return render(request, 'meal/about.html', {})

# This is the view representing the base page.
def base(request):
	return render(request, 'meal/base.html', {})

# This is the view representing the trending page.
def trending(request):
    request.session.set_test_cookie()
    recipe_likes = Recipe.objects.order_by('-likes')[:2]
    recipe_views = Recipe.objects.order_by('-views')[:2]

    context_dict = {"recipe_likes" : recipe_likes, "recipe_views":recipe_views}
    
    response = render(request, 'meal/trending.html', context=context_dict)
    return response

# This is the view representing the index page.
def index(request):
	return render(request, 'meal/index.html', {})

# This is the view representing the user sign up page.
def signUp(request):
	return render(request, 'meal/signup.html', {})

# This is the view representing the register page for the home chefs.
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
    return HttpResponseRedirect(reverse('index'))

# This view allows the user to logout.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

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
	recipeResults = Recipe.objects.filter(recipe_name__icontains=query)
	categoryResults = Category.objects.filter(name__icontains=query)
	return render(request,"meal/search.html",{"query":query,"results":recipeResults, "catResults":categoryResults})
