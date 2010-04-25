# *-* coding: utf-8 *-*
from django.db import models
from sigeo.naselja.models import Naselje

class Ulica(models.Model):
	ul_mid = models.IntegerField(help_text="identifikator ulice", primary_key=True)
	ul_id = models.IntegerField(help_text="šifra ulice")
	ul_ime = models.CharField(help_text="ime ulice", max_length=30)
	ul_uime = models.CharField(help_text="uradno ime ulice", max_length=50)
	ul_dj = models.CharField(help_text="dvojezično ime ulice", max_length=50)
	d_od = models.DateField(help_text="datum veljavnosti")
	naselje = models.ForeignKey(Naselje)
	
	def __unicode__(self):
		return self.ul_uime

