from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic


# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from nails_project import settings
from nails_project.accounts.forms import SignUpForm, SignInForm, ProfileForm
from nails_project.accounts.models import Profile
from nails_project.sonq_nails.models import Nails

UserModel = get_user_model()


class SignUpView(generic.CreateView):
    template_name = 'account/auth/sign_up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('home')


class SignInView(LoginView):
    template_name = 'account/auth/sign_in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home')


class SignOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class ProfileUpdateView(generic.UpdateView):
    model = Profile
    context_object_name = 'profile'  # your own name for the list as a template variable
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'account/profiles/profile_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['nails'] = Nails.objects.filter(user_id=self.request.user)
        return context




