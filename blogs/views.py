from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from blogs.models import Post #,Image


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_post_list'
    
    def get_queryset(self):
        return Post.objects.filter(is_active=True).order_by('-pub_date')[:5]
        
        
class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail.html'
    
    

