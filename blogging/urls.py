from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogging.views.home', name='home'),
    url(r'^blogs/', include('blogs.urls' , namespace="blogs")),
    url(r'^archive/', include('blogs.urls' , namespace="archive")),
    url(r'^archive2/', include('blogs.urls' , namespace="archive2")),
    url(r'^Images/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
