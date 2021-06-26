from django import forms

from expenses_tracker2.expenses.models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = '__all__'


