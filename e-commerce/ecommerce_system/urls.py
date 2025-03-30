from django.contrib import admin
from django.urls import path
from commerce import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # | Manejo de productos destacados y carga de productos 
    #   mediante el panel de admin de Django | 

    path("inicio/", views.lista_destacados, name="lista_destacados"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)