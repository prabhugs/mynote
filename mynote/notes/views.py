from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
#from django.template import RequestContext, loader

from notes.models import Post, Comment


# Create your views here.

class IndexView(generic.ListView):
    template_name = "notes/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        """Return last 5 published posts"""
        return Post.objects.order_by('-published_date')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = "notes/detail.html"

class CommentsView(generic.DetailView):
    model = Post
    template_name = "notes/results.html"

class ResultsView(generic.DetailView):
    model = Post
    template_name = "notes/results.html"

def comment(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    try:
        #selected_comment = p.comment_set.get(pk=request.POST['comment'])
        selected_comment = request.POST['comment']
        print selected_comment
        print post_id
        print p
    except (KeyError, Comment.DoesNotExist):
        return render(request, 'notes/detail.html', {'post': p, 'error_message': "Please select a comment"})
    else:
        #selected_comment.comment_like += 1
        #selected_comment.save()
        return HttpResponseRedirect(reverse('notes:results', args=(p.id,)))
