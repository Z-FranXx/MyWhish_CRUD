from django.urls import include, path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

# Urls de la aplicacion
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('whislist/', views.wishlist_view, name='whislist'),
    path('whislist/crear/', views.create, name='crear'),
    path('whislist/editar/', views.edit, name='editar'),
    path('eliminar/<int:id>/', views.delete, name='eliminar'),
    path('whitelist/editar/<int:id>', views.edit, name='editar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)