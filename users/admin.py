from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm
from .models import User


class UserChangeForm(AuthUserChangeForm):
    pass


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = UserChangeForm
