from django.contrib import admin
from .models import Pais, Equipo, Torneo, EquipoTorneo, Jugador, Partido

# Register your models here.

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'entrenador')
    list_filter = ('pais',)
    search_fields = ('nombre','pais', 'entrenador',)
    
@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    list_filter = ('pais',)
    
@admin.register(EquipoTorneo)
class EquipoTorneoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'torneo')
    list_filter = ('torneo',)
    
@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'posicion', 'pais', 'equipo')
    list_filter = ('nombre', 'pais', 'equipo')
    
@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('equipo_local', 'equipo_visitante', 'fecha', 'goles_local', 'goles_visitante')
    list_filter = ('fecha', 'torneo')
    
    