from django.contrib import admin
from meal.models import Professional, Casual, UserProfile
from django.contrib.auth.admin import UserAdmin

admin.site.register(UserProfile)
admin.site.register(Professional,UserAdmin)
admin.site.register(Casual,UserAdmin)

