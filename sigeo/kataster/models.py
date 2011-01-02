# *-* coding: utf-8 *-*
from django.contrib.gis.db import models

class KatastrskaObcina(models.Model):
	gid = models.AutoField(primary_key=True)
	sifko = models.DecimalField(help_text="šifra katastrske občine", max_digits=20, decimal_places=0)
	imeko = models.CharField(help_text="ime katastrske občine", max_length=50)
	the_geom = models.MultiPolygonField()
	
	class Meta:
		ordering = ('imeko',)
	
	def __unicode__(self):
		return self.imeko
