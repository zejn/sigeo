from django.conf.urls import patterns, url, include

urlpatterns = patterns('sigeo.kataster.views',
    url(r'^$', 'index', name='katastrskaobcina_index'),
    url(r'^polys/(?P<id>\d+).js$', 'polys', name='katastrskaobcina_polys'),
    url(r'^reverse/$', 'reverse_kobcina', name='reverse_kobcina'),
)

