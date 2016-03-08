from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
import datetime

def hola(request):
    fecha_actual = datetime.datetime.now()
    html = "<html><body>La fecha actual es: %s.</body></html>" % fecha_actual
    return HttpResponse(html)

def adios(request):
    return render_to_response('hola_mundo.html', {'test': 'kjsdsjksdjfkcualquier cosa'})

class Index(TemplateView):
    template_name = 'index.html'

class Prueba(TemplateView):
    template_name = 'prueba.html'

class Resume(TemplateView):
    template_name = 'resume.html'

class Login(TemplateView):
    template_name = 'login.html'
    def post(self, request):
        print request.POST.get('username')
