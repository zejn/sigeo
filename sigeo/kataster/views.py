from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
# Import custom modules
from sigeo.kataster.models import KatastrskaObcina

def polys(request, id):
    obc = KatastrskaObcina.objects.get(sifko=int(id))
    poly = ['new GLatLng(%s, %s)' % (y, x) for x,y in obc.the_geom.tuple[0][0]]
    text = 'polyById[%s] = new GPolygon([%s], "#f33f00", 5, 1, "#ff0000", 0.2);' % (obc.sifko, ','.join(poly))
    all_poly = [text]
    all_poly.append('''polygon = polyById[%s]; map.addOverlay(polygon);''' % obc.sifko)
    return HttpResponse('\n'.join(all_poly), mimetype='text/javascript')

def index(request):
    return render_to_response('katastrskaobcina/index.html', {'obcine': KatastrskaObcina.objects.all()})
