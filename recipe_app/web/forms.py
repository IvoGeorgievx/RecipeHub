from django import forms

from recipe_app.web.models import Recipes


class BaseRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
        exclude = ('id', 'created_by', 'updated_by', 'created_at')
        widgets = {
            'name': forms.TextInput(attrs={'id': 'recipe_name'}),
            'recipe_type': forms.Select(attrs={'id': "recipe_type"}),
            'description': forms.Textarea(attrs={'id': "recipe_description"})
        }


class CreateRecipeForm(BaseRecipeForm):
    pass


class EditRecipeForm(BaseRecipeForm):
    pass


class DeleteRecipeForm(BaseRecipeForm):
    class Meta:
        model = Recipes
        fields = ()

