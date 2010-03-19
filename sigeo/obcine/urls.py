from django.conf.urls.defaults import *

urlpatterns = patterns('sigeo.obcine.views',
    url(r'^$', 'index', name='obcina_index'),
    url(r'^polys/(?P<id>\d+).js$', 'polys', name='obcina_polys'),
)

