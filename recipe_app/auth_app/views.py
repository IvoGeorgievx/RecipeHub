from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from recipe_app.auth_app.forms import SignUpForm, ProfileEditForm
from recipe_app.auth_app.models import UserProfile
from recipe_app.web.models import Recipes


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or self.get_default_redirect_url()


class UserLogOutView(auth_views.LogoutView):
    template_name = 'auth/logout.html'


class UserDetailsView(views.DetailView):
    template_name = 'auth/user-details.html'
    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.object.pk
        return context


class UserEditProfileView(views.UpdateView):
    template_name = 'auth/user-edit-profile.html'
    form_class = ProfileEditForm
    model = UserProfile
    success_url = reverse_lazy('index')


class UserRecipesView(views.ListView):
    template_name = 'auth/user-recipes.html'
    model = Recipes

    def get_queryset(self):
        return Recipes.objects.filter(created_by_id=self.request.user.pk).all()
