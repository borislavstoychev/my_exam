from django.urls import path

from nails_project.sonq_nails import views

urlpatterns = [
    path('', views.NailsListView.as_view(), name='list nails'),
    path('comment/<int:pk>/', views.NailsCommentView.as_view(), name='comment nails'),
    path('schedule-view/', views.ScheduleListView.as_view(), name='schedule view'),
    path('schedule/', views.ScheduleCreateView.as_view(), name='schedule nails'),
    path('schedule/delete/<int:pk>', views.ScheduleDeleteView.as_view(), name='delete schedule'),
    path('nail-details/<int:pk>/', views.NailsDetailsView.as_view(), name='nail details'),
    path('like/<int:pk>/', views.NailsLikeView.as_view(), name='like nail'),
    path('create/', views.NailsCreateView.as_view(), name='create'),
    path('edit/<int:pk>', views.NailsEditView.as_view(), name='edit'),
    path('delete/<int:pk>', views.NailsDeleteView.as_view(), name='delete')
]
