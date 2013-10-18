from django.conf.urls import patterns, url

from blogs import views

urlpatterns = patterns('',
    url(r'^$', 'blogs.views.listing', name = 'index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name = 'detail'),
)
