# *-* coding: utf-8 *-*
from django.core.management.base import BaseCommand
from optparse import make_option
from django.db import transaction

class Command(BaseCommand):
    help = "Nalozi bazo in geopodatke obcin"
    option_list = BaseCommand.option_list  + (
        make_option('--drop', dest='drop', action='store_true', default=False,
            help='drop table if exist before loading new data'),
        )
    
    @transaction.commit_on_success()
    def handle(self, *args, **options):
        from django.db import connection
        from sigeo.obcine.models import Obcina
        from sigeo.preprocessing import get_coordtransform
        import subprocess
        
        drop = bool(options.get('drop'))
        table_name = Obcina._meta.db_table
        
        dump_file = args[0]
        shp2pgsql = '/usr/bin/shp2pgsql'
        cmd = [shp2pgsql, '-g', 'the_geom', '-s', '3787', '-W', 'WINDOWS-1250', dump_file, table_name]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        
        sql = p.stdout.read()
        p.wait()
        
        cur = connection.cursor()
        
        print 'Loading...'
        if drop:
            cur.execute('DROP TABLE %s' % table_name)
            connection.connection.commit()
        cur.execute(sql)
        
        # For some strange reason a new connection needs to be made.
        connection.connection.commit()
        connection.connection.close()
        connection.connection = None
        
        print 'Preprocessing...'
        
        cur = connection.cursor()
        
        trans = get_coordtransform()
        cur.execute('''ALTER TABLE %s DROP CONSTRAINT enforce_srid_the_geom;''' % table_name)
        for ob in Obcina.objects.all():
            ob.the_geom.transform(trans)
            ob.save()
        cur.execute('''ALTER TABLE %s ADD CONSTRAINT enforce_srid_the_geom CHECK (st_srid(the_geom) = 4326);''' % table_name)
        cur.execute('''UPDATE geometry_columns SET srid=4326 WHERE f_table_name='%s' AND f_geometry_column = 'the_geom';''' % table_name)
        
        # check now is everything is ok
        from django.contrib.gis.geos import GEOSGeometry
        c = Obcina.objects.get(ob_id=1)
        assert c.ob_ime.upper() == u'AJDOVŠČINA'
        expected = GEOSGeometry('POINT (13.9075089930651767 45.8993739353968309)')
        assert abs(c.the_geom.centroid.x - expected.x) < 0.0000001, (c.ob_ime.upper(), c.the_geom.centroid.x - expected.x)
        assert abs(c.the_geom.centroid.y - expected.y) < 0.0000001, (c.ob_ime.upper(), c.the_geom.centroid.y - expected.y)
        z = Obcina.objects.get(ob_id=23)
        assert z.ob_ime.upper() == u'DOMŽALE'
        expected = GEOSGeometry('POINT (14.6268742810941141 46.1450992072178892)')
        assert abs(z.the_geom.centroid.x - expected.x) < 0.0000001, (z.ob_ime.upper(), z.the_geom.centroid.x - expected.x)
        assert abs(z.the_geom.centroid.y - expected.y) < 0.0000001, (z.ob_ime.upper(), z.the_geom.centroid.y - expected.y)
        
        print 'Done.'

