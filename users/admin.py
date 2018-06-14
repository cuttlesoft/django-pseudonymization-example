from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm
from .models import User


class UserChangeForm(AuthUserChangeForm):
    name = forms.CharField(max_length=128)
    phone = forms.CharField(max_length=16)
    date_of_birth = forms.DateField()
    ip_address = forms.GenericIPAddressField()

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget = admin.widgets.AdminDateWidget()

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

    list_display = ('username', 'name', 'phone', 'date_of_birth', 'ip_address')

    fieldsets = [
        (None, {'fields': ['username', 'password']}),
        ('Personal Data', {'fields': ['name', 'phone', 'date_of_birth', 'ip_address']}),
    ]
