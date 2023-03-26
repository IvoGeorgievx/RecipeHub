from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User

from recipe_app.auth_app.models import UserProfile


class SignUpForm(auth_forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = UserProfile(user=user)
        if commit:
            profile.save()
        return user


class BaseUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class ProfileDetailsForm(BaseUserForm):
    pass


class ProfileEditForm(BaseUserForm):
    pass
