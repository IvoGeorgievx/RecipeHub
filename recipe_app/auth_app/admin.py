from django.contrib import admin

from recipe_app.auth_app.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
