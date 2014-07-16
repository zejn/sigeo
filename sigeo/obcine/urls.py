from django.conf.urls import patterns, url, include

urlpatterns = patterns('sigeo.obcine.views',
    url(r'^$', 'index', name='obcina_index'),
    url(r'^polys/(?P<id>\d+).js$', 'polys', name='obcina_polys'),
    url(r'^reverse/$', 'reverse_obcina', name='reverse_obcina'),
)

