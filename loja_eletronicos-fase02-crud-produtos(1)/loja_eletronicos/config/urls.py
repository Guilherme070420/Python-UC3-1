from django.contrib import admin
from django.urls import path, include

# Adicione estas importações para servir arquivos de mídia em desenvolvimento (Aula 10)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('site-admin/', admin.site.urls),
    path('estoque/', include('estoque.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)