from django.urls import path

from recipe_app.web.views import index, RecipeCreateView, RecipeEditView, DeleteRecipeView, RecipesView, \
    SearchRecipeView

urlpatterns = [
    path('', index, name='index'),
    path('create-recipe', RecipeCreateView.as_view(), name='create recipe'),
    path('edit-recipe/<int:pk>', RecipeEditView.as_view(), name='edit recipe'),
    path('delete-recipe/<int:pk>', DeleteRecipeView.as_view(), name='delete recipe'),
    path('recipes/', RecipesView.as_view(), name='all recipes'),
    path('search-recipes/', SearchRecipeView.as_view(), name='search recipes'),
]
