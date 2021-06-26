from django.urls import path

from expenses_tracker2.expenses.views import index, create_expenses, edit_expenses, delete_expenses

urlpatterns = [
    path('', index, name='home page'),
    path('create/', create_expenses, name='create expense page'),
    path('edit/<int:pk>', edit_expenses, name='edit expense page'),
    path('delete/<int:pk>', delete_expenses, name='delete expense page'),

]