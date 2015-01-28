from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
#from django.template import RequestContext, loader

from notes.models import Post


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