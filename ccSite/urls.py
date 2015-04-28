from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ccSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)