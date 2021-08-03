from django.contrib import admin

# Register your models here.


from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from nails_project.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class NailsUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'age', 'profile_image', 'user', 'is_complete')
    list_filter = ('first_name', 'user', 'phone_number')
    ordering = ('first_name',)

    def has_add_permission(self, request,):
        return False

    def has_change_permission(self, request, obj=None):
        return False


