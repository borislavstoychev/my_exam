from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker2.expenses.models import Expense
from expenses_tracker2.profiles.forms import ProfileForm
from expenses_tracker2.profiles.models import Profile


def profile_home(request):
    profile = Profile.objects.first()
    return render(request, 'profile.html', {'profile': profile})


def persist(request, profile, template):
    if request.method == "GET":
        return render(request, template, {'form': ProfileForm(instance=profile), 'profile': profile})
    new_profile = ProfileForm(request.POST, instance=profile)
    if new_profile.is_valid():
        new_profile.save()
        return redirect('profile page')
    return render(request, template, {'form': new_profile})


def create_profile(request):
    profile = Profile()
    return persist(request, profile, 'home-no-profile.html')


def edit_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return persist(request, profile, 'profile-edit.html')


def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'profile-delete.html', {'profile': profile})
    profile.delete()
    Expense.objects.all().delete()
    return redirect('home page')
