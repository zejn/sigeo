
#from django.contrib import admin
from django.contrib.gis import admin
from sigeo.obcine.models import Obcina

admin.site.register(Obcina, admin.GeoModelAdmin)

