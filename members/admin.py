from django import forms
from django.contrib import admin
from .models import Member
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm #  ReadOnlyPasswordHashField


class MemberCreationAdminForm(forms.ModelForm):

    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification.")

    class Meta:
        model = Member


class MemberChangeAdminForm(UserChangeForm):

    class Meta:
        model = Member

# class MemberCreationAdminForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation',
#                                 widget=forms.PasswordInput)

#     class Meta:
#         model = Member

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         user = super(MemberCreationAdminForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class MemberChangeAdminForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = Member

#     def clean_password(self):
#         return self.initial["password"]



class MemberAdmin(UserAdmin):

    form = MemberChangeAdminForm
    add_form = MemberCreationAdminForm

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'faculty_number')
        }),
        ('Extra Options', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions')
        }),
    )

    change_password_form = AdminPasswordChangeForm

    list_display = ('username', 'faculty_number', 'attended_meetings')
    search_fields = ('username', 'faculty_number')
    ordering = ('username',)


admin.site.register(Member, MemberAdmin)
