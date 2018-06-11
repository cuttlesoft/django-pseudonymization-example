from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm
from .models import User


class UserChangeForm(AuthUserChangeForm):
    pass


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = UserChangeForm

    list_display = ('username', 'name', 'phone', 'date_of_birth', 'ip_address')
