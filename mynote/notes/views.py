from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from notes.models import Post


# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-published_date')
    template = loader.get_template("notes/index.html")
    context = RequestContext(request, {'latest_post_list': latest_post_list})

    return HttpResponse(template.render(context))

def detail(request, post_id):
    return HttpResponse("You are looking at post %s" %post_id)

def comments(request, post_id):
    response = "You are looking at the comments of %s"
    return HttpResponse(response % post_id)