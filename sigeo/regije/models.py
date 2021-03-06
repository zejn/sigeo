# coding: utf-8

from django.contrib.gis.db import models

class Regija(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    ime = models.CharField(max_length=21)
    preb_s = models.DecimalField(max_digits=19, decimal_places=0)
    preb_m = models.DecimalField(max_digits=19, decimal_places=0)
    preb_z = models.DecimalField(max_digits=19, decimal_places=0)
    s_14 = models.DecimalField(max_digits=19, decimal_places=0)
    m_14 = models.DecimalField(max_digits=19, decimal_places=0)
    z_14 = models.DecimalField(max_digits=19, decimal_places=0)
    s_15_64 = models.DecimalField(max_digits=19, decimal_places=0)
    m_15_64 = models.DecimalField(max_digits=19, decimal_places=0)
    z_15_64 = models.DecimalField(max_digits=19, decimal_places=0)
    s_65 = models.DecimalField(max_digits=19, decimal_places=0)
    m_65 = models.DecimalField(max_digits=19, decimal_places=0)
    z_65 = models.DecimalField(max_digits=19, decimal_places=0)
    del_s_14 = models.DecimalField(max_digits=19, decimal_places=1)
    del_m_14 = models.DecimalField(max_digits=19, decimal_places=1)
    del_z_14 = models.DecimalField(max_digits=19, decimal_places=1)
    del_s15_64 = models.DecimalField(max_digits=19, decimal_places=1)
    del_m15_64 = models.DecimalField(max_digits=19, decimal_places=1)
    del_z15_64 = models.DecimalField(max_digits=19, decimal_places=1)
    del_s_65 = models.DecimalField(max_digits=19, decimal_places=1)
    del_m_65 = models.DecimalField(max_digits=19, decimal_places=1)
    del_z_65 = models.DecimalField(max_digits=19, decimal_places=1)
    ind_fem = models.DecimalField(max_digits=19, decimal_places=1)
    star_s = models.DecimalField(max_digits=19, decimal_places=1)
    star_m = models.DecimalField(max_digits=19, decimal_places=1)
    star_z = models.DecimalField(max_digits=19, decimal_places=1)
    ind_star_s = models.DecimalField(max_digits=19, decimal_places=1)
    ind_star_m = models.DecimalField(max_digits=19, decimal_places=1)
    ind_star_z = models.DecimalField(max_digits=19, decimal_places=1)
    gost_preb = models.DecimalField(max_digits=19, decimal_places=1)
    del_tujci = models.DecimalField(max_digits=19, decimal_places=1)
    del_exyu = models.DecimalField(max_digits=19, decimal_places=1)
    del_eu = models.DecimalField(max_digits=19, decimal_places=1)
    del_ostalo = models.DecimalField(max_digits=19, decimal_places=1)
    s0_4 = models.DecimalField(max_digits=19, decimal_places=0)
    m_0_4 = models.DecimalField(max_digits=19, decimal_places=0)
    z_0_4 = models.DecimalField(max_digits=19, decimal_places=0)
    s5_9 = models.DecimalField(max_digits=19, decimal_places=0)
    m_5_9 = models.DecimalField(max_digits=19, decimal_places=0)
    z_5_9 = models.DecimalField(max_digits=19, decimal_places=0)
    s10_14 = models.DecimalField(max_digits=19, decimal_places=0)
    m_10_14 = models.DecimalField(max_digits=19, decimal_places=0)
    z_10_14 = models.DecimalField(max_digits=19, decimal_places=0)
    s15_19 = models.DecimalField(max_digits=19, decimal_places=0)
    m_15_19 = models.DecimalField(max_digits=19, decimal_places=0)
    z_15_19 = models.DecimalField(max_digits=19, decimal_places=0)
    s20_24 = models.DecimalField(max_digits=19, decimal_places=0)
    m_20_24 = models.DecimalField(max_digits=19, decimal_places=0)
    z_20_24 = models.DecimalField(max_digits=19, decimal_places=0)
    s25_29 = models.DecimalField(max_digits=19, decimal_places=0)
    m_25_29 = models.DecimalField(max_digits=19, decimal_places=0)
    z_25_29 = models.DecimalField(max_digits=19, decimal_places=0)
    s30_34 = models.DecimalField(max_digits=19, decimal_places=0)
    m_30_34 = models.DecimalField(max_digits=19, decimal_places=0)
    z_30_34 = models.DecimalField(max_digits=19, decimal_places=0)
    s35_39 = models.DecimalField(max_digits=19, decimal_places=0)
    m_35_39 = models.DecimalField(max_digits=19, decimal_places=0)
    z_35_39 = models.DecimalField(max_digits=19, decimal_places=0)
    s40_44 = models.DecimalField(max_digits=19, decimal_places=0)
    m_40_44 = models.DecimalField(max_digits=19, decimal_places=0)
    z_40_44 = models.DecimalField(max_digits=19, decimal_places=0)
    s45_49 = models.DecimalField(max_digits=19, decimal_places=0)
    m_45_49 = models.DecimalField(max_digits=19, decimal_places=0)
    z_45_49 = models.DecimalField(max_digits=19, decimal_places=0)
    s50_54 = models.DecimalField(max_digits=19, decimal_places=0)
    m_50_54 = models.DecimalField(max_digits=19, decimal_places=0)
    z_50_54 = models.DecimalField(max_digits=19, decimal_places=0)
    s55_59 = models.DecimalField(max_digits=19, decimal_places=0)
    m_55_59 = models.DecimalField(max_digits=19, decimal_places=0)
    z_55_59 = models.DecimalField(max_digits=19, decimal_places=0)
    s60_64 = models.DecimalField(max_digits=19, decimal_places=0)
    m_60_64 = models.DecimalField(max_digits=19, decimal_places=0)
    z_60_64 = models.DecimalField(max_digits=19, decimal_places=0)
    s65_69 = models.DecimalField(max_digits=19, decimal_places=0)
    m_65_69 = models.DecimalField(max_digits=19, decimal_places=0)
    z_65_69 = models.DecimalField(max_digits=19, decimal_places=0)
    s70_74 = models.DecimalField(max_digits=19, decimal_places=0)
    m_70_74 = models.DecimalField(max_digits=19, decimal_places=0)
    z_70_74 = models.DecimalField(max_digits=19, decimal_places=0)
    s75_79 = models.DecimalField(max_digits=19, decimal_places=0)
    m_75_79 = models.DecimalField(max_digits=19, decimal_places=0)
    z_75_79 = models.DecimalField(max_digits=19, decimal_places=0)
    s80_84 = models.DecimalField(max_digits=19, decimal_places=0)
    m_80_84 = models.DecimalField(max_digits=19, decimal_places=0)
    z_80_84 = models.DecimalField(max_digits=19, decimal_places=0)
    s85_89 = models.DecimalField(max_digits=19, decimal_places=0)
    m_85_89 = models.DecimalField(max_digits=19, decimal_places=0)
    z_85_89 = models.DecimalField(max_digits=19, decimal_places=0)
    s90_94 = models.DecimalField(max_digits=19, decimal_places=0)
    m_90_94 = models.DecimalField(max_digits=19, decimal_places=0)
    z_90_99 = models.DecimalField(max_digits=19, decimal_places=0)
    s95_99 = models.DecimalField(max_digits=19, decimal_places=0)
    m_95_99 = models.DecimalField(max_digits=19, decimal_places=0)
    z_95_99 = models.DecimalField(max_digits=19, decimal_places=0)
    s100 = models.DecimalField(max_digits=19, decimal_places=0)
    m_100 = models.DecimalField(max_digits=19, decimal_places=0)
    z_100 = models.DecimalField(max_digits=19, decimal_places=0)
    the_geom = models.MultiPolygonField()

    objects = models.GeoManager()
    
    class Meta:
        ordering = ('ime',)
    
    def __unicode__(self):
        return u'%s' % self.ime

