
from django.contrib.gis import admin
from sigeo.kataster.models import KatastrskaObcina

admin.site.register(KatastrskaObcina, admin.GeoModelAdmin)
