from django.contrib import admin
from meal.models import Professional, Casual, UserProfile, Category, Recipe
from django.contrib.auth.admin import UserAdmin

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'category')

class CategoryAdmin(admin.ModelAdmin):
    populated_fields = {'slug': ('name', )}

admin.site.register(UserProfile)
admin.site.register(Professional, UserAdmin)
admin.site.register(Casual, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)

