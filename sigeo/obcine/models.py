#from django.db import models
from django.contrib.gis.db import models

class Obcina(models.Model):
	ob_mid = models.DecimalField(max_digits=8, decimal_places=0)
	ob_id  = models.DecimalField(max_digits=3, decimal_places=0, primary_key=True)
	ob_ime  = models.CharField(max_length=30)
	ob_uime  = models.CharField(max_length=50)
	ob_dj  = models.CharField(max_length=50)
	ob_tip  = models.CharField(max_length=1)
	d_od_g  = models.DateField()
	ob_pov = models.DecimalField(max_digits=15, decimal_places=4)
	y_c = models.DecimalField(max_digits=6, decimal_places=0)
	x_c = models.DecimalField(max_digits=6, decimal_places=0)
	the_geom = models.MultiPolygonField()
	
	objects = models.GeoManager()
	
	class Meta:
		ordering = ('ob_uime',)
	
	def __unicode__(self):
		return u'%s' % self.ob_uime


