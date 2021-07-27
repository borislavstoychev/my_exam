from django.urls import path

from nails_project.sonq_nails import views

urlpatterns = [
    path('', views.index, name='home'),
    path('all-nails/', views.nails_all, name='list nails'),
    path('nail-details/<int:pk>/', views.nail_detail, name='nail details'),
    path('like/<int:pk>/', views.like_nail, name='like nail'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete')
]
