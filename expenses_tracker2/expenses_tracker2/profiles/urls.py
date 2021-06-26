from django.urls import path

from expenses_tracker2.profiles.views import profile_home, edit_profile, delete_profile

urlpatterns = [
    path('profile/', profile_home, name='profile page'),
    path('profile/edit/<int:pk>', edit_profile, name='profile edit page'),
    path('profile/delete/<int:pk>', delete_profile, name='delete profile page'),

]