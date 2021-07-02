from django.urls import path

from nails_project.sonq_nails.views import index

urlpatterns = [
    path('', index, name='home'),
]