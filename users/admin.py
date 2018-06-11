from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm
from .models import User


class UserChangeForm(AuthUserChangeForm):
    name = forms.CharField()
    phone = forms.CharField()
    date_of_birth = forms.DateField()
    ip_address = forms.GenericIPAddressField()

    class Meta:
        model = User

        fields = (
            'username',
            'password',
            'name',
            'phone',
            'date_of_birth',
            'ip_address',
        )


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = UserChangeForm

    fieldsets = [
        (None, {'fields': ['username', 'password']}),
        ('Personal Data', {'fields': ['name', 'phone', 'date_of_birth', 'ip_address']}),
    ]

    list_display = ('username', 'name', 'phone', 'date_of_birth', 'ip_address')
