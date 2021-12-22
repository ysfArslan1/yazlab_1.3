from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import login_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    url(r'^$', login_view, name='home'),

    url(r'^proje/', include('proje.urls')),

    url(r'^accounts/', include('accounts.urls')),

    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)