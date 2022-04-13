from os import stat
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mesh/', include('mesh.urls')),
    path('', upload_page)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
