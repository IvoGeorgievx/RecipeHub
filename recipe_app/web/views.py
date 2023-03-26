from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from recipe_app.auth_app.models import UserProfile
from recipe_app.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipe_app.web.models import Recipes


def index(request):
    return render(request, 'base.html')


class RecipeCreateView(LoginRequiredMixin, views.CreateView):
    template_name = 'web/create_recipe.html'
    form_class = CreateRecipeForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.created_by = UserProfile.objects.filter(user_id=self.request.user.id).get()
        return super().form_valid(form)


class RecipeEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'web/edit_recipe.html'
    form_class = EditRecipeForm
    model = Recipes
    success_url = reverse_lazy('index')


class DeleteRecipeView(LoginRequiredMixin, views.DeleteView):
    template_name = 'web/delete_recipe.html'
    form_class = DeleteRecipeForm
    model = Recipes
    success_url = reverse_lazy('index')


class RecipesView(views.ListView):
    template_name = 'web/recipe_list.html'
    model = Recipes

    def get_queryset(self):
        return Recipes.objects.all()


class SearchRecipeView(LoginRequiredMixin, views.ListView):
    template_name = 'web/search_form.html'
    model = Recipes

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Recipes.objects.filter(name__icontains=query)
        return Recipes.objects.none()



