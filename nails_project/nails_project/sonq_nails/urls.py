from django.urls import path

from nails_project.sonq_nails import views

urlpatterns = [
    path('', views.NailsListView.as_view(), name='list nails'),
    path('comment/<int:pk>/', views.NailsCommentView.as_view(), name='comment nails'),
    path('nail-details/<int:pk>/', views.NailsDetailsView.as_view(), name='nail details'),
    path('like/<int:pk>/', views.NailsLikeView.as_view(), name='like nail'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete')
]
