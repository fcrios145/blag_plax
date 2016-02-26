from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from blog.views import Index, Prueba, Resume, Login
import blog.urls

urlpatterns = [
    # Examples:
    url(r'^$', Index.as_view(), name='home'),
    url(r'^prueba/', Prueba.as_view(), name='prueba'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^resume/', Resume.as_view(), name='resume'),
    url(r'^blog/', include(blog.urls)),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
