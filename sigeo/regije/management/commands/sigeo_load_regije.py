# *-* coding: utf-8 *-*
from django.core.management.base import BaseCommand
from optparse import make_option
from django.db import transaction

class Command(BaseCommand):
	help = u"Naloži bazo in geopodatke statističnih regij"
	option_list = BaseCommand.option_list  + (
		make_option('--drop', dest='drop', action='store_true', default=False,
			help='drop table if exist before loading new data'),
		)
	
	@transaction.commit_on_success()
	def handle(self, *args, **options):
		from django.db import connection, transaction
		from sigeo.regije.models import Regija
		from sigeo.preprocessing import get_coordtransform
		import subprocess
		
		with transaction.commit_on_success():
			drop = bool(options.get('drop'))
			table_name = Regija._meta.db_table
			
			dump_file = args[0]
			shp2pgsql = '/usr/bin/shp2pgsql'
			cmd = [shp2pgsql, '-s', '3787', '-g', 'the_geom', '-W', 'WINDOWS-1250', dump_file, table_name]
			print ' '.join(cmd)
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
			for ob in Regija.objects.all():
				ob.the_geom.transform(trans)
				ob.save()
			cur.execute('''ALTER TABLE %s ADD CONSTRAINT enforce_srid_geom CHECK (st_srid(the_geom) = 4326);''' % table_name)
			cur.execute('''UPDATE geometry_columns SET srid=4326 WHERE f_table_name='%s' AND f_geometry_column = 'the_geom';''' % table_name)
			
			# check now is everything is ok
			from django.contrib.gis.geos import GEOSGeometry
			cs = Regija.objects.get(id='03')
			
			assert cs.ime.upper() == u'KOROŠKA'
			
			print 'Done.'

