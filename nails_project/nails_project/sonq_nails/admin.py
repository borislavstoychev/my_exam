from django.contrib import admin

# Register your models here.
from nails_project.sonq_nails.models import Nails


@admin.register(Nails)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('type', 'feedback', 'description', 'image', 'user')
    list_filter = ('type', 'feedback', 'user')
    ordering = ('type',)
