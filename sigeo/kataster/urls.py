from django.conf.urls.defaults import *

urlpatterns = patterns('sigeo.kataster.views',
    url(r'^$', 'index', name='katastrskaobcina_index'),
    url(r'^polys/(?P<id>\d+).js$', 'polys', name='katastrskaobcina_polys'),
    url(r'^reverse/$', 'reverse_kobcina', name='reverse_kobcina'),
)

