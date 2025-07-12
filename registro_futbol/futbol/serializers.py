from rest_framework import serializers
from .models import Pais, Equipo, Torneo, EquipoTorneo, Jugador, Partido

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class JugadorSerializer(serializers.ModelSerializer):
    pais = PaisSerializer(read_only=True)
    
    class Meta:
        model = Jugador
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    pais = PaisSerializer(read_only=True)
    jugadores = JugadorSerializer(many=True, read_only=True, source='jugador_set')
    
    class Meta:
        model = Equipo
        fields = '__all__'

class TorneoSerializer(serializers.ModelSerializer):
    pais = PaisSerializer(read_only=True)
    equipos_participantes = serializers.SerializerMethodField()
    
    class Meta:
        model = Torneo
        fields = '__all__'
    
    def get_equipos_participantes(self, obj):
        equipos_torneo = EquipoTorneo.objects.filter(torneo=obj)
        equipos_data = []
        for et in equipos_torneo:
            equipo_data = {
                'id': et.equipo.id,
                'nombre': et.equipo.nombre,
                'cantidad_jugadores': et.equipo.jugador_set.count()
            }
            equipos_data.append(equipo_data)
        return equipos_data

class PartidoSerializer(serializers.ModelSerializer):
    equipo_local = EquipoSerializer(read_only=True)
    equipo_visitante = EquipoSerializer(read_only=True)
    torneo = TorneoSerializer(read_only=True)
    
    class Meta:
        model = Partido
        fields = '__all__'

class PaisDetalleSerializer(serializers.ModelSerializer):
    equipos = EquipoSerializer(many=True, read_only=True, source='equipo_set')
    jugadores = JugadorSerializer(many=True, read_only=True, source='jugador_set')
    torneos = TorneoSerializer(many=True, read_only=True, source='torneo_set')
    
    class Meta:
        model = Pais
        fields = '__all__'