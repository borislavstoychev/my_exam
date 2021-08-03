
from django.urls import path

from nails_project.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('schedule-view/', views.ScheduleListView.as_view(), name='schedule view'),
    path('schedule/', views.ScheduleCreateView.as_view(), name='schedule nails'),
    path('schedule/delete/<int:pk>', views.ScheduleDeleteView.as_view(), name='delete schedule'),

]