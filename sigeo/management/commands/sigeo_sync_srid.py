
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = "Alters the Geo database in order to store data in SRID 4326, the one which all web apps use"
	
	def handle(self, *args, **options):
		from sigeo.obcine.models import Obcina
		from django.db import connection
		
		cur = connection.cursor()
		table = Obcina._meta.db_table
		cur.execute('''ALTER TABLE %s DROP CONSTRAINT enforce_srid_the_geom;''' % table)
		
		for ob in Obcina.objects.all():
			ob.the_geom.transform(4326)
			ob.save()
		
		cur.execute('''ALTER TABLE %s ADD CONSTRAINT enforce_srid_the_geom CHECK (st_srid(the_geom) = 4326);''' % table)
