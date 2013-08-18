from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext as _

from .models import User


class CustomUserChangeForm(UserChangeForm):
    faculty_number = forms.CharField(max_length=8)


class CustomUserCreationForm(UserCreationForm):
    faculty_number = forms.CharField(max_length=8)


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'faculty_number', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'faculty_number', 'password1', 'password2')}),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

admin.site.register(User, CustomUserAdmin)
