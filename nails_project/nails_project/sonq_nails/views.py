from datetime import date
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from nails_project.common.forms import CommentForm, ScheduleForm
from nails_project.common.models import Schedule
from nails_project.sonq_nails.forms import NailForm
from nails_project.sonq_nails.models import Nails, Like


class NailsListView(generic.ListView):
    model = Nails
    template_name = 'nails/nails_list.html'
    context_object_name = 'nails'


class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'nails/schedule_view.html'
    context_object_name = 'schedules'
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedules = Schedule.objects.all().order_by('date', 'start_time')
        context["schedules"] = schedules
        today = date.today()
        current_month = self.months[today.month]
        context['current_month'] = current_month
        return context


class NailsCommentView(auth_mixins.LoginRequiredMixin, generic.FormView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.nails = Nails.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('nail details', self.kwargs['pk'])


class ScheduleCreateView(auth_mixins.LoginRequiredMixin, generic.FormView):
    form_class = ScheduleForm
    template_name = 'nails/schedule.html'

    def form_valid(self, form):
        schedule = form.save(commit=False)
        schedule.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedules = Schedule.objects.all().order_by('date')
        context['schedules'] = schedules
        return context

    def get_success_url(self):
        url = reverse_lazy('schedule nails')
        return url

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ScheduleDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = Schedule
    template_name = 'nails/schedule_delete.html'
    success_url = reverse_lazy('schedule nails')

    def dispatch(self, request, *args, **kwargs):
        schedule = self.get_object()
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class NailsDetailsView(generic.DetailView):
    model = Nails
    template_name = 'nails/nails_detail.html'
    context_object_name = 'nails'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nails = context[self.context_object_name]
        nails.likes_count = nails.like_set.count()
        context['comment_form'] = CommentForm()
        context['comments'] = nails.comment_set.all()
        context['is_owner'] = nails.user == self.request.user
        context['is_liked_by_user'] = nails.like_set.filter(user_id=self.request.user.id).exists()
        return context


class NailsLikeView(auth_mixins.LoginRequiredMixin, generic.View):

    def get(self, request, **kwargs):
        user_profile = self.request.user
        nails = Nails.objects.get(pk=kwargs['pk'])
        like = nails.like_set.filter(user_id=user_profile.id).first()
        if like:
            like.delete()
        else:
            like = Like(
                user=user_profile,
                nails=nails,
            )
            like.save()

        return redirect('nail details', nails.id)

    def dispatch(self, request, *args, **kwargs):
        user_profile = self.request.user
        nails = Nails.objects.get(pk=kwargs['pk'])
        if nails.user_id == user_profile.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class NailsCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'nails/nails_create.html'
    model = Nails
    form_class = NailForm

    def get_success_url(self):
        url = reverse_lazy('nail details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        nails = form.save(commit=False)
        nails.user = self.request.user
        nails.save()
        return super().form_valid(form)
        # return redirect('pet details or comment', pet.id)


class NailsEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'nails/nails_edit.html'
    model = Nails
    form_class = NailForm

    def get_success_url(self):
        url = reverse_lazy('nail details', kwargs={'pk': self.object.id})
        return url

    def dispatch(self, request, *args, **kwargs):
        nails = self.get_object()
        if nails.user_id != request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class NailsDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = Nails
    template_name = 'nails/nails_delete.html'
    success_url = reverse_lazy('list nails')

    def dispatch(self, request, *args, **kwargs):
        nails = self.get_object()
        if nails.user_id != request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

