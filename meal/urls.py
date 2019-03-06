from django.conf.urls import url
from meal import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^register/$', views.register, name='register'),
    url(r'^registerChef/$', views.registerChef, name='registerChef'),
    url(r'^registerRegular/$', views.registerRegular, name='registerRegular'),
    url(r'^search/$', views.search, name='search'),
	url(r'^trending/$', views.trending, name = 'trending'),
	url(r'^base/$', views.base, name = 'base'),
	url(r'^signup/$', views.signUp, name = 'signup'),
	url(r'^about/$', views.about, name = 'about'),
]
