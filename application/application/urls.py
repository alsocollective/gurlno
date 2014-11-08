from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()
from galleries.models import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'artgal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'galleries.views.home', name='home'),
    url(r'^expara/$','galleries.views.expara',name='expara'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    url(r'^galleries/$','galleries.views.gallerylist',name='gal_list'),
    url(r'^shows/$','galleries.views.showlist',name='show_list'),
    url(r'^gallery/(?P<slug>[-_\w]+)/$', ShowDetailView.as_view(),name="gallery-detail"),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
