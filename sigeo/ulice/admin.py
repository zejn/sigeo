from django.contrib import admin
from sigeo.ulice.models import Ulica

admin.site.register(Ulica, admin.ModelAdmin)
