from django.urls import path
from . import api_views

urlpatterns = [
    path('jugadores/', api_views.JugadorListView.as_view(), name='api_jugadores'),
    path('equipos/', api_views.EquipoListView.as_view(), name='api_equipos'),
    path('torneos/', api_views.TorneoListView.as_view(), name='api_torneos'),
    path('partidos/', api_views.PartidoListView.as_view(), name='api_partidos'),
    
    path('jugadores/<int:pk>/', api_views.JugadorDetailView.as_view(), name='api_jugador_detalle'),
    path('equipos/<int:pk>/', api_views.EquipoDetailView.as_view(), name='api_equipo_detalle'),
    path('paises/<int:pk>/', api_views.PaisDetailView.as_view(), name='api_pais_detalle'),
]