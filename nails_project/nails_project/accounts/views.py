from django.contrib.auth import logout, login, get_user_model, authenticate
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth import mixins as auth_mixins
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from nails_project import settings
from nails_project.accounts.forms import SignUpForm, SignInForm, ProfileForm
from nails_project.accounts.models import Profile

UserModel = get_user_model()


class SignUpView(generic.CreateView):
    template_name = 'account/auth/sign_up.html'
    model = UserModel
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        user = authenticate(
            username=form.cleaned_data["email"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return redirect('home')


class SignInView(LoginView):
    template_name = 'account/auth/sign_in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home')


class SignOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class ProfileUpdateView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = Profile
    context_object_name = 'profile'  # your own name for the list as a template variable
    form_class = ProfileForm
    template_name = 'account/profiles/profile_details.html'

    def get_success_url(self):
        url = reverse_lazy('profile details', kwargs={'pk': self.request.user.id})
        return url

    # def dispatch(self, request, *args, **kwargs):
    #     user_profile = self.request.user
    #     profile = Profile.objects.get(pk=kwargs['pk'])
    #     if profile.user_id != user_profile.id:
    #         return self.handle_no_permission()
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the nails
        context['nails'] = self.get_object().user.nails_set.all()
        return context


class ProfileDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = UserModel
    template_name = 'account/profiles/profile_delete.html'
    success_url = reverse_lazy('sign up user')

    def dispatch(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile.id != request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)




