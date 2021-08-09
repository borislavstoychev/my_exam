from datetime import date
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from nails_project.common.forms import CommentForm, ScheduleForm
from nails_project.common.models import Schedule, Comment
from nails_project.sonq_nails.forms import NailsForm
from nails_project.sonq_nails.models import Nails, Like


class NailsListView(generic.ListView):
    model = Nails
    template_name = 'nails/nails_list.html'
    context_object_name = 'nails'


class NailsCommentView(auth_mixins.LoginRequiredMixin, generic.FormView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.nails = Nails.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('nails details', self.kwargs['pk'])


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

        return redirect('nails details', nails.id)

    def dispatch(self, request, *args, **kwargs):
        user_profile = self.request.user
        nails = Nails.objects.get(pk=kwargs['pk'])
        if nails.user_id == user_profile.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class NailsCreateView(auth_mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'nails/nails_create.html'
    model = Nails
    form_class = NailsForm

    def get_success_url(self):
        url = reverse_lazy('nails details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        nails = form.save(commit=False)
        nails.user = self.request.user
        nails.save()
        return super().form_valid(form)


class CommentUpdateView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    model = Comment
    context_object_name = 'comment'  # your own name for the list as a template variable
    form_class = CommentForm
    template_name = 'comment/update_comment.html'

    def get_success_url(self):
        url = reverse_lazy('nails details', kwargs={'pk': self.object.nails.id})
        return url


class CommentDeleteView(auth_mixins.LoginRequiredMixin, generic.DeleteView):
    model = Comment
    template_name = 'comment/delete_comment.html'

    def get_success_url(self):
        url = reverse_lazy('nails details', kwargs={'pk': self.object.nails.id})
        return url

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user_id != request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class NailsEditView(auth_mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'nails/nails_edit.html'
    model = Nails
    form_class = NailsForm

    def get_success_url(self):
        url = reverse_lazy('nails details', kwargs={'pk': self.object.id})
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

