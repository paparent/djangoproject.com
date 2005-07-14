from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^weblog/', include('django_website.apps.blog.urls.blog')),
    (r'^documentation/', include('django_website.apps.docs.urls.docs')),
    (r'', include('django.conf.urls.flatfiles')),
)