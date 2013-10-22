from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.dates import YearArchiveView, MonthArchiveView

from blogs.models import Post
        
        
class DetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/detail.html'
    
    
def listing(request):
    post_list = Post.objects.filter(is_active=True).order_by('pub_date').reverse()
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blogs/index.html', {"posts": posts})
    
    
class PostYearArchiveView(YearArchiveView):
    queryset = Post.objects.filter(is_active=True)
    date_field = "pub_date"
    make_object_list = True

 
class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.filter(is_active=True)
    date_field = "pub_date"
    make_object_list = True

    
    
    

