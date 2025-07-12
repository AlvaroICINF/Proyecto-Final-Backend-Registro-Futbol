from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('jugadores/', views.jugador_lista, name='jugador_lista'),
    path('jugadores/<int:id>/', views.jugador_detalle, name='jugador_detalle'),
    path('jugadores/crear/', views.jugador_crear, name='jugador_crear'),
    path('jugadores/<int:id>/editar/', views.jugador_editar, name='jugador_editar'),
    path('jugadores/<int:id>/eliminar/', views.jugador_eliminar, name='jugador_eliminar'),
    
    path('equipos/', views.equipo_lista, name='equipo_lista'),
    path('equipos/<int:id>/', views.equipo_detalle, name='equipo_detalle'),
    path('equipos/crear/', views.equipo_crear, name='equipo_crear'),
    path('equipos/<int:id>/editar/', views.equipo_editar, name='equipo_editar'),
    path('equipos/<int:id>/eliminar/', views.equipo_eliminar, name='equipo_eliminar'),
]