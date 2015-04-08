from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from home.models import Book
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    site_header = "Secure Witness Interface for Admins"
    list_display = ('title', 'author')
    search_fields = ['title', 'author', 'isbn']

class UserAdminAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                ("This account is inactive."),
                code='inactive',
            )

class UserAdmin(AdminSite):
    login_form = UserAdminAuthenticationForm
    site_header = "Secure Witness Interface for Readers and Bookers"
    def has_permission(self, request):
        # Removed check for is_staff
        return request.user.is_active

    
user_admin_site = UserAdmin(name='useradmin')

admin.site.register(Book, BookAdmin)