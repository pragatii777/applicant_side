from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("username", "email", "usertype")
    list_filter = ("usertype",)
    fieldsets = (
        (None, {'fields': ("username", 'email', "usertype", 'password')}),
        # ('Personal info', {'fields': ('date_of_birth',)}),
        # ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("username", 'email', "usertype", 'password1', 'password2'),
        }),
    )
    search_fields = ("username", "email",)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
