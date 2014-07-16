from django.conf.urls import patterns, url, include

urlpatterns = patterns('sigeo.ue.views',
    url(r'^$', 'index', name='ue_index'),
    url(r'^polys/(?P<id>\d+).js$', 'polys', name='ue_polys'),
    url(r'^reverse/$', 'reverse', name='reverse_ue'),
)

