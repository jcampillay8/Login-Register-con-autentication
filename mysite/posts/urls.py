from django.urls import path
from django.urls.conf import include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crearPost, name='crear'),
    path('registrarse/', views.registrarUsuario,name='register',),
    path('post/<int:pk>', views.verPost, name='post'),
    path('actualizar/<int:pk>', views.actualizarPost, name='actualizar'),
    path('eliminar/<int:pk>', views.eliminarPost, name='eliminar'),
    path('likes/<int:pk>', views.darLike, name='dar_like')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)