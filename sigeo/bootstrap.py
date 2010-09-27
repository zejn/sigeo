
import datetime
import os
import re
import urllib
import lxml.html
import logging
from django.utils import _os

DATA_URL = 'http://e-prostor.gov.si/index.php?id=263&tx_simpltabs_pi1[tab]=561'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s\t %(name)s %(message)s')
log = logging.getLogger('bootstrap')

DATA_EXISTS = 'Not downloading, data already exists.'
NO_DATASET = 'Dataset not found!'


def _data_file(logger_name, filename):
	datadir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
	if not os.path.exists(datadir):
		os.mkdir(datadir)
	data_subdir = _os.safe_join(datadir, logger_name.rsplit('.', 1)[1])
	if not os.path.exists(data_subdir):
		os.mkdir(data_subdir)
	return _os.safe_join(data_subdir, filename)

def _read_url(url):
	log.info('Reading url %s' % url)
	u = urllib.urlopen(url)
	data = u.read()
	html = lxml.html.fromstring(data)
	html.make_links_absolute(url)
	return data, html

def _get_generic_multidownloader(logger_name, data_files, num_downloads):
	def _download_generic(url):
		log = logging.getLogger(logger_name)
		alldata = True
		for data_file in data_files:
			if not os.path.exists(_data_file(logger_name, data_file)):
				alldata = False
		if alldata:
			log.info(DATA_EXISTS)
			return
		data, html = _read_url(url)
		
		# save index file for local reference
		open(_data_file(logger_name, 'index.html'), 'w').write(data)
		
		m = re.search('stanje\s+podatkov:\s*([^><]+)', data, re.I)
		if m:
			log.info('stanje podatkov: %s' % m.groups())
		
		# checks here
		downloads = html.xpath('//a[@class="download"]')
		if len(downloads) != num_downloads:
			log.warn('Something changed - download count != %s at %s' % (num_downloads, url))
		
		shp = dict([(a.attrib['href'].rsplit('/', 1)[1].lower(), a.attrib['href']) for a in downloads])
		for f in data_files:
			if f not in shp:
				log.error(NO_DATASET + f)
				return
		for data_file, shp_url in shp.iteritems():
			if data_file in data_files:
				log.info('Downloading to %s' % _data_file(logger_name, data_file))
				urllib.urlretrieve(shp_url, _data_file(logger_name, data_file))
				log.info('Downloaded.')
	return _download_generic

pregledna_karta_files = ['zdr.zip', 'zdrl.zip', 'zdrbmr.zip', 'zdrm-s.zip', 'rs.zip', 'matematicni_elementi.zip', 'naselja_in_objekti.zip', 'komunikacije.zip', 'relief.zip', 'hidrografija.zip', 'pokritost_tal.zip', 'meje.zip', 'zemljepisna_imena.zip', 'sifranti_dpk.doc']

handlers = {
	u'Dr\u017eavna meja Republike Slovenije': _get_generic_multidownloader('bootstrap.drzavna_meja', ['slo_meja.zip'], 1),
	u'Dr\u017eavna pregledna karta v merilu 1 : 1 000 000': _get_generic_multidownloader('bootstrap.pregledna_karta', pregledna_karta_files, len(pregledna_karta_files)),
	u'Geodetske pisarne obmo\u010dnih geodetskih uprav': _get_generic_multidownloader('bootstrap.geodetske_pisarne', ['gp_-_geodetska_pisarna.zip', 'gp_-_geodetska_pisarna_c.txt'], 2),
	'Geolokacijske datoteke za DTK25 in DTK50 za novi koordinatni sistem': _get_generic_multidownloader('bootstrap.geolokacijske_dtk25_dtk50', ['dtk25_tfw.zip', 'dtk25_navodilo_za_uporabo_novih_geolokacijskih_datotek.doc', 'dtk50_tfw.zip', 'dtk50_navodilo_za_uporabo_novih_geolokacijskih_datotek.doc'], 4),
	'Geolokacijske datoteke za ortofote za novi koordinatni sistem': _get_generic_multidownloader('bootstrap.geolokacijske_za_ortofote', ['dof025_sdw.zip', 'dof025_tfw.zip', 'dof050_navodilo_za_uporabo_novih_geolokacijskih_datotek.doc', 'dof050_sdw.zip', 'dof050_tfw.zip', 'dof050_2009_sdw.zip', 'dof050_2009_tfw.zip', 'dof050_2009_navodilo_za_uporabo_novih_geolokacijskih_datotek.doc'], 9),
	u'Katastrske ob\u010dine': _get_generic_multidownloader('bootstrap.katastrske_obcine', ['ko_zk_slo.zip', 'ko_zk_slo.xls'], 2),
	u'Mre\u017ea listov DTK 25': _get_generic_multidownloader('bootstrap.listi_dtk25', ['dtk25.zip', 'mreza_dtk25_2_.tif'], 2),
	u'Mre\u017ea listov DTK 50': _get_generic_multidownloader('bootstrap.listi_dtk50', ['dtk50.zip', 'mreza_dtk50_1_.tif'], 2),
	u'Mre\u017ea listov TTN 5 in TTN 10': _get_generic_multidownloader('bootstrap.mreza_ttn5_ttn10', ['ttn5.zip', 'ttn10.zip', 'sekcije.zip', 'mreza_ttn5_ttn10_1_.tif'], 4),
	u'Mre\u017ee listov in sekcij v novem koordinatnem sistemu D96': _get_generic_multidownloader('bootstrap.listi_sekcije_d96', ['ttn5_d96.zip', 'sekcije5_d96.zip'], 6),
	u'Obmo\u010dne geodetske uprave': _get_generic_multidownloader('bootstrap.obmocne_geodetske_uprave', ['ogu.zip','ogu_c.txt'], 2),
	u'Ob\u010dine': _get_generic_multidownloader('bootstrap.obcine', ['ob.zip', 'ob_c.txt'], 2),
	'Upravne enote': _get_generic_multidownloader('bootstrap.upravne_enote',['ue.zip', 'ue_c.txt'], 2),
	u'\u0160ifrant naselij': _get_generic_multidownloader('bootstrap.naselja', ['na_s.txt'], 1),
	u'\u0160ifrant ulic': _get_generic_multidownloader('bootstrap.ulice', ['ul_s.txt'], 1),
}

def bootstrap_data():
	data = urllib.urlopen(DATA_URL).read()
	#open("localcache", 'wb').write(data)
	print '='*20
	#data = open("localcache").read()
	html = lxml.html.fromstring(data)
	html.make_links_absolute(DATA_URL)
	if len(html.xpath('//td[@class="maintext"]/ul/li/a')) != 15:
		logging.error('Something changed/new? %s elements on first page.' % len(html.xpath('//td[@class="maintext"]/ul/li/a')))
	for a in html.xpath('//td[@class="maintext"]/ul/li/a'):
		if handlers.get(a.text):
			handlers.get(a.text)(a.attrib['href'])
		else:
			print [a.attrib['href'], a.text]

bootstrap_data()
