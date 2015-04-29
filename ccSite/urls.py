from django.conf.urls import patterns, include, url
from home import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ccSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)