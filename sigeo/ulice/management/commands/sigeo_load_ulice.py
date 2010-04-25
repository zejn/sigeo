import re
from django.core.management.base import BaseCommand

ulica_re = re.compile('\d{8}(?P<ob_id>\d{3}).{30}.{50}.{50}(?P<na_mid>\d{8})\d{3}.{30}.{50}.{50}(?P<ul_mid>\d{8})(?P<ul_id>\d{4})(?P<ul_ime>.{30})(?P<ul_uime>.{50})(?P<ul_dj>.{50})(?P<d_od>\d\d\.\d\d\.\d{4} \d\d:\d\d:\d\d)')

class Command(BaseCommand):
	help = "Nalozi bazo naselij iz tekstovne datoteke"
	
	def handle(self, *args, **options):
		from sigeo.naselja.models import Naselje
		from sigeo.ulice.models import Ulica
		from datetime import date
		import codecs
		
		f = codecs.open(args[0], 'r', encoding='windows-1250')
		
		for line in f:
			
			m = ulica_re.match(line)
			if not m:
				raise Exception("Neprepoznana vrstica!: %r" % line)
			
			data = dict([(k, v.strip()) for k, v in m.groupdict().iteritems()])
			
			# adjust date
			d_od = [int(i) for i in re.match('^(\d\d)\.(\d\d)\.(\d{4})' , data['d_od']).groups()]
			d_od.reverse()
			data['d_od'] = date(*d_od)
			naselje = Naselje.objects.get(na_mid=int(data['na_mid']))
			assert naselje.obcina.ob_id == int(data['ob_id'])
			data['naselje'] = naselje
			del data['ob_id']
			del data['na_mid']
			u = Ulica(**data)
			u.save()
