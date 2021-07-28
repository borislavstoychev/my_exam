from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import mixins as auth_mixins
# Create your views here.
from nails_project.common.forms import CommentForm
from nails_project.common.models import Comment
from nails_project.sonq_nails.forms import NailForm
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
        return redirect('nail details', self.kwargs['pk'])


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


class NailsLikeView(generic.View):

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


def persist(request, nails, template):
    if request.method == "GET":
        form = NailForm(instance=nails)
        return render(request, template, {'form': form})
    else:
        form = NailForm(request.POST, request.FILES, instance=nails)
        if form.is_valid():
            nails = form.save(commit=False)
            nails.user = request.user
            nails.save()
            return redirect('nail details', nails.pk)

        return render(request, template, {'form': form})


def create(request):
    nails = Nails()
    return persist(request, nails, 'nails/nails_create.html')


def edit(request, pk):
    nails = Nails.objects.get(pk=pk)
    return persist(request, nails, 'nails/nails_edit.html')


def delete(request, pk):
    nail = Nails.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'nails/nails_delete.html', {'pet': nail})
    else:
        nail.delete()
        return redirect('list nails')