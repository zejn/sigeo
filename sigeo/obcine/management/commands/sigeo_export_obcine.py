
from django.core.management.base import BaseCommand
from optparse import make_option

class Command(BaseCommand):
    help = "Izvozi bazo za v Google Fusion tables"
    option_list = BaseCommand.option_list
        
    def handle(self, *args, **options):
        from sigeo.obcine.models import Obcina
        import csv
        from django.contrib.gis.geos import GEOSGeometry
        from sigeo.preprocessing import get_coordtransform
        import StringIO

        s = StringIO.StringIO()
        w = csv.writer(s)
        trans = get_coordtransform()
        w.writerow(['id', 'ime', 'uime', 'tip', 'povrsina', 'center', 'geometrija'])

        for ob in Obcina.objects.all():
            center_pt = 'SRID=3787;POINT(%d %d)' % (ob.y_c, ob.x_c)
            pt = GEOSGeometry(center_pt)
            pt.transform(trans)

            row = [
                ob.ob_id,
                ob.ob_ime,
                ob.ob_uime,
                ob.ob_tip,
                ob.ob_pov,
                pt.kml,
                ob.the_geom.kml,
            ]
            w.writerow([unicode(i).encode('utf-8') for i in row])

        print s.getvalue()