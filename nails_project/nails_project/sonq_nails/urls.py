from django.urls import path

from nails_project.sonq_nails import views

urlpatterns = [
    path('', views.NailsListView.as_view(), name='list nails'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('comment/<int:pk>/', views.NailsCommentView.as_view(), name='comment nails'),
    path('details/<int:pk>/', views.NailsDetailsView.as_view(), name='nails details'),
    path('like/<int:pk>/', views.NailsLikeView.as_view(), name='like nails'),
    path('create/', views.NailsCreateView.as_view(), name='create nails'),
    path('edit/<int:pk>', views.NailsEditView.as_view(), name='edit nails'),
    path('delete/<int:pk>', views.NailsDeleteView.as_view(), name='delete nails'),
    path('comment-update/<int:pk>', views.CommentUpdateView.as_view(), name='update comment'),
    path('comment-delete/<int:pk>', views.CommentDeleteView.as_view(), name='delete comment'),
]
