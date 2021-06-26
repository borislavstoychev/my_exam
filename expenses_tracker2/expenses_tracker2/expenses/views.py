from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker2.expenses.forms import ExpenseForm
from expenses_tracker2.expenses.models import Expense
from expenses_tracker2.profiles.models import Profile
from expenses_tracker2.profiles.views import create_profile


def money_left(prof, exp):
    total_exp = sum(e.price for e in exp)
    return prof.budget - total_exp


def index(request):
    if Profile.objects.exists():
        expenses = Expense.objects.all()
        profile = Profile.objects.first()
        profile.money_left = money_left(profile, expenses)
        return render(request, 'home-with-profile.html', {'expenses': expenses, 'profile': profile})
    return create_profile(request)


def persist(request, expense, template):
    if request.method == "GET":
        content = {
            'profile': Profile.objects.first(),
            'expense': ExpenseForm(instance=expense)
        }
        return render(request, template, content)
    new_expense = ExpenseForm(request.POST, instance=expense)
    if new_expense.is_valid():
        new_expense.save()
        return redirect('home page')
    return render(request, template, {'expense': new_expense})


def create_expenses(request):
    expense = Expense()
    return persist(request, expense, 'expense-create.html')


def edit_expenses(request, pk):
    expense = Expense. objects.get(pk=pk)
    return persist(request, expense, 'expense-edit.html')


def delete_expenses(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "GET":
        form = ExpenseForm(instance=expense)
        for _, field in form.fields.items():
            field.widget.attrs['disabled'] = True
        return render(request, 'expense-delete.html', {'form': form})
    expense.delete()
    return redirect('home page')
