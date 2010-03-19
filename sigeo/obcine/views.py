from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
# Import custom modules
from sigeo.obcine.models import Obcina

#@cache_page(60*15)
def polys(request, id):
    sec = 1.0/60/60
    obc = Obcina.objects.get(pk=int(id))
    all_poly = []
    poly = []
    for x,y in obc.the_geom.tuple[0][0]:
        # Now this is because the GRS in use in Slovenia is a bit off compared to WGS84 (GPS).
        # The numbers are approximate and the resulting location can be off up to 50 meters.
        # If you know the exact formula, WKT or proj4text, please help.
        poly.append('new GLatLng(%s, %s)' % (y-1*sec,x-17*sec))
    text = 'polyById[%s] = new GPolygon([%s], "#f33f00", 5, 1, "#ff0000", 0.2);' % (obc.ob_id, ','.join(poly))
    all_poly.append(text)
    all_poly.append('''polygon = polyById[%s]; map.addOverlay(polygon);''' % obc.ob_id)
    return HttpResponse('\n'.join(all_poly), mimetype='text/javascript')

def index(request):
    return render_to_response('obcina/index.html', {'obcine': Obcina.objects.all()})
