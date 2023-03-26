from django.contrib import admin

from recipe_app.web.models import Recipes


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    pass
