from django.contrib.gis.db import models

class UpravnaEnota(models.Model):
	gid = models.AutoField(primary_key=True)
	ue_mid = models.DecimalField(max_digits=11, decimal_places=0)
	ue_id = models.IntegerField()
	ue_ime = models.CharField(max_length=30)
	ue_uime = models.CharField(max_length=50)
	d_od_g = models.DateField()
	ue_pov = models.FloatField()
	y_c = models.DecimalField(max_digits=11, decimal_places=0)
	x_c = models.DecimalField(max_digits=11, decimal_places=0)
	the_geom = models.MultiPolygonField()
	
	objects = models.GeoManager()
	
	class Meta:
		ordering = ('ue_uime',)
	
	def __unicode__(self):
		return u'%s' % self.ue_uime
