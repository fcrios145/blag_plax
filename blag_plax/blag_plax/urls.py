from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from blog.views import Index
import blog.urls

urlpatterns = [
    # Examples:
    url(r'^$', Index.as_view(), name='home'),
    url(r'^blog/', include(blog.urls)),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
