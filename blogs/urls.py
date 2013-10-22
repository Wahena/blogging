from django.conf.urls import patterns, url
from blogs.views import PostYearArchiveView

from blogs import views

urlpatterns = patterns('',
    url(r'^$', 'blogs.views.listing', name = 'index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'^archive/(?P<year>\d{4})/$',views.PostYearArchiveView.as_view(), name = 'post_year_archive'),
)
