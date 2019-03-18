from django.shortcuts import render
from django.template import RequestContext
from meal.models import Category, Recipe
from meal.forms import UserFormRegular,UserFormChef, UserProfileForm, RecipeForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse 
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission
from meal.webhose_search import run_query
from django.db.models import Q

from django.http import HttpResponse

def categories(request):
	return render(request, 'meal/categories.html', {})

# potential replacement for the categories view
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        recipe = Recipe.objects.filter(category=category)
        context_dict['recipes'] = recipe
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['recipes'] = None
        context_dict['category'] = None

    return render(request, 'meal/category.html', context_dict)

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
	
def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
                page = form.save(commit=False)
                page.set_ingredients(page.recipe_ingredients.replace('\r', '').split("\n"))
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print (form.errors)

    context_dict = {'form':form}
    return render(request, 'meal/add_recipe.html', context_dict)

def italian(request):
	return render(request, 'meal/italian.html', {})

def about(request):
	return render(request, 'meal/about.html', {})

def base(request):
	return render(request, 'meal/base.html', {})


def trending(request):
    request.session.set_test_cookie()
    recipe_likes = Recipe.objects.order_by('-likes')[:2]
    recipe_views = Recipe.objects.order_by('-views')[:2]

    context_dict = {"recipe_likes" : recipe_likes, "recipe_views":recipe_views}
    
    response = render(request, 'meal/trending.html', context=context_dict)
    return response

def index(request):
	return render(request, 'meal/index.html', {})

def search(request):
	return render(request, 'meal/search.html', {})
	
def register(request):
    return render(request, 'meal/register.html', {})

def signUp(request):
	return render(request, 'meal/signup.html', {})
	
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
            registered = True;
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserFormRegular()
        profile_form = UserProfileForm()

    context_dict = { 'user_form':user_form,
                     'profile_form':profile_form,
                     'registered':registered}

    return render(request, 'meal/registerRegular.html', context_dict)

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
            registered = True;
        else:
            print(user_formChef.errors,profile_form.errors)
    else:
        user_formChef = UserFormChef()
        profile_form = UserProfileForm()

    context_dict = { 'user_form':user_formChef,
                     'profile_form':profile_form,
                     'registered':registered}

    return render(request, 'meal/registerChef.html', context_dict)

def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your meal account is disabled')
        else:
            print('invalid login details {0}, {1}'.format(username,password))
            return HttpResponse("Invalid login details supplied")

    else:
        
        return render(request,'meal/login.html',{})
		
@permission_required('meal.read_chef',raise_exception=True)
def restricted(request):
    return render(request,'meal/restricted.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

#@login_required
#def like_recipe(request,category_name_slug,recipe_name_slug):
    #rec_id = None
    #category = Category.objects.get(slug = category_name_slug)
    #recipe1 = Recipe.objects.get(slug = recipe_name_slug)

    #if request.method == 'GET':
        #likes = 0
        #if recipe1:
       #    likes = recipe1.likes + 1
      #     recipe1.likes = likes
     #      recipe1.save()
    #return HttpResponse(likes)

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


def search(request):         
        query =  request.GET.get('q')
        results = Recipe.objects.filter(recipe_name__icontains=query)
        return render(request,"meal/search.html",{"query":query,
                                                  "results":results})



