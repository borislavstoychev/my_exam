from django.urls import path

from nails_project.sonq_nails.views import index, like_nail, nail_all, nail_detail, create, edit, delete

urlpatterns = [
    path('', index, name='home'),
    path('all-nails/', nail_all, name='list nails'),
    path('nail-details/<int:pk>/', nail_detail, name='nail details'),
    path('like/<int:pk>/', like_nail, name='like nail'),
    path('create/', create, name='create'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete')
]
