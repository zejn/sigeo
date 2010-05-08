
from django.core.management.base import BaseCommand
from optparse import make_option

class Command(BaseCommand):
	help = "Nalozi bazo in geopodatke obcin"
	option_list = BaseCommand.option_list  + (
		make_option('--drop', dest='drop', action='store_true', default=False,
			help='drop table if exist before loading new data'),
		)
	
	def handle(self, *args, **options):
		from django.db import connection
		from sigeo.obcine.models import Obcina
		from sigeo.preprocessing import get_coordtransform
		import subprocess
		
		drop = bool(options.get('drop'))
		table_name = Obcina._meta.db_table
		
		dump_file = args[0]
		shp2pgsql = '/usr/bin/shp2pgsql'
		cmd = [shp2pgsql, '-s', '3787', '-W', 'WINDOWS-1250', dump_file, table_name]
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
		connection.connection.commit()
		
		print 'Done.'

