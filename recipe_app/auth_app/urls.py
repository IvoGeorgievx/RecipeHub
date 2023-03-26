from django.urls import path

from recipe_app.auth_app.views import SignUpView, UserLoginView, UserDetailsView, UserRecipesView, UserLogOutView, \
    UserEditProfileView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', UserLoginView.as_view(), name='sign in'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('user-details/<int:pk>', UserDetailsView.as_view(), name='user details'),
    path('user-recipes', UserRecipesView.as_view(), name='user recipes'),
    path('edit-profile/<int:pk>', UserEditProfileView.as_view(), name='edit profile'),
]
