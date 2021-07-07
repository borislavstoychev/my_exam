from django.shortcuts import render, redirect

# Create your views here.
from nails_project.common.forms import CommentForm
from nails_project.common.models import Comment
from nails_project.sonq_nails.forms import NailForm
from nails_project.sonq_nails.models import Nail, Like


def index(request):
    return render(request, 'index.html')


def nail_all(request):
    context = {
        'nails': Nail.objects.all(),
    }
    return render(request, "nails_list.html", context)


def nail_detail(request, pk):
    nail = Nail.objects.get(pk=pk)
    nail.likes_count = nail.like_set.count()
    if request.method == "GET":
        context = {
            'nail': nail,
            'comment_form': CommentForm(),
        }
        return render(request, 'nails_detail.html', context)
    else:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(comment=comment_form.cleaned_data['comment'])
            comment.nail = nail
            comment.save()
            return redirect("nail details", pk)

        context = {
            'nail': nail,
            'comment_form': CommentForm(),
        }
        return render(request, 'nails_detail.html', context)


def like_nail(request, pk):
    nail = Nail.objects.get(pk=pk)
    like = Like(pet=nail)
    like.nail = nail
    like.save()
    return redirect('nail details', pk)


def persist(request, nail, template):
    if request.method == "GET":
        form = NailForm(instance=nail)
        return render(request, template, {'form': form})
    else:
        form = NailForm(request.POST, request.FILES, instance=nail)
        if form.is_valid():
            form.save()
            return redirect('nail details', nail.pk)

        return render(request, template, {'form': form})


def create(request):
    nail = Nail()
    return persist(request, nail, 'nails_create.html')


def edit(request, pk):
    nail = Nail.objects.get(pk=pk)
    return persist(request, nail, 'nails_edit.html')


def delete(request, pk):
    nail = Nail.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, 'nails_delete.html', {'pet': nail})
    else:
        nail.delete()
        return redirect('list nails')