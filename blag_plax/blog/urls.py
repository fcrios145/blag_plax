from django.conf.urls import include, url
import blog.views

urlpatterns = [
    # Examples:
    url(r'^hola$', blog.views.hola, name='home'),
    url(r'^adios$', blog.views.adios, name='adios'),
    # url(r'^blog/', include('blog.urls')),
]
