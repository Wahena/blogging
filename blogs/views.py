from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from blogs.models import Blog, Comment


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_blog_list'
    
    def get_queryset(self):
        return Blog.objects.order_by('-pub_date')[:5]
        
        
class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blogs/detail.html'
    
    
class ResultsView(generic.DetailView):
    model = Blog
    template_name = 'blogs/results.html'


def likes(request, blog_id):
    p = get_object_or_404(Blog, pk=blog_id)
    try:
        selected_comment = p.comment_set.get(pk = request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        return render(request, 'blogs/detail.html',{
            'blog': p,
            'error_message': "you didn't select a comment.",
        })
    else:
        selected_comment.likes +=1
        selected_comment.save()
        return HttpResponseRedirect (reverse('blogs:results' , args = (p.id,)))      
