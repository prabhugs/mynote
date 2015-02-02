from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.template import RequestContext, loader

from notes.models import Post, Comment


# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-published_date')
    context = {'latest_post_list': latest_post_list}

    return render(request, "notes/index.html", context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'notes/detail.html', {'post': post})

def comments(request, post_id):
    response = "You are looking at the comments of %s"
    return HttpResponse(response % post_id)

def comment(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    try:
        selected_comment = p.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        return render(request, 'notes/detail.html', {'post': p, 'error_message': "Please select a comment"})
    else:
        selected_comment.comment_like += 1
        selected_comment.save()
        return HttpResponseRedirect(reverse('notes:results  ', args=(p.id,)))

def results(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'notes/results.html', {'post': post})