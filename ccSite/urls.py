from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from home.views import NewsListView, NewsDetailView
from home.views import VacancyListView, VacancyDetailView
from home.views import AnnouncementsListView, AnnouncementsDetailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'news/$', NewsListView.as_view(), name='newsList'),
    url(r'news/(?P<slug>[-_\w]+)/$', NewsDetailView.as_view(), name='vacanDetails'),
    url(r'vacancies/$', VacancyListView.as_view(), name='newsList'),
    url(r'vacancies/(?P<slug>[-_\w]+)/$',VacancyDetailView.as_view(), name='vacanDetails'),
    url(r'announce/$', AnnouncementsListView.as_view(), name='announceList'),
    url(r'announce/(?P<slug>[-_\w]+)/$', AnnouncementsDetailView.as_view(), name='announceDetails'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
