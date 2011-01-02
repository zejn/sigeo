from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
import simplejson
# Import custom modules
from sigeo.ue.models import UpravnaEnota


#@cache_page(60*15)
def polys(request, id):
    obc = UpravnaEnota.objects.get(ue_id=int(id))

    polytext = []
    for polytuple in obc.the_geom.tuple:
        poly = ['new google.maps.LatLng(%s, %s)' % (y, x) for x,y in polytuple[0]]
        polytext.append('new google.maps.Polygon({map: map, fillColor: "#f33f00", fillOpacity: 0.2, paths: [%s], strokeWeight: 5, strokeOpacity: 1, strokeColor: "#ff0000"})' % (','.join(poly),))
    
    text = 'polyById[%s] = [%s];' % (obc.ue_id, ','.join(polytext))
    all_poly = [text]
    all_poly.append('''polygons = polyById[%s];''' % obc.ue_id)
    return HttpResponse('\n'.join(all_poly), mimetype='text/javascript')

def reverse(request):
    latlon = request.GET.get('ll', None)
    obcina_id = None
    if latlon:
        lat, lon = [float(i) for i in latlon.split(',')]
        try:
            obcina = UpravnaEnota.objects.get(the_geom__contains='POINT(%f %f)' % (lon, lat))
        except UpravnaEnota.DoesNotExist:
            pass
        else:
            obcina_id = obcina.ue_id
    return HttpResponse(simplejson.dumps({'status':'ok', 'obcina_id': obcina_id}))

def index(request):
    return render_to_response('ue/index.html', {'obcine': UpravnaEnota.objects.all()})
