from django.contrib import admin

# Register your models here.
from nails_project.common.models import Schedule, Comment


@admin.register(Schedule)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time')
    list_filter = ('date', )
    ordering = ('date',)


@admin.register(Comment)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nails', 'comment', 'user')
    list_filter = ('nails', 'user' )
    ordering = ('user',)
