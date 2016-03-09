from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponseRedirect

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
import datetime

def hola(request):
    fecha_actual = datetime.datetime.now()
    html = "<html><body>La fecha actual e kjaskjaskkjsdfkjsdfkjsdkjfkjjs: %s.</body></html>" % fecha_actual
    return HttpResponse(html)

def adios(request):
    return render_to_response('hola_mundo.html', {'test': 'kjsdsjksdjfkcualquier cosa'})

class Index(TemplateView):
    template_name = 'index.html'

class Prueba(TemplateView):
    template_name = 'prueba.html'

class Resume(TemplateView):
    template_name = 'resume.html'

class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        print 'form'
        print form.get_user()
        # login(self.request, )
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        print 'valiste verga'
        print 'valiste verga verga jajajaj pinche puto ojet asfjdfkjdfse'
        return super(Login, self).form_valid(form)

