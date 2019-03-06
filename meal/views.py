from django.shortcuts import render
from meal.forms import UserFormRegular,UserFormChef, UserProfileForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse 
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission

from django.http import HttpResponse

def categories(request):
	return render(request, 'meal/categories.html', {})
	
def addRecipe(request):
	return render(request, 'meal/add_recipe.html', {})

def italian(request):
	return render(request, 'meal/italian.html', {})

def about(request):
	return render(request, 'meal/about.html', {})

def base(request):
	return render(request, 'meal/base.html', {})


def trending(request):
	return render(request, 'meal/trending.html', {})

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

