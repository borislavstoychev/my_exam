from django.shortcuts import render, redirect
from django.views import generic
# Create your views here.
from nails_project.common.forms import CommentForm
from nails_project.common.models import Comment
from nails_project.sonq_nails.forms import NailForm
from nails_project.sonq_nails.models import Nails, Like


def index(request):
    return render(request, 'nails/index.html')


def nails_all(request):
    context = {
        'nails': Nails.objects.all(),
    }
    return render(request, "nails/nails_list.html", context)


class NailsCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'nails/nails_detail.html'
    fields = "__all__"


class NailsDetailsView(generic.detail.SingleObjectMixin, generic.ListView):
    model = Nails
    template_name = 'nails/nails_detail.html'
    object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Nails.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nail'] = self.object
        context['comment_form'] = CommentForm()
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        if form.is_valid():
            comment = Comment(comment=form.cleaned_data['comment'])
            comment.nail = self.object.nails
            comment.user = self.request.user
            comment.save()
            return redirect("nail details")

        return self.get_context_data()

def nail_detail(request, pk):
    nail = Nails.objects.get(pk=pk)
    nail.likes_count = nail.like_set.count()
    if request.method == "GET":
        context = {
            'nail': nail,
            'comment_form': CommentForm(),
        }
        return render(request, 'nails/nails_detail.html', context)
    else:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(comment=comment_form.cleaned_data['comment'])
            comment.nail = nail
            comment.user = request.user
            comment.save()
            return redirect("nail details", pk)

        context = {
            'nail': nail,
            'comment_form': CommentForm(),
        }
        return render(request, 'nails/nails_detail.html', context)


def like_nail(request, pk):
    nail = Nails.objects.get(pk=pk)
    like = Like(pet=nail)
    like.nail = nail
    like.user = request.user
    like.save()
    return redirect('nail details', pk)


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