# *-* coding: utf-8 *-*
from django.db import models
from sigeo.obcine.models import Obcina

class Naselje(models.Model):
	na_mid = models.IntegerField(help_text="identifikator naselja", primary_key=True)
	na_id = models.IntegerField(help_text="šifra naselja")
	na_ime = models.CharField(help_text="ime naselja", max_length=30)
	na_uime = models.CharField(help_text="ime naselja uradno", max_length=50)
	na_dj = models.CharField(help_text="ime naselja dvojezično", max_length=50)
	d_od = models.DateField(help_text="datum veljavnosti")
	povrsina = models.DecimalField(max_digits=15, decimal_places=4)
	obcina = models.ForeignKey(Obcina)
	
	def __unicode__(self):
		return self.na_uime
