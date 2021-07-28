
from django.urls import path

from nails_project.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]