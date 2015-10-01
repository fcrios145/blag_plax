from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def hola(request):
    fecha_actual = datetime.datetime.now()
    html = "<html><body>La fecha actual es: %s.</body></html>" % fecha_actual
    return HttpResponse(html)

def adios(request):
    return render_to_response('hola_mundo.html', {'test': 'cualquier cosa'})