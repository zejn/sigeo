from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
import simplejson
# Import custom modules
from sigeo.obcine.models import Obcina

#@cache_page(60*15)
def polys(request, id):
    obc = Obcina.objects.get(ob_id=int(id))

    polytext = []
    for polytuple in obc.the_geom.tuple:
        poly = ['new google.maps.LatLng(%s, %s)' % (y, x) for x,y in polytuple[0]]
        polytext.append('new google.maps.Polygon({map: map, fillColor: "#f33f00", fillOpacity: 0.2, paths: [%s], strokeWeight: 5, strokeOpacity: 1, strokeColor: "#ff0000"})' % (','.join(poly),))
    
    text = 'polyById[%s] = [%s];' % (obc.ob_id, ','.join(polytext))
    all_poly = [text]
    all_poly.append('''polygons = polyById[%s];''' % obc.ob_id)
    return HttpResponse('\n'.join(all_poly), mimetype='text/javascript')

def reverse_obcina(request):
    latlon = request.GET.get('ll', None)
    obcina_id = None
    if latlon:
        lat, lon = [float(i) for i in latlon.split(',')]
        try:
            obcina = Obcina.objects.get(the_geom__contains='POINT(%f %f)' % (lon, lat))
        except Obcina.DoesNotExist:
            pass
        else:
            obcina_id = obcina.ob_id
    return HttpResponse(simplejson.dumps({'status':'ok', 'obcina_id': obcina_id}))

def index(request):
    return render_to_response('obcina/index.html', {'obcine': Obcina.objects.all()})
