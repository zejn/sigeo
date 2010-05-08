from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
# Import custom modules
from sigeo.obcine.models import Obcina

#@cache_page(60*15)
def polys(request, id):
    obc = Obcina.objects.get(ob_id=int(id))
    poly = ['new GLatLng(%s, %s)' % (y, x) for x,y in obc.the_geom.tuple[0][0]]
    text = 'polyById[%s] = new GPolygon([%s], "#f33f00", 5, 1, "#ff0000", 0.2);' % (obc.ob_id, ','.join(poly))
    all_poly = [text]
    all_poly.append('''polygon = polyById[%s]; map.addOverlay(polygon);''' % obc.ob_id)
    return HttpResponse('\n'.join(all_poly), mimetype='text/javascript')

def index(request):
    return render_to_response('obcina/index.html', {'obcine': Obcina.objects.all()})
