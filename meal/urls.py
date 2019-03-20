from django.conf.urls import url
from meal import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^registerChef/$', views.registerChef, name='registerChef'),
    url(r'^registerRegular/$', views.registerRegular, name='registerRegular'),
    url(r'^search/$', views.search, name='search'),
    url(r'^trending/$', views.trending, name = 'trending'),
    url(r'^base/$', views.base, name = 'base'),
    url(r'^signup/$', views.signUp, name = 'signup'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^add_recipe/$', views.add_recipe, name = 'add_recipe'),
    url(r'^categories/$', views.categories, name = 'categories'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<recipe_name_slug>[\w\-]+)/$', views.show_recipe, name='show_recipe'),
    url(r'^like/$', views.like_recipe, name='like_recipe'),
    url(r'^unlike/$', views.unlike_recipe, name='unlike_recipe'),
    url(r'^like_exists/$', views.like_exists, name='like_exists'),
]
