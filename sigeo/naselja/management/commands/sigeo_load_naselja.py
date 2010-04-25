import re
from django.core.management.base import BaseCommand

naselje_re = re.compile('(?P<ob_id>\d{3}).{30}.{50}.{50}(?P<na_mid>\d{8})(?P<na_id>\d{3})(?P<na_ime>.{30})(?P<na_uime>.{50})(?P<na_dj>.{50})(?P<d_od>\d\d\.\d\d\.\d{4} \d\d:\d\d:\d\d)(?P<povrsina>[\d.]{15})')

class Command(BaseCommand):
	help = "Nalozi bazo naselij iz tekstovne datoteke"
	
	def handle(self, *args, **options):
		from sigeo.obcine.models import Obcina
		from sigeo.naselja.models import Naselje
		from datetime import date
		import codecs
		
		f = codecs.open(args[0], 'r', encoding='windows-1250')
		
		for line in f:
			
			m = naselje_re.match(line)
			if not m:
				raise Exception("Neprepoznana vrstica!: %r" % line)
			
			data = dict([(k, v.strip()) for k, v in m.groupdict().iteritems()])
			
			# adjust date
			d_od = [int(i) for i in re.match('^(\d\d)\.(\d\d)\.(\d{4})' , data['d_od']).groups()]
			d_od.reverse()
			data['d_od'] = date(*d_od)
			data['obcina'] = Obcina.objects.get(ob_id=int(data['ob_id']))
			del data['ob_id']
			n = Naselje(**data)
			n.save()
